# Quellen und Entscheidungen

Aktuelle Aufbauvorgabe: **3. Oktober 2026**. Technischer Stand der bisherigen Rev. A: **26. September 2026**. Produktseiten sind Beschaffungsquellen, keine Garantie für Lagerbestand, Liefertermin oder die tatsächlich gelieferte Revision. Die unten genannten technischen Primärquellen wurden für Rev. A eingesehen. Beschaffungslinks unterscheiden konkrete Produkte, Sortimente und offene Auswahlpositionen. Die Dokumentprüfung prüft lokal das Format und die Konsistenz; sie ist keine Live-Verfügbarkeitsprüfung.

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

- 03.10.2026: Bei der weiteren Anschlussrecherche den fertigen Mean-Well-Adapter **DC PLUG-R7BF-P1M** gefunden. Das [Hersteller-Auswahlblatt](https://www.meanwell.com/upload/pdf/DC_plug.pdf) ordnet ihn dem R7B-Ausgang der GST120–220-Serie zu; [DigiKey Schweiz](https://www.digikey.ch/de/products/detail/mean-well-usa-inc/DC-PLUG-R7BF-P1M/12142223) führt den Einzelartikel. Er endet auf einem 5,5/2,5-mm-DC-Stecker und löst damit nur den ersten Anschlussabschnitt. Die passende fertig montierte Buchse auf Leitungen/Klemmen und deren 48-V-/Stromfreigabe sind noch offen. Recherchefund, keine neue Bestellfestlegung; CSV und historische Schaltpläne bleiben unverändert.
- 03.10.2026: Nutzer bestätigt erneut, dass noch keine Teile bestellt wurden. Damit können Motor, Controller und Netzteil gemeinsam neu ausgewählt werden. Der bereits bestätigte Bestand bleibt erhalten.
- 03.10.2026: [Vorauswahl fertiger Module](fertige-module.md) recherchiert. Zwei fertig bestückte DFRobot DFR0457 können eine günstige Schnittstelle für STEP/DIR zum DM860T bilden; Herstellerplan zeigt geschaltetes positives VOUT, daher andere Treiberverdrahtung als Rev. A. Geschlossenes Mean Well GST220A48-R7B als Netzteilkandidat mit Schweizer Quellen aufgenommen. Die Kombination ist noch nicht abschließend ausgewählt: insbesondere DC-Kabel/Adapter, Leistungsreserve und belastete Signalpegel offen. Kein vollständiger Rev.-B-Schaltplan und keine Hardwareprüfung. Pololu bleibt Alternative mit begrenztem Motorstrom; kein 6-A-Betrieb ohne ausreichende Kühlung zugesagt.
- 03.10.2026: Nutzer bestätigt: fertige Module sind entscheidend; Aufwand und Fehlerrisiko einer selbst gelöteten Zusatzschaltung sind zu groß. Rev. A wird daher als überholt gekennzeichnet. Die bisherige Beschaffung ist keine Empfehlung für die neue Ausführung; Bestandsänderungen sind erst nach Bestätigung einzutragen. Eine konkrete neue Controller-/Netzteilkombination wurde noch nicht festgelegt.
- Kandidat für unkomplizierte Arduino-Anbindung: [Pololu Tic 36v4 #3140 mit montierten Anschlüssen](https://www.pololu.com/product/3140). [Herstellerhandbuch](https://www.pololu.com/docs/0J71/all): Arduino-Ansteuerung über Serial/I²C, integrierte Bewegungserzeugung; etwa 4 A pro Phase ohne zusätzliche Kühlung, bis 6 A mit ausreichender Kühlung, Versorgung 8–50 V. Deshalb keine pauschale Ersatzempfehlung für M1 mit 6 A oder ungeprüfte Verwendung der bisherigen 48-V-Versorgung. Ein neues Modulkonzept benötigt einen eigenen vollständigen Verbindungsplan und Belastungstest.

- 26.09.2026: Platinen-Abstandshalter E42 und Header-Kabel sind laut Nutzer bereits ausreichend vorhanden. E23 (PIR) und E24 (Uno) verwenden diesen Kabelbestand. Alle drei Positionen bleiben als benötigte Teile in der Materialliste, entfallen aber als Bestellpositionen.

- 26.09.2026: Auf ausdrücklichen Nutzerwunsch Motorhalterung als Ausnahme zum Elektronikumfang aufgenommen: E47, ein [STEPPERONLINE ST-M7](https://www.omc-stepperonline.com/nema-34-bracket-for-stepper-motor-alloy-steel-bracket-st-m7). Produktseite und [Hersteller-Kompatibilitätsübersicht](https://help.omc-stepperonline.com/hc/s/articles/motor-types-that-the-brackets-on-sale-can-match) nennen NEMA-34-Schrittmotoren; M1 hat einen 86×86-mm-Rahmen. Die Maßzeichnungsdownloads waren beim Abruf blockiert, daher kein behaupteter vollständiger Maßabgleich. Lochbild, Zentrierbund und Schraubenlieferumfang vor Montage prüfen; Einbau mit senkrechter Motorwelle und Einstellweg für Riemenspannung berücksichtigen. Übrige Mechanik bleibt außerhalb der Beschaffungsliste.

- 26.09.2026: Distrelec Schweiz auf Nutzerwunsch als weitere Bezugsquelle geprüft. Passende Produktdaten für E07 (L-Com U2A00002-1M, Distrelec 305-04-706) und E17 (Panasonic ECA1HHG100I, 167-25-806) gefunden; konkrete Links stehen in `teile.csv` und der Bestellliste. Die indexierten Händlerseiten bestätigen A–B/1 m beziehungsweise 10 µF/50 V/radial/2,5-mm-Raster. Direkte Seitenabrufe wurden blockiert; Preise, Bestelleinheiten und aktuelle Lieferbarkeit sind nicht bestätigt. Bestehende Bezugsquellen bleiben erhalten.
- Bei dieser Distrelec-Recherche keine eindeutigen Produktseiten für SN74HCT14N, die festgelegten SCHURTER 0001.2532/0001.2533 und die offenen Netzanschluss-/Sicherungshalterpositionen bestätigt. Das ist kein Nachweis, dass Distrelec sie nicht führt. Der gefundene SN74HC14N wird nicht als Ersatz für den festgelegten HCT-Typ übernommen. Die gefundenen 100er-Widerstandsrollen und 100-m-Litzenrollen werden für den kleinen Projektbedarf nicht als bevorzugte Beschaffung eingetragen.

- 26.09.2026: Schrumpfschläuche (E44) sind laut Nutzer ausreichend vorhanden und nicht zu bestellen. Elektrische Beschriftung als E46 getrennt; deren Bestand ist noch nicht bestätigt.

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
