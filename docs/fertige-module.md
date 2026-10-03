# Fertige Module · Auswahl für Revision B

**03.10.2026 · Dokumentierter Entwurf, noch kein Hardwaretest.** Die bisherige Lötplatine wird durch zwei Adafruit-Signalmodule und ein fertiges Uno-Anschluss-Shield ersetzt. Uno, PIR und Patchkabel bleiben. Der vollständige Anschluss steht in [Elektronik](elektronik.md), Beschaffung in [Bestellliste](../bom/bestellliste.md).

## Ausgewählte Kombination

- Motor **34HS46-6004S1** und **DM860T V3.0** bleiben.
- **2 × Adafruit MOSFET Driver #5648**, vollständig bestückt, mit montierter JST-PH-Buchse und Ausgangs-Federklemmen.
- **2 × Adafruit-STEMMA-Kabel #3894**, mit einzelnen Buchsenenden; separat bestellen.
- **DFRobot DFR0265 IO Expansion Shield V7.1** auf dem Uno. Es bietet zusätzliche steckbare Versorgung/GND-Anschlüsse und spart eine manuelle Steuer-Verteilung.
- Geschlossenes **Mean Well GST220A48-R7B**, **48 V / 4,6 A / 221 W**, mit fertigem Typ-12/C13-Netzkabel.
- **GlobTek KPPX4124641M0KPJX4(R)**-Power-DIN-Verlängerung; nur männliches Verlängerungsende abschneiden und zum Treiber klemmen. Netzteil selbst bleibt unverändert.
- Separates USB-Netzteil für Uno; beide fertigen Netzanschlüsse in vorhandene CH-Mehrfachsteckdose.
- PIR direkt an **A0**, über bestehendes RJ45-Kabel und zwei FIT0849-Adapter; keine Sensor-Zusatzplatine.

**Kein Löten, keine zusätzlichen einzelnen Widerstände/Kondensatoren.** Es bleiben Kabelstecken, die Kleinspannungs-Klemmverbindungen, Befestigung der Geräte und Firmware. Ein gekauftes Motor-Treiber-Kit würde diese Aufgaben nicht vollständig übernehmen.

## Warum diese Signalmodule?

Die letzte technische Prüfung ersetzt die DFR0457-Vorauswahl durch Adafruit #5648: Die Adafruit-Module decken Versorgung 3–30 V ab und eignen sich für die Uno-5-V-Schiene. Der dokumentierte Herstellerplan enthält bereits den Widerstand für ausgeschaltete Signale. Separate geklemmte Ausgangswiderstände entfallen. Das sind fertige **Signalschalter**, der eigentliche Motortreiber bleibt der DM860T. [Hersteller-Pins](https://learn.adafruit.com/adafruit-mosfet-driver/pinouts), [Hersteller-Boardunterlagen](https://github.com/adafruit/Adafruit-MOSFET-Driver-STEMMA-PCB).

Bei U4/U5 wird der **Minus-Ausgang geschaltet**, Plus führt die Modulversorgung. Deshalb Ausgangspaare direkt an PUL+/PUL− und DIR+/DIR− anschließen; **keine zusätzliche GND-Brücke an PUL−/DIR−**. Schaltplan und Pinliste gelten ausschließlich für diese Ausführung. Die Module bekommen nie 48 V.

U6-Jumper auf 5 V, Modulversorgung über die **analogen A1-/A2-Versorgungsstifte**; Signal über D2/D3. Die digitale Versorgungsreihe wird nicht benutzt, um deren zusätzlichen Versorgungspfad zu vermeiden. [Shield-Plan](https://dfimg.dfrobot.com/wiki/18598/DFR0265_io-expansion-shield-for-arduino_schematics_V1.0.pdf). Der vorhandene Uno bleibt per USB versorgt.

Vor Motorbetrieb belastete Treiberpegel und Pulszeiten messen. Die Auswahl ist aus Herstellerunterlagen begründet, keine bereits getestete Gesamtanlage. Erstbetrieb maximal 100 Pulse/s, mindestens 500 µs HIGH/LOW und 1 ms DIR-Vorlauf als konservative Prüfwerte.

## Warum 221 W für die langsame Erstkonfiguration?

Motorphasenstrom und Netzteil-Ausgangsstrom sind unterschiedliche Größen. Für die erste Stromstufe beträgt eine bewusst großzügige Kupferverlustabschätzung bei zwei gleichzeitig voll bestromten Wicklungen und angenommenem warmem Widerstand von 0,9 Ω etwa **2 × 2,4² × 0,9 = 10,4 W**. Die Annahme 0,9 Ω enthält Reserve gegenüber dem spezifizierten kalten Phasenwiderstand 0,58 Ω; sie ist kein gemessener Widerstand.

Auch bei 7,2 A Peak ergäbe dieselbe großzügige Abschätzung rund 93 W. Bei 100 Pulsen/s beträgt die Motordrehzahl 0,393 rad/s; selbst mit angenommenen 8,5 Nm entspräche das nur etwa 3,3 W mechanischer Leistung. Mit beispielhaft weiteren 50 W für Treiber-/Eisenverluste bleibt die Abschätzung unter 150 W. Diese zusätzlichen Verlustwerte sind **Planannahmen**, keine Herstellergarantie. Sie begründen die Auswahl für einen langsamen Einzelmotor, ersetzen aber nicht Last-, Temperatur- und Bremstests. Der Erstbetrieb erfolgt ausdrücklich mit 2,40 A Peak; höhere Stromstufen benötigen neue Prüfung.

Das Netzteil kann Bremsenergie nicht nachweislich aktiv aufnehmen. Erst langsame Rampen und Messung unter realer Last erlauben eine Aussage zur Rückspeisung. Der Kabelhersteller nennt 56 V; Entwurfsziel beim Bremsen höchstens 50 V. Keine Zusage für höhere Drehzahlen, mehrere Motoren oder dauerhaft maximales Drehmoment. [Motorprodukt](https://www.omc-stepperonline.com/fr/moteur-pas-a-pas-nema-34-serie-s-8-5nm-1203-94oz-in-14mm-arbre-a-cle-cable-1m-34hs46-6004s1), [GST220A-Datenblatt](https://www.meanwell.com/Upload/PDF/GST220A/GST220A-SPEC.PDF).

## Preis und Alternativen

| Variante | Bewertung |
|---|---|
| DM860T + 2 × Adafruit #5648 + DFR0265 | Preisorientierte Auswahl mit montierten Anschlüssen, keine eigene Signalplatine |
| DFR0457-Vorauswahl | Zusätzliche Ausgangswiderstände und knappe untere Versorgungsspezifikation; durch Adafruit ersetzt, nicht bestellen |
| Pololu Tic 36v4 #3140 | Montierte Anschlüsse und Arduino-Bibliothek, aber etwa 4 A ohne Zusatzkühlung und höchstens 50 V; keine ungeprüfte 6-A-/48-V-Ersatzlösung |
| Geckodrive G201X | Direkte Logikansteuerung laut Handbuch; höherer Preis, Zusatzkühlung oberhalb 3 A |

Quellen: [Tic #3140](https://www.pololu.com/product/3140), [Tic-Handbuch](https://www.pololu.com/docs/0J71/all), [G201X](https://www.geckodrive.com/product/g201x-digital-step-drive/), [G201X-Handbuch](https://www.geckodrive.com/wp-content/uploads/2023/04/G201X-and-G210X-Manual-011717.pdf).

**Aktuelle Beschaffung:** Schweizer Händler oder Amazon bevorzugt, DigiKey und Farnell ausgeschlossen. Zwei Adafruit #5648 kosten bei [Play-Zone](https://www.play-zone.ch/de/adafruit-mosfet-driver-for-motors-solenoids-leds-etc-stemma-jst-ph-2mm.html) beim Abruf zusammen CHF 11.80. Ein DFR0265-Shield kostet bei [Bastelgarage](https://www.bastelgarage.ch/gravity-io-expansion-shield-fur-arduino-v7-1) CHF 11.90. Die zwei Kabel #3894 haben derzeit noch keine verifizierte Schweizer/Amazon-Bezugsquelle. Damit lässt sich für die vollständige Arduino-Schnittstelle noch kein Gesamtpreis nennen; frühere Bündelpreise gelten nicht mehr als Beschaffungsvorschlag.

**Lieferanforderung: binnen 7 Kalendertagen in der Schweiz erhalten.** Antrieb, Motornetzteil und Spezialkabel sind innerhalb dieser Vorgaben noch nicht vollständig beschaffbar belegt. Simpex führt PS1 nur auf Bestellung; Distrelec/RS nennt Nachschub am 16.10.2026. E26 Steuerkabel W4 und E35 DC-Leistungslitze sind inzwischen als vorhanden bestätigt und nicht zu bestellen. BerryBase wird als CH-Shop mit ungeprüftem Versandlager geführt. Keine Teile wurden bestellt oder elektrisch geändert. [Aktuelle Händlerprüfung](quellen-und-entscheidungen.md#schweizer-händler-oder-amazon), [Bestellliste](../bom/bestellliste.md).

**Komplettpreis noch offen:** Antrieb, Anschlusskabel, CH-Versand und Montagezubehör fehlen. Kein Nachweis für das günstigste Gesamtpaket. Für den etwa vierstündigen Aufbau entfällt die Neubeschaffung von Steuergehäuse und Montageplatte. Bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwenden; Montage und Zugentlastung nach tatsächlichem Aufbau festlegen.
