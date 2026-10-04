#!/usr/bin/env python3
"""Prüft lokale Links, Bauteilabdeckung und reproduzierbare Dokumentgenerierung.

Dies ist eine Dokumentprüfung, keine elektrische Simulation oder Hardwareprüfung.
"""
import csv
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []
generated = [ROOT / p for p in (
    "bom/material-stueckliste.md", "bom/bestellliste.md",
    "docs/schaltplan-steuerung.svg", "docs/schaltplan-versorgung.svg")]
before = {p: p.read_bytes() for p in generated}
for script in ("dokumente_generieren.py", "schaltplaene_generieren.py"):
    subprocess.run([sys.executable, str(ROOT / "tools" / script)], check=True)
for p in generated:
    if p.read_bytes() != before[p]: errors.append(f"Erzeugte Datei war veraltet: {p.relative_to(ROOT)}")

for p in ROOT.rglob("*.md"):
    if "archiv" in p.parts: continue
    for dest in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
        if re.match(r"[a-zA-Z]+://", dest) or dest.startswith("#"): continue
        if not (p.parent / unquote(dest.split('#')[0])).exists():
            errors.append(f"Defekter lokaler Link: {p.relative_to(ROOT)} → {dest}")

with (ROOT / "bom/teile.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter=";"))
ids = [r["ID"] for r in rows]
if len(ids) != len(set(ids)): errors.append("Doppelte Stücklisten-IDs")
orders = (ROOT / "bom/bestellliste.md").read_text(encoding="utf-8")
for r in rows:
    if None in r or any(v is None for v in r.values()): errors.append(f"Ungültige CSV-Zeile: {r.get('ID')}")
    if r["Status"] != "vorhanden":
        if not r["Lieferant"]:
            errors.append(f"Lieferant fehlt: {r['ID']}")
        if r["Linkart"] == "Offen":
            if r["Link"] or r["Status"] == "bestellen":
                errors.append(f"Offene Beschaffung fälschlich als bestellbar/verlinkt: {r['ID']}")
        elif r["Linkart"] in ("Produkt", "Sortiment"):
            url = urlparse(r["Link"])
            if url.scheme != "https" or not url.netloc or url.path in ("", "/"):
                errors.append(f"Konkreter HTTPS-Link fehlt (keine Shop-Startseite): {r['ID']}")
        else:
            errors.append(f"Ungültige Linkart: {r['ID']}")
        if f"| {r['ID']} |" not in orders: errors.append(f"Bestellposition fehlt: {r['ID']}")
    elif f"| {r['ID']} |" in orders: errors.append(f"Vorhandenes Teil auf Bestellliste: {r['ID']}")

svg_text = ""
drawn_connections = set()
for p in ROOT.glob("docs/*.svg"):
    tree = ET.parse(p)
    svg_text += "\n".join(tree.getroot().itertext()) + "\n"
    # Nicht nur Namen prüfen: jede Leitung muss genau an ihren beschrifteten Pins enden.
    pin_locations = set()
    for node in tree.getroot().iter():
        if "data-pin" not in node.attrib: continue
        location = (node.attrib["data-pin"], node.attrib["data-x"], node.attrib["data-y"])
        pin_locations.add(location)
        children = list(node)
        if not any(n.tag.endswith("text") and n.text for n in children):
            errors.append(f"Unbeschrifteter Anschluss: {location[0]}")
        if not any(n.tag.endswith("circle") and n.attrib.get("cx") == location[1]
                   and n.attrib.get("cy") == location[2] for n in children):
            errors.append(f"Anschlusskreis fehlt oder verschoben: {location[0]}")
    for node in tree.getroot().iter():
        if "data-from" not in node.attrib: continue
        points = [tuple(v.split(",")) for v in node.attrib["points"].split()]
        for attr, point in [("data-from", points[0]), ("data-to", points[-1])]:
            if (node.attrib[attr], *point) not in pin_locations:
                errors.append(f"Leitung endet nicht an ihrem Anschluss: {p.name} / {node.attrib[attr]}")
        if node.attrib.get("data-kind") != "internal":
            drawn_connections.add(frozenset((node.attrib["data-from"], node.attrib["data-to"])))

# Unabhängiger Anschlussvertrag gemäß Verbindungstabellen in docs/elektronik.md.
# Wiederholte Geräte-Ausschnitte dürfen dieselbe Verbindung erneut zeigen.
expected_connections = {
    frozenset(pair) for pair in [
        ("Haus.Typ13", "S0.Netzstecker"),
        ("S0.Steckplatz1", "PS1.IEC-C14"),
        ("S0.Steckplatz2", "PS2.Netzstecker"),
        ("PS2.USB-A", "U1.USB-B"),
        ("PS1.Power-DIN", "W5.Power-DIN-Buchse"),
        ("W5.+48V_A", "X1.1"), ("W5.+48V_B", "X1.2"),
        ("W5.Rueckleiter_A", "X2.1"), ("W5.Rueckleiter_B", "X2.2"),
        ("X1.3", "U3.AC1"), ("X2.3", "U3.AC2"),
        ("M1.schwarz", "U3.A+"), ("M1.grün", "U3.A-"),
        ("M1.rot", "U3.B+"), ("M1.blau", "U3.B-"),
        ("U1.5V", "X3.1"), ("X3.2", "U4.V+"),
        ("X3.3", "U5.V+"), ("X3.4", "J1.5"),
        ("U1.GND1", "X4.1"), ("X4.2", "U4.GND"),
        ("X4.3", "U5.GND"), ("X4.4", "J1.2"), ("X4.5", "W4.Schirm"),
        ("U1.D2", "U4.In"), ("U1.D3", "U5.In"),
        ("U4.Out+", "U3.PUL+"), ("U4.Out-", "U3.PUL-"),
        ("U5.Out+", "U3.DIR+"), ("U5.Out-", "U3.DIR-"),
        ("U1.A0", "J1.1"), ("U1.GND2", "J1.4"),
        ("J2.1", "B1.OUT"), ("J2.2", "B1.GND"),
        ("J2.5", "B1.VCC"), ("J2.4", "J2.2"),
    ] + [(f"J1.RJ45.{n}", f"J2.RJ45.{n}") for n in [1, 2, 4, 5]]
}
for connection in expected_connections - drawn_connections:
    errors.append("Pinverbindung fehlt im Schaltplan: " + " ↔ ".join(sorted(connection)))
for connection in drawn_connections - expected_connections:
    errors.append("Unerwartete Pinverbindung im Schaltplan: " + " ↔ ".join(sorted(connection)))
electronics = (ROOT / "docs/elektronik.md").read_text(encoding="utf-8")
for ref in ["U1", "U3", "U4", "U5", "B1", "M1", "PS1", "PS2", "S0"] + ["X1","X2","X3","X4"] + ["J1","J2"] + [f"W{i}" for i in range(1,6)]:
    if not re.search(rf"\b{ref}\b", svg_text): errors.append(f"Referenz fehlt in SVG: {ref}")
    if not re.search(rf"\b{ref}\b", electronics): errors.append(f"Referenz fehlt in Elektronik-Dokument: {ref}")
    if not any(re.search(rf"\b{ref}\b", r["Teil"]) for r in rows):
        errors.append(f"Referenz fehlt in Stückliste: {ref}")

# Revisionswechsel und bestätigten Bestand gegen versehentliche Altbestellungen sichern.
by_id={r["ID"]:r for r in rows}
for item in ["E01","E02","E07","E08","E23","E24","E28","E29","E42","E44","T03","T04"]:
    if by_id.get(item,{}).get("Status")!="vorhanden":errors.append(f"Bestätigter Bestand verändert: {item}")
obsolete={"E10","E11","E12","E13","E14","E16","E17","E18","E20","E21","E30","E31","E32","E33","E34","E36","E41","E56"}
if obsolete.intersection(ids):errors.append("Entfallene Teile in aktueller CSV")
for item,qty in [("E09","2"),("E48","2"),("E50","2"),("E55","2"),("E57","2")]:
    if by_id.get(item,{}).get("Menge")!=qty:errors.append(f"Anzahl im Klemmplan stimmt nicht: {item}")
for ref in ["U2","U6","Q1","Q2","J0","J3","F1","F2","XPE"]:
    if re.search(rf"\b{ref}\b",svg_text):errors.append(f"Entfallenes Bauteil im aktuellen Schaltplan: {ref}")
firmware=(ROOT/"docs/firmware.md").read_text(encoding="utf-8")
for token in ["A0","INPUT_PULLUP","500 µs","1 ms","3200"]:
    if token not in firmware or token not in electronics:errors.append(f"Pin-/Zeitvertrag unvollständig: {token}")
from schaltplaene_generieren import DEVICES
for ref,model in DEVICES.items():
    # Jede Gerätebox verwendet dieselbe Modellbezeichnung, auch bei Wiederholung.
    expected=ref+" · "+model
    if expected not in svg_text:errors.append(f"Gerätemodell fehlt im Schaltplan: {expected}")
    for p in ROOT.glob("docs/schaltplan-*.svg"):
        for node in ET.parse(p).getroot().iter():
            if node.tag.endswith("text") and (node.text or "").startswith(ref+" · ") and node.text!=expected:
                errors.append(f"Inkonsistente Gerätebox: {node.text}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(rows)} Stücklistenpositionen, {len(expected_connections)} Pinverbindungen mit Anschlusskreisen, Bestellabdeckung, lokale Links, SVG-XML und reproduzierbare Erzeugung.")
print("Keine elektrische Simulation, kein Firmware-Build und kein Hardwaretest durchgeführt.")
