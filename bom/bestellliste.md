# Bestellliste · Elektronik

Stand **03.10.2026 · Revision B · fertige Module, keine selbst gelötete Zusatzplatine**. Noch nicht aufgebaut/getestet, keine Bestellung ausgelöst. Umfang: Elektronik, elektrische Leitungen und Gehäusezubehör sowie ausdrücklich Motorhalterung ST-M7. Keine weitere Konstruktion/Mechanik.

**Nicht bestellen, bereits vorhanden:** E01 U1 Arduino Uno R3, E02 B1 PIR-Modul, E08 W3 Patchkabel, E23 PIR-Anschlussleitung, E24 Uno-Verbindungsleitungen, E28 S0 CH-Mehrfachsteckdose/Hauptschalter, E42 Platinen-Abstandshalter, E44 Schrumpfschlauch, T03 Multimeter, T04 Logikanalysator.

Die festgelegte Elektronik ist unten mit konkreten Artikelmodellen aufgeführt. Gehäuse und Durchführungen setzen derzeit einen **trockenen, geschützten Standort** voraus; Ausführung nach realem Layout bestätigen. Offene Zubehörpositionen gehören zum vollständigen Aufbau und sind bewusst keine vermeintlich geprüften Kaufartikel.

**Produkt** verlinkt einen konkreten Artikel. **Offen** bedeutet: kein bestätigter Artikel, erst nach Aufmaß/Bestandsprüfung bestellbar. Linkrecherche und technische Auswahl sind keine Liefer- oder Hardwarefunktionszusage. CHF-Endpreise, Packungsmengen, Einfuhr, Versand und Halloween-Lieferdatum im Warenkorb prüfen. Ein Gesamtpreis ist wegen offener Zubehörmaße und Versandkosten noch nicht verlässlich berechenbar.

Die Menge ist der Bedarf. Bei E50 zwei WAGO-Einzelstücke, bei E55 zwei STEMMA-Kabel #3894, bei E56 ein fertig bestücktes Shield wählen. Vor Bestellung Module vollständig mit Anschlussklemmen/Kabeln und Treiber ausdrücklich als **V3.0** bestätigen. [Technische Auswahl und Abnahmekriterien](../docs/fertige-module.md).

Automatisch erzeugt aus [teile.csv](teile.csv); Änderungen dort pflegen.

## Festgelegte Elektronik und Anschlussmaterial

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E03 | 1 Stück | M1 NEMA-34-Motor — STEPPERONLINE 34HS46-6004S1, 14-mm-Welle, mit 1-m-Motorkabel | [STEPPERONLINE · Produkt](https://www.omc-stepperonline.com/fr/moteur-pas-a-pas-nema-34-serie-s-8-5nm-1203-94oz-in-14mm-arbre-a-cle-cable-1m-34hs46-6004s1) | Produktseite geprüft, Motorvariante bestätigen |
| ☐ | E47 | 1 Stück | Motorhalterung für M1 — STEPPERONLINE ST-M7, Stahl-Montagewinkel für NEMA 34 / 86-mm-Motoren | [STEPPERONLINE · Produkt](https://www.omc-stepperonline.com/nema-34-bracket-for-stepper-motor-alloy-steel-bracket-st-m7) | Ein Stück ST-M7 mit dem Motor bestellen. Hersteller ordnet ST-M7 NEMA-34-Schrittmotoren zu. Vor Montage Lochbild, Zentrierbund und Freiraum am 34HS46-6004S1 abgleichen. Schraubenlieferumfang nicht bestätigt; Befestigungsmittel und Schraubenlängen passend zu Motorflansch und Träger ergänzen. Montage für senkrechte Motorwelle und verschiebbare Riemenspannung vorsehen. CH-Endpreis/Versand im Warenkorb prüfen. |
| ☐ | E04 | 1 Stück | U3 Schrittmotortreiber — STEPPERONLINE DM860T V3.0 mit 5/24-V-Wahlschalter | [STEPPERONLINE · Produkt](https://www.omc-stepperonline.com/digital-stepper-driver-2-4-7-2a-18-80vac-or-24-110vdc-for-nema-34-motor-dm860t) | Produktseite geprüft, V3.0 und passende Klemmstecker vor Kauf bestätigen |
| ☐ | E05 | 1 Stück | PS1 geschlossenes Motornetzteil — Mean Well GST220A48-R7B, 48 V / 4,6 A / 221 W, IEC-C14 und Power-DIN-R7B | [DigiKey Schweiz / alternativ Distrelec · Produkt](https://www.digikey.ch/de/products/detail/mean-well-usa-inc/GST220A48-R7B/7703644) | Ein Stück GST220A48-R7B, nicht LRS-350. Netzleitung W1 separat. Distrelec 300-42-762: https://www.distrelec.ch/en/power-supply-gst220a-series-48v-6a-221w-iec-60320-c14-din-pin-mean-well-gst220a48-r7b/p/30042762 . CHF-Endpreis/Liefertermin nicht bestätigt. Für langsamen Einzelmotorbetrieb ausgewählt, Leistungs- und Bremstest erforderlich. |
| ☐ | E06 | 1 Stück | PS2 USB-Netzteil — Geschlossenes Steckernetzteil, geregelt 5 V / mindestens 1 A, USB-A, CH-Stecker oder flacher Eurostecker | [BerryBase Schweiz · Produkt](https://www.berrybase.ch/dual-usb-netzteil-ladeadapter-2-4a-2x-usb-flache-bauform-weiss) | Goobay 44952: 5 V / 2,4 A gesamt, USB-A, Eurostecker. Einen Anschluss für U1 verwenden. |
| ☐ | E07 | 1 Stück | W2 USB-Kabel — USB-A auf USB-B, Datenkabel, etwa 1 m | [BerryBase Schweiz · Produkt](https://www.berrybase.ch/usb-2.0-hi-speed-kabel-a-stecker-b-stecker-schwarz) | Goobay USB 2.0 A auf B; gewünschte Länge um 1 m auswählen. Kein Mini-/Micro-B. Alternative: [Distrelec 305-04-706](https://www.distrelec.ch/de/usb-male-usb-to-male-usb-1m-stecker-1m-usb-schwarz-com-u2a00002-1m/p/30504706), L-Com U2A00002-1M, USB 2.0 A–B, 1 m. Bedarf ein Kabel. Produktdaten im Suchindex bestätigt; Direktabruf blockiert, Preis/Bestelleinheit/Lagerbestand offen. |
| ☐ | E09 | 2 Stück | J1/J2 RJ45-Klemmenadapter — 8P8C-Buchse auf nummerierte Schraubklemmen, passiv ohne Magnetics | [Bastelgarage · Produkt](https://www.bastelgarage.ch/rj45-buchse-8p-adapter-mit-schraubklemme) | Art. 423938, DFRobot FIT0849. Zwei Buchsenadapter bestellen; keine Steckeradapter. Pinzuordnung vor Anschluss durchmessen. |
| ☐ | E48 | 2 Stück | U4/U5 fertige Signalmodule — Adafruit MOSFET Driver #5648, STEMMA-JST-PH und montierte Ausgangs-Federklemmen | [DigiKey Schweiz · Produkt](https://www.digikey.ch/de/products/detail/adafruit-industries-llc/5648/17282414) | 1528-5648-ND, zwei Einzelmodule. STEMMA-Kabel E55 separat, keine Stiftleisten nötig. Nur nominal 5 V, nicht 48 V. Ausgang +/− geht an PUL+/PUL− bzw. DIR+/DIR−. |
| ☐ | E55 | 2 Stück | STEMMA-Anschlusskabel für U4/U5 — Adafruit #3894, JST PH 2 mm, 3-polig auf einzelne weibliche Header-Buchsen, 200 mm | [DigiKey Schweiz · Produkt](https://www.digikey.ch/de/products/detail/adafruit-industries-llc/3894/9603620) | 1528-3894-ND, zwei Einzelkabel. Buchsenenden passen auf U6-Stiftleisten. Nicht #3893 (männliche Enden) und nicht 4-poliges Kabel. Im #5648-Modul nicht enthalten. |
| ☐ | E56 | 1 Stück | U6 fertiges Uno-Anschluss-Shield — DFRobot DFR0265, IO Expansion Shield V7.1, fertig bestückt | [BerryBase Schweiz · Produkt](https://www.berrybase.ch/fr/dfrobot-io-expansion-shield-fuer-arduino-xbee-uart-schnellwechselschalter-i2c-spi-bt-3.3-5v) | DFR0265, ein Shield mit montierten Stiftleisten/Jumper. Auf Uno R3 stecken, 5V/3.3V-Jumper auf 5 V. Keine externe Versorgung, keine XBee-Module. Modulversorgung über A1/A2, Signal über D2/D3. |
| ☐ | E50 | 2 Stück | X1/X2 Verbindungsklemmen — WAGO 221-413, 3 Leiter | [BerryBase Schweiz · Produkt](https://www.berrybase.ch/wago-221-413-verbindungsklemme-3-fach) | W221-413-1: zwei Einzelstücke, keine Mehrfachpackungen. Je Leiter eigener Platz, 11 mm Kontaktlänge. |
| ☐ | E26 | 0,5 m | W4 Steuerkabel — 2 geschirmte verdrillte Paare, etwa 0,25 mm² | [Conrad Schweiz · Produkt](https://www.conrad.ch/de/p/lapp-35800-1-datenleitung-unitronic-liycy-tp-2-x-2-x-0-25-mm-grau-1-m-601980.html) | Art. 601980, LAPP 35800/1: 2×2×0,25 mm², paarverseilt und geschirmt. 1 m kaufen, ca. 0,5 m verwenden. |
| ☐ | E29 | 1 Stück | W1 Netzanschlussleitung — Fertiges Typ-12-auf-IEC-C13-Netzkabel mit Schutzleiter, 1,8 m | [Simpex Schweiz · Produkt](https://www.simpex.ch/en/shop/power-supplies/cables-and-accessories/apparate-netzkabel-schweiz-3-pol-1-8-m-schwarz/) | POWER CABLE T12-C13, ein Einzelkabel. Am Gerätekabel IEC-C13-Buchse für PS1-C14-Eingang, keine offenen Enden und kein C14-Stecker. |
| ☐ | E49 | 1 Stück | W5 Power-DIN-Verlängerung — GlobTek KPPX4124641M0KPJX4(R), 1 m, 4×AWG18, Stecker/Buchse | [DigiKey Schweiz · Produkt](https://www.digikey.ch/de/products/detail/globtek-inc/KPPX4124641M0KPJX4-R/12343635) | 1939-KPPX4124641M0KPJX4(R)-ND, ein Kabel. Produkt/Herstellerdaten bestätigt, CH-Preis/Liefertermin offen. Nur männliches Verlängerungsende abschneiden. Beide + und beide − Adern verwenden. Kontaktlage durchmessen, unterschiedliche Hersteller-Pinnummerierung! Kein gewöhnlicher RJ45- oder Mini-DIN-Stecker. |
| ☐ | E35 | 1 m | DC-Leistungslitze — 1,5 mm² Kupfer-Silikonlitze, schwarz, 1 m; zwei kurze Abschnitte | [Elektrobedarf Troller · Produkt](https://www.elektrobedarf.ch/silikonlitze-180%C3%B8-1-5mm2-schwarz-d%201903.20) | Art. D1903.20, Bedarf 1 m Meterware. Bestelleinheit beim Händler bestätigen, keine ganze 100-m-Rolle. Positive Ader mit vorhandenem Schrumpfschlauch/Beschriftung markieren, je Verbindung möglichst kurz. |

## Ausführung noch klären

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E43 | 1 Satz | Aderendhülsen, Ringkabelschuhe und PE-Schrauben — Aderendhülsen für tatsächliche Schraubklemmen und 0,25/1,5 mm² sowie Motorkabel | Elektrogehäuse-/Elektroniklieferant, Auswahl offen — Produkt offen | Querschnitt der mitgelieferten Motorleitungen und Klemmvorgaben prüfen. Konkrete Größen/Mengen danach wählen. Keine PE-Ringkabelschuhe im Basisaufbau. |

## Gehäuse und Zubehör nach Aufmaß

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E37 | 1 Stück | Steuergehäuse mit Montageplatte — Vorgeschlagen Hammond 1554YAGY ABS, 300×240×120 mm, trockener geschützter Ort | [DigiKey Schweiz · Produkt](https://www.digikey.ch/de/products/detail/hammond-manufacturing/1554YAGY/11498211) | 164-1554YAGY-ND, ein Gehäuse. Modell vorläufig: realen Modulplan und Kühlung prüfen. ABS-Ausführung nur für geschützte Aufstellung vorgesehen. 48-V-Netzteil außerhalb. Befestigung und notwendige Lüftung nach Temperaturtest festlegen. |
| ☐ | E53 | 1 Stück | Montageplatte für Steuergehäuse — Hammond 1554YPL, passende Stahl-Innenplatte | [DigiKey Schweiz · Produkt](https://www.digikey.ch/de/products/detail/hammond-manufacturing/1554YPL/11498199) | 164-1554YPL-ND, ein Stück nur bei bestätigtem 1554YAGY. Lochbild selbst anordnen, Uno/Module isoliert über vorhandene Abstandshalter befestigen. |
| ☐ | E38 | 1 Satz | Lüftungselemente und Wetterschutz — Lüftung zum tatsächlichen Gehäuse; DM860T-Umgebung maximal 40 °C | Elektrogehäuse-/Elektroniklieferant, Auswahl offen — Produkt offen | Nach Gehäuselayout/Temperaturprüfung bestimmen. Kein fertiges Modell behauptet. Kein Regenbetrieb ohne neue Auslegung. |
| ☐ | E39 | 1 Stück | PIR-Sensorgehäuse — PIR-Sensorgehäuse für B1 und J2, Linse freiliegend | Elektrogehäuse-/Elektroniklieferant, Auswahl offen — Produkt offen | Sensor und Adapter tatsächlich messen, Linse frei, feste Ausrichtung. Modell nach Aufstellort/Abmessungen festlegen. |
| ☐ | E40 | 1 Satz | Kabelverschraubungen/Zugentlastungen — Mindestens vier Steuerbox-Durchführungen: W2/W3/W5/Motorkabel; eine am Sensor | Elektrogehäuse-/Elektroniklieferant, Auswahl offen — Produkt offen | Kabeldurchmesser UND USB-/RJ45-Steckergröße messen. Fertige Stecker nicht zum Durchziehen abschneiden. Geteilte Durchführung oder Montageöffnung samt Zugentlastung vorsehen. Stückzahl/Modell erst nach Gehäuselayout. |
| ☐ | E54 | 1 Satz | Befestigungen für Treiber, Klemmen und Motorhalterung — Passende Schrauben/Muttern/Unterlegscheiben, ggf. WAGO-Halter | Elektronik-/Befestigungslieferant, Auswahl offen — Produkt offen | Lieferumfang von Treiber/ST-M7 prüfen. Schraubenlängen nach Materialdicke und Motorflansch wählen, nicht pauschal erfinden. Gehäuse/Platine nicht leitend überbrücken. |

## Bedingter Bedarf; zuerst Bestand prüfen

| Erledigt | ID | Menge | Teil / genaue Auswahl | Lieferant / Link | Vor Bestellung beachten |
|---|---|---|---|---|---|
| ☐ | E46 | 1 Satz | Elektrische Beschriftung — Elektrische Beschriftung für PIR 5V KEIN LAN/PoE, 48V und Gerätekennungen | Elektrogehäuse-/Elektroniklieferant, Auswahl offen — Produkt offen | Vorhandenes Beschriftungsmaterial verwenden, nur fehlenden Bestand kaufen. |
| ☐ | E45 | 1 Stück | RCD-Zwischenstecker bei fehlendem geeignetem RCD — 30 mA, CH-tauglich, zum Aufstellort passend | Schweizer Elektrofachbetrieb — Produkt offen | Nur bei fehlendem geeignetem vorgeschaltetem RCD und entsprechendem Aufstellbedarf. Kein zusätzlicher RCD pauschal vorgeschrieben; tatsächlichen Anschluss prüfen. |
| ☐ | T02 | 1 Stück | Crimpzange für Aderendhülsen — Für Aderendhülsen 0,25–2,5 mm² | [BerryBase Schweiz · Produkt](https://www.berrybase.ch/crimpzange-fuer-aderendhuelsen-0-25-2-5mm2) | Nur bei fehlendem Bestand beschaffen oder ausleihen; für gewählte Aderendhülsen. Keine Ringösen oder Netzverdrahtung erforderlich. |

## Beschaffung bündeln

1. **STEPPERONLINE:** Motor E03, Halterung E47, Treiber E04.
2. **Bastelgarage:** zwei RJ45-Buchsenadapter E09.
3. **BerryBase Schweiz:** USB-Netzteil E06, USB-A/B-Kabel E07, Anschluss-Shield E56 und WAGO E50.
4. **DigiKey Schweiz:** Power-DIN-Kabel E49, zwei Adafruit-Module E48 und zwei STEMMA-Kabel E55; PS1 E05 und gegebenenfalls das gewählte Gehäuse samt Platte mitbestellen. PS1 alternativ Distrelec 300-42-762 oder [Simpex GST220A48-R7B](https://www.simpex.ch/shop/stromversorgungen/netzteile-ac-dc/tischnetzteile/gst220a48-r7b/), jeweils ein Netzteil, keine Großpackung.
5. **Simpex / Conrad / Elektrobedarf Troller:** W1, W4 und 1 m DC-Litze; zusätzliche Versandkosten mit lokalen Bezugsoptionen vergleichen.

Distrelec wurde für PS1 als konkrete Alternative recherchiert. Preise/Lagerbestand waren dort nicht zuverlässig abrufbar. Die Händleraufteilung ist kein Nachweis für den niedrigsten Schweizer Gesamtpreis; Kleinmaterial nach Möglichkeit bei ohnehin verwendeten Lieferanten bündeln und gleiche Spezifikation beibehalten.

Keine Bestellung wird durch diese Liste ausgelöst. Der 230-V-Anschluss besteht ausschließlich aus fertigen Steckverbindungen. Keine zusätzliche Dienstleistung für eine selbst gebaute Netzbaugruppe eingeplant.
