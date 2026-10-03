# Elektronik · Revision B

Stand **04.10.2026**. Maßgeblicher Anschlussplan für den Aufbau mit fertigen Modulen. Noch keine Hardwaremessung; die Abnahmekriterien stehen in [Inbetriebnahme](inbetriebnahme.md). Revision A ist [historisch archiviert](archiv/revision-a/README.md).

## Schaltplanblätter

- [Blatt 1: Versorgung und Motor](schaltplan-versorgung.svg)
- [Blatt 2: Arduino, Signalmodule und PIR](schaltplan-steuerung.svg)

Die Bauteilnummer bleibt auf beiden Blättern gleich. Jeder Gerätekasten enthält Nummer und Modell. Gleichnamige Anschlüsse auf getrennten Feldern sind dieselben realen Anschlüsse. **X-Klemmen sind fertige WAGO-Verbindungsklemmen, keine Platinen.** Innerhalb einer einzelnen WAGO sind alle Anschlüsse verbunden; verschiedene WAGO müssen bei Bedarf ausdrücklich über ein Kabel verbunden werden.

## Geräte und Leitungen

| Kennung | Reales Bauteil |
|---|---|
| U1 | Arduino Uno R3 |
| U3 | STEPPERONLINE DM860T V3.0 |
| U4 / U5 | Adafruit MOSFET Driver #5648, je ein Modul für STEP / DIR |
| B1 | Vorhandenes PIR-Modul, HC-SR501-Bauform |
| M1 | STEPPERONLINE 34HS46-6004S1 |
| PS1 | Mean Well GST220A48-R7B, geschlossenes Tischnetzteil |
| PS2 | Goobay 44952, USB-Netzteil, nominal 5 V |
| S0 | Vorhandene geschaltete CH-Mehrfachsteckdose |
| J1 / J2 | DFRobot FIT0849, RJ45-Buchse auf Schraubklemmen; Steuerung / Sensor |
| X1 / X2 | WAGO 221-413, je 3 Anschlüsse für +48 V / 48-V-Rückleiter |
| X3 / X4 | WAGO 221-415, je 5 Anschlüsse für Uno +5 V / Signal-GND |
| W1 | Vorhandenes 230-V-Anschlusskabel; für PS1 CH-Stecker auf IEC-C13-Buchse auswählen |
| W2 | USB-A-auf-USB-B-Datenkabel zum Uno |
| W3 | Vorhandenes normales Cat5-/Cat6-RJ45-Patchkabel, 1:1, bis 3 m |
| W4 | 2 × 2 × 0,25 mm², paarverseilte Signalleitung zum Treiber, höchstens 0,5 m |
| W5 | GlobTek KPPX4124641M0KPJX4(R), 1-m-Power-DIN-Verlängerung, treiberseitig gekürzt |

Für den etwa vierstündigen Aufbau sind weder ein neues Steuergehäuse samt Montageplatte noch ein separates PIR-Sensorgehäuse vorgesehen. Den PIR fest ausrichten und seine Linse freihalten. Geräte mit vorhandenen Abstandshaltern befestigen und Leitungen zugentlasten; bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwenden.

## 1. Netzanschluss und Motorversorgung

**Keine offenen 230-V-Anschlüsse im Aufbau.** W1 aus dem bestätigten Kabelbestand auswählen; passende IEC-C13-Buchse für PS1 und Schutzleiter prüfen. W1 in Steckplatz 1 von S0 und in den IEC-C14-Eingang von PS1 stecken. PS2 in Steckplatz 2, W2 von PS2 zum Uno-USB-B-Anschluss. Das Netzteil PS1 separat, trocken, belüftet und zugentlastet aufstellen. Keine Änderung an Netzsteckern oder Netzteilgehäusen.

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

## 2. Direkte Arduino-Anschlüsse und Signalmodule

**Das DFRobot-Anschluss-Shield U6 / DFR0265 entfällt.** Der Uno bleibt per USB-B versorgt. Zwei fertige Hebelklemmen **X3/X4, WAGO 221-415**, verteilen seine 5 V und GND. Innerhalb einer Klemme sind alle fünf Plätze verbunden; **X3 und X4 niemals miteinander verbinden.** Die Platznummern werden von links nach rechts selbst beschriftet, sie sind keine WAGO-Werksnummern.

U4/U5 bekommen jeweils ein unverändertes **Adafruit-3894-Kabel**, JST PH 2 mm auf drei einzelne Buchsen. Diese Kabel sind nicht im Modul enthalten. Vorhandene 2,54-mm-Header-Leitungen E24 mit männlichen Steckern passen in diese Buchsen und in die Uno-Buchsenleisten. Die freien Löt-/Headerplätze am Modul bleiben unbenutzt. [Uno-Pins](https://docs.arduino.cc/resources/pinouts/A000066-full-pinout.pdf), [Adafruit #3894](https://www.adafruit.com/product/3894).

| Von | Nach | Ausführung |
|---|---|---|
| Uno **D2** | U4 STEMMA **In**, weiße E55-Buchse | Vorhandene Stecker/Stecker-Header-Leitung |
| Uno **D3** | U5 STEMMA **In**, weiße E55-Buchse | Vorhandene Stecker/Stecker-Header-Leitung |
| Uno **5V**, Power-Leiste | **X3.1** | Header-Stecker am Uno; anderes Ende abisoliert |
| **X3.2** | U4 STEMMA **V+**, rote E55-Buchse | Abisolierter Leiter an X3; Header-Stecker in E55-Buchse |
| **X3.3** | U5 STEMMA **V+**, rote E55-Buchse | Wie U4 |
| **X3.4** | **J1.5**, PIR +5 V | Beidseitig abisolierte Leitung |
| **X3.5** | Frei | Nicht belegen |
| Uno **erster GND nach 5V**, Power-Leiste | **X4.1** | Header-Stecker am Uno; anderes Ende abisoliert |
| **X4.2** | U4 STEMMA **GND**, schwarze E55-Buchse | Abisolierter Leiter an X4; Header-Stecker in E55-Buchse |
| **X4.3** | U5 STEMMA **GND**, schwarze E55-Buchse | Wie U4 |
| **X4.4** | **J1.2**, PIR GND | Beidseitig abisolierte Leitung |
| **X4.5** | **W4-Schirm** | Nur Steuerungsende; treiberseitig isolieren |
| Uno **zweiter GND nach 5V**, Power-Leiste | **J1.4**, zweite PIR-GND-Ader | Header-Stecker am Uno; anderes Ende abisoliert |
| Uno **A0** | **J1.1**, PIR OUT | Header-Stecker am Uno; anderes Ende abisoliert |

Die beiden GND-Buchsen der Power-Leiste liegen zwischen **5V und VIN** und sind intern verbunden. **VIN ist hier kein Anschluss.** A1/A2/A3 bleiben frei.

E24-Bedarf: zwei Stecker/Stecker-Leitungen, acht Steckerleitungen mit freiem Ende und zwei beidseitig freie Leiter, aus vorhandenem Kabelmaterial. Für X3/X4 nur zum Klemmbereich passende Leiter verwenden: feindrähtig **0,14–4 mm²**, vorzugsweise vorhandene AWG24-/AWG22-Leitungen; Ausführung im Bestand prüfen. Je Platz nur einen abisolierten Leiter, **11 mm Abisolierlänge**. Keine Header-Metallstifte einklemmen, keine verzinnten Litzenenden, zu dünne Litzen nicht durch Falten anpassen. Hebel schließen und leicht ziehen. STEMMA-Kabel selbst nicht kürzen; die Steckverbindungen zugentlasten. [WAGO 221-415](https://www.wago.com/ch-de/installationsklemmen/verbindungsklemme-mit-hebeln/p/221-415).

| Moduleingang / Ausgang | Verbindung zum Treiber |
|---|---|
| U4 Ausgang **+** | W4 → U3 **PUL+** |
| U4 Ausgang **−** | W4 → U3 **PUL−** |
| U5 Ausgang **+** | W4 → U3 **DIR+** |
| U5 Ausgang **−** | W4 → U3 **DIR−** |
| U3 ENA+/ENA−, ALM, BRK | Unbeschaltet |

**Die Minus-Ausgänge der Module sind keine dauerhaften GND-Anschlüsse. PUL−/DIR− nicht zusätzlich an GND anschließen.** Arduino-HIGH aktiviert das entsprechende Signal. Beide Ausgangspaare gehen unmittelbar zum Treiber. Zusätzliche einzelne Widerstände oder eine Ausgangsverteilerplatine sind nicht erforderlich.

Die Ausgangsklemmen am Modul sind **Federklemmen mit Drucktaste**, keine Schraubklemmen: Taste vorsichtig mit kleinem Schraubendreher drücken, abisolierte 0,25-mm²-Ader einführen, Taste loslassen und Zugprobe machen. Abisolierlänge nach gelieferter Klemme prüfen, keinen 11-mm-WAGO-221-Wert pauschal übertragen. [Herstelleranleitung](https://learn.adafruit.com/adafruit-mosfet-driver/plugging-into-the-terminal-block).

W4: ein verdrilltes Paar für PUL+/PUL−, das andere für DIR+/DIR−. Schirm nur am Ende an der Steuerung an X4.5, treiberseitig isolieren. Von Motor-/DC-Leistungskabeln getrennt führen. Gegebenenfalls freies Schirmende für die Klemme passend vorbereiten und isolieren.

Die Module sind für Versorgung **3–30 V** spezifiziert; hier ausschließlich Uno nominal 5 V. **S2 am DM860T auf 5 V.** Vor Motorbetrieb die Signalspannung **zwischen PUL+ und PUL−** beziehungsweise **DIR+ und DIR−** unter Last prüfen. Kein Anschluss dieser Module oder von X3/X4 an 48 V. Die Versorgung über USB-B des Uno bleibt bestehen.

## 3. PIR und RJ45-Patchkabel

Der PIR wird ohne Zusatzplatine direkt an **A0**, einen analogen Eingang des Uno, angeschlossen. Die Firmware wertet den typischen 3–3,3-V-Pegel aus. **D7 aus Revision A wird nicht verwendet.** Die tatsächliche VCC/OUT/GND-Pinfolge am vorhandenen PIR ist vor dem Anschließen zu prüfen.

| RJ45-Pin an J1 und J2 | Verbindung an der Steuerung J1 | Verbindung am Sensor J2 | Paar, T568B |
|---|---|---|---|
| 1 | Uno A0 direkt | B1 OUT | Weiß/Orange |
| 2 | X4.4 (Signal-GND) | B1 GND | Orange |
| 4 | Uno zweiter Power-GND direkt | Brücke zu J2.2 | Blau |
| 5 | X3.4 (+5 V) | B1 VCC | Weiß/Blau |
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

1. Module und Uno isoliert befestigen; trockenen Standort und Lüftung sicherstellen. PS1 separat und frei belüftet aufstellen. Zugentlastungen nach tatsächlicher Montage wählen.
2. Header-Kabel aus Bestand verwenden: jeweils nur das benötigte freie Ende abisolieren. Keine Header-Metallstifte in WAGO stecken, sondern nur Leiter mit passendem Querschnitt. Aderendhülsen und Crimpzange sind nicht vorgesehen. Vor dem Anschluss an DM860T und FIT0849 prüfen, ob die tatsächlich gelieferten Schraubklemmen blanke Litzen des verwendeten Querschnitts zulassen. Bei geeigneter Klemme alle Einzeldrähte vollständig einführen und den Halt durch leichtes Ziehen prüfen; keine verzinnten Litzenenden.
3. X3/X4 getrennt beschriften und gemäß Tabelle an Uno 5V/GND anschließen. STEMMA-Kabel über vorhandene Header-Leitungen an D2/D3 und X3/X4 verbinden. X1/X2 ebenfalls mit 11 mm abisolierter Leitung anklemmen.
4. J1/J2 und PIR verbinden; Patchkabel prüfen und anschließen. Alle Verbindungen durchmessen.
5. W5 ausschließlich an der Verlängerung bearbeiten, Kontakte identifizieren, X1/X2 verdrahten und 48 V separat messen. Netzteilkabel selbst nicht verändern.
6. Treiber einstellen, Motorwicklungen messen und anschließen. Danach die gestuften [Inbetriebnahmeprüfungen](inbetriebnahme.md) durchführen.

Es werden keine Lochrasterplatine, IC-Sockel, HCT-Chip, Einzeltransistoren oder externen Widerstände oder Kondensatoren aufgebaut. Nicht benötigte Rev.-A-Bauteile stehen nur im Archiv. Die Motorhalterung ST-M7 ist die einzige mechanische Ausnahme in der Bestellliste; ihre Schrauben müssen nach dem tatsächlichen Lieferumfang gewählt werden.
