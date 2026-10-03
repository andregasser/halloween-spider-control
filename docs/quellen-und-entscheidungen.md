# Quellen und Entscheidungen · Revision B

Stand **04.10.2026**. Aktuelle Entscheidung ist der Aufbau mit fertig bestückten Modulen ohne eigene Lötplatine. Frühere Entscheidungen und Recherche einschließlich des R7B-Barreladapters bleiben im [Archiv](archiv/revision-a/quellen-und-entscheidungen.md) erhalten. Sie gelten nicht parallel zu diesem Anschlussplan.

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
| [Hammond 1554](https://www.hammfg.com/electronics/small-case/plastic/1554) | Historischer Gehäuse-/Montageplattenvorschlag; Neubeschaffung entfällt auf Nutzerwunsch |
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
8. **Ursprünglicher Gehäusevorschlag:** Hammond 1554YAGY/1554YPL für trockenen, geschützten Standort. Die Neubeschaffung wurde später auf Nutzerwunsch gestrichen, siehe Entscheidung 11. Der tatsächliche Standort ist noch nicht bestätigt.
9. Schaltpläne zeigen nur Geräte, reale Pins, Kabel und Einstellungen. Innere Schaltungen fertiger Geräte werden nicht gezeichnet. Material-/Bestellliste bleibt auf Elektronik plus ausdrücklich ST-M7 beschränkt.

10. Nutzer bestätigt ausreichend vorhandene **230-V-Anschlusskabel** sowie normale **Cat5-/Cat6-Netzwerkkabel**. E29/W1 wird als Bestand geführt und aus den Bestellpositionen entfernt; E08/W3 bleibt vorhanden. Für W1 passende CH-/IEC-C13-Ausführung im Bestand auswählen, genaue Steckerform ist noch nicht bestätigt. Für PIR vorhandenes 1:1-Patchkabel bis 3 m verwenden. Keine elektrische Anschlussänderung.

11. Nutzer verzichtet auf die Neubeschaffung des **Steuergehäuses E37 und der zugehörigen Montageplatte E53**. Temporärer Betrieb etwa vier Stunden, danach Abbau; bei Bedarf ist eigenes Gehäusematerial vorhanden. Beide festen Kaufpositionen entfallen aus der CSV. Lüftungszubehör E38 ist nur noch bedingter Bedarf; E40 wird nach tatsächlicher Montage gewählt. Befestigung, Isolation, Zugentlastung und freie Belüftung bleiben Aufbauanforderungen. Keine elektrische Anschlussänderung.

12. **PIR-Sensorgehäuse E39 entfällt ebenfalls auf Nutzerwunsch.** Aus aktuellem Material-/Bestellbedarf entfernt. PIR und RJ45-Adapter bleiben vorgesehen; den Sensor fest ausrichten, Linse freihalten und Anschlussleitung zugentlasten. Keine elektrische Anschlussänderung.

## Entscheidung vom 04.10.2026: keine Hülsen oder Crimpzange

Auf Nutzerwunsch entfallen **Aderendhülsen E43 und Crimpzange T02** aus aktuellem Material- und Bestellbedarf. Keine Änderung an Geräten, Leitungen oder Pinbelegung. [WAGO 221](https://www.wago.com/us/lp-221) beschreibt den direkten Anschluss abisolierter Litzen; [Adafruit #5648](https://learn.adafruit.com/adafruit-mosfet-driver/plugging-into-the-terminal-block) zeigt das Einsetzen der Leitungen bei gedrückter Federklemme.

Für die tatsächlich gelieferten Schraubklemmen an DM860T und FIT0849 ist die Eignung für blanke Litzen noch nicht belegt. Das [DM860T-V3.0-Handbuch](https://www.omc-stepperonline.com/download/DM860T_V3.0.pdf) enthält keine eindeutige Leiter-/Hülsenspezifikation für die gelieferten Klemmstecker. Diese Anschlussprüfung bleibt deshalb in Elektronik und Inbetriebnahme festgehalten; die Streichung ist keine pauschale Freigabe für jede Schraubklemme.

## Schweizer Händler oder Amazon

**Aktuelle Nutzerentscheidung vom 03.10.2026:** Keine Bestellung bei DigiKey oder Farnell, auch keine Empfehlungen als Ausweichquelle. Schweizer Händler oder Amazon bevorzugen. Die Wochenfrist bleibt verbindliche Beschaffungsanforderung. Diese Entscheidung ersetzt die Händlerempfehlungen der früheren Recherche weiter unten; der elektrische Aufbau bleibt unverändert.

| Position | Aktueller Stand nach Händlerprüfung |
|---|---|
| E48, zwei Module #5648 | [Play-Zone ada-5648](https://www.play-zone.ch/de/adafruit-mosfet-driver-for-motors-solenoids-leds-etc-stemma-jst-ph-2mm.html) bleibt Schweizer Bezugsquelle; zuvor direkt ab eigenem Lager Steinhausen geprüft. E55 gehört separat dazu und ist noch nicht beschaffbar belegt. |
| E56, ein Shield DFR0265 | Neu [Bastelgarage 422020](https://www.bastelgarage.ch/gravity-io-expansion-shield-fur-arduino-v7-1): direkter HTML-Abruf am 03.10. zeigt „Lagernd“, CHF 11.90, ein fertig bestücktes V7.1-Shield. Mit zwei RJ45-Adaptern E09 bündeln. Kein Modell-/Pinwechsel. |
| E05, PS1 | Neu [Simpex GST220A48-R7B](https://www.simpex.ch/shop/stromversorgungen/netzteile-ac-dc/tischnetzteile/gst220a48-r7b/), Schweizer Händler in Wetzikon. Gelesene/indexierte Seite nennt „Lieferbar auf Bestellung“, keinen Lagerbestand; Direktabruf blockiert. Kandidat mit Terminrisiko, keine belegte Wochenlieferung. Ein Stück bestellen, nicht die angegebene 12er-Werksverpackung. |
| E05, weitere Prüfung | [Distrelec 300-42-762](https://www.distrelec.ch/en/power-supply-gst220a-series-48v-6a-221w-iec-60320-c14-din-pin-mean-well-gst220a48-r7b/p/30042762) bleibt möglicher Lieferant. Die jetzt gelesene [RS-CH-Seite 117-6158](https://ch.rs-online.com/web/p/steckernetzteile/1176158) zeigt vorübergehend ausverkauft und Nachschub erst ab 16.10.2026, damit außerhalb der Frist. |
| E05, Marktplatzprüfung | [Galaxus 57336550](https://www.galaxus.ch/en/s1/product/meanwell-mean-well-gst220a48-r7b-85-264-v-220-w-48-v-rohs-85-mm-210-mm-220-w-power-supply-pc-57336550) führt das Modell, aber Verkäufer ist GetGoods DE. Der Abruf enthält veraltete Juni-Lieferdaten. Kein belegter aktueller CH-Termin, kein eigenes Schweizer Lager behauptet; deshalb keine neue erste Quelle. |
| E55, zwei Kabel #3894 | Schweizer Händler und Amazon recherchiert, kein verifiziertes passendes Angebot gefunden. Direkte Play-Zone-Artikelsuche nach 3894 liefert keine Ergebnisse. [Adafruit-Produktreferenz](https://www.adafruit.com/product/3894) definiert den benötigten Stecker; ist kein bevorzugter Bestelllieferant. In CSV weiterhin zwei benötigte Kabel, Beschaffungsstatus offen. Keine Verwechslung mit #3893 oder vierpoligem STEMMA QT. |
| E49, W5 | Keine verifizierte Schweizer/Amazon-Bezugsquelle für GlobTek KPPX4124641M0KPJX4(R) gefunden. Kein Bestelllink. Die Spezifikation und die Herstellerunterlagen bleiben maßgeblich; kein lötenpflichtiger oder ungeprüfter Steckerersatz. |
| E03/E04/E47, Antrieb | Kein Angebot bei Schweizer Händler/Amazon mit genauem Modell, Treiberrevision V3.0 und belegtem CH-Termin gefunden. STEPPERONLINE-Links dienen als Hersteller-/Modellreferenzen. Beschaffungsstatus jetzt ausdrücklich offen; China-Versand ist keine Wochenfrist-Empfehlung. |
| E37/E53, Gehäuse | Auf Nutzerwunsch aus dem aktuellen Material-/Bestellbedarf entfernt. Aufbau etwa vier Stunden, danach Abbau. Bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwenden; keine konkrete Hammond-Ausführung als Bestand bestätigt. |
| E26/E35, Meterware | Nutzer bestätigt beide als vorhanden. Steuerkabel W4 und DC-Leistungslitze bleiben im Materialbedarf, entfallen aber als Bestellpositionen. Die bisherige Bürklin-Ausweichquelle wird nicht mehr benötigt; keine konkrete Herstellermarke des vorhandenen Materials bestätigt. |

**BerryBase richtig einordnen:** Das gelesene [CH-Impressum](https://www.berrybase.ch/footer-ch/informationen/impressum/) nennt BerryBase GmbH c/o Sertronics AG in Birmenstorf und eine CH-Steuernummer. Die gelesenen [CH-AGB](https://www.berrybase.ch/agb/) nennen dagegen einen deutschen Vertragspartner. Deshalb weder ausschließlich deutschen noch eindeutig schweizerischen Vertragspartner aus diesen widersprüchlichen Webangaben ableiten. E06/E07/E50 als CH-Shop mit ungeprüftem Versandlager führen; tatsächlichen Vertragspartner/Versandort im Checkout prüfen. Eine Schweizer Adresse allein bestätigt keinen Schweizer Lagerbestand.

Amazon wurde als gewünschte Bezugsquelle geprüft, aber ohne verifiziertes konkretes Angebot für die schwierigen Modellpositionen kein Produktlink aufgenommen. Ein Treffer oder deutsches Lieferdatum belegt keine Zustellung an eine Schweizer Adresse. Verkäufer, Variante, Packungsmenge und konkreten CH-Termin vor einer Empfehlung prüfen. Keine Bestellungen oder Lieferantenanfragen ausgelöst.

Die aktuelle Bestellliste enthält keine DigiKey-/Farnell-Bestelllinks. Die folgenden Recherchebelege bleiben als datierte Historie erhalten. Die vollständige Beschaffung binnen einer Woche ist weiterhin nicht belegt; technisch benötigte Teile werden wegen fehlender Bezugsquelle nicht aus der Materialliste entfernt.

## Beschaffung binnen einer Woche

**Historische Recherche vor der abschließenden Händlerwahl:** Die darin genannten DigiKey-/Farnell-Empfehlungen sind durch den Abschnitt [Schweizer Händler oder Amazon](#schweizer-händler-oder-amazon) ersetzt. Maßgeblich sind die aktuelle CSV und Bestellliste.

**Anforderung vom Nutzer am 03.10.2026: Erhalt in der Schweiz binnen 7 Kalendertagen nach Bestellung.** Bei Bestellung am 03.10.2026 ist der Zieltermin spätestens 10.10.2026. Die Bestellliste enthält jetzt eine Lieferbewertung je Position. „Lagerangebot“ bedeutet: Lagerware wurde auf einer Händlerseite angezeigt und die genannte normale Transportzeit passt grundsätzlich zur Frist. Es bedeutet keine bestätigte Bestellung oder garantierte Zustellung. Die konkrete Wochenlieferung aller Teile ist weiterhin **nicht belegt**.

Recherche am 03.10.2026. Direkte HTML-Abrufe und über die Webrecherche gelesene bzw. indexierte Händlerseiten sind unten unterschieden. Index-/Cachewerte können älter sein und voneinander abweichen; sie sind keine Reservierung. Vor Zahlung Bestand in der benötigten Menge und Zustelldatum für die tatsächliche CH-Adresse prüfen. Arbeitstage, Zuschnitt, Zahlungseingang, Wochenende und Einfuhr gehören zur gesamten Lieferzeit.

| Position | Bezugsquelle / Artikel | Gelesener Lieferbeleg und Entscheidung |
|---|---|---|
| E05 PS1 | [DigiKey GST220A48-R7B](https://www.digikey.ch/de/products/detail/mean-well-usa-inc/GST220A48-R7B/7703644), 1866-2086-ND | Gelesene CH-Seite zeigt Lagerbestand, trotz 17 Wochen Hersteller-Standardlieferzeit. Das ist ein kurzfristiges Lagerangebot; DigiKey bleibt erste Quelle. |
| E48 U4/U5 | [Play-Zone ada-5648](https://www.play-zone.ch/de/adafruit-mosfet-driver-for-motors-solenoids-leds-etc-stemma-jst-ph-2mm.html), 2 Stück | Direkter Abruf zeigt über 20 Stück ab eigenem Schweizer Lager, CHF 5.90 pro Stück. Neue erste Quelle mit Priority-/Abholmöglichkeit. [DigiKey #5648](https://www.digikey.ch/de/products/detail/adafruit-industries-llc/5648/17282414) bleibt preislich günstigere Alternative zum Bündeln; gelesene CH-Seite weist Lagerware aus. |
| E55 Kabel | [DigiKey #3894](https://www.digikey.ch/de/products/detail/adafruit-industries-llc/3894/9603620), 1528-3894-ND, 2 Stück | Gelesene CH-Seite zeigt Lagerbestand neben 18 Wochen Hersteller-Standardlieferzeit. Kein Grund, bei verfügbarem Bestand 18 Wochen einzuplanen. |
| E56 U6 | [DigiKey DFR0265](https://www.digikey.ch/de/products/detail/dfrobot/DFR0265/6588546), 1738-1124-ND | Neue erste Quelle zur Bündelung. [CH-Sprachseite im Rechercheindex](https://www.digikey.ch/it/products/detail/dfrobot/DFR0265/6588546) zeigt Lagerware; deutscher Direktabruf nicht lesbar. [Farnell Schweiz 2946070](https://ch.farnell.com/dfrobot/dfr0265/gravity-io-erweit-shield-arduino/dp/2946070) listet ebenfalls Bestand und Express 1–2 Arbeitstage. Dasselbe fertig bestückte Shield, kein Pinwechsel. |
| E49 W5 | [DigiKey GlobTek-Kabel, lesbare US-Seite](https://www.digikey.com/en/products/detail/globtek-inc/KPPX4124641M0KPJX4-R/12343635), 1939-KPPX4124641M0KPJX4(R)-ND | Gelesene US-Seite zeigt 39 Stück Lagerware neben 18 Wochen Hersteller-Standardlieferzeit. CH-Direktabruf nicht lesbar. Ein Lagerhinweis derselben Artikelnummer ist ein Indiz; CH-Verfügbarkeit/Termin bleibt offen. Kein unbewiesener Steckerersatz. |
| E09 J1/J2 | [Bastelgarage FIT0849, 423938](https://www.bastelgarage.ch/rj45-buchse-8p-adapter-mit-schraubklemme), 2 Stück | Direkter HTML-Abruf zeigt „Lagernd“. Das enthaltene allgemeine Benachrichtigungsformular ist kein Nachweis für fehlenden Bestand. [DigiKey FIT0849](https://www.digikey.ch/de/products/detail/dfrobot/FIT0849/15848077), 1738-FIT0849-ND, zeigt im Rechercheindex ebenfalls Bestand; Alternative für Sammelbestellung. |
| E06 PS2 | [BerryBase Goobay 44952](https://www.berrybase.ch/dual-usb-netzteil-ladeadapter-2-4a-2x-usb-flache-bauform-weiss) | Gelesene Produktseite: sofort verfügbar, 2–5 Tage. Bleibt; tatsächliches CH-Datum prüfen. |
| E07 W2 | [BerryBase USB-2.0-A/B-Kabel](https://www.berrybase.ch/usb-2.0-hi-speed-kabel-a-stecker-b-stecker-schwarz), Variante 1,80 m | Direkter Abruf listet 1,80 m als lagernd, 2–5 Tage. Eine 1-m-Variante wird hier nicht angeboten; Bestellhinweis korrigiert. Funktion unverändert. |
| E50 X1/X2 | [BerryBase W221-413-1](https://www.berrybase.ch/wago-221-413-verbindungsklemme-3-fach), 2 Einzelstücke | Direkter Abruf: Einzelstück-Variante lagernd, 2–5 Tage. Keine 50er-Packung für zwei benötigte Klemmen. |
| E26 W4 | [Bürklin 94F4080](https://www.buerklin.com/de/p/rautronic/datenkabel/2-liycy-tp-2x2x0-25-gr/94F4080/), Rautronic P9021025, 1 m | Gelesene Produktseite: 141 m sofort verfügbar und Preisstaffel ab 1 m. Ersetzt Conrad als Bezugsquelle; zwei geschirmte verdrillte Paare à 0,25 mm² entsprechen dem vorhandenen Anschlussplan. Kein 100-m-Ring erforderlich. |
| E35 DC-Litze | [Bürklin 93F2750](https://www.buerklin.com/de/p/helu/isolierte-litzen/23601/93F2750/), HELU 23601, 1 m | Rechercheindex: 73 m sofort verfügbar, Preisstaffel ab 1 m, Silikon/Kupfer 1,5 mm², 300/500 V; Direktabruf blockiert. Ersetzt die Troller-Quelle, deren HTML widersprüchliche Bestands-/Bestellhinweise enthält. Mit E26 bündeln; elektrische Ausführung bleibt gleich. |

Die [DigiKey-Schweiz-Versandinformation](https://www.digikey.ch/de/help-support/delivery-information/delivery-time-and-cost) nennt normalerweise etwa 48 Stunden Transport aus dem US-Distributionszentrum. Marktplatzprodukte haben abweichende Bedingungen. Bei Lagerware ist die Hersteller-Standardlieferzeit **keine Wartezeit vor dem Versand**; bei fehlendem Händlerbestand wird sie dagegen relevant. [Bastelgarage](https://www.bastelgarage.ch/lieferung-versandkosten) nennt Priority am nächsten Werktag nach Versand und werktags meist Versand am Zahlungstag bis 15 Uhr. [Play-Zone](https://www.play-zone.ch/de/lieferung/) bietet Versand aus Steinhausen mit Priority oder Abholung nach Reservation. [Bürklin](https://www.buerklin.com/de/support/versand/) nennt 1–2 Tage Schweiz-Transport. Diese Angaben sind keine individuelle Zustellgarantie.

### Antrieb: Wochenfrist noch nicht belegt

E03 **34HS46-6004S1**, E04 **DM860T V3.0** und E47 **ST-M7** bleiben technisch ausgewählt. Ihre allgemeinen Produktseiten nennen „Auf Lager: 200“, verlangen für den jeweiligen Lagerbestand aber eine Länderauswahl. Daraus lässt sich kein deutscher Lagerbestand für diese drei Teile ableiten.

Die [STEPPERONLINE-Versandseite](https://www.omc-stepperonline.com/shipping-policy) meldet Versandpause im China-Lager vom 1. bis 5. Oktober 2026, Wiederaufnahme am 6. Oktober; DHL/FedEx-Express aus China wird mit 3–6 Arbeitstagen angegeben. Das ist für den 10. Oktober keine belastbare Planung. Deutschland arbeitet laut Hinweis weiter. Allerdings fehlt die Schweiz in der [Liste der zulässigen Ziele des deutschen Lagers](https://www.omc-stepperonline.com/why-there-is-no-shipping-options), während die Versandseite Deutschland→Schweiz erwähnt. **Deutschen Lagerbestand, tatsächliche CH-Versandmöglichkeit und Zustelldatum deshalb ausdrücklich bestätigen, keine Zusage daraus ableiten.** Beim DM860T warnt die [Produktseite](https://www.omc-stepperonline.com/digital-stepper-driver-2-4-7-2a-18-80vac-or-24-110vdc-for-nema-34-motor-dm860t) zudem vor zufälliger Lieferung alter/neuer Revisionen aus China.

Andere recherchierte Angebote erfüllen die Frist ebenfalls nicht nachweislich: [CNClab 34HS46-6004S1](https://cnclab.cz/produkt/nema-34-krokovy-motor-6a-8-5nm/) nennt Lieferantenbestand mit 3–5 Arbeitstagen ohne belegten CH-Zustelltermin; [V-slot](https://vslot-poland.com/SteppermotorNEMA34-1%2C8-8%2C5Nm-1204OZ) ist ausverkauft. Das gefundene [eBay-DM860T-Angebot aus Bremen](https://www.ebay.de/itm/204396616911) ist beendet. Keines wird als bestellbare Wochenfrist-Alternative aufgenommen. Ein anderes Motor-/Treiberfabrikat würde eine erneute Prüfung von Welle, Wicklungen, Signalen und Einstellungen benötigen; es ist hier nicht ungeprüft ersetzt.

### Weitere geprüfte Quellen und offene Zubehörteile

[Simpex PS1](https://www.simpex.ch/shop/stromversorgungen/netzteile-ac-dc/tischnetzteile/gst220a48-r7b/) ließ sich aktuell nicht direkt auslesen. [Distrelec 300-42-762](https://www.distrelec.ch/en/power-supply-gst220a-series-48v-6a-221w-iec-60320-c14-din-pin-mean-well-gst220a48-r7b/p/30042762) war ebenfalls nicht lesbar; [RS Schweiz 117-6158](https://ch.rs-online.com/web/p/steckernetzteile/1176158) liefert eine ältere Lageranzeige ohne konkretes Datum. Die [deutsche RS-Seite](https://de.rs-online.com/web/p/steckernetzteile/1176158) nennt hingegen Nachschub erst am 16.10.2026. Diese regional unterschiedlichen Angaben begründen keine kurzfristige CH-Zusage; deshalb entfällt „alternativ Distrelec“ als bevorzugte Lieferantenangabe bei E05.

E37/E53 sind weiterhin Gehäuse-/Plattenvorschläge nach Aufmaß. Andere DigiKey-Länderseiten zeigen Lagerhinweise, aber keinen bestätigten CH-Termin. E38/E39/E40/E43/E54 und bedingter Bedarf E45/E46/T02 bleiben ohne bestätigte Ausführung; eine vollständige Wochenbeschaffung einschließlich Zubehör ist damit offen. Vorhandene Kabel und Werkzeuge bleiben Bestand. Bestellhinweise und Lieferbewertungen werden aus der CSV erzeugt; es wurde keine Bestellung ausgelöst.

## Noch ausstehende Nachweise

- Reale Treiberrevision, PIR-Pinfolge, belastete Modulpegel und Versorgungsspannung.
- Finaler Standort, Befestigung und Zugentlastung; gegebenenfalls Abdeckung aus Bestand und passende Lüftung/Durchführungen.
- Netzteil-Leistungsreserve und Spannung beim Bremsen an tatsächlicher Last.
- Firmware, Sensor-Störfestigkeit am 3-m-Kabel, Temperatur- und Bewegungstests.
- Schweizer Warenkorbpreise und tatsächliche Liefertermine.

Dokumentprüfungen sind keine Hardware-, Sicherheits- oder Verfügbarkeitsprüfung. Modellangaben stammen aus Herstellerunterlagen; tatsächliche Lieferung vor Aufbau vergleichen. Referenzen in alten Mechanikdokumenten sind Projektkontext und begründen keine zusätzliche Mechanikbestellung.
