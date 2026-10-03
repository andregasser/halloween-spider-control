# Firmware-Anforderungen · Revision B

Stand 04.10.2026. **Noch keine Firmware, Build-Konfiguration oder Hardwaretests.** Dieser Vertrag ist Grundlage der nächsten Implementierung. Maßgeblicher elektrischer Aufbau: [Elektronik](elektronik.md).

## Pins und Zeiten

| Uno-Pin | Funktion | Pegel |
|---|---|---|
| D2 | STEP → U4 STEMMA-In | HIGH aktiviert STEP über PUL− |
| D3 | DIR → U5 STEMMA-In | HIGH aktiviert DIR über DIR− |
| A0 | PIR über J1.1 | Analogauswertung mit internem Pull-up |
| D4 / D7 / D8 | Frei | Kein Rev.-A-PIR an D7 |
| A1 / A2 / A3 | Frei | Kein Anschluss-Shield; Versorgung über 5V/GND und X3/X4 |

D2/D3 zunächst LOW setzen, dann OUTPUT aktivieren. Kein Schritt beim Start. A0 `INPUT_PULLUP`, ADC-Referenz `DEFAULT` (Vcc). Pull-up beim Lesen nicht abschalten. Analogpins können diesen Modus nutzen; [Arduino-Dokumentation](https://github.com/arduino/docs-content/blob/main/content/learn/02.microcontrollers/02.analog-input/analog-input.md).

STEP-HIGH und STEP-LOW jeweils mindestens **500 µs**, DIR mindestens **1 ms** vor der nächsten STEP-Flanke setzen. Konservative Prüfwerte für diese Ausführung; Erstbetrieb bleibt bei **100 Pulse/s**. Beschleunigungs-/Bremsrampen in Software, keine blockierenden `delay()` oder `runToPosition()`. ADC, Fehlerüberwachung und Bewegung müssen gleichzeitig weiterlaufen. 1600 Pulse/Motorumdrehung, 3200 Pulse/Hauptachsenumdrehung.

## PIR-Auswertung

Alle 10 ms messen. Die folgenden 10-Bit-Bereiche sind **Startwerte zur Kalibrierung**, keine Messwerte des vorhandenen Sensors:

| ADC-Wert | Zustand |
|---|---|
| 0–200 | Gültiges LOW |
| 450–850 | Gültige Bewegung; mindestens 100 ms stabil |
| 201–449 und 851–1023 | Ungültig; nie als Bewegung interpretieren |

OUT nominal 3–3,3 V liegt bei nominal 5-V-ADC-Referenz ungefähr bei 614–675. Ein offenes OUT wird durch den Pull-up typischerweise nahe 1023 gezogen. Tatsächliche Bereiche am vorhandenen Sensor einschließlich Pull-up, 3-m-Kabel und Motorbetrieb messen. Stabilitätszeiten setzen neue gültige Messwerte voraus; ungültige Messungen zählen weder als LOW noch als Bewegung.

Ungültiger Zustand für mindestens 100 ms: laufende Sequenz abbrechen, STEP LOW setzen, Fehler verriegeln. Kein automatisches Weiterfahren. Nach Fehler Startposition prüfen und bewusst neu starten. Nach einem zulässigen Sensorausgangswechsel wird innerhalb der Stabilitätsprüfung nicht voreilig ein Fehler verriegelt. Die Auswertung erkennt nicht jede Unterbrechung von 5V/GND und ist keine Sicherheitssteuerung.

## Ablauf

1. `WARMUP`: Nach Einschalten/Reset **60 s ohne Motorpulse**.
2. `WAIT_LOW`: Mindestens **500 ms** durchgehend gültiges LOW abwarten.
3. `READY`: Neue stabile LOW→Bewegung-Flanke akzeptieren; bestehendes HIGH startet keine Fahrt.
4. `FORWARD`: Mit Beschleunigung begrenzte Pulszahl vorfahren.
5. `PAUSE`: Einstellbare Pause ohne neue Fahrt.
6. `RETURN`: Gleiche Pulszahl mit Rampen zurückfahren.
7. `COOLDOWN`: Weitere PIR-Flanken ignorieren, danach wieder `WAIT_LOW`.
8. `FAULT`: Pulse stoppen und Fehler verriegeln; kein automatischer Neustart einer alten Fahrt.

Ungeklärte Parameter vor Implementierung als Konfiguration definieren: Fahrwinkel, Pause, Cooldown, Beschleunigung und Richtung. Für den ersten Versuch ohne Mechanik **1600 Pulse** als eine Motorumdrehung; am späteren Riemenaufbau 3200 Pulse als eine Hauptachsenumdrehung. Erst dann kleinen sicheren Fahrwinkel festlegen.

Bei 1 m Radius und 3200 Pulsen/Hauptachsenumdrehung entsprechen 100 Pulse/s etwa **0,196 m/s**; ein erster Zielwert von 50 Pulse/s entspricht etwa **0,098 m/s**. Diese Werte gelten nach Erreichen der Geschwindigkeit; Rampen verlängern die Fahrt.

## Position und Ausfälle

Kein Home-Sensor. Startposition vor Einschalten bei ausgeschalteter Motorversorgung manuell setzen. Nach Reset alte Sequenz verwerfen, 60-s-Anlauf und neue PIR-Flanke verlangen. Ein Ausfall von PS1 bei weiterlaufendem Uno wird nicht automatisch erkannt: gemeinsam abschalten, Position neu einrichten und neu starten. Blockade oder Schrittverlust erzeugt ebenfalls unbekannte Position. ENA bleibt frei; der Treiber kann im Stillstand bestromen. Ein Softwarefehler oder S0 garantiert keine sofortige mechanische Stillsetzung.
