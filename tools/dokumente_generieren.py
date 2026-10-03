#!/usr/bin/env python3
"""Erzeugt Stück- und Bestellliste aus bom/teile.csv; nur Standardbibliothek."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'bom/teile.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter=';'))
STATUS={'vorhanden':'Vorhanden','bestellen':'Noch bestellen','aufmass':'Aufmaß/Ausführung offen','abklaeren':'Bezugsquelle/Ausführung klären','bestand_pruefen':'Bestand/Bedarf prüfen'}
def table(headers,entries):
 def cell(v):return v.replace('|','\\|').replace('\n',' ')
 return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(cell(x) for x in e)+' |' for e in entries])+'\n\n'
def quantity(r):return r['Menge']+' '+r['Einheit']
def supplier(r):
 return f"[{r['Lieferant']} · {r['Linkart']}]({r['Link']})" if r['Link'] else r['Lieferant']+' — Produkt offen'
inventory=', '.join(r['ID']+' '+r['Teil'] for r in rows if r['Status']=='vorhanden')
intro='Stand **04.10.2026 · Revision B · fertige Module, keine selbst gelötete Zusatzplatine**. Noch nicht aufgebaut/getestet, keine Bestellung ausgelöst. Umfang: Elektronik, elektrische Leitungen und Gehäusezubehör sowie ausdrücklich Motorhalterung ST-M7. Keine weitere Konstruktion/Mechanik.\n\n'
bom='# Material-Stückliste · Elektronik\n\n'+intro+f'**Bestätigt vorhanden:** {inventory}.\n\nAutomatisch aus [teile.csv](teile.csv) erzeugt. [Bestellliste](bestellliste.md) nennt Lieferanten; [Anschlussplan](../docs/elektronik.md) beschreibt die Verdrahtung. Leitungs-/Zubehörmengen sind Planbedarf; Packungsmengen stehen in der Bestellliste.\n\n'
for group in dict.fromkeys(r['Gruppe'] for r in rows):
 bom+='## '+group+'\n\n'+table(['ID','Menge','Teil / Spezifikation','Warum benötigt?','Status'],[[r['ID'],quantity(r),r['Teil']+' — '+r['Spezifikation'],r['Begruendung'],STATUS[r['Status']]] for r in rows if r['Gruppe']==group])
bom+='''## Lieferumfang und entfallene Teile

Motor enthält 1 m Anschlusskabel; Adafruit #5648 wird ohne STEMMA-Kabel geliefert: zwei Kabel #3894 separat bestellen. Treiber-Klemmstecker bei Lieferung prüfen. Kabel W5 ist eine fertige Verlängerung; nur dessen männliches Ende wird zum Klemmen abgeschnitten.

Steuergehäuse E37, zugehörige Montageplatte E53 und PIR-Sensorgehäuse E39 entfallen als festgelegte Projektteile. Für den etwa vierstündigen Aufbau kann bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwendet werden; kein bestimmtes Modell als Bestand bestätigt.

Aderendhülsen E43 und Crimpzange T02 sind auf Nutzerwunsch aus dem Material-/Bestellbedarf entfernt. Die Eignung der tatsächlich gelieferten Schraubklemmen für blanke Litzen ist vor Aufbau zu prüfen, siehe [Anschlussplan](../docs/elektronik.md).

Lochrasterplatinen, HCT-Chip, Sockel, Einzeltransistoren, externe Kondensatoren, Netzsicherungsaufbau und interne 230-V-Verkabelung aus Revision A entfallen. Lötwerkzeug/Lot/Flussmittel sind bestätigt vorhanden, werden für Rev. B aber nicht benötigt und stehen deshalb nicht als Projektbedarf in dieser Liste. Kein Ethernet/PoE, Home-Sensor oder Freigabeschalter im Basisaufbau.
'''
(ROOT/'bom/material-stueckliste.md').write_text(bom,encoding='utf-8')
order='# Bestellliste · Elektronik\n\n'+intro+f'**Nicht bestellen, bereits vorhanden:** {inventory}.\n\n'
order+='''Die festgelegte Elektronik ist unten mit konkreten Artikelmodellen aufgeführt. Aderendhülsen E43 und Crimpzange T02 sind auf Nutzerwunsch gestrichen; die Prüfung der Schraubklemmen für blanke Litzen bleibt im Anschlussplan festgehalten. **Steuergehäuse E37, Montageplatte E53 und PIR-Sensorgehäuse E39 nicht bestellen:** Bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwenden. Für den temporären Aufbau ist ein **trockener, geschützter Standort** angenommen; tatsächliche Montage und Zugentlastung festlegen. Offene Zubehörpositionen gehören zum vollständigen Aufbau und sind bewusst keine vermeintlich geprüften Kaufartikel.

**Lieferanforderung: Erhalt in der Schweiz binnen 7 Kalendertagen nach Bestellung.** Bei Bestellung am 03.10.2026 bedeutet das spätestens 10.10.2026. Ein angezeigter Lagerbestand plus übliche Versandzeit ist ein Angebot für die kurzfristige Beschaffung, keine garantierte Zustellung. Lieferdatum für die eigene Schweizer Adresse vor Zahlung prüfen. **Antrieb E03/E04/E47, Motornetzteil E05 und Anschlusskabel E49/E55 sind noch nicht mit passendem Liefertermin beschaffbar belegt.** Erst diese Positionen klären, bevor der gesamte Aufbau als rechtzeitig beschaffbar gilt.

**Produkt** verlinkt einen konkreten Artikel. **Offen** bedeutet: kein bestätigtes Händlerangebot oder noch ungeklärte Ausführung. Ein technisch festgelegtes Modell bleibt auch ohne Bezugsquelle erforderlich. Die Lieferbewertung stammt aus der Recherche vom 03.10.2026; Webabrufe können zwischengespeicherte Händlerangaben enthalten. **Hersteller-Standardlieferzeit** ist die Nachbeschaffungszeit und darf nicht mit dem Versand vorhandener Händler-Lagerware verwechselt werden. [Lieferbelege und Alternativen](../docs/quellen-und-entscheidungen.md#beschaffung-binnen-einer-woche). CHF-Endpreise, Packungsmengen, Einfuhr und Versand im Warenkorb prüfen. Ein Gesamtpreis ist wegen offener Zubehörmaße und Versandkosten noch nicht verlässlich berechenbar.

**Händlerwahl:** DigiKey und Farnell sind ausgeschlossen. Schweizer Händler oder Amazon bevorzugt. Ausländische Ausweichquellen sind als solche markiert. Ein CH-Shop ist kein Nachweis für ein Schweizer Versandlager; bei Amazon zählen konkreter Verkäufer, Variante und Zustellung an die Schweizer Adresse.

Die Menge ist der Bedarf. Bei E50 zwei WAGO-Einzelstücke, bei E55 zwei STEMMA-Kabel #3894, bei E56 ein fertig bestücktes Shield wählen. Vor Bestellung Module vollständig mit Anschlussklemmen/Kabeln und Treiber ausdrücklich als **V3.0** bestätigen. [Technische Auswahl und Abnahmekriterien](../docs/fertige-module.md).

Automatisch erzeugt aus [teile.csv](teile.csv); Änderungen dort pflegen.

'''
for status,title in [('bestellen','Festgelegte Elektronik und Anschlussmaterial'),('abklaeren','Bezugsquelle oder Ausführung noch klären'),('aufmass','Montagezubehör nach Aufmaß'),('bestand_pruefen','Bedingter Bedarf; zuerst Bestand prüfen')]:
 selected=[r for r in rows if r['Status']==status]
 if selected:order+='## '+title+'\n\n'+table(['Erledigt','ID','Menge','Teil / genaue Auswahl','Lieferant / Link','Lieferbewertung / Hinweis','Vor Bestellung beachten'],[['☐',r['ID'],quantity(r),r['Teil']+' — '+r['Spezifikation'],supplier(r),r['Lieferbewertung']+' — '+r['Lieferhinweis'],r['Bestellhinweis']] for r in selected])
order+='''## Beschaffung bündeln

1. **Play-Zone (CH):** zwei Adafruit-Module E48 ab eigenem Lager; Priority oder reservierte Abholung. Kabel E55 sind separat nötig und noch ohne Bezugsquelle.
2. **Bastelgarage (CH):** ein DFR0265-Shield E56 und zwei FIT0849-RJ45-Adapter E09 gemeinsam. Angezeigte Lagerware, Priority oder reservierte Abholung.
3. **Motornetzteil E05:** Simpex ist ein Schweizer Händler mit genauem Modell, zeigt aber nur „lieferbar auf Bestellung“. Zustelldatum noch offen. Distrelec/RS nennt inzwischen Nachschub erst am 16.10.2026 und erfüllt damit die Wochenfrist nicht.
4. **Antrieb und Spezialkabel:** Bezugsquelle bei Schweizer Händler oder Amazon für E03/E04/E47 und E49/E55 noch offen. Herstellerreferenzen sind keine Empfehlung für eine China-Bestellung. Keine ungeprüften Ersatzmodelle oder falschen JST-/DIN-Kabel einsetzen.
5. **BerryBase CH-Shop:** E06/E07/E50 bleiben konkrete Angebote. CH-Impressum und AGB nennen unterschiedliche Vertragsadressen; tatsächlichen Vertragspartner, Versandort und CH-Termin im Checkout prüfen. Die angezeigten 2–5 Tage sind keine bestätigte Wochenzustellung.

**Zusätzlich bestätigt vorhanden:** E26 Steuerkabel W4 und E35 DC-Leistungslitze. Beide aus Bestand verwenden; dafür entfällt die Beschaffung bei Bürklin.

E37/E53/E39 sind gestrichen. Nur tatsächlich fehlendes Montagezubehör benötigt zusätzlich Aufmaß und Lieferterminprüfung. Distrelec wird als mögliche Bezugsquelle weiter berücksichtigt. Für Amazon ist bislang kein konkretes Angebot mit passender Variante und belegtem CH-Termin aufgenommen; Suchseiten werden nicht als Bestelllinks ausgegeben. [Aktuelle Händlerprüfung](../docs/quellen-und-entscheidungen.md#schweizer-händler-oder-amazon).

Die Händleraufteilung ist kein Nachweis für den niedrigsten Schweizer Gesamtpreis. Erst Zustellung binnen sieben Kalendertagen sichern, danach Versandkosten bündeln. Fehlende Bezugsquellen dürfen nicht als vollständige, sofort bestellbare Einkaufsliste verstanden werden.

Keine Bestellung wird durch diese Liste ausgelöst. Der 230-V-Anschluss besteht ausschließlich aus fertigen Steckverbindungen. Keine zusätzliche Dienstleistung für eine selbst gebaute Netzbaugruppe eingeplant.
'''
(ROOT/'bom/bestellliste.md').write_text(order,encoding='utf-8')
print(f'Stück- und Bestellliste erzeugt: {len(rows)} Positionen.')
