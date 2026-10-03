# Quellen und Entscheidungen · Revision B

Stand **03.10.2026**. Aktuelle Entscheidung ist der Aufbau mit fertig bestückten Modulen ohne eigene Lötplatine. Frühere Entscheidungen und Recherche einschließlich des R7B-Barreladapters bleiben im [Archiv](archiv/revision-a/quellen-und-entscheidungen.md) erhalten. Sie gelten nicht parallel zu diesem Anschlussplan.

## Herstellerquellen

| Quelle | Verwendung |
|---|---|
| [34HS46-6004S1](https://www.omc-stepperonline.com/fr/moteur-pas-a-pas-nema-34-serie-s-8-5nm-1203-94oz-in-14mm-arbre-a-cle-cable-1m-34hs46-6004s1) | Motor, Wicklungen, Phasenwiderstand, Lieferkabel |
| [DM860T V3.0](https://www.omc-stepperonline.com/download/DM860T_V3.0.pdf) | Klemmen, DIP, Signalpegel, Peak/RMS und Stromstufen |
| [Adafruit #5648 Pins](https://learn.adafruit.com/adafruit-mosfet-driver/pinouts) | Versorgung, Signale und Ausgangsklemmen |
| [Adafruit-Boardunterlagen](https://github.com/adafruit/Adafruit-MOSFET-Driver-STEMMA-PCB) | Vorbestückte Schaltung mit Signal-Pull-down und geschaltetem Minus-Ausgang |
| [AO3406-Datenblatt](https://cdn-shop.adafruit.com/product-files/5648/5648_ds_AO3406.pdf) | Schalttransistor, niedriger Spannungsabfall bei kleinem Treibersignalstrom |
| [DFR0265-Shield](https://wiki.dfrobot.com/dfr0265/) | Steckbare Uno-Anschlüsse und 5-V-Jumper |
| [DFR0265-Schaltplan](https://dfimg.dfrobot.com/wiki/18598/DFR0265_io-expansion-shield-for-arduino_schematics_V1.0.pdf) | Direkte Analog-Versorgung, digitale Versorgungsreihe und gemeinsamer GND |
| [GST220A](https://www.meanwell.com/Upload/PDF/GST220A/GST220A-SPEC.PDF) | 48 V / 4,6 A, Ausgangskontakte R7B, PE-Verbindung, Temperatur und Überlastschutz |
| [GlobTek Kabelspezifikation](https://spec.globtek.info/spec/cord_spec?id=01t3a000004eQInAAM) | KPPX4124641M0KPJX4(R), 4×AWG18, 5 A pro Ader, 56-V-Steckerfreigabe, Kontaktzeichnungen |
| [WAGO 221](https://www.wago.com/fr/produits/technique-de-raccordement/bornes-de-raccordement-221) | Klemmbereiche, Verbindungsprinzip und Abisolierlänge |
| [Arduino Analogpins](https://github.com/arduino/docs-content/blob/main/content/learn/02.microcontrollers/02.analog-input/analog-input.md) | Analogauswertung und INPUT_PULLUP auf A0 |
| [Joy-IT HC-SR501](https://joy-it.net/en/products/SEN-HC-SR501) | Vergleichsdaten PIR, keine Herstelleridentifikation des eigenen Sensors |
| [Hammond 1554](https://www.hammfg.com/electronics/small-case/plastic/1554) | Gehäuse-/Montageplattenvorschlag, ABS für geschützten Einsatz |
| [ST-M7](https://www.omc-stepperonline.com/de/nema-34-halterung-fuer-schrittmotor-halterung-aus-legiertem-stahl-st-m7) | Ausdrücklich gewünschte NEMA-34-Motorhalterung |

GlobTek und Mean Well verwenden **unterschiedliche Pinnummern**. Maßgeblich ist deshalb die geprüfte Kontaktlage am Netzteil, nicht die Übernahme von Ziffern auf die Verlängerung. Herstellerunterlagen belegen Kabel-/Steckerfamilie und Belastbarkeit, aber keine individuelle Aderfarbe des gelieferten Kabels. Durchgangs- und Spannungsprüfung bleibt Pflicht.

## Entscheidungen vom 03.10.2026

1. Nutzer bestätigt: **keine Antriebsteile bestellt**, fertige Module entscheidend. Vorhandener Elektronik-/Werkzeugbestand bleibt; keine Bestellung wird ausgelöst.
2. **DM860T V3.0 und 34HS46-6004S1 bleiben.** Kompaktheit ist nachrangig, kein Wechsel zum DM870 allein deswegen. Pololu/G201X bleiben recherchierte Alternativen, keine parallel vorgesehenen Teile.
3. **U4/U5 Adafruit #5648 statt Eigenbauplatine**, mit #3894-Kabeln und U6 DFR0265-Shield. Die DFR0457-Vorauswahl wird ersetzt: Adafruit unterstützt die Uno-Versorgung ohne nominelle 5-V-Untergrenze und braucht keine zusätzlichen geklemmten Ausgangswiderstände. Hersteller-Schaltplan bestätigt vorhandenen Signal-Pull-down. Ausgangspaare direkt an Treiber, keine GND-Brücke auf PUL−/DIR−. Shield-Versorgung für Module bewusst aus A1/A2; digitale Versorgungsreihe bleibt unbenutzt. Dadurch durchgehend gesteckte Modul-Eingangsanschlüsse. Belastete Treiberpegel bleiben real zu messen.
4. **PIR von D7 auf A0.** Analogauswertung mit Pull-up spart den HCT-/Filteraufbau und erlaubt, ein offenes OUT typischerweise als ungültig zu erkennen. Schwellen müssen am vorhandenen Exemplar gemessen werden; keine zugesicherte Erkennung aller Kabelfehler. 60 s Anlauf, 500 ms LOW und neue Bewegung bleiben.
5. **GST220A48-R7B statt LRS-350-48.** Fertiger Netzanschluss und berührungsgeschlossenes Gehäuse reduzieren Eigenbau. Leistungsabschätzung und Grenzen in [Modulauswahl](fertige-module.md), Abnahme in [Inbetriebnahme](inbetriebnahme.md). Langsame Erstkonfiguration, keine Zusage für volle Dauerleistung des Motors.
6. **W5 GlobTek Power-DIN-Verlängerung** statt R7BF/P1M-Barreladapter. Adapter wäre der erste Anschlussabschnitt, sein nachfolgender Buchsen-/Klemmteil war nicht nachgewiesen. Das ausgewählte W5 hat fertig montierte Enden und dokumentierte Belastbarkeit; nur das männliche Verlängerungsende wird bearbeitet. Beide Adern je Schiene verwenden.
7. **Keine eigene Netzbaugruppe.** S0 speist PS1 über fertiges Typ-12/C13-Kabel und PS2 direkt. Offene Netzenden, zusätzliche Rev.-A-Sicherungen und PE-Verteilung entfallen. Andere Leitungsquerschnitte/Abgänge erfordern erneute Auslegung; kein Netzteil öffnen.
8. **Gehäuseannahme trocken/geschützt**, noch keine Nutzerbestätigung. Vorschlag Hammond 1554YAGY/1554YPL; Auswahl und Durchführungen nach realem Layout. Kein Regen-/IP-Nachweis nach eigenen Bohrungen.
9. Schaltpläne zeigen nur Geräte, reale Pins, Kabel und Einstellungen. Innere Schaltungen fertiger Geräte werden nicht gezeichnet. Material-/Bestellliste bleibt auf Elektronik plus ausdrücklich ST-M7 beschränkt.

## Noch ausstehende Nachweise

- Reale Treiberrevision, PIR-Pinfolge, belastete Modulpegel und Versorgungsspannung.
- Finaler Standort, Gehäuselayout, Lüftung, Durchführungen und Schraubenmaße.
- Netzteil-Leistungsreserve und Spannung beim Bremsen an tatsächlicher Last.
- Firmware, Sensor-Störfestigkeit am 3-m-Kabel, Temperatur- und Bewegungstests.
- Schweizer Warenkorbpreise und tatsächliche Liefertermine.

Dokumentprüfungen sind keine Hardware-, Sicherheits- oder Verfügbarkeitsprüfung. Modellangaben stammen aus Herstellerunterlagen; tatsächliche Lieferung vor Aufbau vergleichen. Referenzen in alten Mechanikdokumenten sind Projektkontext und begründen keine zusätzliche Mechanikbestellung.
