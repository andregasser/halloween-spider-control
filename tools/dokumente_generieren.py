#!/usr/bin/env python3
"""Erzeugt Stück- und Bestellliste aus bom/teile.csv; nur Standardbibliothek."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'bom/teile.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter=';'))
STATUS={'vorhanden':'Vorhanden','bestellen':'Noch bestellen','aufmass':'Aufmaß/Ausführung offen','abklaeren':'Ausführung klären','bestand_pruefen':'Bestand/Bedarf prüfen'}
def table(headers,entries):
 def cell(v):return v.replace('|','\\|').replace('\n',' ')
 return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(cell(x) for x in e)+' |' for e in entries])+'\n\n'
def quantity(r):return r['Menge']+' '+r['Einheit']
def supplier(r):
 return f"[{r['Lieferant']} · {r['Linkart']}]({r['Link']})" if r['Link'] else r['Lieferant']+' — Produkt offen'
inventory=', '.join(r['ID']+' '+r['Teil'] for r in rows if r['Status']=='vorhanden')
intro='Stand **03.10.2026 · Revision B · fertige Module, keine selbst gelötete Zusatzplatine**. Noch nicht aufgebaut/getestet, keine Bestellung ausgelöst. Umfang: Elektronik, elektrische Leitungen und Gehäusezubehör sowie ausdrücklich Motorhalterung ST-M7. Keine weitere Konstruktion/Mechanik.\n\n'
bom='# Material-Stückliste · Elektronik\n\n'+intro+f'**Bestätigt vorhanden:** {inventory}.\n\nAutomatisch aus [teile.csv](teile.csv) erzeugt. [Bestellliste](bestellliste.md) nennt Lieferanten; [Anschlussplan](../docs/elektronik.md) beschreibt die Verdrahtung. Leitungs-/Zubehörmengen sind Planbedarf; Packungsmengen stehen in der Bestellliste.\n\n'
for group in dict.fromkeys(r['Gruppe'] for r in rows):
 bom+='## '+group+'\n\n'+table(['ID','Menge','Teil / Spezifikation','Warum benötigt?','Status'],[[r['ID'],quantity(r),r['Teil']+' — '+r['Spezifikation'],r['Begruendung'],STATUS[r['Status']]] for r in rows if r['Gruppe']==group])
bom+='''## Lieferumfang und entfallene Teile

Motor enthält 1 m Anschlusskabel; Adafruit #5648 wird ohne STEMMA-Kabel geliefert: zwei Kabel #3894 separat bestellen. Treiber-Klemmstecker bei Lieferung prüfen. Kabel W5 ist eine fertige Verlängerung; nur dessen männliches Ende wird zum Klemmen abgeschnitten.

Lochrasterplatinen, HCT-Chip, Sockel, Einzeltransistoren, externe Kondensatoren, Netzsicherungsaufbau und interne 230-V-Verkabelung aus Revision A entfallen. Lötwerkzeug/Lot/Flussmittel sind bestätigt vorhanden, werden für Rev. B aber nicht benötigt und stehen deshalb nicht als Projektbedarf in dieser Liste. Kein Ethernet/PoE, Home-Sensor oder Freigabeschalter im Basisaufbau.
'''
(ROOT/'bom/material-stueckliste.md').write_text(bom,encoding='utf-8')
order='# Bestellliste · Elektronik\n\n'+intro+f'**Nicht bestellen, bereits vorhanden:** {inventory}.\n\n'
order+='''Die festgelegte Elektronik ist unten mit konkreten Artikelmodellen aufgeführt. Gehäuse und Durchführungen setzen derzeit einen **trockenen, geschützten Standort** voraus; Ausführung nach realem Layout bestätigen. Offene Zubehörpositionen gehören zum vollständigen Aufbau und sind bewusst keine vermeintlich geprüften Kaufartikel.

**Lieferanforderung: Erhalt in der Schweiz binnen 7 Kalendertagen nach Bestellung.** Bei Bestellung am 03.10.2026 bedeutet das spätestens 10.10.2026. Ein angezeigter Lagerbestand plus übliche Versandzeit ist ein Angebot für die kurzfristige Beschaffung, keine garantierte Zustellung. Lieferdatum für die eigene Schweizer Adresse vor Zahlung prüfen. **Motor E03, Treiber E04 und Halterung E47 erfüllen die Wochenfrist bisher nicht nachweislich; bei Power-DIN-Kabel E49 ist der CH-Termin offen.** Erst diese Positionen klären, bevor der gesamte Aufbau als rechtzeitig beschaffbar gilt.

**Produkt** verlinkt einen konkreten Artikel. **Offen** bedeutet: kein bestätigter Artikel, erst nach Aufmaß/Bestandsprüfung bestellbar. Die Lieferbewertung stammt aus der Recherche vom 03.10.2026; Webabrufe können zwischengespeicherte Händlerangaben enthalten. **Hersteller-Standardlieferzeit** ist die Nachbeschaffungszeit und darf nicht mit dem Versand vorhandener Händler-Lagerware verwechselt werden. [Lieferbelege und Alternativen](../docs/quellen-und-entscheidungen.md#beschaffung-binnen-einer-woche). CHF-Endpreise, Packungsmengen, Einfuhr und Versand im Warenkorb prüfen. Ein Gesamtpreis ist wegen offener Zubehörmaße und Versandkosten noch nicht verlässlich berechenbar.

Die Menge ist der Bedarf. Bei E50 zwei WAGO-Einzelstücke, bei E55 zwei STEMMA-Kabel #3894, bei E56 ein fertig bestücktes Shield wählen. Vor Bestellung Module vollständig mit Anschlussklemmen/Kabeln und Treiber ausdrücklich als **V3.0** bestätigen. [Technische Auswahl und Abnahmekriterien](../docs/fertige-module.md).

Automatisch erzeugt aus [teile.csv](teile.csv); Änderungen dort pflegen.

'''
for status,title in [('bestellen','Festgelegte Elektronik und Anschlussmaterial'),('abklaeren','Ausführung noch klären'),('aufmass','Gehäuse und Zubehör nach Aufmaß'),('bestand_pruefen','Bedingter Bedarf; zuerst Bestand prüfen')]:
 selected=[r for r in rows if r['Status']==status]
 if selected:order+='## '+title+'\n\n'+table(['Erledigt','ID','Menge','Teil / genaue Auswahl','Lieferant / Link','Lieferbewertung / Hinweis','Vor Bestellung beachten'],[['☐',r['ID'],quantity(r),r['Teil']+' — '+r['Spezifikation'],supplier(r),r['Lieferbewertung']+' — '+r['Lieferhinweis'],r['Bestellhinweis']] for r in selected])
order+='''## Beschaffung bündeln

1. **Zuerst Termin klären:** Motor E03, Halterung E47 und Treiber E04 bei STEPPERONLINE; keine China-Standardlieferung für die Wochenfrist einplanen. E49 bei DigiKey mit konkretem CH-Termin bestätigen. Ohne diese vier Klärungen ist die Gesamtbeschaffung offen.
2. **DigiKey Schweiz:** PS1 E05, zwei STEMMA-Kabel E55 und Shield E56; E49 nach Terminbestätigung bündeln. Zwei Adafruit-Module E48 und RJ45-Adapter E09 können bei bestätigtem Lagerbestand ebenfalls hier mitbestellt werden, um zusätzliche Versandkosten zu sparen. Nur reguläre DigiKey-Lagerware, keine Hersteller-Nachbestellung/Marktplatzlieferung.
3. **Play-Zone Schweiz:** zwei Adafruit-Module E48 als Bezugsquelle ab eigenem CH-Lager, Priority oder reservierte Abholung. Originalmodell #5648 bleibt.
4. **Bastelgarage:** zwei RJ45-Buchsenadapter E09, Priority oder reservierte Abholung.
5. **BerryBase Schweiz:** USB-Netzteil E06, USB-A/B-Kabel E07 (1,80 m) und zwei WAGO E50. Angegebene 2–5 Tage für die eigenen CH-Lieferdaten prüfen.
6. **Bürklin Elektronik:** 1 m W4 E26 und 1 m DC-Litze E35 gemeinsam. Ausgewiesene Lagerware mit 1–2 Tagen Schweiz-Transport; Zuschnitt, Zahlung und Einfuhr können die Gesamtzeit verlängern.

**Ausweichquelle für E56:** Farnell Schweiz, DFR0265 / 2946070, gelistete Lagerware und Express 1–2 Arbeitstage. Distrelec/RS und Simpex wurden erneut für PS1 geprüft; mangels belastbarem aktuellem CH-Zustelltermin sind sie keine bestätigten Wochenfrist-Alternativen. Details und konkrete Links in den Lieferbelegen. Gehäuse und noch offene Zubehörmaße benötigen zusätzlich eine Ausführungs- und Terminprüfung.

Die Händleraufteilung ist kein Nachweis für den niedrigsten Schweizer Gesamtpreis. E48 bei Play-Zone kostet beim Abruf CHF 5.90 pro Stück und zusätzlichen Versand; eine gemeinsame DigiKey-Lagerbestellung kann günstiger sein. Termin vor Preis optimieren, danach Versandkosten bündeln.

Keine Bestellung wird durch diese Liste ausgelöst. Der 230-V-Anschluss besteht ausschließlich aus fertigen Steckverbindungen. Keine zusätzliche Dienstleistung für eine selbst gebaute Netzbaugruppe eingeplant.
'''
(ROOT/'bom/bestellliste.md').write_text(order,encoding='utf-8')
print(f'Stück- und Bestellliste erzeugt: {len(rows)} Positionen.')
