# Material-Stückliste · Elektronik

Stand: **26.09.2026 · Revision A**. Diese Liste umfasst ausschließlich die Elektronik einschließlich Motor, Versorgung, elektrischer Leitungen, Anschlüsse und zugehörigem Elektrogehäuse-/Isolationsmaterial. Konstruktionsmaterial wie Rohre, Holzplatten, Riemenantrieb und Kabelbinder gehört nicht zum Umfang. Elektronikwerkzeuge und Lötmaterial stehen separat am Ende. Mengen von Leitungen und Zubehör sind Planmengen.

**Bestätigt vorhanden: E01 U1 Arduino Uno R3, E02 B1 PIR-Modul, E08 W3 Patchkabel, E28 S0 CH-Mehrfachsteckdose/Hauptschalter, V01 Elektroniklot und Flussmittel, T01 Lötkolben, T03 Multimeter, T04 Logikanalysator.** Noch keine Bestellung ausgelöst.

Die [Bestellliste](bestellliste.md) ergänzt Lieferant und Auswahlhinweise. Die IDs bleiben über beide Listen gleich. Alle eingebauten elektronischen Referenzen gehören zum [Schaltplan](../docs/elektronik.md). Preise sind bewusst nicht aus alten Schätzungen übernommen.

Automatisch erzeugt aus [teile.csv](teile.csv) mit `python3 tools/dokumente_generieren.py`.

## Steuerung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E01 | 1 Stück | U1 Arduino Uno R3 — ATmega328P, 5-V-Logik | Erzeugt STEP/DIR und wertet PIR aus | Vorhanden |
| E02 | 1 Stück | B1 PIR-Modul — Vorhandene HC-SR501-Bauform | Löst die Bewegungssequenz aus | Vorhanden |

## Antrieb

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E03 | 1 Stück | M1 NEMA-34-Motor — STEPPERONLINE 34HS46-6004S1, 14-mm-Welle, mit 1-m-Motorkabel | Bewegt den Riemenantrieb | Noch bestellen |
| E04 | 1 Stück | U3 Schrittmotortreiber — STEPPERONLINE DM860T V3.0 mit 5/24-V-Wahlschalter | Schaltet die Motorwicklungen stromgeregelt | Noch bestellen |

## Versorgung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E05 | 1 Stück | PS1 Motornetzteil — Mean Well LRS-350-48, 48 V / 7,3 A | Versorgt den Motortreiber | Noch bestellen |
| E06 | 1 Stück | PS2 USB-Netzteil — Geschlossenes Steckernetzteil, geregelt 5 V / mindestens 1 A, USB-A, CH-Stecker oder flacher Eurostecker | Versorgt Uno und Sensor getrennt vom Motorstrom | Noch bestellen |
| E07 | 1 Stück | W2 USB-Kabel — USB-A auf USB-B, Datenkabel, etwa 1 m | Versorgung und Programmierung des Uno | Noch bestellen |
| E28 | 1 Stück | S0 CH-Mehrfachsteckdose/Hauptschalter — Fertige CH-Steckdosenleiste, Typ-13-Buchsen, 10 A gesamt, mindestens 2 Steckplätze, gemeinsamer zweipoliger Schalter, PE durchverbunden | Gemeinsame Abschaltung beider Netzteile | Vorhanden |
| E29 | 1 Stück | W1 Netzanschlussleitung — Ca. 2 m, angespritzter CH-Typ-12-Stecker mit Schutzleiter, offene Geräteenden, 3G1,5 mm², für Aufstellort geeignet | Verbindet S0 Steckplatz 1 mit dem geschützten Netzanschluss des PS1 | Noch beschaffen, Variante klären |
| E30 | 1 Stück | F1 Netzsicherung — SCHURTER SPT 0001.2532, T6,3 A, 6,3×32 mm, 250 VAC | Zusätzlicher Schutz der Gerätezuleitung | Noch beschaffen, Variante klären |
| E31 | 1 Stück | F2 DC-Sicherung — SCHURTER SPT 0001.2533, T8 A, 6,3×32 mm, 63 VDC | Schutz der 48-V-Abgangsleitung | Noch bestellen |
| E32 | 2 Stück | Sicherungshalter — Berührungsgeschützt für 6,3×32 mm, mindestens 10 A, 250 VAC und 63 VDC, Klemmenanschluss | Sichere Befestigung von F1 und F2 | Noch beschaffen, Variante klären |
| E33 | 1 Satz | XPE Schutzleiterverteilung — PE-Klemmenblock mit mindestens 6 Anschlüssen und Befestigung | Verteilt PE auf PS1, Gehäuse, Deckel, Montageplatte und Motorrahmen | Noch beschaffen, Variante klären |
| E34 | 3 m | Schutzleiterlitze — 1,5 mm², grün-gelb | Erdung der berührbaren Metallteile | Noch bestellen |
| E35 | 2 m | DC-Leistungslitze — 1,5 mm², rot und schwarz, zusammen 2 m | Verbindet PS1, F2 und U3 | Noch beschaffen, Variante klären |
| E36 | 1 m | Netz-Installationslitze — 1,5 mm², braun und blau, zusammen 1 m | Interne L/N-Verdrahtung | Noch beschaffen, Variante klären |
| E45 | 1 Stück | RCD-Zwischenstecker bei fehlendem geeignetem RCD — 30 mA, CH-tauglich, zum Aufstellort passend | Fehlerstromschutz der Netzversorgung | Bestand/Bedarf prüfen |

## Sensorleitung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E08 | 1 Stück | W3 Patchkabel — Cat5e/Cat6 Vollkupfer, 1:1 T568B, bis 3 m | Überträgt 5 V, Masse und PIR-Signal | Vorhanden |
| E09 | 2 Stück | J1/J2 RJ45-Klemmenadapter — 8P8C-Buchse auf nummerierte Schraubklemmen, passiv ohne Magnetics | Trennbare Sensorverbindung ohne Crimpen eigener RJ45-Stecker | Noch bestellen |
| E23 | 1 Satz | PIR-Anschlussleitung — Drei einzelne 2,54-mm-Buchsenleitungen mit freiem Ende, etwa 20 cm | Direkte Verbindung B1 zu J2 | Noch bestellen |

## Steuerplatine

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E10 | 1 Stück | U2 Schmitt-Trigger — Texas Instruments SN74HCT14N, DIP-14 | Bereitet das PIR-Signal auf 5-V-Pegel auf | Noch bestellen |
| E11 | 1 Stück | IC-Sockel — DIP-14, 7,62-mm-Reihenabstand | Erlaubt lötschonenden Einbau und Austausch von U2 | Noch bestellen |
| E12 | 2 Stück | Q1/Q2 NPN-Transistor — onsemi 2N3904, TO-92, E/B/C nach Datenblatt | Schaltet STEP-/DIR-Optokoppler ohne starke GPIO-Belastung | Noch bestellen |
| E13 | 3 Stück | R1/R2/R5 Widerstände — 1 kΩ, 0,25 W, Metallfilm, bedrahtet | Zwei Basiswiderstände und ein PIR-Filterwiderstand | Noch bestellen |
| E14 | 3 Stück | R3/R4/R6 Widerstände — 100 kΩ, 0,25 W, bedrahtet | Definierte ausgeschaltete Transistoren und PIR-LOW bei Kabeltrennung | Noch bestellen |
| E16 | 2 Stück | C1/C5 Keramikkondensatoren — 100 nF, mindestens 25 V, bedrahtet | IC-Entkopplung und Signalfilter | Noch bestellen |
| E17 | 1 Stück | C2 Elektrolytkondensator — 10 µF, 16 V oder höher, radial | Stützt 5 V lokal an der Steuerplatine | Noch bestellen |
| E18 | 1 Stück | Steuer-Lochrasterplatine — Einzelpads 2,54 mm, 120×80 mm, doppelseitig | Träger für U2, Q1/Q2 und passive Teile | Noch bestellen |
| E20 | 1 Stück | J0 Anschlussklemme — 6-polig aus drei anreihbaren 2-poligen Platinenklemmen, Raster 5,08 mm | Beschrifteter Anschluss zum Uno | Noch bestellen |
| E21 | 1 Stück | J3 Anschlussklemme — 4-polig aus zwei anreihbaren 2-poligen Platinenklemmen, Raster 5,08 mm | Trennbare STEP/DIR-Verbindung | Noch bestellen |
| E24 | 1 Satz | Uno-Verbindungsleitungen — 5 einzelne passende Header-Steckleitungen, etwa 20 cm | Verbindet Uno 5V/GND/D2/D3/D7 mit J0, J0.5 bleibt frei | Noch bestellen |
| E26 | 0,5 m | W4 Steuerkabel — 2 geschirmte verdrillte Paare, etwa 0,25 mm² | Störarme STEP/DIR-Verbindung zum Treiber | Noch bestellen |
| E27 | 5 m | Kleinspannungslitze — 0,25–0,5 mm², mehrere Farben, Gesamtmenge | Interne 5-V-, Sensor- und Signalverdrahtung | Noch bestellen |

## Gehäuse

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E37 | 1 Stück | Steuergehäuse mit Montageplatte — Metall, abschließbar/verschraubt, Planmaß ca. 400×300×180 mm, Lüftung und Trennbereich | Berührungsschutz, Befestigung und Wärmeabfuhr | Noch beschaffen, Aufmaß nötig |
| E38 | 1 Satz | Lüftungselemente und Wetterschutz — Geschützte Zu-/Abluftöffnungen, Regenhaube bei Außenbetrieb | Verhindert Wärmestau und direkten Wassereintritt | Noch beschaffen, Aufmaß nötig |
| E39 | 1 Stück | PIR-Sensorgehäuse — Platz für PIR und J2, Linse frei, Spritzwasserschutz | Schützt PIR-Modul und ermöglicht feste Ausrichtung | Noch beschaffen, Aufmaß nötig |
| E40 | 1 Satz | Kabelverschraubungen/Zugentlastungen — Mindestens 5 passende Durchführungen für Netz, Motor, USB, Sensor und Motor-PE | Verhindert Zug auf Klemmen und scharfe Blechkanten | Noch beschaffen, Aufmaß nötig |
| E41 | 1 Satz | Klemmenabdeckungen und Trennwand — Isolierend, flammhemmend, zwischen Netz- und Steuerbereich | Verhindert versehentlichen Kontakt mit 230 V | Noch beschaffen, Aufmaß nötig |
| E42 | 8 Stück | Platinen-Abstandshalter — M3, isolierend, passende Schrauben/Muttern | Befestigt Uno und Steuer-Lochrasterplatine elektrisch isoliert | Noch bestellen |

## Verdrahtungszubehör

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E43 | 1 Satz | Aderendhülsen, Ringkabelschuhe und PE-Schrauben — Zu 0,25–1,5 mm² und jeweiligen Klemmen, Ringösen für PE | Dauerhafte elektrische und mechanische Anschlüsse | Noch beschaffen, Variante klären |
| E44 | 1 Satz | Schrumpfschlauch und elektrische Beschriftung — Schrumpfschlauch in passenden Durchmessern, Leitungsetiketten | Isoliert elektrische Verbindungen und kennzeichnet Anschlüsse | Noch bestellen |

## Verbrauchsmaterial

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| V01 | 1 Packung | Elektroniklot und Flussmittel — Für bedrahtete Kleinspannungselektronik geeignet | Herstellung der Lötverbindungen | Vorhanden |

## Werkzeug

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| T01 | 1 Stück | Lötkolben — Für bedrahtete Kleinspannungselektronik geeignet | Löten der Steuerplatine | Vorhanden |
| T02 | 1 Stück | Crimpzange für Aderendhülsen — Für Aderendhülsen 0,25–2,5 mm² | Erzeugt zugfeste Klemmanschlüsse | Bestand/Bedarf prüfen |
| T03 | 1 Stück | Multimeter — Durchgang, Widerstand und DC-Spannung | Prüft Verdrahtung, Wicklungen und Versorgung | Vorhanden |
| T04 | 1 Stück | Logikanalysator — Für 5-V-Signale und Mikrosekunden-Pulse geeignet | Prüft STEP-Pulsbreite und DIR-Vorlauf | Vorhanden |

## Enthaltene und nicht benötigte Teile

- Das Motorkabel zählt zum Motorlieferumfang und wird nicht noch einmal bestellt. Montage der Steuerbox in Reichweite des 1-m-Kabels einplanen.
- Schraubklemmen des DM860T bei Lieferung auf Vollständigkeit prüfen.
- Keine zusätzliche Lochrasterplatine am PIR erforderlich: Die Sensorleitung verbindet B1 direkt mit J2. E18 ist die weiterhin benötigte Steuer-Lochrasterplatine für U2 und die übrige Schaltung.
- Kein 48→5-V-Wandler, Ethernet-Modul, PoE-Injector, separater PIR, Hall-Sensor, Endschalter, Soundmodul oder externe Status-LED erforderlich. S0 ist vorgesehen, eine sicherheitsgerichtete Not-Halt-Baugruppe ist nicht Bestandteil von Rev. A.
- Aufbau und Prüfung der Netzbaugruppe sind eine zusätzliche Leistung, kein Bauteil; in der Bestellliste gesondert aufgeführt.
