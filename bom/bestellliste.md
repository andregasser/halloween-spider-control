# Bestellliste

Stand: **26.09.2026 · Revision A**. Noch keine Bestellung ausgelöst.

**Nicht bestellen:** E01 Arduino Uno R3 und E02 PIR, beide vorhanden. Alle übrigen Einbauteile sind unten aufgeführt. Werkzeuge, Verbrauchsmaterial und gegebenenfalls RCD werden nach Bestandsprüfung beschafft oder geliehen.

Ein Link zu einer Produktseite belegt die gefundene Produktfamilie, nicht jede auswählbare Variante. Mit **Bezugsquelle** gekennzeichnete Einträge nennen einen vorgeschlagenen Lieferanten, aber noch keine einzeln geprüfte Artikelnummer. Keine Lieferbarkeit oder Schweizer Versandkosten zugesichert. Bei Anfragepositionen erst Maße/Kompatibilität klären, dann bestellen. Das verhindert insbesondere Fehlkäufe bei Welle, Schellen, Gehäuse und Riemennaben.

Die ursprünglichen Budgetwerte aus dem Handover sind keine aktuellen Angebote. Vor Zahlung Endpreis in CHF einschließlich Versand/Einfuhr und Lieferdatum bis Halloween kontrollieren.

Automatisch erzeugt aus [teile.csv](teile.csv). Die [Material-Stückliste](material-stueckliste.md) erklärt den Zweck jedes Teils.

## 1. Fehlende Standardteile und festgelegte Modelle

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E03 | 1 Stück | M1 NEMA-34-Motor — STEPPERONLINE 34HS46-6004S1, 14-mm-Welle, mit 1-m-Motorkabel | [STEPPERONLINE](https://www.omc-stepperonline.com/fr/moteur-pas-a-pas-nema-34-serie-s-8-5nm-1203-94oz-in-14mm-arbre-a-cle-cable-1m-34hs46-6004s1) | Produktseite geprüft, Passfeder-Lieferumfang bestätigen |
| ☐ | E04 | 1 Stück | U3 Schrittmotortreiber — STEPPERONLINE DM860T V3.0 mit 5/24-V-Wahlschalter | [STEPPERONLINE](https://www.omc-stepperonline.com/digital-stepper-driver-2-4-7-2a-18-80vac-or-24-110vdc-for-nema-34-motor-dm860t) | Produktseite geprüft, V3.0 und passende Klemmstecker vor Kauf bestätigen |
| ☐ | E05 | 1 Stück | PS1 Motornetzteil — Mean Well LRS-350-48, 48 V / 7,3 A | [STEPPERONLINE](https://www.omc-stepperonline.com/fr/lrs-350-48-mean-well-350w-48vdc-7-3a-115-230vac-alimentation-a-decoupage-fermee-lrs-350-48) | Produktseite gefunden, Herstellerhinweise zum Einsatzort und CH-Versand prüfen |
| ☐ | E06 | 1 Stück | PS2 USB-Netzteil — Geschlossen, geregelt 5 V / mindestens 1 A, USB-A, CH-tauglicher Stecker | [Digitec Galaxus](https://www.digitec.ch/) | Bezugsquelle, konkretes Markenmodell mit Sicherheitszulassung wählen |
| ☐ | E07 | 1 Stück | W2 USB-Kabel — USB-A auf USB-B, Datenkabel, etwa 1 m | [Digitec Galaxus](https://www.digitec.ch/) | Bezugsquelle, kein USB-C/Micro-USB am Uno R3 |
| ☐ | E08 | 1 Stück | W3 Patchkabel — Cat5e/Cat6 Vollkupfer, 1:1 T568B, bis 3 m | [Digitec Galaxus](https://www.digitec.ch/) | Bezugsquelle, kein Crossover, keine CCA-Adern |
| ☐ | E09 | 2 Stück | J1/J2 RJ45-Klemmenadapter — 8P8C-Buchse auf nummerierte Schraubklemmen, passiv ohne Magnetics | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Schirmkontakt nicht intern mit Signalklemmen verbunden |
| ☐ | E10 | 1 Stück | U2 Schmitt-Trigger — Texas Instruments SN74HCT14N, DIP-14 | [DigiKey Schweiz](https://www.digikey.ch/) | Exakte Herstellernummer suchen, ausdrücklich HCT und DIP |
| ☐ | E11 | 1 Stück | IC-Sockel — DIP-14, 7,62-mm-Reihenabstand | [Reichelt](https://www.reichelt.com/) | Bezugsquelle |
| ☐ | E12 | 2 Stück | Q1/Q2 NPN-Transistor — onsemi 2N3904, TO-92, E/B/C nach Datenblatt | [DigiKey Schweiz](https://www.digikey.ch/) | Herstellernummer und Pinbelegung prüfen |
| ☐ | E13 | 3 Stück | R1/R2/R5 Widerstände — 1 kΩ, 0,25 W, Metallfilm, bedrahtet | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, günstige Packung möglich |
| ☐ | E14 | 3 Stück | R3/R4/R6 Widerstände — 100 kΩ, 0,25 W, bedrahtet | [Reichelt](https://www.reichelt.com/) | Bezugsquelle |
| ☐ | E15 | 1 Stück | R7 Widerstand — 10 kΩ, 0,25 W, bedrahtet | [Reichelt](https://www.reichelt.com/) | Bezugsquelle |
| ☐ | E16 | 3 Stück | C1/C3/C5 Keramikkondensatoren — 100 nF, mindestens 25 V, bedrahtet | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, C3 am Sensor montieren |
| ☐ | E17 | 2 Stück | C2/C4 Elektrolytkondensatoren — 10 µF, 16 V oder höher, radial | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Polarität beachten |
| ☐ | E18 | 1 Stück | Steuer-Lochrasterplatine — Einzelpads 2,54 mm, etwa 100×80 mm | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, keine Netzspannung auf dieser Platine |
| ☐ | E19 | 1 Stück | Sensor-Lochrasterplatine — Einzelpads 2,54 mm, etwa 30×30 mm | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, an Sensorgehäuse anpassen |
| ☐ | E20 | 1 Stück | J0 Anschlussklemme — 6-polig, Platinenklemme mit passendem Raster | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, 5,08-mm-Raster passt auf 2,54-mm-Lochraster |
| ☐ | E21 | 1 Stück | J3 Anschlussklemme — 4-polig, Raster 5,08 mm | [Reichelt](https://www.reichelt.com/) | Bezugsquelle |
| ☐ | E22 | 1 Stück | J4 Anschlussklemme — 2-polig, Raster 5,08 mm | [Reichelt](https://www.reichelt.com/) | Bezugsquelle |
| ☐ | E23 | 1 Satz | PIR-Anschlussleitung — 3-polige 2,54-mm-Buchse mit Litzen, etwa 20 cm | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Reihenfolge nach tatsächlicher B1-Beschriftung |
| ☐ | E24 | 1 Satz | Uno-Verbindungsleitungen — 6 einzelne passende Header-Steckleitungen, etwa 20 cm | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, zugentlasten und mechanisch sichern |
| ☐ | E25 | 1 Stück | S1 Freigabeschalter — Rastender EIN/AUS-Schalter, 1 Schließer, kleinspannungstauglich | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Beschriftung FREIGABE, keine Not-Halt-Funktion behaupten |
| ☐ | E26 | 0,5 m | W4 Steuerkabel — 2 geschirmte verdrillte Paare, etwa 0,25 mm² | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Schirm einseitig an PE |
| ☐ | E27 | 5 m | Kleinspannungslitze — 0,25–0,5 mm², mehrere Farben, Gesamtmenge | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Menge mit Reserve |
| ☐ | E29 | 2 m | W1 Netzanschlussleitung — CH-Typ-J-Stecker, offene Geräteenden, 3G1,5 mm², für Aufstellort geeignet | [Elektrofachhandel / Reichelt](https://www.reichelt.com/) | Montage durch Elektrofachperson |
| ☐ | E30 | 1 Stück | F1 Netzsicherung — SCHURTER SPT 0001.2532, T6,3 A, 6,3×32 mm, 250 VAC | [DigiKey Schweiz](https://www.schurter.com/en/datasheet/typ_spt_6.3x32.pdf) | Datenblatt geprüft, Projekt-Auslegungswert durch Elektrofachperson bestätigen |
| ☐ | E31 | 1 Stück | F2 DC-Sicherung — SCHURTER SPT 0001.2533, T8 A, 6,3×32 mm, 63 VDC | [DigiKey Schweiz](https://www.schurter.com/en/datasheet/typ_spt_6.3x32.pdf) | Datenblatt geprüft, keine nur für 32 V zugelassene KFZ-Sicherung |
| ☐ | E32 | 2 Stück | Sicherungshalter — Berührungsgeschützt für 6,3×32 mm, mindestens 10 A, 250 VAC und 63 VDC, Klemmenanschluss | [DigiKey Schweiz](https://www.digikey.ch/) | Bezugsquelle, konkrete AC/DC-Zulassung und Montageart prüfen |
| ☐ | E33 | 1 Satz | XPE Schutzleiterverteilung — PE-Klemmenblock mit mindestens 6 Anschlüssen und Befestigung | [Elektrofachhandel / Reichelt](https://www.reichelt.com/) | Bezugsquelle, sichere PE-Verbindung zur Montagefläche herstellen |
| ☐ | E34 | 3 m | Schutzleiterlitze — 1,5 mm², grün-gelb | [Elektrofachhandel / Reichelt](https://www.reichelt.com/) | Bezugsquelle, Menge mit Reserve |
| ☐ | E35 | 2 m | DC-Leistungslitze — 1,5 mm², rot und schwarz, zusammen 2 m | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Verbindungen kurz halten |
| ☐ | E36 | 1 m | Netz-Installationslitze — 1,5 mm², braun und blau, zusammen 1 m | [Elektrofachhandel / Reichelt](https://www.reichelt.com/) | Bezugsquelle, nur im abgetrennten Netzbereich |
| ☐ | E42 | 12 Stück | Platinen-Abstandshalter — M3, isolierend, passende Schrauben/Muttern | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, Uno-Lochabstände und Bauteilunterseite prüfen |
| ☐ | E43 | 1 Satz | Aderendhülsen, Ringkabelschuhe und PE-Schrauben — Zu 0,25–1,5 mm² und jeweiligen Klemmen, Ringösen für PE | [Reichelt](https://www.reichelt.com/) | Bezugsquelle, PE mit geeigneten Zahnscheiben/Sicherung befestigen |
| ☐ | E44 | 1 Satz | Schrumpfschlauch, Kabelbinder und Beschriftung — Verschiedene Durchmesser, Kabelhalter, Etiketten | [Reichelt](https://www.reichelt.com/) | Beschriftungen PIR 5V KEIN LAN/PoE, 48V, PE, S0 und S1 vorsehen |
| ☐ | M01 | 1 Stück | Motorhalter — STEPPERONLINE ST-M7 für NEMA 34 | [STEPPERONLINE](https://www.omc-stepperonline.com/de/nema-34-halterung-fuer-schrittmotor-halterung-aus-legiertem-stahl-st-m7) | Produktseite geprüft, erforderliche Einbaulage überprüfen |
| ☐ | M04 | 1 Stück | Zahnriemen — Geschlossen HTD 450-5M-15, 90 Zähne, 15 mm breit | [ConCar](https://www.concar-shop.de/shop/en/belts/timing-belts/timing-belts/gates-synchronous-belts-powergrip-htd/gates-synchronous-belts-powergrip-htd-dimension-5m.html) | Geprüfte Variante GT045005015, Preis/CH-Versand prüfen, frühere CHF-20–30-Gesamtschätzung nicht bestätigt |
| ☐ | M06 | 2 Stück | Flanschlager — UCFL204, 20-mm-Bohrung, DOLD Artikel 35334 | [DOLD Mechatronik](https://www.dold-mechatronik.de/Flanschlager-20mm-UCFL-204) | Produktseite geprüft, beide identische Ausführung bestellen |
| ☐ | M07 | 2 Stück | Geteilte Wellen-Klemmringe — 20-mm-Bohrung, zur Lageranordnung passend | [DOLD Mechatronik](https://www.dold-mechatronik.de/) | Bezugsquelle, Baubreite im Wellenlayout berücksichtigen |
| ☐ | M15 | 1 Streifen | Gummieinlage — Etwa 2–3 mm, zwischen Rohr und Schellen | [Hornbach Schweiz](https://www.hornbach.ch/) | Bezugsquelle, Auflageflächen anpassen |
| ☐ | M21 | 2 Stück | Befestigungsgurte — Zur Spinne und Wagenplatte passend | [Hornbach Schweiz](https://www.hornbach.ch/) | Bezugsquelle |

## 2. Fehlende Teile mit noch zu bestätigender Ausführung

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E28 | 1 Stück | S0 Netzverteilung/Hauptschalter — Fertig konfektioniert, zweipolig schaltend, Schutzleiter durchverbunden, mindestens 2 Ausgänge, CH-Stecker | [Elektrofachhandel / Elektroinstallateur](https://www.brennenstuhl.com/) | Bezugsquelle, Eignung für PS1-Einschaltstrom 60 A und Aufstellort vor Bestellung nachweisen |
| ☐ | M02 | 1 Stück | Motor-Riemenscheibe — HTD-5M, 20T, für 15-mm-Riemen, Bohrung 14 mm mit passender Nut | [eBay, Händler glhk01](https://www.ebay.com/itm/156430925515) | 20T + 15 mm + 14 mm (5×2,3-mm-Nutangabe) auswählen, Motorpassfeder und Nabenlänge bestätigen |
| ☐ | M03 | 1 Stück | Hauptachsen-Riemenscheibe — HTD-5M, 40T, für 15-mm-Riemen, Bohrung 20 mm mit passender Nut | [eBay, Händler glhk01](https://www.ebay.com/itm/156430925515) | 40T + 15 mm + 20 mm (6×2,8-mm-Nutangabe) auswählen, passend zu bearbeiteter Welle |
| ☐ | M08 | 1 Stück | Flansch-Klemmnabe — 20-mm-Bohrung, geschlitzte Klemmung, dokumentiertes Moment mindestens 20 Nm | [Mädler / mechanische Werkstatt](https://www.maedler.de/) | Anfrageposition, konkretes Modell und Lochbild noch auswählen, keine bestätigte günstige SKU |
| ☐ | M09 | 1 Stück | Passfeder Motor — Zur 14-mm-Motorwelle und M02 passend | [STEPPERONLINE / DOLD](https://www.omc-stepperonline.com/) | Nur separat kaufen, falls nicht im Motorlieferumfang, Breite/Höhe/Länge abgleichen |

## 3. Fehlende Teile nach Aufmaß/Zuschnitt

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E37 | 1 Stück | Steuergehäuse mit Montageplatte — Metall, abschließbar/verschraubt, Planmaß ca. 400×300×180 mm, Lüftung und Trennbereich | [Reichelt / Elektrogehäuse-Fachhandel](https://www.reichelt.com/) | Maß anhand PS1/U3 und Biegeradien bestätigen, nicht einfach luftdicht verschließen |
| ☐ | E38 | 1 Satz | Lüftungselemente und Wetterschutz — Geschützte Zu-/Abluftöffnungen, Regenhaube bei Außenbetrieb | [Elektrogehäuse-Fachhandel / Reichelt](https://www.reichelt.com/) | Gehäuseausführung und Wärmetest bestimmen Größe, kein unbelegter IP-Wert |
| ☐ | E39 | 1 Stück | Sensorgehäuse mit Halter — Platz für PIR, J2 und C3/C4, Linse frei, Spritzwasserschutz | [Hornbach Schweiz](https://www.hornbach.ch/) | Bezugsquelle, kein normales Glas vor der PIR-Linse |
| ☐ | E40 | 1 Satz | Kabelverschraubungen/Zugentlastungen — Mindestens 5 passende Durchführungen für Netz, Motor, USB, Sensor und Motor-PE | [Reichelt](https://www.reichelt.com/) | Klemmbereich passend zu realen Kabeldurchmessern wählen |
| ☐ | E41 | 1 Satz | Klemmenabdeckungen und Trennwand — Isolierend, flammhemmend, zwischen Netz- und Steuerbereich | [Elektrofachhandel / Reichelt](https://www.reichelt.com/) | Mit Gehäuse und Klemmenanordnung abstimmen |
| ☐ | M05 | 1 Stück | Hauptachse — Stahl 20 mm, ca. 200 mm, bearbeitbar, Passfedernut zur 40T-Scheibe | [DOLD Mechatronik / mechanische Werkstatt](https://www.dold-mechatronik.de/) | Fertigbearbeitung anfragen, Nabenmaße festlegen, keine gehärtete Linearwelle ohne Bearbeitung kaufen |
| ☐ | M10 | 1 Stück | Passfeder Hauptachse — Zur 20-mm-Welle und M03 passend | [DOLD Mechatronik / mechanische Werkstatt](https://www.dold-mechatronik.de/) | Nutbreite typischerweise 6 mm, konkrete Höhe/Länge und Zeichnung bestätigen |
| ☐ | M11 | 1 Satz | Grundrahmen mit zwei Lagerträgern — Steife Grundplatte, zwei parallele Tragebenen, Lagerabstand etwa 80–120 mm | [Hornbach Schweiz / lokale Metallwerkstatt](https://www.hornbach.ch/) | Materialstärken, Lochbild und Abmessungen nach Layout festlegen |
| ☐ | M12 | 1 Stück | Verschiebbare Motoraufnahme — Langlöcher für etwa 140–160 mm Achsabstand | [Lokale Metallwerkstatt / Hornbach Schweiz](https://www.hornbach.ch/) | Kein zusätzlicher Riemenspanner erforderlich, Lochbild ST-M7 übernehmen |
| ☐ | M13 | 1 Stück | Arm-Montageplatte — Metallplatte, passend zu M08 und zwei Rohrschellen | [Lokale Metallwerkstatt / Hornbach Schweiz](https://www.hornbach.ch/) | Größe und Dicke nach Rohrdurchmesser, Schellenabstand und Nabenlochbild |
| ☐ | M14 | 2 Stück | Rohrschellen/U-Bügel mit Gegenplatten — Passend zum gemessenen Kunststoffrohr-Außendurchmesser | [Hornbach Schweiz](https://www.hornbach.ch/) | Rohrdurchmesser vor Kauf messen |
| ☐ | M16 | 1 m | Kunststoffrohr — Etwa 1 m Arm, Durchmesser/Wandstärke noch festzulegen | [Hornbach Schweiz](https://www.hornbach.ch/) | Bestand aus Vorarbeiten abgleichen, mechanische Eignung prüfen |
| ☐ | M17 | 1 Satz | Wagen-Rohr-Aufnahme — Befestigte Aufnahme mit gesichertem Gelenkbolzen und Gegenplatte | [Hornbach Schweiz / lokale Metallwerkstatt](https://www.hornbach.ch/) | Rohr-, Wagen- und Bodenmaße bestimmen Ausführung |
| ☐ | M18 | 1 Stück | Wagenplatte — Stabile wettergeeignete Holz-/Siebdruckplatte, zur Spinne passend | [Hornbach Schweiz](https://www.hornbach.ch/) | Maße und möglicher Bestand aus Vorarbeiten vor Neukauf prüfen |
| ☐ | M19 | 6 Stück | Kugelgelagerte Rollen — Für Boden und Kreisfahrt geeignet, schwenkbar oder tangential ausgerichtet | [Hornbach Schweiz](https://www.hornbach.ch/) | Raddurchmesser/Befestigung/Tragfähigkeit wählen, möglicher Bestand prüfen |
| ☐ | M20 | 1 Stück | Halloween-Spinne — Abmessungen zum Wagen, Gesamtmasse Wagen/Spinne etwa 5 kg | [Galaxus / Halloween-Fachhandel](https://www.galaxus.ch/) | Wunschmodell und möglicher Bestand aus Vorarbeiten prüfen |
| ☐ | M22 | 1 Satz | Mechanische Schrauben/Muttern/Scheiben — Mindestens 4 Motor-, 4 Lager-, 4 Halter-, 4 Naben-, 4 Schellenbefestigungen, plus Rahmen/Rollen | [Hornbach Schweiz / DOLD](https://www.hornbach.ch/) | Gewinde und Längen nach gelieferten Lochbildern, Rollen ggf. 24 zusätzliche Befestigungen |
| ☐ | M23 | 1 Satz | Riemenabdeckung mit Befestigung — Feste Abdeckung beider Scheiben und des Riemens | [Hornbach Schweiz / lokale Metallwerkstatt](https://www.hornbach.ch/) | Abdeckung darf Riemen/Naben nicht berühren |
| ☐ | M24 | 1 Satz | Grundrahmen-Verankerung — Bodenabhängige Schrauben, Anker oder geeignete Ballastierung | [Hornbach Schweiz](https://www.hornbach.ch/) | Untergrund und Kräfte vor Auswahl prüfen |
| ☐ | M25 | 1 Satz | Abgrenzung des Bewegungsbereichs — Absperrung außerhalb Kreisbahn inklusive Wagenüberstand | [Hornbach Schweiz](https://www.hornbach.ch/) | Umfang nach Montageort festlegen |

## 4. Werkstattbestand und bedingter Bedarf

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E45 | 1 Stück | RCD-Zwischenstecker bei fehlendem geeignetem RCD — 30 mA, CH-tauglich, zum Aufstellort passend | [Elektrofachhandel](https://www.galaxus.ch/) | Nur beschaffen, wenn kein passender geprüfter Schutz vorgeschaltet ist |
| ☐ | V01 | 1 Packung | Elektroniklot und Flussmittel — Für bedrahtete Kleinspannungselektronik geeignet | [Reichelt](https://www.reichelt.com/) | Werkstattbestand prüfen, nur fehlende Menge beschaffen |
| ☐ | V02 | 1 Flasche | Mittelfeste Schraubensicherung — Für geeignete metallische Gewindeverbindungen | [Hornbach Schweiz](https://www.hornbach.ch/) | Herstellerhinweise beachten, nicht auf Kunststoff oder elektrische Kontakte |
| ☐ | T01 | 1 Satz | Lötstation, Seitenschneider und Abisolierer — Für bedrahtete Bauteile und Leitungsquerschnitte geeignet | [Reichelt](https://www.reichelt.com/) | Kein Einbauteil, leihen oder vorhandenes Werkzeug nutzen |
| ☐ | T02 | 1 Stück | Crimpzange — Passend zu Aderendhülsen/Kabelschuhen | [Reichelt](https://www.reichelt.com/) | Kein Einbauteil, Elektrofachperson hat Netzverdrahtungswerkzeug |
| ☐ | T03 | 1 Stück | Multimeter — Durchgang, Widerstand und DC-Spannung | [Reichelt](https://www.reichelt.com/) | Netzseitige Messungen durch Fachperson mit geeignetem Messgerät |
| ☐ | T04 | 1 Stück | Logikanalysator oder Oszilloskop — Für 5-V-Signale und Mikrosekunden-Pulse geeignet | [Reichelt](https://www.reichelt.com/) | Kein Einbauteil, Ausleihe genügt |
| ☐ | T05 | 1 Satz | Mechanik-Werkzeug und Federwaage — Messschieber, Bohrer, Gewindewerkzeug, Schlüssel, Zugkraftmessung | [Hornbach Schweiz](https://www.hornbach.ch/) | Bearbeitung bei Bedarf durch Werkstatt statt Werkzeugneukauf |

## 5. Zusätzlich einplanen: Leistungen

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
