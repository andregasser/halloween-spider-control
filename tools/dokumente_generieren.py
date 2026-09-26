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

def supplier(row):
    if not row["Link"]:
        return row["Lieferant"] + " — Produkt noch offen"
    return f'[{row["Lieferant"]} · {row["Linkart"]}]({row["Link"]})'

def qty(row):
    return row["Menge"] + " " + row["Einheit"]

inventory = ", ".join(f"{r['ID']} {r['Teil']}" for r in rows if r["Status"] == "vorhanden")

bom = f"""# Material-Stückliste · Elektronik

Stand: **26.09.2026 · Revision A**. Diese Liste umfasst die Elektronik einschließlich Motor, Versorgung, elektrischer Leitungen, Anschlüsse und zugehörigem Elektrogehäuse-/Isolationsmaterial sowie auf ausdrücklichen Wunsch die Motorhalterung E47. Konstruktionsmaterial wie Rohre, Holzplatten, Riemenantrieb und Kabelbinder gehört nicht zum Umfang. Elektronikwerkzeuge und Lötmaterial stehen separat am Ende. Mengen von Leitungen und Zubehör sind Planmengen.

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

**Nicht bestellen, bereits vorhanden:** {inventory}. Die Liste enthält fehlende Elektronik und zugehöriges elektrisches Anschluss-/Gehäusematerial sowie die ausdrücklich ergänzte Motorhalterung E47. Weitere Prüf-/Crimpwerkzeuge und gegebenenfalls RCD werden nach Bestandsprüfung beschafft oder geliehen.

**Lieferantenlinks überarbeitet am 26.09.2026, ohne Reichelt:** **Produkt** führt zum konkreten Artikel; Artikelnummern, Varianten und Packungsmengen stehen im Hinweis. **Sortiment** führt zu einer passenden Kategorie, die genaue Ausführung ist noch offen. **Produkt noch offen** enthält bewusst keinen unbestätigten Link; diese Position ist erst nach Auswahl bestellbar. Eine recherchierte Produktseite ist keine Lager- oder Lieferzusage.

Die Spalte Menge beschreibt den Bedarf im Aufbau. Bei Mehrfachpackungen die Bestellmenge aus dem Hinweis verwenden: für E20/E21 zusammen fünf 2-polige Klemmen. Header-Kabel (E23/E24) und Abstandshalter (E42) aus dem vorhandenen Bestand verwenden.

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
         supplier(r), r["Bestellhinweis"]]
        for r in rows if r["Status"] == status
    ]) + "\n"
order += """## Zusätzlich einplanen: Netzaufbau und Prüfung

| Leistung | Anbieter | Umfang |
|---|---|---|
| Netzbaugruppe aufbauen und prüfen | Lokaler Elektroinstallateur / Elektrofachbetrieb | S0-Eignung, W1/F1/PS1/XPE, Gehäuse/PE, Trennung, RCD und Prüfung nach Einsatzort |

Noch kein konkreter regionaler Betrieb ausgewählt. Die Anbieterangabe ist eine Beschaffungsroute, kein eingeholtes Angebot.

## Empfohlene Bündelung

1. STEPPERONLINE: Motor, Motorhalterung ST-M7 (E47), Treiber und Motornetzteil. Treiberrevision und Lieferung in die Schweiz vorher bestätigen.
2. BerryBase Schweiz: Widerstände, Kondensatoren, Sockel, Platinenklemmen, USB-Versorgung und weiteres Kleinzubehör.
3. Bastelgarage: RJ45-Adapter und Steuerplatine.
4. DigiKey Schweiz: exakter HCT-Chip, Transistoren und Sicherungen. E30 ist bei der Recherche nicht lagernd; Termin klären.
5. Conrad Schweiz / Elektrofachbetrieb: Steuerkabel, PE-Litze und die noch auszuwählenden Netz-/Gehäuseteile.

Distrelec Schweiz ist als zusätzliche Bezugsquelle für E07 und E17 im jeweiligen Hinweis verlinkt. Die Produktdaten sind über indexierte Händlerseiten recherchiert; der direkte Abruf wurde blockiert. Aktuelle Preise, Bestelleinheiten und Lagerbestand sind deshalb nicht bestätigt. Je Position nur eine Bezugsquelle wählen.

Versandkosten der Teilbestellungen vor Kauf zusammenrechnen; diese Aufteilung ist kein Nachweis für den günstigsten Gesamtpreis. Vorhandene Teile nicht doppelt bestellen.

Bestellstatus künftig in `teile.csv` pflegen und beide Listen gemeinsam neu erzeugen. Ein angekreuztes Feld in einem Ausdruck ist keine automatische Bestellung.
"""
(ROOT / "bom/bestellliste.md").write_text(order, encoding="utf-8")
print(f"Stückliste und Bestellliste erzeugt: {len(rows)} Positionen.")
