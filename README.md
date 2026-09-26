# Halloween-Spinne

Eine große Halloween-Spinne fährt auf einem Wagen mit sechs kugelgelagerten Rollen. Ein ungefähr ein Meter langes Kunststoffrohr zieht und schiebt den Wagen auf einer Kreisbahn. Ein PIR-Bewegungsmelder löst eine langsame, beschleunigte und wieder abgebremste Bewegungssequenz aus.

**Stand: 26. September 2026 · Dokumentationsentwurf Rev. A · noch nicht aufgebaut oder elektrisch getestet.**

## Projektstand

Vorhanden sind laut Bestätigung vom 26.09.2026 ausschließlich **Arduino Uno R3 und PIR-Modul**. Motor, Treiber, Netzteil, Riemenantrieb und weiteres Material sind noch zu beschaffen. Der PIR entspricht optisch einem HC-SR501; die tatsächliche Anschlussbeschriftung ist vor dem Verdrahten zu prüfen.

Die Grundarchitektur steht fest. Diese Dokumentation konkretisiert die Elektronik zu einem durchgängig verdrahtbaren Entwurf. Eine funktionierende Gesamtanlage benötigt zusätzlich die noch zu entwickelnde Firmware und die Inbetriebnahmeprüfungen. Insbesondere ist dies keine bereits erprobte Bauanleitung.

## Dokumente

| Dokument | Inhalt |
|---|---|
| [Elektronik und Schaltplan](docs/elektronik.md) | Zwei grafische Schaltplanblätter, sämtliche Verbindungen, Lötaufbau und Treibereinstellungen |
| [Material-Stückliste](bom/material-stueckliste.md) | Alle vorgesehenen Einbauteile, Mengen, Begründung und Bestand |
| [Bestellliste](bom/bestellliste.md) | Fehlende Teile mit Lieferanten und konkreten Auswahlmerkmalen |
| [Mechanik](docs/mechanik.md) | Riemenantrieb, Lagerung, Befestigung und noch zu messende Maße |
| [Hauptwelle: 15 oder 20 mm](docs/hauptwelle-auslegung.md) | Rechnerische Vorprüfung, Einfluss des Riemenüberhangs und offene Maße |
| [Firmware-Anforderungen](docs/firmware.md) | Pinbelegung, Zustände und Bewegungsparameter; noch keine Implementierung |
| [Inbetriebnahme](docs/inbetriebnahme.md) | Prüfungen vom spannungslosen Aufbau bis zum Wagen |
| [Quellen und Entscheidungen](docs/quellen-und-entscheidungen.md) | Datenblätter und Abweichungen vom frühen Handover |
| [AGENTS.md](AGENTS.md) | Arbeitskontext für Coding-Agents |
| [Ursprüngliches Handover](docs/archiv/PROJECT_HANDOFF_Halloween_Spider.md) | Unveränderte historische Quelle; neuere Dokumente haben Vorrang |

## Aufbau

```mermaid
flowchart LR
    PIR[HC-SR501 PIR] -->|RJ45-Patchkabel bis 3 m| E[Signalaufbereitung]
    E --> U[Arduino Uno R3]
    U -->|STEP/DIR über Transistoren| D[DM860T V3.0]
    P[48-V-Netzteil] --> D
    USB[5-V-USB-Netzteil] --> U
    D --> M[NEMA 34]
    M -->|20T / HTD-5M / 40T| A[Separat gelagerte 20-mm-Hauptachse]
    A --> R[1-m-Kunststoffrohr]
    R --> W[Wagen mit Spinne, etwa 5 kg]
```

Das Gewicht liegt auf den Rollen. Der Motor muss Rollwiderstand und Beschleunigung überwinden; er trägt nicht die Spinne an einem frei schwebenden Hebel. Seine Welle trägt nur die motorseitige Riemenscheibe.

## Festgelegte Basis

- Motor: STEPPERONLINE **34HS46-6004S1**, NEMA 34, 14-mm-Welle.
- Treiber: **DM860T**, dieser Plan bezieht sich ausdrücklich auf **V3.0**.
- Motorversorgung: **Mean Well LRS-350-48**, 48 V; Uno separat über USB.
- Netzanschluss Schweiz: beide Netzteile an derselben geschalteten **CH-Mehrfachsteckdose S0**; Motornetzteil über W1 mit Typ-12-Stecker, USB-Netzteil direkt eingesteckt.
- Mechanik: **20T : 40T**, **HTD-5M**, **15 mm** Riemenbreite, vorläufig **450-5M-15**.
- Hauptachse: Stahl, zwei Lager; 20 mm als vorläufige Referenz, 15 mm als noch zu dimensionierende Alternative.
- Trigger: vorhandener PIR, vier Adern in zwei Paaren eines RJ45-Patchkabels bis 3 m; drei elektrische Netze: 5 V, GND, OUT.
- Kein Hall-Sensor und keine automatische Referenzfahrt in der ersten Version.

Modellwerte und Quellen stehen in [Elektronik](docs/elektronik.md) und [Quellen](docs/quellen-und-entscheidungen.md). Haltemoment ist kein Nachweis für das verfügbare Drehmoment während der Fahrt.

## Geplanter Ablauf

Einschalten → Sensor stabilisieren lassen → manuell freigeben → auf neue Bewegung warten → langsam vorfahren → Pause → zurückfahren → Cooldown → erneut scharf werden, wenn der PIR wieder LOW war.

Die Ausgangsposition wird vor der Freigabe manuell festgelegt. Nach Stromausfall, Blockade oder Schrittverlust ist sie unbekannt und muss neu eingerichtet werden. Die ersten Versuche erfolgen ohne Arm und Wagen.

## Grenzen des Entwurfs

Der 230-V-Teil wird geklemmt/gecrimpt und durch eine Elektrofachperson aufgebaut und geprüft. Die Lötanleitung betrifft die Kleinspannungsplatinen. Schwenkbereich und Riemenantrieb müssen gegen Zugriff geschützt sein. Der vorgesehene Hauptschalter ist eine Netzabschaltung, kein nachgewiesener Not-Halt; der Freigabeschalter ist eine Software-Bedienfunktion. Eine sofortige mechanische Stillsetzung ist damit nicht zugesichert.

Vor der Bestellung der gekennzeichneten Mechanikteile fehlen insbesondere Rohrdurchmesser, Plattenmaße und die Ausführung der Welle-Nabe-Verbindungen. Diese Punkte sind in der Bestellliste vollständig aufgeführt, aber noch nicht als fertige Einkaufsposition freigegeben.
