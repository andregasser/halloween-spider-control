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
from urllib.parse import unquote

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
        if not r["Lieferant"] or not r["Link"].startswith("https://"):
            errors.append(f"Lieferant/Link fehlt: {r['ID']}")
        if f"| {r['ID']} |" not in orders: errors.append(f"Bestellposition fehlt: {r['ID']}")
    elif f"| {r['ID']} |" in orders: errors.append(f"Vorhandenes Teil auf Bestellliste: {r['ID']}")

svg_text = ""
for p in ROOT.glob("docs/*.svg"):
    tree = ET.parse(p)
    svg_text += "\n".join(tree.getroot().itertext()) + "\n"
electronics = (ROOT / "docs/elektronik.md").read_text(encoding="utf-8")
for ref in ["U1", "U2", "U3", "B1", "M1", "PS1", "PS2", "S0", "Q1", "Q2", "F1", "F2", "XPE"] + [f"R{i}" for i in range(1,7)] + [f"C{i}" for i in (1,2,5)] + [f"J{i}" for i in range(4)] + [f"W{i}" for i in range(1,5)]:
    if not re.search(rf"\b{ref}\b", svg_text): errors.append(f"Referenz fehlt in SVG: {ref}")
    if not re.search(rf"\b{ref}\b", electronics): errors.append(f"Referenz fehlt in Elektronik-Dokument: {ref}")
    if not any(re.search(rf"\b{ref}\b", r["Teil"]) for r in rows):
        errors.append(f"Referenz fehlt in Stückliste: {ref}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(rows)} Stücklistenpositionen, Bestellabdeckung, lokale Links, SVG-XML und reproduzierbare Erzeugung.")
print("Keine elektrische Simulation, kein Firmware-Build und kein Hardwaretest durchgeführt.")
