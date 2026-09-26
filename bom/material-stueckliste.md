# Material-Stückliste

Stand: **26.09.2026 · Revision A**. Diese Liste umfasst den beschriebenen Basisaufbau einschließlich Elektronik-Kleinteilen, Versorgung, Leitungen, Mechanik, Gehäusen und Montagezubehör. Werkzeuge und Verbrauchsmaterial stehen separat am Ende. Mengen von Kabeln/Zubehör sind Planmengen; maßabhängige Teile sind ausdrücklich gekennzeichnet.

**Bestätigt vorhanden: Arduino Uno R3 und PIR. Sonst nichts als bestellt verbucht.** Bei den im Handover beschriebenen Wagen-/Dekorationsteilen vor einem Neukauf dennoch den realen Bestand abgleichen.

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
| E06 | 1 Stück | PS2 USB-Netzteil — Geschlossen, geregelt 5 V / mindestens 1 A, USB-A, CH-tauglicher Stecker | Versorgt Uno und Sensor getrennt vom Motorstrom | Noch bestellen |
| E07 | 1 Stück | W2 USB-Kabel — USB-A auf USB-B, Datenkabel, etwa 1 m | Versorgung und Programmierung des Uno | Noch bestellen |
| E28 | 1 Stück | S0 Netzverteilung/Hauptschalter — Fertig konfektioniert, zweipolig schaltend, Schutzleiter durchverbunden, mindestens 2 Ausgänge, CH-Stecker | Gemeinsame Abschaltung beider Netzteile | Noch beschaffen, Variante klären |
| E29 | 2 m | W1 Netzanschlussleitung — CH-Typ-J-Stecker, offene Geräteenden, 3G1,5 mm², für Aufstellort geeignet | Netzzuleitung vom S0-Ausgang zu PS1 | Noch bestellen |
| E30 | 1 Stück | F1 Netzsicherung — SCHURTER SPT 0001.2532, T6,3 A, 6,3×32 mm, 250 VAC | Zusätzlicher Schutz der Gerätezuleitung | Noch bestellen |
| E31 | 1 Stück | F2 DC-Sicherung — SCHURTER SPT 0001.2533, T8 A, 6,3×32 mm, 63 VDC | Schutz der 48-V-Abgangsleitung | Noch bestellen |
| E32 | 2 Stück | Sicherungshalter — Berührungsgeschützt für 6,3×32 mm, mindestens 10 A, 250 VAC und 63 VDC, Klemmenanschluss | Sichere Befestigung von F1 und F2 | Noch bestellen |
| E33 | 1 Satz | XPE Schutzleiterverteilung — PE-Klemmenblock mit mindestens 6 Anschlüssen und Befestigung | Verteilt PE auf PS1, Gehäuse, Deckel, Montageplatte und Motorrahmen | Noch bestellen |
| E34 | 3 m | Schutzleiterlitze — 1,5 mm², grün-gelb | Erdung der berührbaren Metallteile | Noch bestellen |
| E35 | 2 m | DC-Leistungslitze — 1,5 mm², rot und schwarz, zusammen 2 m | Verbindet PS1, F2 und U3 | Noch bestellen |
| E36 | 1 m | Netz-Installationslitze — 1,5 mm², braun und blau, zusammen 1 m | Interne L/N-Verdrahtung | Noch bestellen |
| E45 | 1 Stück | RCD-Zwischenstecker bei fehlendem geeignetem RCD — 30 mA, CH-tauglich, zum Aufstellort passend | Fehlerstromschutz der Netzversorgung | Bestand/Bedarf prüfen |

## Sensorleitung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E08 | 1 Stück | W3 Patchkabel — Cat5e/Cat6 Vollkupfer, 1:1 T568B, bis 3 m | Überträgt 5 V, Masse und PIR-Signal | Noch bestellen |
| E09 | 2 Stück | J1/J2 RJ45-Klemmenadapter — 8P8C-Buchse auf nummerierte Schraubklemmen, passiv ohne Magnetics | Trennbare Sensorverbindung ohne Crimpen eigener RJ45-Stecker | Noch bestellen |
| E23 | 1 Satz | PIR-Anschlussleitung — 3-polige 2,54-mm-Buchse mit Litzen, etwa 20 cm | Verbindung B1 zu Sensorplatine/J2 | Noch bestellen |

## Steuerplatine

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E10 | 1 Stück | U2 Schmitt-Trigger — Texas Instruments SN74HCT14N, DIP-14 | Bereitet das PIR-Signal auf 5-V-Pegel auf | Noch bestellen |
| E11 | 1 Stück | IC-Sockel — DIP-14, 7,62-mm-Reihenabstand | Erlaubt lötschonenden Einbau und Austausch von U2 | Noch bestellen |
| E12 | 2 Stück | Q1/Q2 NPN-Transistor — onsemi 2N3904, TO-92, E/B/C nach Datenblatt | Schaltet STEP-/DIR-Optokoppler ohne starke GPIO-Belastung | Noch bestellen |
| E13 | 3 Stück | R1/R2/R5 Widerstände — 1 kΩ, 0,25 W, Metallfilm, bedrahtet | Zwei Basiswiderstände und ein PIR-Filterwiderstand | Noch bestellen |
| E14 | 3 Stück | R3/R4/R6 Widerstände — 100 kΩ, 0,25 W, bedrahtet | Definierte ausgeschaltete Transistoren und PIR-LOW bei Kabeltrennung | Noch bestellen |
| E15 | 1 Stück | R7 Widerstand — 10 kΩ, 0,25 W, bedrahtet | Externer Pull-up am Freigabeschalter | Noch bestellen |
| E16 | 3 Stück | C1/C3/C5 Keramikkondensatoren — 100 nF, mindestens 25 V, bedrahtet | IC-Entkopplung, PIR-Entkopplung, Signalfilter | Noch bestellen |
| E17 | 2 Stück | C2/C4 Elektrolytkondensatoren — 10 µF, 16 V oder höher, radial | Stützt 5 V lokal an Steuerung und entferntem Sensor | Noch bestellen |
| E18 | 1 Stück | Steuer-Lochrasterplatine — Einzelpads 2,54 mm, etwa 100×80 mm | Träger für U2, Q1/Q2 und passive Teile | Noch bestellen |
| E19 | 1 Stück | Sensor-Lochrasterplatine — Einzelpads 2,54 mm, etwa 30×30 mm | Träger für C3/C4 und Sensoranschluss | Noch bestellen |
| E20 | 1 Stück | J0 Anschlussklemme — 6-polig, Platinenklemme mit passendem Raster | Beschrifteter Anschluss zum Uno | Noch bestellen |
| E21 | 1 Stück | J3 Anschlussklemme — 4-polig, Raster 5,08 mm | Trennbare STEP/DIR-Verbindung | Noch bestellen |
| E22 | 1 Stück | J4 Anschlussklemme — 2-polig, Raster 5,08 mm | Anschluss des Freigabeschalters | Noch bestellen |
| E24 | 1 Satz | Uno-Verbindungsleitungen — 6 einzelne passende Header-Steckleitungen, etwa 20 cm | Verbindet Uno 5V/GND/D2/D3/D4/D7 mit J0 | Noch bestellen |
| E26 | 0,5 m | W4 Steuerkabel — 2 geschirmte verdrillte Paare, etwa 0,25 mm² | Störarme STEP/DIR-Verbindung zum Treiber | Noch bestellen |
| E27 | 5 m | Kleinspannungslitze — 0,25–0,5 mm², mehrere Farben, Gesamtmenge | Interne 5-V-, Sensor- und Schalterverdrahtung | Noch bestellen |

## Bedienung

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E25 | 1 Stück | S1 Freigabeschalter — Rastender EIN/AUS-Schalter, 1 Schließer, kleinspannungstauglich | Bewusste Betriebsfreigabe und kontrollierter Softwarestopp | Noch bestellen |

## Gehäuse

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E37 | 1 Stück | Steuergehäuse mit Montageplatte — Metall, abschließbar/verschraubt, Planmaß ca. 400×300×180 mm, Lüftung und Trennbereich | Berührungsschutz, Befestigung und Wärmeabfuhr | Noch beschaffen, Aufmaß nötig |
| E38 | 1 Satz | Lüftungselemente und Wetterschutz — Geschützte Zu-/Abluftöffnungen, Regenhaube bei Außenbetrieb | Verhindert Wärmestau und direkten Wassereintritt | Noch beschaffen, Aufmaß nötig |
| E39 | 1 Stück | Sensorgehäuse mit Halter — Platz für PIR, J2 und C3/C4, Linse frei, Spritzwasserschutz | Schützt Sensorplatine und ermöglicht feste Ausrichtung | Noch beschaffen, Aufmaß nötig |
| E40 | 1 Satz | Kabelverschraubungen/Zugentlastungen — Mindestens 5 passende Durchführungen für Netz, Motor, USB, Sensor und Motor-PE | Verhindert Zug auf Klemmen und scharfe Blechkanten | Noch beschaffen, Aufmaß nötig |
| E41 | 1 Satz | Klemmenabdeckungen und Trennwand — Isolierend, flammhemmend, zwischen Netz- und Steuerbereich | Verhindert versehentlichen Kontakt mit 230 V | Noch beschaffen, Aufmaß nötig |
| E42 | 12 Stück | Platinen-Abstandshalter — M3, isolierend, passende Schrauben/Muttern | Befestigt Uno und beide Lochrasterplatinen | Noch bestellen |

## Verdrahtungszubehör

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| E43 | 1 Satz | Aderendhülsen, Ringkabelschuhe und PE-Schrauben — Zu 0,25–1,5 mm² und jeweiligen Klemmen, Ringösen für PE | Dauerhafte elektrische und mechanische Anschlüsse | Noch bestellen |
| E44 | 1 Satz | Schrumpfschlauch, Kabelbinder und Beschriftung — Verschiedene Durchmesser, Kabelhalter, Etiketten | Isoliert freie Enden, entlastet Leitungen und verhindert Verwechslung | Noch bestellen |

## Mechanik

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| M01 | 1 Stück | Motorhalter — STEPPERONLINE ST-M7 für NEMA 34 | Befestigt Motor am Grundrahmen | Noch bestellen |
| M02 | 1 Stück | Motor-Riemenscheibe — HTD-5M, 20T, für 15-mm-Riemen, Bohrung 14 mm mit passender Nut | Kleine Scheibe der 2:1-Untersetzung | Noch beschaffen, Variante klären |
| M03 | 1 Stück | Hauptachsen-Riemenscheibe — HTD-5M, 40T, für 15-mm-Riemen, Bohrung 20 mm mit passender Nut | Große Scheibe der 2:1-Untersetzung | Noch beschaffen, Variante klären |
| M04 | 1 Stück | Zahnriemen — Geschlossen HTD 450-5M-15, 90 Zähne, 15 mm breit | Überträgt Motorbewegung zur Hauptachse | Noch bestellen |
| M05 | 1 Stück | Hauptachse — Stahl 20 mm, ca. 200 mm, bearbeitbar, Passfedernut zur 40T-Scheibe | Trägt Armaufnahme und überträgt Drehmoment | Noch beschaffen, Aufmaß nötig |
| M06 | 2 Stück | Flanschlager — UCFL204, 20-mm-Bohrung, DOLD Artikel 35334 | Separate Lagerung der Hauptachse | Noch bestellen |
| M07 | 2 Stück | Geteilte Wellen-Klemmringe — 20-mm-Bohrung, zur Lageranordnung passend | Axiale Sicherung der Hauptachse | Noch bestellen |
| M08 | 1 Stück | Flansch-Klemmnabe — 20-mm-Bohrung, geschlitzte Klemmung, dokumentiertes Moment mindestens 20 Nm | Verbindet Welle drehfest mit Armplatte | Noch beschaffen, Variante klären |
| M09 | 1 Stück | Passfeder Motor — Zur 14-mm-Motorwelle und M02 passend | Formschlüssige Drehmomentübertragung auf 20T-Scheibe | Noch beschaffen, Variante klären |
| M10 | 1 Stück | Passfeder Hauptachse — Zur 20-mm-Welle und M03 passend | Formschlüssige Drehmomentübertragung auf 40T-Scheibe | Noch beschaffen, Aufmaß nötig |
| M11 | 1 Satz | Grundrahmen mit zwei Lagerträgern — Steife Grundplatte, zwei parallele Tragebenen, Lagerabstand etwa 80–120 mm | Nimmt Motor, Riemenzug und Armkräfte auf | Noch beschaffen, Aufmaß nötig |
| M12 | 1 Stück | Verschiebbare Motoraufnahme — Langlöcher für etwa 140–160 mm Achsabstand | Ermöglicht Montage und Spannung des 450-mm-Riemens | Noch beschaffen, Aufmaß nötig |
| M13 | 1 Stück | Arm-Montageplatte — Metallplatte, passend zu M08 und zwei Rohrschellen | Überträgt Bewegung von Nabe auf Rohr | Noch beschaffen, Aufmaß nötig |
| M14 | 2 Stück | Rohrschellen/U-Bügel mit Gegenplatten — Passend zum gemessenen Kunststoffrohr-Außendurchmesser | Fixiert Rohr an zwei Stellen der Armplatte | Noch beschaffen, Aufmaß nötig |
| M15 | 1 Streifen | Gummieinlage — Etwa 2–3 mm, zwischen Rohr und Schellen | Verringert Schlupf und schützt Kunststoff vor Quetschen | Noch bestellen |
| M16 | 1 m | Kunststoffrohr — Etwa 1 m Arm, Durchmesser/Wandstärke noch festzulegen | Verbindet Hauptachse mit Wagen | Noch beschaffen, Aufmaß nötig |
| M17 | 1 Satz | Wagen-Rohr-Aufnahme — Befestigte Aufnahme mit gesichertem Gelenkbolzen und Gegenplatte | Überträgt Zug/Druck und erlaubt nötigen Höhenausgleich | Noch beschaffen, Aufmaß nötig |
| M22 | 1 Satz | Mechanische Schrauben/Muttern/Scheiben — Mindestens 4 Motor-, 4 Lager-, 4 Halter-, 4 Naben-, 4 Schellenbefestigungen, plus Rahmen/Rollen | Verbindet alle mechanischen Baugruppen | Noch beschaffen, Aufmaß nötig |
| M23 | 1 Satz | Riemenabdeckung mit Befestigung — Feste Abdeckung beider Scheiben und des Riemens | Verhindert Eingreifen und Einziehen | Noch beschaffen, Aufmaß nötig |
| M24 | 1 Satz | Grundrahmen-Verankerung — Bodenabhängige Schrauben, Anker oder geeignete Ballastierung | Verhindert Wandern und Kippen des Antriebs | Noch beschaffen, Aufmaß nötig |
| M25 | 1 Satz | Abgrenzung des Bewegungsbereichs — Absperrung außerhalb Kreisbahn inklusive Wagenüberstand | Hält Besucher vom bewegten Arm und Wagen fern | Noch beschaffen, Aufmaß nötig |

## Wagen

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| M18 | 1 Stück | Wagenplatte — Stabile wettergeeignete Holz-/Siebdruckplatte, zur Spinne passend | Trägt Spinne und Rollen | Noch beschaffen, Aufmaß nötig |
| M19 | 6 Stück | Kugelgelagerte Rollen — Für Boden und Kreisfahrt geeignet, schwenkbar oder tangential ausgerichtet | Tragen Wagen und reduzieren Rollwiderstand | Noch beschaffen, Aufmaß nötig |
| M20 | 1 Stück | Halloween-Spinne — Abmessungen zum Wagen, Gesamtmasse Wagen/Spinne etwa 5 kg | Sichtbare Halloween-Dekoration | Noch beschaffen, Aufmaß nötig |
| M21 | 2 Stück | Befestigungsgurte — Zur Spinne und Wagenplatte passend | Sichert die Dekoration bei Richtungswechseln | Noch bestellen |

## Verbrauchsmaterial

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| V01 | 1 Packung | Elektroniklot und Flussmittel — Für bedrahtete Kleinspannungselektronik geeignet | Herstellung der Lötverbindungen | Bestand/Bedarf prüfen |
| V02 | 1 Flasche | Mittelfeste Schraubensicherung — Für geeignete metallische Gewindeverbindungen | Sichert gegen vibrationsbedingtes Lösen | Bestand/Bedarf prüfen |

## Werkzeug

| ID | Menge | Teil / Spezifikation | Warum benötigt? | Status |
|---|---|---|---|---|
| T01 | 1 Satz | Lötstation, Seitenschneider und Abisolierer — Für bedrahtete Bauteile und Leitungsquerschnitte geeignet | Erforderlich zum Bau der Kleinspannungsplatinen | Bestand/Bedarf prüfen |
| T02 | 1 Stück | Crimpzange — Passend zu Aderendhülsen/Kabelschuhen | Erzeugt zugfeste Klemmanschlüsse | Bestand/Bedarf prüfen |
| T03 | 1 Stück | Multimeter — Durchgang, Widerstand und DC-Spannung | Prüft Verdrahtung, Wicklungen und Versorgung | Bestand/Bedarf prüfen |
| T04 | 1 Stück | Logikanalysator oder Oszilloskop — Für 5-V-Signale und Mikrosekunden-Pulse geeignet | Prüft STEP-Pulsbreite und DIR-Vorlauf | Bestand/Bedarf prüfen |
| T05 | 1 Satz | Mechanik-Werkzeug und Federwaage — Messschieber, Bohrer, Gewindewerkzeug, Schlüssel, Zugkraftmessung | Ermittelt Maße und Rollwiderstand und ermöglicht Montage | Bestand/Bedarf prüfen |

## Enthaltene und nicht benötigte Teile

- Das Motorkabel zählt zum Motorlieferumfang und wird nicht noch einmal bestellt. Montage der Steuerbox in Reichweite des 1-m-Kabels einplanen.
- Schraubklemmen des DM860T und Befestigungsschrauben der Klemmnaben/Lager sind auf Vollständigkeit bei Lieferung zu prüfen. Fehlende Befestiger aus M22 ergänzen.
- Kein 48→5-V-Wandler, Ethernet-Modul, PoE-Injector, separater PIR, Hall-Sensor, Endschalter, Soundmodul oder externe Status-LED erforderlich. S0/S1 sind vollständig vorgesehen, eine sicherheitsgerichtete Not-Halt-Baugruppe ist nicht Bestandteil von Rev. A.
- 230-V-Aufbau/Prüfung sowie nötige Wellen-/Plattenbearbeitung sind zusätzliche Leistungen, keine Bauteile. In der Bestellliste gesondert aufgeführt.
