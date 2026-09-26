# Quellen und Entscheidungen

Recherche und Dokumentationsstand: **26. September 2026**. Produktseiten sind Beschaffungsquellen, keine Garantie für Lagerbestand, Liefertermin oder die tatsächlich gelieferte Revision. Die unten genannten technischen Primärquellen wurden für Rev. A eingesehen. Händlerlinks für Standardmaterial in der Bestellliste sind teilweise nur Bezugsquellen; dies wird dort ausdrücklich unterschieden.

## Primärquellen

| Quelle | Verwendung |
|---|---|
| [STEPPERONLINE 34HS46-6004S1](https://www.omc-stepperonline.com/fr/moteur-pas-a-pas-nema-34-serie-s-8-5nm-1203-94oz-in-14mm-arbre-a-cle-cable-1m-34hs46-6004s1) | Motor, Maße, Welle, Aderfarben |
| [DM860T Produktseite](https://www.omc-stepperonline.com/digital-stepper-driver-2-4-7-2a-18-80vac-or-24-110vdc-for-nema-34-motor-dm860t) | Treiber-Beschaffung und dokumentierte Variantenunterschiede |
| [DM860T V3.0 Handbuch](https://www.omc-stepperonline.com/download/DM860T_V3.0.pdf) | Kapitel 3 Anschluss, 4 Optokoppler, 7 DIP-Tabelle, 10 Pulszeiten |
| [Mean Well LRS-350 Datenblatt](https://www.meanwell.com/Upload/PDF/LRS-350/LRS-350-SPEC.PDF) | 48-V-Versorgung, Netzspannungswahl, Einschaltstrom, Einbaubedingungen |
| [TI SN74HCT14](https://www.ti.com/lit/gpn/SN74HCT14) | HCT-Eingangspegel und DIP-Pinbelegung |
| [onsemi 2N3904](https://www.onsemi.com/pdf/datasheet/2n3904-d.pdf) | Transistor-Anschlüsse und Schaltbetrieb |
| [SCHURTER SPT 6,3×32](https://www.schurter.com/en/datasheet/typ_spt_6.3x32.pdf) | Sicherungsnummern und DC-Spannungsfreigabe |
| [Joy-IT HC-SR501](https://joy-it.net/en/products/SEN-HC-SR501) | Vergleichsmodul; nicht Herstelleridentifikation des vorhandenen Exemplars |
| [Adafruit PIR-Anleitung](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor?view=all) | Signalverhalten, Einschwingzeit, H/L-Modus |
| [Adafruit zur Kabelverlängerung](https://forums.adafruit.com/viewtopic.php?p=750863) | Hersteller-Support zu CAT5 als PIR-Leitung; keine garantierte Längenfreigabe |
| [DOLD UCFL204, Artikel 35334](https://www.dold-mechatronik.de/Flanschlager-20mm-UCFL-204) | Konkreter Lagerkandidat |
| [STEPPERONLINE ST-M7](https://www.omc-stepperonline.com/de/nema-34-halterung-fuer-schrittmotor-halterung-aus-legiertem-stahl-st-m7) | Montagewinkel-Kandidat |
| [eBay, Händler glhk01, Riemenscheibenangebot](https://www.ebay.com/itm/156430925515) | 20T/40T, 15-mm-Riemen, Bohrungen/Nutvarianten; Kombination im Auswahlmenü prüfen |
| [ConCar, Gates HTD-5M-Riemen](https://www.concar-shop.de/shop/en/belts/timing-belts/timing-belts/gates-synchronous-belts-powergrip-htd/gates-synchronous-belts-powergrip-htd-dimension-5m.html) | Riemen 450-5M-15, Artikel GT045005015 |

## Festlegungen aus dem Gespräch

- 26.09.2026: Handover gelesen; Architektur mit Zahnriemen und separater Hauptachse bleibt Grundlage.
- Vorhandenes PIR-Modul optisch als HC-SR501-Bauform eingeordnet, Hersteller nicht feststellbar. Nutzer will es verwenden.
- Sensorleitung: RJ45-Patchkabel, bis 3 m, zwei verdrillte Paare für OUT/GND und 5V/GND.
- Nutzer bestätigt: **Nur Uno und PIR vorhanden, alles Weitere noch zu bestellen.** Dies ist der aktuelle Bestand, auch wenn das Handover bereits einen Wagen beschreibt. Für Wagen/Spinne ist vor Neukauf ein Bestandsabgleich sinnvoll.
- Auftrag dieser Revision: deutsche Projektdokumente, Schaltplan, vollständige Material- und Bestellliste sowie Einchecken ins Repository. Keine Teile bestellen und noch keine Firmware implementieren.

## Technische Konkretisierungen dieser Revision

| Punkt | Entscheidung / Begründung |
|---|---|
| STEP/DIR | Zwei NPN-Stufen statt direkt belasteter GPIOs. Das konkretisiert die Treiberschnittstelle, der mechanische Antrieb bleibt gleich. |
| PIR-Leitung | RC-Filter und HCT-Schmitt-Trigger auf Empfängerseite; definierte Pegel und etwas Reserve gegen Störungen. Bei 3 m nicht grundsätzlich zwingend, aber Bestandteil dieses einheitlichen Entwurfs. |
| Arduino-Versorgung | Separates geschlossenes USB-Netzteil; kein 48→5-V-Wandler. Gemeinsame Netzverteilung S0 schaltet beide Netzteile. |
| Bedienung | S1 als Freigabeschalter ergänzt; Firmware muss nach Reset eine bewusste Freigabe verlangen. S0 ist Netzabschaltung, S1 Softwarefunktion, kein zertifizierter Not-Halt. |
| ENA / ALM / BRK | In Rev. A unbeschaltet. Der Treiber kann im Stillstand bestromen. Ausfall der Motorversorgung bei aktivem Uno wird nicht automatisch erkannt. |
| DM860T-Versorgung | Handbuchreferenz V3.0 mit AC/AC-Klemmen und 48-VDC-Versorgung, nicht die vereinfachte VDC+/VDC−-Darstellung aus dem Handover. |
| Strom | Peak und RMS getrennt. Unterschiedliche Herstellerangaben offengelegt; Strom zunächst niedrig und Drehmoment praktisch prüfen. |
| Bewegungswerte | Handover-Tempo nicht als langsam garantiert. Rechnung mit Radius und Rampen in `firmware.md`; langsamer Prüfstandstart. |
| Riemen/Welle | Budget-Alu-Scheiben bleiben vorgesehen, Nut/Passfeder und Drehmomentübertragung werden aber ausdrücklich geprüft. |
| Historisches Material | Handover unverändert archiviert. Neuere Verdrahtung und Bestand stehen in den aktuellen Dokumenten. |

## Noch offene Freigaben am realen Aufbau

1. Physische PIR-Pinreihenfolge und tatsächliche Treiberversion.
2. Rohrmaße, Wagengeometrie, Rollwiderstand, Nabenmaße und Wellenbearbeitung.
3. Schaltvermögen der gewählten Netzverteilung, Schutzkoordination und Elektroprüfung der 230-V-Baugruppe.
4. Preise, Versand in die Schweiz und Variantenverfügbarkeit. Frühere CHF-Schätzungen nicht als aktuelle Gesamtkosten verwenden.
5. Firmware-Implementierung, Pulszeitmessung, Temperaturtest und mechanischer Funktionstest.

Das LRS-350-Datenblatt enthält außerdem Einschränkungen zur Netzoberschwingungskonformität bestimmter Anwendungen. Der Lieferant/Elektroaufbauer muss die Eignung für Einsatzort und fertige Anlage bestätigen; die Modellwahl ist keine pauschale Konformitätszusage. Eine gegebenenfalls notwendige Netzteilalternative muss wieder 48 V und ausreichende Leistung liefern und wird erst nach Auswahl in den Plan eingearbeitet.
