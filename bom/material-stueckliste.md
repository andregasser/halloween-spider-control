# Material-Stückliste · Elektronik

Stand **04.10.2026 · Revision B · fertige Module, keine selbst gelötete Zusatzplatine**. Noch nicht aufgebaut/getestet, keine Bestellung ausgelöst. Umfang: Elektronik, elektrische Leitungen und Gehäusezubehör sowie ausdrücklich Motorhalterung ST-M7. Keine weitere Konstruktion/Mechanik.

**Bestätigt vorhanden:** E01 U1 Arduino Uno R3, E02 B1 PIR-Modul, E08 W3 Patchkabel, E23 PIR-Anschlussleitung, E24 Uno-Verbindungsleitungen, E26 W4 Steuerkabel, E28 S0 CH-Mehrfachsteckdose/Hauptschalter, E29 W1 Netzanschlussleitung, E35 DC-Leistungslitze, E42 Platinen-Abstandshalter, E44 Schrumpfschlauch, T03 Multimeter, T04 Logikanalysator.

Automatisch aus [teile.csv](teile.csv) erzeugt. [Bestellliste](bestellliste.md) nennt Lieferanten; [Anschlussplan](../docs/elektronik.md) beschreibt die Verdrahtung. Leitungs-/Zubehörmengen sind Planbedarf; Packungsmengen stehen in der Bestellliste.

## Steuerung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E01 | 1 Stück | U1 Arduino Uno R3 — ATmega328P, 5-V-Logik | Erzeugt STEP/DIR und wertet PIR aus | Vorhanden |
| E02 | 1 Stück | B1 PIR-Modul — Vorhandene HC-SR501-Bauform | Löst die Bewegungssequenz aus | Vorhanden |

## Antrieb

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E03 | 1 Stück | M1 NEMA-34-Motor — STEPPERONLINE 34HS46-6004S1, 14-mm-Welle, mit 1-m-Motorkabel | Bewegt den Riemenantrieb | Bezugsquelle/Ausführung klären |
| E47 | 1 Stück | Motorhalterung für M1 — STEPPERONLINE ST-M7, Stahl-Montagewinkel für NEMA 34 / 86-mm-Motoren | Befestigt den Motor am Träger und hält seine Lage zum Zahnriemen | Bezugsquelle/Ausführung klären |
| E04 | 1 Stück | U3 Schrittmotortreiber — STEPPERONLINE DM860T V3.0 mit 5/24-V-Wahlschalter | Schaltet die Motorwicklungen stromgeregelt | Bezugsquelle/Ausführung klären |

## Versorgung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E05 | 1 Stück | PS1 geschlossenes Motornetzteil — Mean Well GST220A48-R7B, 48 V / 4,6 A / 221 W, IEC-C14 und Power-DIN-R7B | Versorgt den einzelnen Treiber ohne eigene Netzverdrahtung | Bezugsquelle/Ausführung klären |
| E06 | 1 Stück | PS2 USB-Netzteil — Geschlossenes Steckernetzteil, geregelt 5 V / mindestens 1 A, USB-A, CH-Stecker oder flacher Eurostecker | Versorgt Uno und Sensor getrennt vom Motorstrom | Noch bestellen |
| E07 | 1 Stück | W2 USB-Kabel — USB-2.0-A auf USB-B, Datenkabel; ausgewählte BerryBase-Variante 1,80 m | Versorgung und Programmierung des Uno | Noch bestellen |
| E28 | 1 Stück | S0 CH-Mehrfachsteckdose/Hauptschalter — Fertige CH-Steckdosenleiste, Typ-13-Buchsen, 10 A gesamt, mindestens 2 Steckplätze, gemeinsamer zweipoliger Schalter, PE durchverbunden | Gemeinsame Abschaltung beider Netzteile | Vorhanden |
| E29 | 1 Stück | W1 Netzanschlussleitung — Benötigt: fertiges CH-Typ-12-auf-IEC-C13-Netzkabel mit Schutzleiter; passende Länge aus Bestand | Steckfertiger Netzanschluss PS1 an vorhandene CH-Leiste | Vorhanden |
| E49 | 1 Stück | W5 Power-DIN-Verlängerung — GlobTek KPPX4124641M0KPJX4(R), 1 m, 4×AWG18, Stecker/Buchse | Fertig montierte passende Netzteilbuchse, andere Seite in Treiberklemmen | Bezugsquelle/Ausführung klären |
| E35 | 1 m | DC-Leistungslitze — 1,5 mm² Kupfer-Silikonlitze, schwarz, 1 m; zwei kurze Abschnitte | Verbindet X1/X2 mit U3, positive Ader dauerhaft markieren | Vorhanden |
| E45 | 1 Stück | RCD-Zwischenstecker bei fehlendem geeignetem RCD — 30 mA, CH-tauglich, zum Aufstellort passend | Fehlerstromschutz der Netzversorgung | Bestand/Bedarf prüfen |

## Sensorleitung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E08 | 1 Stück | W3 Patchkabel — Normales Cat5/Cat5e/Cat6-RJ45-Patchkabel aus Bestand, 1:1, bis 3 m | Überträgt 5 V, Masse und PIR-Signal | Vorhanden |
| E09 | 2 Stück | J1/J2 RJ45-Klemmenadapter — 8P8C-Buchse auf nummerierte Schraubklemmen, passiv ohne Magnetics | Trennbare Sensorverbindung ohne Crimpen eigener RJ45-Stecker | Noch bestellen |
| E23 | 1 Satz | PIR-Anschlussleitung — Drei einzelne 2,54-mm-Buchsenleitungen mit freiem Ende, etwa 20 cm | Direkte Verbindung B1 zu J2 | Vorhanden |

## Signalmodule

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E48 | 2 Stück | U4/U5 fertige Signalmodule — Adafruit MOSFET Driver #5648, STEMMA-JST-PH und montierte Ausgangs-Federklemmen | Schaltet STEP und DIR ohne Eigenbauplatine oder zusätzliche Einzelbauteile | Noch bestellen |
| E55 | 2 Stück | STEMMA-Anschlusskabel für U4/U5 — Adafruit #3894, JST PH 2 mm, 3-polig auf einzelne weibliche Header-Buchsen, 200 mm | Steckbare Modulversorgung und Uno-Ansteuerung ohne Löten | Bezugsquelle/Ausführung klären |
| E56 | 1 Stück | U6 fertiges Uno-Anschluss-Shield — DFRobot DFR0265, IO Expansion Shield V7.1, fertig bestückt | Stellt genügend steckbare 5-V-/GND-/Signalanschlüsse bereit und spart Steuer-Verteilerklemmen | Noch bestellen |

## Verbindungsklemmen

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E50 | 2 Stück | X1/X2 Verbindungsklemmen — WAGO 221-413, 3 Leiter | Beide Adern jeder DC-Schiene mit kurzem Treiberabgang verbinden | Noch bestellen |

## Interne Verdrahtung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E24 | 1 Satz | Uno-Verbindungsleitungen — Vier einzelne Buchsen-Header-Leitungen zu U6/PIR-Adapter, etwa 20 cm | Steckt PIR OUT/5V und zwei GND-Leitungen auf U6 und führt sie zu J1 | Vorhanden |
| E26 | 0,5 m | W4 Steuerkabel — 2 geschirmte verdrillte Paare, etwa 0,25 mm² | Störarme STEP/DIR-Verbindung zum Treiber | Vorhanden |

## Gehäuse

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E38 | 1 Satz | Lüftungselemente und Wetterschutz — Lüftung zum tatsächlichen Gehäuse; DM860T-Umgebung maximal 40 °C | Verhindert Wärmestau und direkten Wassereintritt | Bestand/Bedarf prüfen |
| E40 | 1 Satz | Kabelverschraubungen/Zugentlastungen — Zugentlastungen passend zu W2/W3/W5/Motorkabel und Sensorleitung; Durchführungen nur bei verwendeter Abdeckung | Verhindert Zug auf Klemmen und scharfe Blechkanten | Aufmaß/Ausführung offen |
| E42 | 10 Stück | Platinen-Abstandshalter — Isolierende Platinen-Abstandshalter samt Schrauben, zu realen Lochbildern | Befestigt Uno, zwei Module und RJ45-Adapter elektrisch isoliert | Vorhanden |
| E54 | 1 Satz | Befestigungen für Treiber, Klemmen und Motorhalterung — Passende Schrauben/Muttern/Unterlegscheiben, ggf. WAGO-Halter | Zugfeste Befestigung der elektrischen Geräte und ausdrücklich gewünschten Motorhalterung | Aufmaß/Ausführung offen |

## Verdrahtungszubehör

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E46 | 1 Satz | Elektrische Beschriftung — Elektrische Beschriftung für PIR 5V KEIN LAN/PoE, 48V und Gerätekennungen | Kennzeichnet Leitungen und Anschlüsse eindeutig | Bestand/Bedarf prüfen |
| E44 | 1 Satz | Schrumpfschlauch — Schrumpfschlauch in passenden Durchmessern | Isoliert elektrische Verbindungen | Vorhanden |

## Werkzeug

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| T03 | 1 Stück | Multimeter — Durchgang, Widerstand und DC-Spannung | Prüft Verdrahtung, Wicklungen und Versorgung | Vorhanden |
| T04 | 1 Stück | Logikanalysator — Für 5-V-Signale und Mikrosekunden-Pulse geeignet | Prüft STEP-Pulsbreite und DIR-Vorlauf | Vorhanden |

## Lieferumfang und entfallene Teile

Motor enthält 1 m Anschlusskabel; Adafruit #5648 wird ohne STEMMA-Kabel geliefert: zwei Kabel #3894 separat bestellen. Treiber-Klemmstecker bei Lieferung prüfen. Kabel W5 ist eine fertige Verlängerung; nur dessen männliches Ende wird zum Klemmen abgeschnitten.

Steuergehäuse E37, zugehörige Montageplatte E53 und PIR-Sensorgehäuse E39 entfallen als festgelegte Projektteile. Für den etwa vierstündigen Aufbau kann bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwendet werden; kein bestimmtes Modell als Bestand bestätigt.

Aderendhülsen E43 und Crimpzange T02 sind auf Nutzerwunsch aus dem Material-/Bestellbedarf entfernt. Die Eignung der tatsächlich gelieferten Schraubklemmen für blanke Litzen ist vor Aufbau zu prüfen, siehe [Anschlussplan](../docs/elektronik.md).

Lochrasterplatinen, HCT-Chip, Sockel, Einzeltransistoren, externe Kondensatoren, Netzsicherungsaufbau und interne 230-V-Verkabelung aus Revision A entfallen. Lötwerkzeug/Lot/Flussmittel sind bestätigt vorhanden, werden für Rev. B aber nicht benötigt und stehen deshalb nicht als Projektbedarf in dieser Liste. Kein Ethernet/PoE, Home-Sensor oder Freigabeschalter im Basisaufbau.
