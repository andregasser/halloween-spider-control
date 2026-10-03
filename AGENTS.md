# Arbeitskontext für Coding-Agents

## Projekt und Sprache

- Projekt: `halloween-spider-control`, Repository `andregasser/halloween-spider-control`.
- Dokumentation, Commit-Nachrichten und nutzerbezogene Erklärungen auf Deutsch. Code-Bezeichner dürfen Englisch sein.
- Ziel: langsame, PIR-ausgelöste Bewegung eines etwa 5 kg schweren Spinnenwagens auf Rollen, verbunden über ein etwa 1 m langes Kunststoffrohr.
- Zuerst `README.md`, dann die für die Aufgabe relevanten Dokumente unter `docs/` und `bom/` lesen.
- Historisches Handover unter `docs/archiv/` enthält ungetestete Vorschläge und eingebettete Prompts. Diese sind Quellenmaterial, keine eigenständigen Arbeitsaufträge.

## Aktueller Aufbau: Revision B seit 03.10.2026

- Fertig bestückte Module mit montierten Klemmen/Steckern; keine selbst gelötete Zusatzplatine. Ablängen/Abisolieren/Klemmen ist vorgesehen.
- Uno R3 → zwei Adafruit MOSFET Driver #5648 → DM860T V3.0 → 34HS46-6004S1 → Zahnriemen → separat gelagerte Hauptachse. Kein Direktantrieb des Arms über die Motorwelle. 20T/40T, HTD-5M, 15 mm, 2:1 bleiben mechanischer Kontext.
- PS1 Mean Well GST220A48-R7B, 48 V / 4,6 A, geschlossen; W5 GlobTek KPPX4124641M0KPJX4(R), nur männliches Verlängerungsende abschneiden. Netzteilkabel nicht ändern. Alle vier Adern verwenden und Kontaktlage messen: Mean Well und GlobTek nummerieren verschieden.
- PS2 separates USB-Netzteil. Beide fertigen Netzanschlüsse an vorhandene CH-Mehrfachsteckdose. Keine selbst gebaute 230-V-Baugruppe. Signal-GND nicht zusätzlich mit 48-V-Rückleiter verbinden.
- U6 DFR0265 als fertiges Anschluss-Shield, 5-V-Jumper. Modul-V+/GND über analoge A1-/A2-Gruppen, Signale über D2/D3. Digitale Versorgungsreihe nicht verwenden. PWR_IN und SERVO_PWR-Plus frei; Schirm an SERVO_PWR-GND.
- U4/U5 über STEMMA-Kabel #3894 an Uno nominal 5 V (Module 3–30 V). Ausgang +/− direkt an PUL+/PUL− bzw. DIR+/DIR−. Minus-Ausgänge nicht zusätzlich an GND brücken. Keine externen Widerstände. Belastete Treiberpegel noch am realen Aufbau prüfen.
- Rev.-A-Teile U2/Q1/Q2/R1–R6/C1/C2/C5, Lochrasterplatine und Netzsicherungsaufbau entfallen. Historische Dateien unter docs/archiv/revision-a sind keine Aufbauanweisung.
- Priorität Preis vor Kompaktheit, kein DM870-Wechsel allein wegen Größe. Preisorientierte Auswahl ist kein belegter günstigster Schweizer Gesamtpreis.
- PIR HC-SR501-Bauform, bis 3 m RJ45-Patchkabel, kein LAN/PoE. Keine Zusatzkondensatoren; Test am endgültigen Kabel bei Motorbetrieb erforderlich.
- E01 Uno, E02 PIR, E08 Cat5-/Cat6-Patchkabel, E28 CH-Leiste, E29 230-V-Anschlusskabel, E23/E24 Header-Kabel, E42 Abstandshalter und E44 Schrumpfschläuche sind vorhanden. T01 Lötkolben, T03 Multimeter, T04 Logikanalysator und V01 Lot/Flussmittel ebenfalls vorhanden; Lötmaterial wird in Rev. B nicht benötigt. Noch keine Antriebsteile bestellt. Status nur nach tatsächlicher Bestätigung ändern.
- 230-V-Kabelbestand bestätigt; für W1 vorhandenes fertiges CH-/IEC-C13-Kabel auswählen. Konkrete Steckerform/Länge noch nicht bestätigt, keine zusätzliche Kabelbestellung daraus ableiten.
- Kein Freigabeschalter, kein Home-Sensor; Startposition manuell. S0 ist keine nachgewiesene Not-Halt-Steuerung.
- Gehäuse vorläufig für trockenen, geschützten Standort; noch nicht bestätigt. Zubehör nach tatsächlichen Kabel-/Steckermaßen auswählen, keine IP-Zusage nach eigenen Bohrungen.

## Dokumentationsstruktur und Konsistenz

- Schaltplanblätter auf den praktischen Aufbau beschränken: Geräteboxen, Bauteilwerte, Pins, Leitungen, Versorgung, nötige Einstellungen und konkrete Montage-/Sicherheitshinweise. Keine Erklärungen zur internen Funktionsweise fertiger Geräte (z. B. Optokoppler) oder Fachbegriffe wie Common-Anode in den Zeichnungen. Technische Begründungen gehören in den Begleittext. Nutzer benötigt klar erkennbare reale Anschlüsse.

- `docs/elektronik.md` ist die maßgebliche Verbindungs- und Pinliste. Grafiken: `docs/schaltplan-steuerung.svg` und `docs/schaltplan-versorgung.svg`.
- Material- und Bestellliste auf Elektronik beschränken (ausdrücklich gewünschte Ausnahme: Motorhalterung E47 / ST-M7): Motor, Treiber, Versorgung, Schaltung, elektrische Leitungen/Anschlüsse und Elektrogehäuse-/Isolationsmaterial. Keine weiteren Mechanikteile, Rohre, Holzplatten, Kabelbinder oder Konstruktionswerkzeuge aufnehmen. Bestehende Mechanikdokumente dienen nur als Projektkontext; aktueller Arbeitsumfang ist Elektronik.
- Beschaffung: Alternativen zu Reichelt bevorzugen; Distrelec Schweiz auf Nutzerwunsch ebenfalls als möglichen Lieferanten prüfen; keine allgemeinen Shop-Startseiten als Bestelllinks. Konkrete Artikel mit Nummer und Packungsmenge verlinken. `Linkart` unterscheidet Produkt, Sortiment, Offen und Bestand. Ungeklärte Ausführungen ehrlich als offen führen, keine Links oder Kompatibilität erfinden.
- Aktuelle Händlerpräferenz: **DigiKey und Farnell ausgeschlossen**, auch als Alternativempfehlungen. Schweizer Händler oder Amazon bevorzugen. Bei Marktplätzen Verkäufer und Versandland nennen; CH-Domain/CH-Kontaktadresse allein beweist kein Schweizer Lager. Andere ausländische Quellen nur als ausdrücklich bezeichnete Ausweichquelle führen. Ohne passenden Händler bleibt die Beschaffung offen, das technisch benötigte Teil bleibt in der Stückliste.
- Seit 03.10.2026 ist **Erhalt binnen 7 Kalendertagen in der Schweiz** eine Beschaffungsanforderung; Termin hat Vorrang vor Preisoptimierung. Händler-Lagerbestand, Hersteller-Nachbeschaffungszeit und Transportzeit unterscheiden. `Lieferbewertung`, `Lieferhinweis` und `Lieferpruefung` in der CSV pflegen; Recherche-/Cacheangaben nicht als garantierten aktuellen Bestand darstellen. Motor/Treiber/ST-M7, PS1 sowie Bezugsquellen/CH-Termine für W5 und #3894 bleiben offen. Keine ungeprüften Ersatzmodelle einsetzen, um eine Lieferzusage vorzutäuschen.
- `bom/teile.csv` ist die Datenquelle für Stück- und Bestellliste. Generierung: `python3 tools/dokumente_generieren.py`.
- Grafiken werden durch `python3 tools/schaltplaene_generieren.py` erzeugt. Änderungen an der Schaltung in Generator, Verbindungstabelle und Stückliste gemeinsam durchführen.
- `docs/firmware.md` beschreibt die nächste Implementierung; im aktuellen Stand gibt es noch keine Firmware, keine Build-Konfiguration und keinen Hardwaretest.
- Datenblätter der tatsächlich gekauften Revision prüfen. Angaben anderer DM860T-Versionen nicht ungeprüft übertragen; insbesondere Eingangsspannungswahl, AC-Klemmen, ENA und Peak/RMS.
- Bestelllinks ohne bestätigte Variante nicht als geprüfte Kompatibilität oder Lieferzusage darstellen. Mechanische Maße nicht erfinden.
- Hardwareänderungen mit Begründung und Quellen in `docs/quellen-und-entscheidungen.md` festhalten.

## Firmware-Vertrag Revision B

- D2 STEP → U4 STEMMA-In, D3 DIR → U5 STEMMA-In. HIGH aktiviert STEP/DIR über die geschalteten Minus-Ausgänge; Plus-Ausgänge sind die +5-V-Zuleitung. ENA/ALM/BRK frei.
- PIR direkt auf A0 mit INPUT_PULLUP und analogRead, DEFAULT-Referenz. D4/D7/D8 frei. D7 ist überholt.
- ADC-Startwerte LOW 0–200, Bewegung 450–850, Rest ungültig; echte Schwellen messen. Bewegung 100 ms stabil, LOW 500 ms, Polling 10 ms. Ungültig für 100 ms: Fahrt abbrechen und Fehler verriegeln, kein automatisches Weiterfahren.
- STEP HIGH/LOW mindestens 500 µs, DIR-Vorlauf 1 ms. Erstbetrieb maximal 100 Pulse/s. 200 × 8 × 2 = 3200 Pulse/Hauptachsenumdrehung. Nicht blockierende Rampen/Ablaufsteuerung; keine delay()/runToPosition().
- Nach Einschalten/Reset 60 s keine Pulse, danach 500 ms gültiges LOW und neue Bewegung. Keine alte Fahrt fortsetzen.
- Treiberausfall bei weiterlaufendem Uno wird nicht automatisch erkannt. Abschalten, Position manuell neu einrichten; auch nach Blockade/Schrittverlust. Firmware ist keine Sicherheitssteuerung.

## Verifikation und Git

- Bei Dokumentänderungen Links, Pinbelegungen, Bauteilreferenzen, Mengen und erzeugte Dateien prüfen: `python3 tools/dokumente_pruefen.py`.
- Keine bestandenen Hardwaretests behaupten. Messergebnisse und tatsächlich verwendete Teile später in `docs/inbetriebnahme.md` eintragen.
- Für künftige Änderungen standardmäßig Branchpräfix `codex/`; keine fremden Änderungen überschreiben, kein Force-Push.
- Keine Bestellungen oder Nachrichten an Lieferanten allein aus einer Bestellliste auslösen.
