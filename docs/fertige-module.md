# Fertige Module ohne eigene Lötplatine

Stand: **03.10.2026 · Recherche und Vorauswahl, kein fertiger Anschlussplan und kein Hardwaretest.**

Der Nutzer hat noch keine Antriebsteile bestellt. Arduino Uno R3, vorhandener PIR, Patchkabel und das weitere dokumentierte Zubehör bleiben Bestand. Die neue Ausführung soll aus fertig bestückten Modulen mit montierten Anschlüssen bestehen. Kabel stecken oder in Klemmen anschließen bleibt erforderlich; eine eigene Lötplatine entfällt.

## Ergebnis der Vorauswahl

**Eine preisorientierte Lösung ist mit dem bisherigen Motor und DM860T möglich:** zwei fertige **DFRobot DFR0457** für STEP und DIR, dazu ein **geschlossenes Tischnetzteil** statt LRS-350-48. Der Motortreiber selbst ist bereits ein fertiges Gerät mit Anschlussklemmen. Der Eigenbau in Rev. A betraf seine Schnittstelle zum Arduino und die PIR-Aufbereitung.

Die DFR0457-Module werden hier ausschließlich zum Schalten der **5-V-Steuersignale** vorgeschlagen. Sie treiben weder den Motor noch dessen 48-V-Versorgung. Herstellerunterlagen nennen 3,3–10 V Steuersignal, 5–36 V am Lastanschluss und bis 1 kHz Schaltfrequenz. Für die geplante langsame Bewegung reicht diese Frequenz rechnerisch aus. [DFRobot Produkt](https://www.dfrobot.com/product-1567.html), [Hersteller-Wiki](https://wiki.dfrobot.com/dfr0457/).

**Noch nicht als komplettes Set bestellen:** Das passende fertig konfektionierte DC-Netzteilkabel ist noch nicht bestimmt. Außerdem sind Leistungsreserve und belastete Signalpegel abschließend zu prüfen. Die bisherigen Schaltplanblätter bleiben ausdrücklich überholt; ihre Verdrahtung darf nicht auf die neuen Module übertragen werden.

## Vergleich

| Variante | Aufbau ohne eigene Lötplatine | Verbleibende Einschränkung | Bewertung |
|---|---|---|---|
| DM860T + 2 × DFR0457 | Zwei fertig bestückte Module, mitgelieferte Signalkabel und Schraubklemmen; Uno erzeugt STEP/DIR | Zusätzliche Leitungen; langsamer als eine direkte digitale Schnittstelle; Pegel unter Last prüfen | Preisorientierte Vorauswahl für den bisherigen NEMA-34-Motor |
| Pololu Tic 36v4 **#3140** | Anschlüsse bereits eingelötet; Arduino-Bibliothek, Bewegungserzeugung im Controller | Etwa 4 A ohne Zusatzkühlung, 6 A nur mit ausreichender Kühlung; maximal 50 V | Bequeme Alternative bei entsprechend ausgelegtem Motorstrom und Netzteil |
| Geckodrive G201X | Fertiger Treiber; laut Handbuch direkte 3,3-/5-V-Ansteuerung mit rund 2,5 mA möglich | Oberhalb 3 A ausdrücklich Kühlkörper erforderlich; höhere Anschaffungskosten | Technisch interessante Alternative, nicht allein wegen des Gehäuses wählen |
| Motor-Treiber-Kit von STEPPERONLINE | Motor und fertiger Treiber gemeinsam geliefert | Netzteil, Arduino-Schnittstelle, passende Kabel und gegebenenfalls Netzanschluss bleiben zusätzliche Aufgaben | Ein Kit allein löst den vollständigen Aufbau nicht |

Quellen: [Tic #3140](https://www.pololu.com/product/3140), [Tic-Handbuch](https://www.pololu.com/docs/0J71/all), [G201X Produkt](https://www.geckodrive.com/product/g201x-digital-step-drive/), [G201X-Handbuch](https://www.geckodrive.com/wp-content/uploads/2023/04/G201X-and-G210X-Manual-011717.pdf), [Beispiel Motor-Treiber-Kit 1-DM860I-34HS39](https://www.omc-stepperonline.com/1-axis-stepper-cnc-kit-8-0nm-1132-89oz-in-nema-34-stepper-motor-driver-1-dm860i-34hs39). Das Beispiel-Kit enthält andere Modelle als die bisherige Referenz; es ist keine festgelegte Bestellung.

## Anschlusskonzept der preisorientierten Variante

Die folgenden Namen beschreiben die Vorauswahl und ersetzen noch nicht die verbindliche Pinliste in `elektronik.md`. Dort gilt weiterhin ausschließlich der als überholt gekennzeichnete Rev.-A-Plan.

| Funktion | Vorgesehene Verbindung |
|---|---|
| Schritte | Uno D2 → Signaleingang des ersten DFR0457 → dessen VOUT → DM860T PUL+ |
| Richtung | Uno D3 → Signaleingang des zweiten DFR0457 → dessen VOUT → DM860T DIR+ |
| Modulversorgung | Uno 5V → VIN beider Module; Modul-GND und Signal-GND → Uno GND |
| Treibersignal-Rückleiter | DM860T PUL− und DIR− → Uno GND |
| PIR | B1 OUT → bestehendes RJ45-Patchkabel und zwei fertige RJ45-Klemmenadapter → Uno D7; 5V/GND über das zweite Paar |
| Motor | Vier Motorleitungen → DM860T A+/A−/B+/B− nach Motordatenblatt |
| Motornetzteil | Geschlossenes 48-V-Netzteil → noch auszuwählendes DC-Anschlusskabel → DM860T AC/AC, nur für V3.0 |
| Netzanschluss | CH-Mehrfachsteckdose S0 → fertiges Typ-12/C13-Netzkabel → geschlossenes Motornetzteil; zweiter Steckplatz → USB-Netzteil → Uno |

Der [DFRobot-Schaltplan](https://dfimg.dfrobot.com/wiki/17549/DFR0457_mosfet-power-control-module_schematics_V1.0.pdf) zeigt, dass das Modul die positive Versorgung auf VOUT schaltet. Deshalb werden **PUL+/DIR+ geschaltet und PUL−/DIR− an GND gelegt**. In Rev. A war es andersherum. Keine Brücke von 48 V an diese Module oder an den Arduino; der DM860T-Signalwahlschalter muss auf 5 V stehen. Seine ENA-Anschlüsse können laut Handbuch frei bleiben. [DM860T V3.0 Handbuch](https://www.omc-stepperonline.com/download/DM860T_V3.0.pdf).

Die Gravity-Kabel sind enthalten. Je nach Kabelende wird der vorhandene Header-Kabelbestand zum Uno benötigt. Beschriftung und Pinfolge am gelieferten Modul prüfen; nicht allein nach einer Kabelfarbe verbinden. Ein einfaches Uno-Klemmen-Shield wäre nur eine passive Anschlusshilfe, kein zusätzlicher Motortreiber.

### Langsame Bewegung und Firmware

Bei weiterhin 200 Vollschritten, 8 Mikroschritten und 2:1-Untersetzung sind es 3200 Pulse pro Hauptachsenumdrehung. Bei einem Radius von 1 m und 0,1 m/s Wagenbewegung ergeben sich rund **51 Pulse/s**. Das liegt deutlich unter 1 kHz. Diese Geschwindigkeit ist ein Rechenbeispiel, kein festgelegtes Fahrprofil.

Mit DFR0457 sind breitere Pulse und mehr DIR-Vorlauf als in Rev. A erforderlich: als konservative Auslegungswerte zunächst mindestens **500 µs HIGH und LOW**, **1 ms DIR-Vorlauf** und höchstens **500 Pulse/s**. Das ist ein Vorschlag mit Reserve gegenüber den veröffentlichten Schaltzeiten von 20/50 µs; tatsächliche Pulse am Treiber messen. Die Firmware wird weiterhin mit Beschleunigung und ohne blockierende Abläufe entwickelt.

Der PIR wäre in dieser Variante direkt am Uno angeschlossen. Der HCT-Chip und sämtliche Bauteile seiner Zusatzplatine entfielen. Dazu gehört auch das bisherige RC-Filter. Ein Betrieb mit dem 3-m-Kabel bei laufendem Motor muss deshalb geprüft werden; eine softwareseitige Mindest-HIGH-Zeit ersetzt keinen elektrischen Störschutz. Ein definierter LOW-Zustand bei abgezogenem Sensor ist in diesem Konzept noch nicht gelöst und muss vor dem endgültigen Aufbau berücksichtigt werden.

## Geschlossenes Motornetzteil

**Mean Well GST220A48-R7B** ist ein konkreter Kandidat: 48 V, 4,6 A, 221 W, geschlossenes Kunststoffgehäuse, IEC-C14-Netzeingang und vierpoliger Power-DIN-Ausgang. Damit ist am Netzteil keine offene 230-V-Verdrahtung nötig. Ein fertiges Schweizer Typ-12/C13-Kabel verbindet es mit S0. [Herstellerdatenblatt](https://www.meanwell.com/Upload/PDF/GST220A/GST220A-SPEC.PDF).

Der 6-A-Phasenstrom des Motors ist nicht gleich dem Strom am 48-V-Netzteilausgang. Trotzdem ist die geringere Leistung gegenüber dem bisherigen 350-W-Netzteil noch kein abgeschlossener Belastungsnachweis. Strombedarf, Beschleunigung, Rückspeisung beim Abbremsen und Temperatur sind für das endgültige Fahrprofil zu berücksichtigen.

**Noch fehlendes Anschlussstück:** fertig konfektionierte passende Power-DIN-Buchse auf Anschlussleitungen/Klemmen, mit ausreichender Spannungs- und Strombelastbarkeit. Ein gewöhnliches vierpoliges Mini-DIN-Kabel ist kein nachgewiesener Ersatz. Eine lose Buchse mit Lötanschlüssen erfüllt die Aufbauvorgabe nicht. Noch kein geeigneter Einzelartikel für diese Verbindung bestätigt; kein ungesicherter Kauflink und kein stillschweigend verlangtes Abschneiden des Netzteilsteckers.

Wichtig für den späteren Gesamtplan: Bei diesem Netzteil ist DC− laut Hersteller mit dem Schutzleiter verbunden. Die bisherige Aussage „M48− und PE getrennt“ gilt somit nicht für diesen Kandidaten. Die Arduino-Signalmasse wird weiterhin nicht zusätzlich an DC− angeschlossen. Schutzleiterführung und Gehäuse müssen beim endgültigen Netzteil-/Gehäuseentwurf neu berücksichtigt werden.

## Recherchierte Preise und Bezugsquellen

Preisstand Recherche 03.10.2026; kein verbindlicher Warenkorb und keine Lieferzusage. Einzelpreise sind ausdrücklich keine Gesamtkosten der Anlage.

| Teil / benötigte Menge | Konkreter Artikel | Recherchierter Preis | Umfang / offene Kosten |
|---|---|---:|---|
| 2 × DFR0457 | [Bastelgarage 421644](https://www.bastelgarage.ch/module-de-driver-mosfet-gravity-10a) | CHF 6.90 pro Stück, zusammen CHF 13.80 | Jeweils ein Modul und Signalkabel; Seite auf Französisch; Versand zusätzlich |
| 2 × DFR0457, alternative Bezugsquelle | [DigiKey DFR0457 / 1738-1297](https://www.digikey.ch/de/products/detail/dfrobot/DFR0457/7087194) | CHF 3.13 ohne / rund CHF 3.38 mit ausgewiesener MwSt. pro Stück | Standardpackung ein Stück; Versandbedingungen im Warenkorb |
| 1 × GST220A48-R7B | [Simpex GST220A48-R7B](https://www.simpex.ch/shop/stromversorgungen/netzteile-ac-dc/tischnetzteile/gst220a48-r7b/) | CHF 57.00 ohne MwSt. | Seite: lieferbar auf Bestellung; 12 Stück ist die Werkverpackung, Einzelbestellmenge vor Kauf bestätigen; Netzkabel/Adapter zusätzlich |
| 1 × GST220A48-R7B, Alternative | [DigiKey 1866-2086-ND](https://www.digikey.ch/de/products/detail/mean-well-usa-inc/GST220A48-R7B/7703644) | CHF 54.14 ohne / rund CHF 58.53 mit ausgewiesener MwSt. | Einzelstück; Netzleitung/DC-Adapter nicht enthalten; Lieferung prüfen |
| 1 × GST220A48-R7B, weitere Alternative | [Distrelec 300-42-762](https://www.distrelec.ch/en/power-supply-gst220a-series-48v-6a-221w-iec-60320-c14-din-pin-mean-well-gst220a48-r7b/p/30042762) | Kein bestätigter CHF-Preis | Modell und technische Daten recherchiert; Preis und Termin offen |
| 1 × Tic 36v4 #3140 | [Pololu #3140](https://www.pololu.com/product/3140) | USD 64.95 | Anschlüsse montiert; keine bestätigten Schweizer Gesamtkosten |
| 1 × G201X | [Geckodrive G201X](https://www.geckodrive.com/product/g201x-digital-step-drive/) | USD 117.00 | Kühlkörper zusätzlich; Schweizer Versand/Einfuhr nicht bestätigt |

Als Vergleich: zwei DFR0457 und der Netzteilkandidat kosten bei den recherchierten DigiKey-Einzelpreisen zusammen etwa **CHF 65.30 inklusive ausgewiesener MwSt.**, vor eventuellem Versand. Das enthält **keinen Motor, DM860T, Netzkabel, DC-Adapter, USB-Versorgung, RJ45-Adapter oder Gehäuse**. Ein belastbarer Gesamtkostenvergleich für die Schweiz setzt diese Positionen und die Versand-/Einfuhrkosten sämtlicher Lieferanten voraus. Ein günstigster vollständiger Warenkorb wurde noch nicht nachgewiesen.

## Abschluss der Auswahl

Für eine vollständige Rev. B noch das DC-Anschlussstück bestimmen, Leistungsreserve bestätigen sowie PIR-Eingang bei Kabeltrennung und Signalpegel der fertigen Schnittstelle klären. Anschließend Schaltplan, verbindliche Verbindungstabelle, CSV-Stückliste, Bestellliste, Firmware-Vertrag und Inbetriebnahme gemeinsam ersetzen. Die alten Einzelteile werden dann aus der aktuellen Beschaffung entfernt, nicht als vermeintlich vorhandener Bestand umgebucht.
