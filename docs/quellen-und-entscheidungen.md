# Quellen und Entscheidungen

Recherche und Dokumentationsstand: **26. September 2026**. Produktseiten sind Beschaffungsquellen, keine Garantie für Lagerbestand, Liefertermin oder die tatsächlich gelieferte Revision. Die unten genannten technischen Primärquellen wurden für Rev. A eingesehen. Beschaffungslinks unterscheiden konkrete Produkte, Sortimente und offene Auswahlpositionen. Die Dokumentprüfung prüft lokal das Format und die Konsistenz; sie ist keine Live-Verfügbarkeitsprüfung.

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

- 26.09.2026: Nutzer möchte nicht bevorzugt bei Reichelt bestellen und meldet unbrauchbare Links. Allgemeine Shop-Startseiten durch recherchierte Produktseiten bei BerryBase Schweiz, Bastelgarage, DigiKey und Conrad ersetzt. Kategorieverweise sind als Sortiment markiert; unbestätigte Artikel bleiben ohne vermeintlichen Kauflink offen. Artikel-/Packungshinweise ergänzen die Einbaumengen. F1 0001.2532 wird auf der recherchierten DigiKey-Seite als nicht lagernd geführt; keine ungeprüfte Sicherungsalternative übernommen.
- Beschaffungskonkretisierung ohne Änderung der Netze: J0 aus drei, J3 aus zwei anreihbaren 2-poligen Klemmen; Steuerplatine 120×80 mm statt ungefährem Planmaß 100×80 mm. PIR-/Uno-Leitungen aus fertigen Dupont-Leitungen mit je einem abgetrennten Stecker. Basis sind die in der CSV verlinkten Anbieterbeschreibungen; die Tabellen in `elektronik.md` bleiben maßgeblich.

- 26.09.2026: Logikanalysator (T04) laut Nutzer vorhanden; aus den Bestellpositionen entfernt.

- 26.09.2026: Multimeter (T03) laut Nutzer ebenfalls vorhanden; aus den Bestellpositionen entfernt.

- 26.09.2026: Lötkolben, Elektroniklot und Flussmittel laut Nutzer bereits vorhanden. T01 und V01 als Bestand führen, nicht als Bestellpositionen.

- 26.09.2026: Nutzer bestätigt E08 Patchkabel und E28 CH-Mehrfachsteckdose zusätzlich als vorhanden. Beide bleiben in der Materialliste, entfallen aber als Bestellposition. Arbeitsumfang und Beschaffungslisten werden auf Elektronik und zugehöriges elektrisches Zubehör begrenzt; Konstruktion, Mechanikteile und Kabelbinder entfallen. Keine zusätzliche Lochrasterplatine am PIR nötig; die Steuer-Lochrasterplatine E18 bleibt erforderlich.

- 26.09.2026: Nutzer entfernt S1 und Feld F aus dem Aufbau. S1/R7/J4 sowie C3/C4 und die zusätzliche Sensor-Lochrasterplatine entfallen. Der PIR wird direkt an J2 angeschlossen; Betrieb ohne Zusatzkondensatoren am endgültigen Kabel bei Motorstarts/-stopps prüfen. C1/C2/C5 bleiben auf der Steuerplatine. Nach Einschalten/Reset 60 s Anlaufzeit, danach mindestens 500 ms PIR-LOW und neue Bewegung; automatische Bereitschaft ohne manuelle Freigabe. J0.5 und D4 bleiben frei, übrige Anschlussnummern unverändert.

- 26.09.2026: Nutzer priorisiert **Preis vor Kompaktheit**. DM870 als kompaktere Alternative besprochen, aber nicht ausgewählt. **DM860T V3.0 bleibt der vorgesehene Treiber**; Schaltplan und Stückliste führen ihn bereits. Der Nutzer sieht einen Preisvorteil beim DM860T; ein aktueller Gesamtpreisvergleich inklusive Versand und Einfuhrkosten für die Schweiz wurde in diesem Entscheidungsschritt nicht durchgeführt.

- 26.09.2026: Nutzer bestätigt Einsatz in der Schweiz und gemeinsame Mehrfachsteckdose für beide Netzteile. S0 konkretisiert als fertige CH-Leiste mit Typ-13-Buchsen und gemeinsamem zweipoligem Schalter. Blatt 1 zeigt beide Steckplätze: W1 mit Typ-12-Stecker zu PS1, PS2 direkt eingesteckt. Die interne Netzverdrahtung von PS1 bleibt im geschützten Gehäuse. [ESTI: Schweizer Stecksystem](https://www.esti.admin.ch/inhalte/Info_SN_441011_de-fr-it-en.pdf); Anschlussklemmen siehe oben verlinktes Mean-Well-Datenblatt. Kein bestimmtes Leistenmodell damit für den Einschaltstrom freigegeben.

- 26.09.2026: Handover gelesen; Architektur mit Zahnriemen und separater Hauptachse bleibt Grundlage.
- Vorhandenes PIR-Modul optisch als HC-SR501-Bauform eingeordnet, Hersteller nicht feststellbar. Nutzer will es verwenden.
- Sensorleitung: RJ45-Patchkabel, bis 3 m, zwei verdrillte Paare für OUT/GND und 5V/GND.
- Aktueller bestätigter Elektronikbestand: **Uno (E01), PIR (E02), Patchkabel (E08) und Mehrfachsteckdose (E28)**. Frühere Bestandsangaben nur zu Uno/PIR sind damit ergänzt.
- Auftrag dieser Revision: deutsche Projektdokumente, Schaltplan, vollständige Material- und Bestellliste sowie Einchecken ins Repository. Keine Teile bestellen und noch keine Firmware implementieren.
- 26.09.2026: Auf Nutzeranfrage [15-mm-Hauptwelle gegenüber 20 mm rechnerisch vorgeprüft](hauptwelle-auslegung.md). 20 mm sind kein nachgewiesenes Mindestmaß; 15 mm sind eine plausible Alternative, abhängig von Riemenüberhang, Lasten und Nut-/Nabenausführung. Rechnung und zusätzliche Primärquellen stehen im Prüfdokument. Keine endgültige Durchmesseränderung beschlossen; davon abhängige Bestellpositionen bleiben bis zur Maßzeichnung offen.

## Technische Konkretisierungen dieser Revision

| Punkt | Entscheidung / Begründung |
|---|---|
| STEP/DIR | Zwei NPN-Stufen statt direkt belasteter GPIOs. Das konkretisiert die Treiberschnittstelle, der mechanische Antrieb bleibt gleich. |
| PIR-Leitung | RC-Filter und HCT-Schmitt-Trigger auf Empfängerseite; definierte Pegel und etwas Reserve gegen Störungen. Bei 3 m nicht grundsätzlich zwingend, aber Bestandteil dieses einheitlichen Entwurfs. |
| Arduino-Versorgung | Separates geschlossenes USB-Netzteil; kein 48→5-V-Wandler. Gemeinsame Netzverteilung S0 schaltet beide Netzteile. |
| Bedienung | Nur S0 als gemeinsame Netzabschaltung; kein Freigabeschalter. Nach jedem Einschalten/Reset automatische Bereitschaft nach Sensor-Anlauf und LOW-Phase. S0 ist kein zertifizierter Not-Halt. |
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
