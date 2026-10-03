# Elektronik · Revision B

Stand **03.10.2026**. Maßgeblicher Anschlussplan für den Aufbau mit fertigen Modulen. Noch keine Hardwaremessung; die Abnahmekriterien stehen in [Inbetriebnahme](inbetriebnahme.md). Revision A ist [historisch archiviert](archiv/revision-a/README.md).

## Schaltplanblätter

- [Blatt 1: Versorgung und Motor](schaltplan-versorgung.svg)
- [Blatt 2: Arduino, Signalmodule und PIR](schaltplan-steuerung.svg)

Die Bauteilnummer bleibt auf beiden Blättern gleich. Jeder Gerätekasten enthält Nummer und Modell. Gleichnamige Anschlüsse auf getrennten Feldern sind dieselben realen Anschlüsse. **X-Klemmen sind fertige WAGO-Verbindungsklemmen, keine Platinen.** Innerhalb einer einzelnen WAGO sind alle Anschlüsse verbunden; verschiedene WAGO müssen bei Bedarf ausdrücklich über ein Kabel verbunden werden.

## Geräte und Leitungen

| Kennung | Reales Bauteil |
|---|---|
| U1 | Arduino Uno R3 |
| U3 | STEPPERONLINE DM860T V3.0 |
| U6 | DFRobot IO Expansion Shield V7.1, DFR0265, auf Uno gesteckt |
| U4 / U5 | Adafruit MOSFET Driver #5648, je ein Modul für STEP / DIR |
| B1 | Vorhandenes PIR-Modul, HC-SR501-Bauform |
| M1 | STEPPERONLINE 34HS46-6004S1 |
| PS1 | Mean Well GST220A48-R7B, geschlossenes Tischnetzteil |
| PS2 | Goobay 44952, USB-Netzteil, nominal 5 V |
| S0 | Vorhandene geschaltete CH-Mehrfachsteckdose |
| J1 / J2 | DFRobot FIT0849, RJ45-Buchse auf Schraubklemmen; Steuerbox / Sensor |
| X1 / X2 | WAGO 221-413, je 3 Anschlüsse für +48 V / 48-V-Rückleiter |
| W1 | Vorhandenes 230-V-Anschlusskabel; für PS1 CH-Stecker auf IEC-C13-Buchse auswählen |
| W2 | USB-A-auf-USB-B-Datenkabel zum Uno |
| W3 | Vorhandenes normales Cat5-/Cat6-RJ45-Patchkabel, 1:1, bis 3 m |
| W4 | 2 × 2 × 0,25 mm², paarverseilte Signalleitung zum Treiber, höchstens 0,5 m |
| W5 | GlobTek KPPX4124641M0KPJX4(R), 1-m-Power-DIN-Verlängerung, treiberseitig gekürzt |

## 1. Netzanschluss und Motorversorgung

**Keine offenen 230-V-Anschlüsse im Aufbau.** W1 aus dem bestätigten Kabelbestand auswählen; passende IEC-C13-Buchse für PS1 und Schutzleiter prüfen. W1 in Steckplatz 1 von S0 und in den IEC-C14-Eingang von PS1 stecken. PS2 in Steckplatz 2, W2 von PS2 zum Uno-USB-B-Anschluss. Das Netzteil PS1 bleibt außerhalb der Steuerbox, trocken, belüftet und zugentlastet. Keine Änderung an Netzsteckern oder Netzteilgehäusen.

W5 hat einen passenden vierpoligen Power-DIN-Buchsenstecker für PS1. **Nur den männlichen Stecker am anderen Ende der Verlängerung abschneiden**, nicht das Kabel von PS1. W5 hat vier AWG-18-Adern, zwei pro Versorgungsschiene. Alle vier werden verwendet.

| Von | Nach | Ausführung |
|---|---|---|
| W5, beide identifizierten +48-V-Adern | X1, Plätze 1 und 2 | Getrennt in zwei Klemmplätze |
| X1, Platz 3 | U3, erste AC-Klemme | Kurze 1,5-mm²-Kupferlitze |
| W5, beide identifizierten Rückleiter-Adern | X2, Plätze 1 und 2 | Getrennt in zwei Klemmplätze |
| X2, Platz 3 | U3, zweite AC-Klemme | Kurze 1,5-mm²-Kupferlitze |
| M1 schwarz | U3 A+ | Motorlieferkabel |
| M1 grün | U3 A− | Motorlieferkabel |
| M1 rot | U3 B+ | Motorlieferkabel |
| M1 blau | U3 B− | Motorlieferkabel |

V3.0 hat zwei mit **AC** beschriftete Versorgungsklemmen und akzeptiert dort 48 V Gleichspannung ohne vorgegebene Polarität. Andere Revisionen benötigen ihren eigenen Anschlussplan. Motorwicklungen vor Anschluss durchmessen; nie bei eingeschaltetem Treiber stecken oder umklemmen.

**W5-Aderzuordnung durchmessen, nicht nach Farben oder aufgedruckten GlobTek-Pinnummern raten.** Mean Well und GlobTek verwenden unterschiedliche Pinnummerierungen. Beim Blick auf die Kontaktseite des PS1-Steckers, Führungsnase oben, sind die beiden unteren Kontakte +48 V und die beiden oberen Rückleiter. Im Mean-Well-Datenblatt heißen diese 1/4 beziehungsweise 2/3. Am Gegenstecker ist die Ansicht gespiegelt. Spannungsfrei per Durchgang die Zuordnung bestimmen, danach PS1 allein einschalten und an X1/X2 Polarität und Spannung messen, wieder ausschalten und erst dann U3 anschließen. W5-Abschirmung am abgeschnittenen Ende einzeln isolieren.

**Keine Brücke von X2 an die Arduino-GND-Klemmen.** Die Signalmasse wird nur in Abschnitt 2 verbunden. PS1 verbindet seinen DC-Rückleiter intern mit Schutzleiter; das ist eine Eigenschaft des fertigen Geräts, keine zusätzliche Verdrahtungsaufgabe. Das Netzteil schützt seinen Ausgang gegen Kurzschluss/Überlast. Zusätzliche Sicherungen aus Rev. A sind nicht übernommen: alle Adern verwenden, DC-Abgang kurz halten und nur den einen Treiber versorgen. Änderungen an Leitungsquerschnitt oder Abgängen erfordern erneute Auslegung.

## 2. Steckbare Arduino-Anschlüsse und Signalmodule

**U6 DFRobot DFR0265** wird vollständig auf die Buchsenleisten des Uno gesteckt. Seine farbigen Stifte machen Signal, Versorgung und GND einzeln zugänglich. Den **5V/3.3V-Jumper auf 5 V** setzen, Schalter auf **PROG** lassen. Die externe Versorgung **PWR_IN bleibt frei**. Kein Funkmodul und keine zusätzliche Versorgung anschließen.

Die Module U4/U5 bekommen je ein fertig konfektioniertes **Adafruit-3894-Kabel**, JST PH 2 mm auf drei einzelne **Buchsen**. Diese Kabel sind nicht im Modul enthalten. Alle drei Kabelenden werden gesteckt; nichts abschneiden. Die freien Löt-/Headerplätze am Modul bleiben unbenutzt.

| Funktion | Verbindung an U6 | Modul / Sensorleitung |
|---|---|---|
| STEP | Digitalgruppe **D2, grüner Signalstift** | U4 STEMMA **In**, weiße Leitung |
| Versorgung U4 | Analoggruppe **A1, roter +V-Stift** | U4 STEMMA **V+**, rote Leitung |
| GND U4 | Analoggruppe **A1, schwarzer GND-Stift** | U4 STEMMA **GND**, schwarze Leitung |
| DIR | Digitalgruppe **D3, grüner Signalstift** | U5 STEMMA **In**, weiße Leitung |
| Versorgung U5 | Analoggruppe **A2, roter +V-Stift** | U5 STEMMA **V+**, rote Leitung |
| GND U5 | Analoggruppe **A2, schwarzer GND-Stift** | U5 STEMMA **GND**, schwarze Leitung |
| PIR OUT | Analoggruppe **A0, blauer Signalstift** | J1.1 |
| PIR +5 V | Analoggruppe **A0, roter +V-Stift** | J1.5 |
| PIR GND | Analoggruppe **A0, schwarzer GND-Stift** | J1.2 |
| Zweite PIR-GND-Ader | Analoggruppe **A3, schwarzer GND-Stift** | J1.4 |
| W4-Schirm | **SERVO_PWR, Minus-/GND-Schraubklemme** | Nur Steuerbox-Ende; SERVO_PWR-Plus bleibt frei |

**Bewusst die roten/schwarzen A1-/A2-Stifte für die Modulversorgung verwenden.** Die rote Versorgungsreihe der digitalen D-Pins wird hier nicht benutzt. Im Herstellerplan läuft diese über einen zusätzlichen Versorgungspfad; die Analoggruppen stellen bei gesetztem 5-V-Jumper die direkte Uno-5-V-Versorgung bereit. Die analogen Signalstifte A1/A2/A3 selbst bleiben frei. [U6-Herstellerplan](https://dfimg.dfrobot.com/wiki/18598/DFR0265_io-expansion-shield-for-arduino_schematics_V1.0.pdf).

| Moduleingang / Ausgang | Verbindung zum Treiber |
|---|---|
| U4 Ausgang **+** | W4 → U3 **PUL+** |
| U4 Ausgang **−** | W4 → U3 **PUL−** |
| U5 Ausgang **+** | W4 → U3 **DIR+** |
| U5 Ausgang **−** | W4 → U3 **DIR−** |
| U3 ENA+/ENA−, ALM, BRK | Unbeschaltet |

**Die Minus-Ausgänge der Module sind keine dauerhaften GND-Anschlüsse. PUL−/DIR− nicht zusätzlich an GND anschließen.** Arduino-HIGH aktiviert das entsprechende Signal. Beide Ausgangspaare gehen unmittelbar zum Treiber. Zusätzliche einzelne Widerstände oder eine Ausgangsverteilerplatine sind nicht erforderlich.

Die Ausgangsklemmen am Modul sind **Federklemmen mit Drucktaste**, keine Schraubklemmen: Taste vorsichtig mit kleinem Schraubendreher drücken, abisolierte 0,25-mm²-Ader einführen, Taste loslassen und Zugprobe machen. Abisolierlänge nach gelieferter Klemme prüfen, keinen 11-mm-WAGO-221-Wert pauschal übertragen. [Herstelleranleitung](https://learn.adafruit.com/adafruit-mosfet-driver/plugging-into-the-terminal-block).

W4: ein verdrilltes Paar für PUL+/PUL−, das andere für DIR+/DIR−. Schirm nur am Steuerbox-Ende an U6 SERVO_PWR-GND, treiberseitig isolieren. Von Motor-/DC-Leistungskabeln getrennt führen. Gegebenenfalls freies Schirmende für die Klemme passend vorbereiten und isolieren.

Die Module sind für Versorgung **3–30 V** spezifiziert; hier ausschließlich Uno nominal 5 V. **S2 am DM860T auf 5 V.** Vor Motorbetrieb die Signalspannung **zwischen PUL+ und PUL−** beziehungsweise **DIR+ und DIR−** unter Last prüfen. Kein Anschluss dieser Module oder des Shields an 48 V. Die Versorgung über USB-B des Uno bleibt bestehen.

## 3. PIR und RJ45-Patchkabel

Der PIR wird ohne Zusatzplatine direkt an **A0**, einen analogen Eingang des Uno, angeschlossen. Die Firmware wertet den typischen 3–3,3-V-Pegel aus. **D7 aus Revision A wird nicht verwendet.** Die tatsächliche VCC/OUT/GND-Pinfolge am vorhandenen PIR ist vor dem Anschließen zu prüfen.

| RJ45-Pin an J1 und J2 | Verbindung in Steuerbox J1 | Verbindung am Sensor J2 | Paar, T568B |
|---|---|---|---|
| 1 | U6 A0, blauer Signalstift → U1 A0 | B1 OUT | Weiß/Orange |
| 2 | U6 A0, schwarzer GND-Stift | B1 GND | Orange |
| 4 | U6 A3, schwarzer GND-Stift | Brücke zu J2.2 | Blau |
| 5 | U6 A0, roter +V-Stift (+5 V) | B1 VCC | Weiß/Blau |
| 3 / 6 / 7 / 8 | Frei | Frei | Nicht anschließen |

Damit gibt es drei elektrische Netze auf vier Adern: OUT/GND als Paar und +5V/GND als Paar. Bei abweichender Farbnorm sind die **Pinnummern** maßgeblich. Mit dem vorhandenen Patchkabel alle acht Leitungen auf 1:1-Durchgang prüfen. J1/J2 beschriften: **PIR · 5 V · KEIN LAN / PoE**.

A0 wird per `INPUT_PULLUP` und `analogRead()` ausgewertet. Ein abgezogenes OUT wird damit typischerweise als ungültiger hoher Messwert erkannt. Die Firmware muss gültiges LOW, gültige Bewegung und ungültige Werte unterscheiden; Details in [Firmware](firmware.md). Softwarefilter ersetzen keine Prüfung auf Motorstörungen und erkennen nicht jeden Leitungsfehler. Sensorlinse frei lassen; kein Glasfenster davor.

## 4. DM860T-V3.0-Einstellungen

Spannungslos einstellen; [Herstellerhandbuch](https://www.omc-stepperonline.com/download/DM860T_V3.0.pdf) hat Vorrang vor abweichenden Produktseiten.

| Schalter | Erstinbetriebnahme |
|---|---|
| S2 | **5 V** |
| SW1 / SW2 / SW3 | **ON / ON / ON**, 2,40 A Peak / 1,70 A RMS |
| SW4 | **OFF**, reduzierter Stillstandsstrom |
| SW5 / SW6 / SW7 / SW8 | **ON / OFF / ON / ON**, 1600 Pulse/Motorumdrehung |
| SW9 | **OFF**, STEP/DIR |
| SW10 | **OFF**, Rampen durch Firmware |

200 Vollschritte × 8 Mikroschritte × 2 Untersetzung = **3200 Pulse/Hauptachsenumdrehung**. Zunächst maximal 100 Pulse/s, mindestens 500 µs HIGH/LOW und 1 ms DIR-Vorlauf. Bei höherem Strom Temperatur und Leistungsbedarf erneut prüfen. Maximalwert laut V3.0-Handbuch: 7,20 A Peak / 5,09 A RMS; das sind nicht 6 A RMS und nicht garantiert 8,5 Nm im Betrieb.

## 5. Aufbau ohne Löten

1. Module und Uno isoliert befestigen; trockenen Standort und Lüftung sicherstellen. PS1 bleibt außerhalb der Box. Durchführungen nach tatsächlichen Kabeln wählen.
2. Header-Kabel aus Bestand verwenden: jeweils nur das benötigte freie Ende abisolieren. Keine Header-Metallstifte in WAGO stecken, sondern nur Leiter mit passendem Querschnitt. Schraubklemmen nach Herstellervorgabe mit passenden Aderendhülsen anschließen; keine verzinnten Litzenenden.
3. U6 auf den Uno stecken, Jumper auf 5 V setzen. STEMMA-Kabel und U4/U5 gemäß Tabellen verbinden. X1/X2 mit 11 mm abisolierter Leitung anklemmen.
4. J1/J2 und PIR verbinden; Patchkabel prüfen und anschließen. alle Verbindungen durchmessen.
5. W5 ausschließlich an der Verlängerung bearbeiten, Kontakte identifizieren, X1/X2 verdrahten und 48 V separat messen. Netzteilkabel selbst nicht verändern.
6. Treiber einstellen, Motorwicklungen messen und anschließen. Danach die gestuften [Inbetriebnahmeprüfungen](inbetriebnahme.md) durchführen.

Es werden keine Lochrasterplatine, IC-Sockel, HCT-Chip, Einzeltransistoren oder externen Widerstände oder Kondensatoren aufgebaut. Nicht benötigte Rev.-A-Bauteile stehen nur im Archiv. Die Motorhalterung ST-M7 ist die einzige mechanische Ausnahme in der Bestellliste; ihre Schrauben müssen nach dem tatsächlichen Lieferumfang gewählt werden.
