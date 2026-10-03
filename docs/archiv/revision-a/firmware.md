# Firmware-Anforderungen

**Neue Vorgabe vom 03.10.2026: Aufbau mit fertig bestückten Modulen, ohne selbst gelötete Zusatzplatine. Der folgende Rev.-A-Entwurf ist ein historischer Zwischenstand und noch keine Bestell- oder Aufbauempfehlung für die neue Ausführung. Controller, Versorgung und Anschlussplan werden gemeinsam neu ausgewählt.**

Stand: 26.09.2026. **Spezifikation, noch keine implementierte oder getestete Firmware.** Zielplattform: Arduino Uno R3 / ATmega328P; vorgesehene Bibliothek: AccelStepper.

## Pinvertrag

| Uno-Pin | Funktion | Verhalten |
|---|---|---|
| D2 | STEP über R1/Q1 | LOW = Optokoppler aus, HIGH = aktiv; Ruhezustand LOW |
| D3 | DIR über R2/Q2 | Richtung durch realen Drehtest zuordnen |
| D4 | unbenutzt | Nicht anschließen; J0.5 bleibt frei |
| D7 | PIR über U2 | `INPUT`; HIGH = Bewegung; kein Pull-up nötig |
| D13 | eingebaute LED | Bereitschaft/Status; keine externe LED erforderlich |
| D8 | reserviert | ENA wird in Rev. A nicht angeschlossen |

## Zustände

Die mechanische Startposition vor dem Einschalten bei ausgeschalteter Motorversorgung einrichten. Beim Start wird die aktuelle Position als relativer Nullpunkt angenommen; eine automatische Positionsprüfung gibt es nicht.

1. **START/ANLAUF:** D2/D3 zuerst LOW initialisieren; keine Pulse. Sensor nach jedem Einschalten oder Reset 60 s stabilisieren lassen. Währenddessen erkannte PIR-Ereignisse verwerfen.
2. **WARTEN AUF LOW:** Erst nach der Anlaufzeit mindestens 500 ms durchgehend PIR-LOW erkennen. Ein bereits anliegendes HIGH löst keine Fahrt aus.
3. **BEREIT:** Eine neue steigende Flanke, mindestens 50 ms bestätigt, startet die Sequenz. Keine manuelle Freigabe erforderlich.
4. **VORFAHRT:** relativer Zielweg mit Geschwindigkeits- und Beschleunigungsbegrenzung.
5. **PAUSE:** zeitgesteuert mit `millis()`, ohne blockierendes Warten.
6. **RÜCKFAHRT:** zum gespeicherten Startwert; Beschleunigung und Bremsung.
7. **COOLDOWN:** mindestens 5 s, danach wieder WARTEN AUF LOW. PIR-Ereignisse während der Sequenz nicht aufstauen.

`motor.run()` muss im Hauptloop häufig aufgerufen werden. Zustandswechsel und Sensor werden auch während der Fahrt ausgewertet. Ausschalten erfolgt über S0; ein kontrollierter Softwarestopp per Schalter ist nicht vorgesehen. S0 ist kein Not-Halt.

Nach Reset oder Stromwiederkehr wird eine unterbrochene Fahrt verworfen. Die Steuerung wird nach dem beschriebenen Startablauf automatisch wieder bereit und kann auf eine neue Bewegung reagieren. Sie erkennt eine verschobene mechanische Ausgangsposition nicht.

## Parameter

| Parameter | Erster Versuch ohne Arm | Späterer Planwert |
|---|---:|---:|
| Pulse je Hauptachsenumdrehung | 3200 | 3200 |
| Maximalgeschwindigkeit | 50 Pulse/s | zunächst 100–300 Pulse/s, vor Ort prüfen |
| Beschleunigung | 20 Pulse/s² | zunächst 50 Pulse/s², vor Ort prüfen |
| Weg vor/zurück | 200 Pulse = 22,5° Hauptachse | konfigurierbar, bis 3200 Pulse nur bei freiem Vollkreis |
| Pause | 1500 ms | 1500 ms |
| Cooldown | 5000 ms | 5000 ms |
| STEP-HIGH und STEP-LOW | jeweils mindestens 5 µs | identisch |
| DIR stabil vor erstem STEP | mindestens 10 µs | identisch |

`setMinPulseWidth(5)` sichert nur die Pulsbreite. Den DIR-Vorlauf separat implementieren bzw. am Ausgang messen; eine Bibliotheksvoreinstellung ist dafür kein Nachweis. Bei HIGH an D2 leitet Q1, dadurch steigt die Spannung PUL+ gegen PUL−: keine zusätzliche STEP-Invertierung für die Transistorstufe erforderlich.

Rechnung: `200 × 8 × (40/20) = 3200 Pulse/Umdrehung`.
`Weg_Pulse = Winkel_Grad × 3200 / 360` mit sinnvoller Rundung.

Bei 1 m Radius ergeben 400 Pulse/s etwa **0,79 m/s** am Wagen. Die im Handover genannten 8 s pro Runde sind nur die Fahrzeit bei konstantem Tempo. Mit 80 Pulse/s² dauert eine 3200-Pulse-Fahrt aus dem Stillstand bis zum Stillstand etwa **13 s** (5 s Beschleunigung, 3 s konstant, 5 s Bremsung). Deshalb 400 Pulse/s nicht ungeprüft als „langsam“ übernehmen.

## Ausfälle und spätere Tests

- Kein automatisches Homing gegen einen Anschlag. Ohne Sensor existiert nur eine relative Softwareposition.
- Nach Schrittverlust, Riemenschlupf oder Treiberabschaltung manuell neu ausrichten und Steuerung zurücksetzen.
- Tests der späteren Firmware: Start mit PIR HIGH und LOW; keine Pulse während 60 s Anlauf; mindestens 500 ms LOW erst nach Anlauf; neue Flanke mindestens 50 ms; dauerhaftes HIGH; Trigger während Fahrt/Cooldown; `millis()`-Überlauf; Reset während Fahrt verwirft die alte Sequenz; erneute automatische Bereitschaft; fehlender Sensor.
- Motor nur am Prüfstand ansteuern, bevor Arm/Wagen montiert werden. Die detaillierte Prüfreihenfolge steht in [Inbetriebnahme](inbetriebnahme.md).
