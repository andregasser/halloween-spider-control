# Inbetriebnahme · Revision B

**Noch nicht durchgeführt.** Sollprüfungen, keine bestandenen Tests. Reale Modelle, Revisionen und Messwerte am Ende eintragen. [Anschlussplan](elektronik.md) und [Firmware-Vertrag](firmware.md) gemeinsam beachten.

## 1. Spannungsfrei

- Prüfen: DM860T tatsächlich V3.0, montierte Klemmen, S2 5 V und DIP-Stellungen gemäß Plan.
- Kein Shield: D2/D3 direkt zu den weißen E55-Buchsen, X3 ausschließlich Uno +5 V, X4 ausschließlich Signal-GND. Power-GND-Buchsen nicht mit VIN verwechseln. E24-Stecker passend; Leiter in X3/X4 im Klemmbereich und 11 mm abisoliert. W4-Schirm an X4.5; J1.4 an zweiter Power-GND-Buchse.
- Vor Anschluss blanker Litzen die Eignung der gelieferten Schraubklemmen an DM860T/FIT0849 prüfen; Leiter vollständig geklemmt und ohne herausstehende Einzeldrähte. Halt spannungsfrei durch leichtes Ziehen prüfen.
- Alle Verbindungen gegen Tabellen durchmessen, insbesondere X3 +5 V gegenüber X1 +48 V; X3 gegen X4 auf Kurzschluss prüfen. Keine zusätzliche Verbindung von X2 an Signal-GND.
- Motor: schwarz/grün bilden eine Wicklung, rot/blau die andere; Farben am tatsächlichen Motor bestätigen. Zwischen Wicklungen kein Durchgang.
- W3 ist 1:1 und höchstens 3 m; PIR-Pinfolge prüfen. STEMMA-Kabel korrekt eingesteckt, offene Enden isoliert. PUL−/DIR− ausschließlich an die jeweiligen Minus-Ausgänge, keine zusätzliche GND-Brücke.
- W5-Adern über die Kontaktlage am Mean-Well-Stecker identifizieren; GlobTek-Pinnummern nicht übernehmen. Beide Adern jeder Versorgungsschiene anschließen.
- Alle Geräte isoliert befestigt und Leitungen zugentlastet, Netzteile trocken und frei belüftet. Bei Bedarf vorhandenes Gehäuse-/Abdeckungsmaterial verwenden; ein neues Steuergehäuse ist nicht vorgesehen.

## 2. Nur Arduino und Signalmodule

PS1 noch nicht mit U3 verbinden. PS2/W2 einschalten. Eine spätere Prüffirmware muss D2/D3 zunächst LOW halten und Messwerte ausgeben; sie existiert noch nicht.

| Messung | Kriterium / Reaktion |
|---|---|
| U4/U5 STEMMA-V+ gegen GND | Nominal etwa 5 V aus Uno; Modulbereich 3–30 V. Keine 48 V und keine zusätzliche Modulversorgung. |
| PUL+ gegen PUL−, DIR+ gegen DIR−, bei angeschlossenem Treibersignaleingang | LOW **0–0,5 V**, HIGH **4,5–5 V** gemäß DM860T-V3.0-Handbuch. Außerhalb: keine Motorfreigabe. |
| A0 bei Sensor-LOW / Bewegung | Messwert stabil in den konfigurierten gültigen Bereichen; Werte mit Pull-up protokollieren. |
| OUT-Leitung am Sensor abziehen | Ungültiger Messwert, keine Fahrt; bei laufendem Prüfabschnitt Abbruch/Fehler. 5V-/GND-Trennung separat untersuchen, keine vollständige Fehlererkennung voraussetzen. |
| STEP/DIR mit vorhandenem Logikanalysator | HIGH/LOW mindestens 500 µs, DIR-Vorlauf mindestens 1 ms; keine Pulse während Warmup/Reset/Fehler. |

Ein Logikanalysator bestätigt Zeiten, nicht analoge Pegelqualität. Statische Pegel mit Multimeter messen; bei unklaren Flanken zusätzlich Oszilloskopmessung organisieren. Keine Signalmessgeräte an 48 V anschließen.

## 3. Motornetzteil separat

U3 noch abgetrennt. PS1 an W1/S0, W5 an PS1. An X1/X2 ungefähr **48 V, Toleranz ±2 %** und Polarität messen. Ausschalten, Entladung abwarten, Spannung kontrollieren, erst danach U3/M1 anschließen. Nicht am 230-V-Eingang messen oder das fertige Netzteil öffnen.

## 4. Motor ohne Rohr, Riemen und Wagen

Niedrige Stromstufe 2,40 A Peak / 1,70 A RMS. Mit Rampe 1600 Pulse fahren, volle Motorumdrehung und beide Richtungen prüfen. Mindestens 500-µs-Pulse und maximal 100 Pulse/s. Reset, PIR-Fehler und gemeinsames Aus-/Einschalten prüfen; alte Fahrt darf nicht fortgesetzt werden.

PIR mit endgültigem W3 testen, während Motor startet, stoppt und die Richtung wechselt. Fehltrigger oder ungültige ADC-Werte sind zu beheben, bevor der Wagen angeschlossen wird. Erst nach mindestens 30 Minuten Betrieb Motor-/Treibertemperatur und gegebenenfalls Temperatur unter der Abdeckung und Versorgung protokollieren. Herstellergrenzen einhalten; Strom nicht vorsorglich maximal einstellen.

**Netzteilreserve und Bremsen praktisch prüfen:** PS1 darf nicht in Überlast abschalten. Beim Bremsen darf die 48-V-Schiene nicht unzulässig ansteigen; Entwurfsziel höchstens **50 V**, W5 ist für **56 V** ausgelegt. Für kurze Überspannungsspitzen reicht ein gewöhnliches Multimeter nicht als Nachweis; bei Bedarf geeignete Messung organisieren. Wenn das Ziel nicht eingehalten wird, Rampen/Last anpassen und erforderliche fertige Schutzbaugruppe neu auswählen. Keine pauschale Rückspeisefestigkeit behaupten.

## 5. Mechanik und Betrieb

Separat gelagerte Achse, Motorhalterung und Riemen prüfen. Dann ohne Wagen 3200 Pulse als eine Hauptachsenumdrehung bestätigen. Abschließend kleinen Fahrwinkel mit Wagen und etwa 50 Pulse/s testen, langsam steigern. Bewegungsbereich frei und geschützt halten. Bei Blockade, Schrittverlust oder Treiberausfall gemeinsam abschalten und manuell neu referenzieren.

## Messprotokoll

| Prüfpunkte | Ergebnis |
|---|---|
| Datum, Prüfer, Geräte-/Treiberrevision | Offen |
| W5-Kontakte/Aderzuordnung, 48-V-Ruhe-/Bremswerte | Offen |
| U4/U5 V+, belastete PUL-/DIR-LOW/HIGH-Pegel | Offen |
| PIR-ADC LOW/HIGH/offenes OUT, endgültige Kabellänge | Offen |
| Pulsbreite, DIR-Vorlauf, Warmup-/Fehler-/Reset-Verhalten | Offen |
| Stromstufe, Geschwindigkeit, Rampen, Temperatur nach 30 min | Offen |
| Tatsächliche Befestigung/Zugentlastung, gegebenenfalls Abdeckung aus Bestand | Offen |
| Motorumdrehung/Hauptachse, Fahrwinkel und Lastversuch | Offen |
