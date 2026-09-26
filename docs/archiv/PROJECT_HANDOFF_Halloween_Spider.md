# Halloween Spider Project – Projektübergabe

Stand: 26. September 2026

## 1. Projektziel

Für Halloween soll eine große Spinne auf einem fahrbaren Wagen bewegt werden.

Der Wagen:

- trägt die Spinne,
- wiegt zusammen mit der Spinne ungefähr **5 kg**,
- steht auf einem Brett mit **6 kugelgelagerten Rollen**,
- wird über ein ungefähr **1 Meter langes Kunststoffrohr** bewegt,
- soll sich eher **langsam und kontrolliert** bewegen.

Das Kunststoffrohr ist mit dem Antrieb verbunden und schiebt/zieht den Wagen auf einer Kreisbahn.

Wichtig: Die Spinne hängt **nicht** am Ende eines frei tragenden 1-m-Hebels. Das Gewicht wird vom Wagen und seinen Rollen getragen. Deshalb muss der Motor primär Rollwiderstand und Beschleunigung überwinden und nicht das Gewicht gegen die Schwerkraft halten.

---

# 2. Gewählte Antriebslösung

Wir haben uns bewusst für folgende Konstruktion entschieden:

**Arduino Uno R3 → Stepper-Treiber → NEMA-34-Schrittmotor → Zahnriemen-Untersetzung → separat gelagerte Hauptachse → 1-m-Kunststoffrohr → Spinnenwagen**

Die Zahnriemenlösung soll beibehalten werden.

## Übersetzung

Geplant:

- Motor-Riemenrad: **20 Zähne**
- Hauptachsen-Riemenrad: **40 Zähne**
- Zahnriementyp: **HTD-5M**
- Riemenbreite: **15 mm**
- Übersetzung: **2:1**

Das bedeutet:

- Motor dreht 2 Umdrehungen
- Hauptachse dreht 1 Umdrehung

Vorteile:

- ungefähr doppeltes Drehmoment an der Hauptachse,
- langsamere und kontrolliertere Bewegung,
- Motor wird mechanisch entlastet,
- Riemen kann Stöße etwas abfedern.

---

# 3. Motor

## Gewählte Größenordnung

Ein **NEMA 34 mit ungefähr 8–12 Nm Haltemoment** ist für dieses Projekt ausreichend.

Die zuletzt bevorzugte Variante war ungefähr:

- **NEMA 34**
- ca. **8,5 Nm Haltemoment**
- ca. **6 A**
- Motorwelle ca. **14 mm**
- Motorgehäuselänge ca. **118 mm**
- damit unter der gewünschten maximalen Bauhöhe von ca. 15 cm

Beispielmodell:

**StepperOnline 34HS46-6004S1**

Typische Daten:

- 8,5 Nm Haltemoment
- 6 A
- 14-mm-Welle
- ca. 118 mm Länge

Für den 5-kg-Wagen auf kugelgelagerten Rollen ist ein noch größerer NEMA 42 nicht notwendig.

---

# 4. Stepper-Treiber

Empfohlen wurde:

**DM860T**

Der Arduino steuert den Motor **nicht direkt**.

Der Arduino liefert lediglich:

- STEP / PUL
- DIR
- optional ENABLE

Der DM860T versorgt und schaltet die Motorwicklungen.

Typische Eigenschaften:

- geeignet für NEMA 34
- bis ungefähr 7,2 A Motorstrom
- STEP/DIR-Eingänge
- Betrieb mit deutlich höherer Motorspannung als der Arduino

---

# 5. Stromversorgung

Empfehlung:

**48-V-Netzteil mit ca. 350 W**

Beispiel:

**Mean Well LRS-350-48**

Typische Daten:

- Eingang: 230 V AC
- Ausgang: 48 V DC
- ca. 7,3 A
- ca. 350 W

Der Arduino wird separat über:

- USB
- oder ein eigenes 5-V-Netzteil

versorgt.

## Sicherheit

Das 48-V-Netzteil hat netzspannungsführende 230-V-Anschlüsse.

Daher:

- Netzteil in ein geschlossenes Gehäuse,
- Zugentlastung für 230-V-Leitung,
- Sicherung vorsehen,
- Schutzleiter korrekt anschließen,
- keine offenen 230-V-Klemmen im Halloween-Aufbau.

---

# 6. Mechanischer Aufbau

Der Motor soll **nicht direkt den 1-m-Arm tragen**.

Stattdessen wird eine separate Hauptachse verwendet.

Geplanter Aufbau:

```text
                     Spinnenwagen
                  ┌────────────────┐
                  │       🕷        │
                  │  6 Rollen      │
                  └───────┬────────┘
                          │
                 ca. 1 m Kunststoffrohr
                          │
                          │
                   Rohrbefestigung
                          │
                     Montageplatte
                          │
                       Klemmnabe
                          │
                    20-mm-Hauptachse
                          │
                  ┌───────┴───────┐
                  │    Lager      │
                  └───────┬───────┘
                          │
                  ┌───────┴───────┐
                  │    Lager      │
                  └───────┬───────┘
                          │
                    40T HTD-5M
                          ╲
                           ╲
                           HTD-5M
                             ╲
                              ╲
                           20T HTD-5M
                                │
                            NEMA 34
```

---

# 7. Hauptachse und Lager

Vorgeschlagen:

- **20-mm-Stahlwelle**
- Länge ca. **15–20 cm**
- zwei Lager
- z. B. **UCFL204 20-mm-Flanschlager**

Die beiden Lager sollten mit Abstand montiert werden, z. B.:

- ungefähr **8–12 cm Abstand**

Dadurch nimmt die Lagerung die radialen Kräfte des 1-m-Arms auf.

Der NEMA-34-Motor muss dadurch nicht als tragendes Lager dienen.

---

# 8. Befestigung des Kunststoffrohrs

Vorgeschlagene Lösung:

1. 20-mm-Hauptachse
2. Klemmnabe mit Flansch
3. kleine Montageplatte
4. zwei Rohrschellen / U-Bügel
5. Kunststoffrohr

Beispiel:

```text
Draufsicht

       Kunststoffrohr
══════════════════════════
       ∩          ∩
       │          │
┌────────────────────────┐
│     Montageplatte      │
└───────────┬────────────┘
        Klemmnabe
            │
        20-mm-Achse
```

Zwischen Rohrschellen und Kunststoffrohr empfiehlt sich Gummi.

Das verhindert:

- Verrutschen,
- Beschädigung,
- Zerquetschen des Kunststoffrohrs.

---

# 9. Zahnriemen und Riemenräder

Die erste Industrievariante von Mädler/DOLD war zu teuer.

Daher wurde entschieden, günstige Standard-Aluminiumteile zu verwenden.

## Zielkonfiguration

### Motorseite

- HTD-5M
- **20 Zähne**
- **14-mm-Bohrung**
- für **15-mm-Riemen**

### Hauptachse

- HTD-5M
- **40 Zähne**
- **20-mm-Bohrung**
- für **15-mm-Riemen**

### Zahnriemen

- HTD-5M
- **15 mm breit**
- ungefähr **450 mm Länge**

Zielpreis für:

- 20T-Riemenrad
- 40T-Riemenrad
- Zahnriemen

zusammen ungefähr:

**CHF 20–30**

Billige Aluminium-Riemenräder von eBay/AliExpress/etc. sind für dieses temporäre Halloween-Projekt ausreichend.

Die teuren Industrie-Riemenräder sind nicht nötig.

---

# 10. Riemenabstand

Bei ungefähr:

- 20T
- 40T
- 450-mm-Riemen

ergibt sich grob ein Achsabstand von etwa:

**150 mm**

Die Motorhalterung sollte trotzdem Langlöcher besitzen, damit der Motor zur Riemenspannung verschoben werden kann.

Ziel:

- ca. ±10 mm Spannweg

---

# 11. Motorhalterung

StepperOnline verkauft passende NEMA-34-Halterungen.

Genannt wurde:

**StepperOnline ST-M7**

Typ:

- NEMA-34-Motorhalter
- Winkelhalterung

Alternativ kann jede stabile NEMA-34-Montageplatte verwendet werden.

Wichtig ist:

- stabil genug für einen ca. 4-kg-Motor,
- Möglichkeit zur Riemenspannung,
- möglichst Langlöcher oder verschiebbare Befestigung.

---

# 12. Arduino

Vorhanden:

**Arduino Uno R3**

Das reicht für das komplette Projekt problemlos.

---

# 13. Verkabelung Arduino → DM860T

Grundidee:

```text
Arduino Uno                  DM860T

Pin 2  --------------------> PUL+ / STEP+
Pin 3  --------------------> DIR+

optional:
Pin 8  --------------------> ENA+

GND -----------------------> PUL-
GND -----------------------> DIR-
GND -----------------------> ENA-
```

Motorseite:

```text
DM860T
  A+  ───── Motor Phase A
  A-  ───── Motor Phase A
  B+  ───── Motor Phase B
  B-  ───── Motor Phase B
```

Versorgung:

```text
48-V-Netzteil +  ───── DM860T VDC+
48-V-Netzteil -  ───── DM860T VDC-
```

Arduino:

```text
USB oder separates 5-V-Netzteil
```

## Hinweis

Vor dem endgültigen Anschluss muss die konkrete Beschriftung des gekauften DM860T geprüft werden.

Je nach Treiberversion kann auch Common-Anode-/Common-Cathode-Verkabelung verwendet werden.

---

# 14. Bewegungsmelder

Für Halloween soll der Ablauf wahrscheinlich über einen Bewegungsmelder ausgelöst werden.

Eine einfache Variante ist ein PIR-Sensor.

Beispielanschluss:

```text
PIR        Arduino Uno

VCC ------ 5V
GND ------ GND
OUT ------ Pin 7
```

Wenn größere Entfernungen zwischen Sensor und Arduino benötigt werden, kann die Leitung über ein Netzwerkkabel geführt werden.

---

# 15. Arduino Library

Empfohlen:

**AccelStepper**

Installation in Arduino IDE:

```text
Tools / Sketch → Include Library → Manage Libraries
```

nach:

```text
AccelStepper
```

suchen und installieren.

AccelStepper ist sinnvoll, weil der 1-m-Arm und der 5-kg-Wagen nicht abrupt gestartet oder gestoppt werden sollten.

---

# 16. Basis-Arduino-Code

```cpp
#include <AccelStepper.h>

const int STEP_PIN = 2;
const int DIR_PIN  = 3;

AccelStepper motor(
    AccelStepper::DRIVER,
    STEP_PIN,
    DIR_PIN
);

void setup() {
    motor.setMaxSpeed(400);
    motor.setAcceleration(80);
}

void loop() {

    // eine volle Runde des Arms
    motor.moveTo(3200);
    motor.runToPosition();

    delay(2000);

    // wieder zurück
    motor.moveTo(0);
    motor.runToPosition();

    delay(2000);
}
```

---

# 17. Warum 3200 Schritte ungefähr 360° entsprechen

Annahme:

Motor:

- 200 Vollschritte pro Umdrehung

DM860T:

- Microstepping 8×

Damit:

```text
200 × 8 = 1600 Pulse pro Motorumdrehung
```

Durch die 2:1-Riemenuntersetzung:

```text
1600 × 2 = 3200 Pulse
```

Damit entsprechen ungefähr:

```text
3200 Pulse = 360° Hauptachse
```

Die tatsächliche Zahl hängt von der eingestellten Microstep-Konfiguration des DM860T ab.

---

# 18. Geschwindigkeit

Bei:

```cpp
motor.setMaxSpeed(400);
```

und 3200 Pulsen pro kompletter Hauptachsenumdrehung:

```text
3200 / 400 = 8 Sekunden
```

Eine volle 360°-Runde dauert also ohne Berücksichtigung der Beschleunigungs- und Bremsphase ungefähr:

**8 Sekunden**

Das passt gut zu einer eher langsamen Halloween-Bewegung.

---

# 19. Empfohlene Startwerte

Für die ersten Tests:

```cpp
motor.setMaxSpeed(300);
motor.setAcceleration(50);
```

Dann langsam steigern.

Beispielsweise:

```cpp
motor.setMaxSpeed(400);
motor.setAcceleration(80);
```

Wichtig:

Der Wagen sollte wegen des langen Arms nicht schlagartig gestartet werden.

---

# 20. Geplanter Halloween-Ablauf

Eine mögliche Sequenz:

```text
PIR erkennt Bewegung
        ↓
kurze Verzögerung
        ↓
Spinne beginnt langsam zu fahren
        ↓
beschleunigen
        ↓
z. B. 360° fahren
        ↓
abbremsen
        ↓
kurze Pause
        ↓
eventuell 180° oder 360° zurück
        ↓
Cooldown
        ↓
warten auf nächste Bewegung
```

Später kann eine komplexere Bewegung programmiert werden.

---

# 21. Beispielcode mit PIR

Noch nicht endgültig getestet, aber guter Startpunkt:

```cpp
#include <AccelStepper.h>

const int STEP_PIN = 2;
const int DIR_PIN  = 3;
const int PIR_PIN  = 7;

const long STEPS_PER_REVOLUTION = 3200;

AccelStepper motor(
    AccelStepper::DRIVER,
    STEP_PIN,
    DIR_PIN
);

void setup() {
    pinMode(PIR_PIN, INPUT);

    motor.setMaxSpeed(400);
    motor.setAcceleration(80);
}

void loop() {

    if (digitalRead(PIR_PIN) == HIGH) {

        // eine komplette Runde
        motor.move(STEPS_PER_REVOLUTION);
        motor.runToPosition();

        delay(1500);

        // wieder zurück
        motor.move(-STEPS_PER_REVOLUTION);
        motor.runToPosition();

        // Cooldown, damit PIR nicht sofort erneut auslöst
        delay(5000);
    }
}
```

---

# 22. Mechanische Sicherheitsaspekte

Da ein 1-m-Arm bewegt wird:

- Bewegung langsam starten,
- langsame Beschleunigung,
- keine abrupten Richtungswechsel,
- Hauptachse separat lagern,
- Motor nicht als Lager verwenden,
- Rohr sicher mit mindestens zwei Schellen befestigen,
- Riemen und Riemenräder abdecken, wenn Personen in der Nähe sind,
- keine Fingerzugänglichkeit am Riemenantrieb,
- feste mechanische End-/Freiraumprüfung durchführen,
- sicherstellen, dass niemand in den 1-m-Schwenkbereich laufen kann.

Ein Not-Aus/Hauptschalter wäre sinnvoll.

---

# 23. Grobe Kosten

Die zuletzt diskutierte Größenordnung:

## Motorseite

- NEMA 34 ca. 8,5 Nm: ungefähr **CHF 45–55**
- DM860T: ungefähr **CHF 30–40**
- 48-V-/350-W-Netzteil: ungefähr **CHF 20–30**
- NEMA-34-Halterung: ungefähr **CHF 5–15**

Zusammen:

**ca. CHF 100–140**, abhängig von Händler und Versand.

## Riemenantrieb Budget

- 20T HTD-5M / 14 mm: ca. CHF 7–10
- 40T HTD-5M / 20 mm: ca. CHF 7–12
- HTD-5M / 15-mm-Riemen: ca. CHF 5–10

Zusammen:

**ca. CHF 20–30**

## Zusätzlich

Noch benötigt:

- 20-mm-Stahlwelle
- 2× Lager
- Klemmnabe
- Rohrschellen
- Montageplatte
- Schrauben
- Gehäuse für Elektronik
- Kabel
- Hauptschalter/Sicherung
- Bewegungsmelder

---

# 24. Aktuell festgelegte Architektur

```text
                           230 V
                             │
                     ┌───────▼────────┐
                     │ 48-V-Netzteil  │
                     └───────┬────────┘
                             │
                             ▼
Arduino Uno ── STEP/DIR ──> DM860T
   ▲                         │
   │                         ▼
   │                     NEMA 34
   │                         │
PIR-Sensor                   │ 20T
                             O
                              ╲
                               ╲ HTD-5M 15 mm
                                ╲
                                 O 40T
                                 │
                           20-mm-Hauptachse
                                 │
                            2 × Lager
                                 │
                         Rohrbefestigung
                                 │
                       ca. 1 m Kunststoffrohr
                                 │
                              Wagen
                                 │
                         Spinne + Brett
                          ca. 5 kg total
```

---

# 25. Offene Punkte für die nächste Session

## Mechanik

Noch konkret auswählen:

- genaue 20-mm-Stahlwelle
- genaue Lager
- Klemmnabe
- Montageplatte
- Befestigung des Rohrarms
- konkretes günstiges 20T-Riemenrad
- konkretes günstiges 40T-Riemenrad
- konkreter HTD-5M-Riemen
- endgültiger Achsabstand
- Riemenspanner oder verschiebbare Motorhalterung

## Elektronik

Noch festlegen:

- genaue DM860T-Version
- DIP-Schalter für Motorstrom
- Microstepping-Einstellung
- Netzteilabsicherung
- Gehäuse
- Hauptschalter
- eventuell Not-Aus
- PIR-Typ
- eventuell LED/Sound/weitere Halloween-Effekte

## Software

Noch programmieren:

- PIR-Auslösung
- Cooldown
- Bewegungsmuster
- Beschleunigungskurve
- Drehrichtung
- Anzahl Umdrehungen
- optional zufällige Bewegungsabläufe
- eventuell Endschalter/Home-Sensor
- eventuell Hall-Sensor

Aktuell wurde entschieden, einen Hall-Sensor **zunächst wegzulassen**.

---

# 26. GitHub-Repo-Vorschlag

Für die Weiterentwicklung bietet sich folgendes Repository an:

```text
halloween-spider/
│
├── README.md
│
├── docs/
│   ├── hardware.md
│   ├── wiring.md
│   └── mechanical-design.md
│
├── firmware/
│   └── spider_controller/
│       └── spider_controller.ino
│
├── diagrams/
│   └── README.md
│
└── bom/
    └── parts.md
```

## README.md

Soll enthalten:

- Projektbeschreibung
- Foto/Skizze
- Aufbau
- Hardware
- Quick Start
- Sicherheit

## firmware/

Hier liegt die Arduino-Software.

## bom/

Bill of Materials mit:

- Artikel
- Händler
- Preis
- Link
- Status bestellt/nicht bestellt

---

# 27. Empfohlene nächste Schritte

1. NEMA-34-Motor endgültig auswählen.
2. DM860T und 48-V-Netzteil zusammen bestellen.
3. günstige 20T-/40T-HTD-5M-Riemenscheiben bestellen.
4. Zahnriemenlänge festlegen.
5. Hauptachse und Lager bestellen.
6. Mechanischen Grundrahmen bauen.
7. Motor zunächst ohne Wagen testen.
8. Arduino + DM860T testen.
9. Hauptachse mit sehr geringer Geschwindigkeit testen.
10. Rohr montieren.
11. Wagen ohne Spinne bewegen.
12. Spinne montieren.
13. PIR anschließen.
14. Halloween-Bewegungsablauf programmieren.

---

# 28. Wichtige Projektentscheidungen aus dem bisherigen Chat

- Arduino Uno R3 ist vorhanden.
- Der Wagen wiegt ungefähr 5 kg.
- Der Wagen besitzt 6 kugelgelagerte Rollen.
- Das Kunststoffrohr ist ungefähr 1 m lang.
- Die Bewegung soll eher langsam sein.
- Es soll ein Schrittmotor verwendet werden.
- NEMA 34 ist ausreichend.
- Zielbereich ca. 8–12 Nm.
- Motor soll möglichst unter 15 cm lang sein.
- Es wird **keine Direktkupplung** verwendet.
- Es wird ausdrücklich die **Zahnriemenlösung** verwendet.
- Übersetzung soll ungefähr **2:1** sein.
- HTD-5M und 15-mm-Riemenbreite wurden gewählt.
- teure Industrie-Riemenräder wurden verworfen.
- günstige Alu-Riemenräder sind ausreichend.
- der Motor treibt eine separat gelagerte Hauptachse an.
- Hauptachse ungefähr 20 mm.
- DM860T als Motortreiber.
- 48-V-Netzteil.
- AccelStepper für Arduino.
- langsame Beschleunigung und Abbremsung.
- PIR als Bewegungsmelder vorgesehen.
- Hall-Sensor zunächst nicht nötig.
- Projekt muss nicht industriell langlebig sein; es ist ein temporäres Halloween-Projekt.

---

# 29. Kontext für eine neue ChatGPT-/Codex-Session

Folgenden Prompt kann man in einer neuen Session verwenden:

> Ich baue ein Halloween-Projekt mit einer motorisierten Spinne. Bitte lies zuerst die Datei `PROJECT_HANDOFF.md` vollständig. Die dort dokumentierten Entscheidungen gelten als aktueller Stand. Ändere die grundlegende Architektur nicht ohne guten Grund. Hilf mir als Nächstes dabei, die noch fehlenden mechanischen Komponenten auszuwählen und ein Arduino-Uno-R3-Projekt für den DM860T/NEMA-34-Antrieb aufzubauen. Das Projekt soll anschließend in einem GitHub-Repository weiterentwickelt werden.

---

# 30. Ziel für das Code-Repository

Am Ende sollte das Repository mindestens enthalten:

- reproduzierbare Arduino-Firmware,
- dokumentierte Pinbelegung,
- dokumentierte DIP-Schalter-Einstellungen des DM860T,
- Stückliste,
- mechanische Skizzen,
- Sicherheitsinformationen,
- Parameter für Schritte/Umdrehung,
- konfigurierbare Geschwindigkeit,
- konfigurierbare Beschleunigung,
- PIR-Trigger,
- Cooldown,
- Bewegungssequenzen.

