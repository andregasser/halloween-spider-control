# Inbetriebnahme und Prüfprotokoll

**Alle Kästchen sind offen. Es wurde bisher weder aufgebaut noch gemessen.**

## Vor Montage und Einschalten

- [ ] Tatsächliche Typen/Revisionen und Fotos von M1, U3 und PS1 dokumentiert.
- [ ] PIR-Anschlüsse anhand der eigenen Platinenbeschriftung identifiziert.
- [ ] U3-Eingangsbelegung und Stromtabelle stimmen mit dem referenzierten V3.0-Handbuch überein; S2 = 5 V.
- [ ] Zwei Motorwicklungen spannungslos per Durchgang/Widerstand identifiziert. Keine Motorader mit Motorgehäuse verbunden.
- [ ] Riemennaben, Passfedern und Wellenlänge passen tatsächlich; Schrauben gesichert.
- [ ] Riemenabdeckung und Abgrenzung des gesamten Schwenkbereichs vorhanden.

## Netzteilbaugruppe

Durch eine Elektrofachperson: Schutzleiterdurchgängigkeit, Isolation, Berührungsschutz, Zugentlastung, Sicherungsauswahl, Schaltvermögen von S0 und örtlicher RCD. PS1 auf 230-V-Eingang stellen. Montage der Netzbaugruppe abgeschlossen dokumentieren, bevor die Steuerung angeschlossen wird.

- [ ] PE an PS1, Gehäuse/Deckel/Metallplatte und vorgesehenen Metallteilen geprüft.
- [ ] PS1-Ausgang unbelastet gemessen: etwa 48 VDC, Polarität an F2 bestätigt.
- [ ] F1 und F2 samt Haltern stimmen mit Schaltplan überein; F2 ist ausdrücklich DC-geeignet.
- [ ] S0 trennt im Betriebsaufbau beide Netzteile; beim Programmieren bleibt PS1 aus.

## Steuerung zuerst ohne 48 V

- [ ] +5V/GND nicht kurzgeschlossen; M48− und PE nicht unbeabsichtigt mit GND gebrückt.
- [ ] RJ45-Pins 1→1, 2→2, 4→4, 5→5 geprüft, übrige Pins frei; kein Crossover-Kabel.
- [ ] 5-V-Versorgung am Uno und am PIR gemessen; U2 muss innerhalb 4,5–5,5 V liegen.
- [ ] U2.14 = +5V, U2.7 = GND; freie Eingänge auf GND.
- [ ] Nach 60 s stabiler PIR-Anlaufzeit reagiert PIR_RAW ungefähr mit 0/3,3 V.
- [ ] D7 zeigt gleiche Polarität, ungefähr 0/5 V; abgezogenes PIR-Kabel ergibt LOW.
- [ ] S1 AUS ergibt D4 HIGH, S1 EIN ergibt LOW.
- [ ] Reset erzeugt keine STEP-Pulse; R3/R4 halten Q1/Q2 aus.

## Treiber und Motor ohne Riemen/Arm

- [ ] Erst eine Firmware gemäß `firmware.md` entwickeln und Softwaretests durchführen. Die Beispiele im historischen Handover nicht als fertige Steuerung flashen.
- [ ] Motor festgeschraubt, Welle frei, U3 zunächst auf 2,40 A Peak, 8× Microstepping.
- [ ] STEP/DIR-Spannung **differenziell zwischen + und −** am Treiber geprüft. D2 HIGH muss PUL-Optokoppler aktivieren.
- [ ] Oszilloskop/Logikanalysator: mindestens 5 µs HIGH/LOW und mindestens 10 µs DIR-Vorlauf nachgewiesen. Messgerät-Masse nur auf GND der Steuerung, nicht auf beliebige Leistungsklemmen legen.
- [ ] Je 1600 Pulse ergeben eine Motorumdrehung; Richtung und Rückfahrt stimmen.
- [ ] S1 AUS bremst und sperrt; erneutes Freigeben startet nicht unerwartet.
- [ ] Nach Reset mit S1 EIN und/oder PIR HIGH erfolgt keine Fahrt.

## Mechanik schrittweise hinzufügen

1. Riemen/Hauptachse ohne Rohr: 3200 Pulse ergeben eine Hauptachsenumdrehung.
2. Rohr ohne Wagen: zunächst kleiner Winkel, niedrige Geschwindigkeit, Freiraum beobachten.
3. Wagen ohne Spinne: Boden, Rollwiderstand und Verbindung prüfen; erforderliche Zugkraft messen.
4. Vollständiger Wagen: Geschwindigkeit und Beschleunigung schrittweise anpassen; keine Personen im Bewegungsraum.
5. PIR am endgültigen Ort mit endgültigem 3-m-Kabel testen, auch bei laufendem Motor und Netzteillüfter. Keine Phantomtrigger/Resets akzeptieren.
6. Wiederholte Zyklen mindestens 30 Minuten unter Aufsicht, Temperatur und Positionsmarkierung beobachten. Bei Drift, Schlupf, Klemmen oder starker Erwärmung abbrechen.

S0 abschalten und Nachlauf erfassen. Eine Netzabschaltung nimmt dem Motor anschließend das Haltemoment. Die Anlage darf nicht auf einer Neigung selbständig wegrollen. Nach Stromausfall oder Treiberfehler nicht automatisch weiterfahren; Startposition neu einrichten.

## Messprotokoll

| Datum | Aufbau/Revision | Prüfung | Messwert/Beobachtung | Ergebnis / nächste Änderung |
|---|---|---|---|---|
| — | — | Noch keine Hardwareprüfung | — | Offen |
