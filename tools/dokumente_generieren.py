#!/usr/bin/env python3
"""Erzeugt deutsche Material- und Bestelllisten aus bom/teile.csv (nur Standardbibliothek)."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "bom/teile.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter=";"))

STATUS = {
    "vorhanden": "Vorhanden",
    "bestellen": "Noch bestellen",
    "aufmass": "Noch beschaffen, Aufmaß nötig",
    "abklaeren": "Noch beschaffen, Variante klären",
    "bestand_pruefen": "Bestand/Bedarf prüfen",
}

def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")

def table(headers, entries):
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(cell(x) for x in row) + " |" for row in entries]
    return "\n".join(lines) + "\n"

def qty(row):
    return row["Menge"] + " " + row["Einheit"]

inventory = ", ".join(f"{r['ID']} {r['Teil']}" for r in rows if r["Status"] == "vorhanden")

bom = f"""# Material-Stückliste · Elektronik

Stand: **26.09.2026 · Revision A**. Diese Liste umfasst ausschließlich die Elektronik einschließlich Motor, Versorgung, elektrischer Leitungen, Anschlüsse und zugehörigem Elektrogehäuse-/Isolationsmaterial. Konstruktionsmaterial wie Rohre, Holzplatten, Riemenantrieb und Kabelbinder gehört nicht zum Umfang. Elektronikwerkzeuge und Lötmaterial stehen separat am Ende. Mengen von Leitungen und Zubehör sind Planmengen.

**Bestätigt vorhanden: {inventory}.** Noch keine Bestellung ausgelöst.

Die [Bestellliste](bestellliste.md) ergänzt Lieferant und Auswahlhinweise. Die IDs bleiben über beide Listen gleich. Alle eingebauten elektronischen Referenzen gehören zum [Schaltplan](../docs/elektronik.md). Preise sind bewusst nicht aus alten Schätzungen übernommen.

Automatisch erzeugt aus [teile.csv](teile.csv) mit `python3 tools/dokumente_generieren.py`.

"""
for group in dict.fromkeys(r["Gruppe"] for r in rows):
    bom += f"## {group}\n\n"
    bom += table(["ID", "Menge", "Teil / Spezifikation", "Warum benötigt?", "Status"], [
        [r["ID"], qty(r), r["Teil"] + " — " + r["Spezifikation"], r["Begruendung"], STATUS[r["Status"]]]
        for r in rows if r["Gruppe"] == group
    ]) + "\n"
bom += """## Enthaltene und nicht benötigte Teile

- Das Motorkabel zählt zum Motorlieferumfang und wird nicht noch einmal bestellt. Montage der Steuerbox in Reichweite des 1-m-Kabels einplanen.
- Schraubklemmen des DM860T bei Lieferung auf Vollständigkeit prüfen.
- Keine zusätzliche Lochrasterplatine am PIR erforderlich: Die Sensorleitung verbindet B1 direkt mit J2. E18 ist die weiterhin benötigte Steuer-Lochrasterplatine für U2 und die übrige Schaltung.
- Kein 48→5-V-Wandler, Ethernet-Modul, PoE-Injector, separater PIR, Hall-Sensor, Endschalter, Soundmodul oder externe Status-LED erforderlich. S0 ist vorgesehen, eine sicherheitsgerichtete Not-Halt-Baugruppe ist nicht Bestandteil von Rev. A.
- Aufbau und Prüfung der Netzbaugruppe sind eine zusätzliche Leistung, kein Bauteil; in der Bestellliste gesondert aufgeführt.
"""
(ROOT / "bom/material-stueckliste.md").write_text(bom, encoding="utf-8")

order = f"""# Bestellliste · Elektronik

Stand: **26.09.2026 · Revision A**. Noch keine Bestellung ausgelöst.

**Nicht bestellen, bereits vorhanden:** {inventory}. Die Liste enthält nur fehlende Elektronik und zugehöriges elektrisches Anschluss-/Gehäusematerial. Weitere Prüf-/Crimpwerkzeuge und gegebenenfalls RCD werden nach Bestandsprüfung beschafft oder geliehen.

Ein Link zu einer Produktseite belegt die gefundene Produktfamilie, nicht jede auswählbare Variante. Mit **Bezugsquelle** gekennzeichnete Einträge nennen einen vorgeschlagenen Lieferanten, aber noch keine einzeln geprüfte Artikelnummer. Keine Lieferbarkeit oder Schweizer Versandkosten zugesichert. Bei Anfragepositionen erst Maße/Kompatibilität klären, dann bestellen. Bei Elektrogehäusen und Kabeldurchführungen die Abmessungen der Elektronik und Leitungen abgleichen.

Die ursprünglichen Budgetwerte aus dem Handover sind keine aktuellen Angebote. Vor Zahlung Endpreis in CHF einschließlich Versand/Einfuhr und Lieferdatum bis Halloween kontrollieren.

Automatisch erzeugt aus [teile.csv](teile.csv). Die [Material-Stückliste](material-stueckliste.md) erklärt den Zweck jedes Teils.

"""
for status, title in [
    ("bestellen", "Fehlende Standardteile und festgelegte Modelle"),
    ("abklaeren", "Fehlende Teile mit noch zu bestätigender Ausführung"),
    ("aufmass", "Elektrogehäuse und Anschlussteile nach Aufmaß"),
    ("bestand_pruefen", "Elektronikwerkzeug und bedingter Bedarf"),
]:
    if not any(r["Status"] == status for r in rows):
        continue
    order += f"## {title}\n\n"
    order += table(["Erledigt", "ID", "Menge", "Teil / genaue Auswahl", "Lieferant / Link", "Vor Bestellung beachten"], [
        ["☐", r["ID"], qty(r), r["Teil"] + " — " + r["Spezifikation"],
         f'[{r["Lieferant"]}]({r["Link"]})', r["Bestellhinweis"]]
        for r in rows if r["Status"] == status
    ]) + "\n"
order += """## Zusätzlich einplanen: Netzaufbau und Prüfung

| Leistung | Anbieter | Umfang |
|---|---|---|
| Netzbaugruppe aufbauen und prüfen | Lokaler Elektroinstallateur / Elektrofachbetrieb | S0-Eignung, W1/F1/PS1/XPE, Gehäuse/PE, Trennung, RCD und Prüfung nach Einsatzort |

Noch kein konkreter regionaler Betrieb ausgewählt. Die Anbieterangabe ist eine Beschaffungsroute, kein eingeholtes Angebot.

## Empfohlene Bündelung

1. STEPPERONLINE: Motor, Treiber und Motornetzteil. Treiberrevision und Lieferung in die Schweiz vorher bestätigen.
2. Elektronikdistributor: U2, Transistoren, Widerstände/Kondensatoren, Sicherungen und Halter. Weitere Kleinteile bei Reichelt bündeln.
3. Elektrogehäuse und Kabeldurchführungen anhand des Elektroniklayouts auswählen. Vorhandene Teile nicht doppelt bestellen.

Bestellstatus künftig in `teile.csv` pflegen und beide Listen gemeinsam neu erzeugen. Ein angekreuztes Feld in einem Ausdruck ist keine automatische Bestellung.
"""
(ROOT / "bom/bestellliste.md").write_text(order, encoding="utf-8")
print(f"Stückliste und Bestellliste erzeugt: {len(rows)} Positionen.")
