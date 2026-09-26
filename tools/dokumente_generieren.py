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

bom = """# Material-Stückliste

Stand: **26.09.2026 · Revision A**. Diese Liste umfasst den beschriebenen Basisaufbau einschließlich Elektronik-Kleinteilen, Versorgung, Leitungen, Mechanik, Gehäusen und Montagezubehör. Werkzeuge und Verbrauchsmaterial stehen separat am Ende. Mengen von Kabeln/Zubehör sind Planmengen; maßabhängige Teile sind ausdrücklich gekennzeichnet.

**Bestätigt vorhanden: Arduino Uno R3 und PIR. Sonst nichts als bestellt verbucht.** Bei den im Handover beschriebenen Wagen-/Dekorationsteilen vor einem Neukauf dennoch den realen Bestand abgleichen.

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
- Schraubklemmen des DM860T und Befestigungsschrauben der Klemmnaben/Lager sind auf Vollständigkeit bei Lieferung zu prüfen. Fehlende Befestiger aus M22 ergänzen.
- Kein 48→5-V-Wandler, Ethernet-Modul, PoE-Injector, separater PIR, Hall-Sensor, Endschalter, Soundmodul oder externe Status-LED erforderlich. S0 ist vorgesehen, eine sicherheitsgerichtete Not-Halt-Baugruppe ist nicht Bestandteil von Rev. A.
- 230-V-Aufbau/Prüfung sowie nötige Wellen-/Plattenbearbeitung sind zusätzliche Leistungen, keine Bauteile. In der Bestellliste gesondert aufgeführt.
"""
(ROOT / "bom/material-stueckliste.md").write_text(bom, encoding="utf-8")

order = """# Bestellliste

Stand: **26.09.2026 · Revision A**. Noch keine Bestellung ausgelöst.

**Nicht bestellen:** E01 Arduino Uno R3 und E02 PIR, beide vorhanden. Alle übrigen Einbauteile sind unten aufgeführt. Werkzeuge, Verbrauchsmaterial und gegebenenfalls RCD werden nach Bestandsprüfung beschafft oder geliehen.

Ein Link zu einer Produktseite belegt die gefundene Produktfamilie, nicht jede auswählbare Variante. Mit **Bezugsquelle** gekennzeichnete Einträge nennen einen vorgeschlagenen Lieferanten, aber noch keine einzeln geprüfte Artikelnummer. Keine Lieferbarkeit oder Schweizer Versandkosten zugesichert. Bei Anfragepositionen erst Maße/Kompatibilität klären, dann bestellen. Das verhindert insbesondere Fehlkäufe bei Welle, Schellen, Gehäuse und Riemennaben.

Die ursprünglichen Budgetwerte aus dem Handover sind keine aktuellen Angebote. Vor Zahlung Endpreis in CHF einschließlich Versand/Einfuhr und Lieferdatum bis Halloween kontrollieren.

Automatisch erzeugt aus [teile.csv](teile.csv). Die [Material-Stückliste](material-stueckliste.md) erklärt den Zweck jedes Teils.

"""
for status, title in [
    ("bestellen", "1. Fehlende Standardteile und festgelegte Modelle"),
    ("abklaeren", "2. Fehlende Teile mit noch zu bestätigender Ausführung"),
    ("aufmass", "3. Fehlende Teile nach Aufmaß/Zuschnitt"),
    ("bestand_pruefen", "4. Werkstattbestand und bedingter Bedarf"),
]:
    order += f"## {title}\n\n"
    order += table(["Erledigt", "ID", "Menge", "Teil / genaue Auswahl", "Lieferant / Link", "Vor Bestellung beachten"], [
        ["☐", r["ID"], qty(r), r["Teil"] + " — " + r["Spezifikation"],
         f'[{r["Lieferant"]}]({r["Link"]})', r["Bestellhinweis"]]
        for r in rows if r["Status"] == status
    ]) + "\n"
order += """## 5. Zusätzlich einplanen: Leistungen

| Leistung | Anbieter | Umfang |
|---|---|---|
| Netzbaugruppe aufbauen und prüfen | Lokaler Elektroinstallateur / Elektrofachbetrieb | S0-Eignung, W1/F1/PS1/XPE, Gehäuse/PE, Trennung, RCD und Prüfung nach Einsatzort |
| Welle und Platten fertigen | Lokale mechanische Werkstatt, alternativ DOLD-Anfrage | Hauptachse ablängen/entgraten und Nut passend zur 40T-Scheibe fertigen, Platten bohren/Langlöcher herstellen |

Noch kein konkreter regionaler Betrieb ausgewählt. Für diese Leistungen fehlen Ort und endgültige Mechanikmaße; die Anbieterangabe ist eine Beschaffungsroute, kein eingeholtes Angebot.

## Empfohlene Bündelung

1. STEPPERONLINE: Motor, Treiber, Motornetzteil und Halter. Treiberrevision und Lieferung in die Schweiz vorher bestätigen.
2. Elektronikdistributor: U2, Transistoren, Widerstände/Kondensatoren, Sicherungen und Halter. Weitere Kleinteile bei Reichelt bündeln.
3. Riemenscheiben: zwei passende Varianten beim genannten eBay-Händler, keine ähnlich benannte GT2-/3M-/T5-Ausführung.
4. Mechanik: Lager und Klemmringe; danach Welle, Nabe und Platten anhand der realen Anschlussmaße.
5. Gehäuse-/Baumarktmaterial erst nach Layout. Arduino und PIR nicht doppelt bestellen.

Bestellstatus künftig in `teile.csv` pflegen und beide Listen gemeinsam neu erzeugen. Ein angekreuztes Feld in einem Ausdruck ist keine automatische Bestellung.
"""
(ROOT / "bom/bestellliste.md").write_text(order, encoding="utf-8")
print(f"Stückliste und Bestellliste erzeugt: {len(rows)} Positionen.")
