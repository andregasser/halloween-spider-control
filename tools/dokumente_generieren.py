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

**Produkt** verlinkt einen konkreten Artikel. **Offen** bedeutet: kein bestätigter Artikel, erst nach Aufmaß/Bestandsprüfung bestellbar. Linkrecherche und technische Auswahl sind keine Liefer- oder Hardwarefunktionszusage. CHF-Endpreise, Packungsmengen, Einfuhr, Versand und Halloween-Lieferdatum im Warenkorb prüfen. Ein Gesamtpreis ist wegen offener Zubehörmaße und Versandkosten noch nicht verlässlich berechenbar.

Die Menge ist der Bedarf. Bei E50 zwei WAGO-Einzelstücke, bei E55 zwei STEMMA-Kabel #3894, bei E56 ein fertig bestücktes Shield wählen. Vor Bestellung Module vollständig mit Anschlussklemmen/Kabeln und Treiber ausdrücklich als **V3.0** bestätigen. [Technische Auswahl und Abnahmekriterien](../docs/fertige-module.md).

Automatisch erzeugt aus [teile.csv](teile.csv); Änderungen dort pflegen.

'''
for status,title in [('bestellen','Festgelegte Elektronik und Anschlussmaterial'),('abklaeren','Ausführung noch klären'),('aufmass','Gehäuse und Zubehör nach Aufmaß'),('bestand_pruefen','Bedingter Bedarf; zuerst Bestand prüfen')]:
 selected=[r for r in rows if r['Status']==status]
 if selected:order+='## '+title+'\n\n'+table(['Erledigt','ID','Menge','Teil / genaue Auswahl','Lieferant / Link','Vor Bestellung beachten'],[['☐',r['ID'],quantity(r),r['Teil']+' — '+r['Spezifikation'],supplier(r),r['Bestellhinweis']] for r in selected])
order+='''## Beschaffung bündeln

1. **STEPPERONLINE:** Motor E03, Halterung E47, Treiber E04.
2. **Bastelgarage:** zwei RJ45-Buchsenadapter E09.
3. **BerryBase Schweiz:** USB-Netzteil E06, USB-A/B-Kabel E07, Anschluss-Shield E56 und WAGO E50.
4. **DigiKey Schweiz:** Power-DIN-Kabel E49, zwei Adafruit-Module E48 und zwei STEMMA-Kabel E55; PS1 E05 und gegebenenfalls das gewählte Gehäuse samt Platte mitbestellen. PS1 alternativ Distrelec 300-42-762 oder [Simpex GST220A48-R7B](https://www.simpex.ch/shop/stromversorgungen/netzteile-ac-dc/tischnetzteile/gst220a48-r7b/), jeweils ein Netzteil, keine Großpackung.
5. **Conrad / Elektrobedarf Troller:** W4 und 1 m DC-Litze; zusätzliche Versandkosten mit lokalen Bezugsoptionen vergleichen.

Distrelec wurde für PS1 als konkrete Alternative recherchiert. Preise/Lagerbestand waren dort nicht zuverlässig abrufbar. Die Händleraufteilung ist kein Nachweis für den niedrigsten Schweizer Gesamtpreis; Kleinmaterial nach Möglichkeit bei ohnehin verwendeten Lieferanten bündeln und gleiche Spezifikation beibehalten.

Keine Bestellung wird durch diese Liste ausgelöst. Der 230-V-Anschluss besteht ausschließlich aus fertigen Steckverbindungen. Keine zusätzliche Dienstleistung für eine selbst gebaute Netzbaugruppe eingeplant.
'''
(ROOT/'bom/bestellliste.md').write_text(order,encoding='utf-8')
print(f'Stück- und Bestellliste erzeugt: {len(rows)} Positionen.')
