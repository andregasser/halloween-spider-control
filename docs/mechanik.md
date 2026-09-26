# Mechanischer Aufbau

**Wellendurchmesser vorläufig:** Die bisher vorgesehenen 20 mm sind kein nachgewiesenes Mindestmaß. [Vorprüfung 15 mm gegenüber 20 mm](hauptwelle-auslegung.md): 15 mm sind bei kompakter Anordnung plausibel, aber erst mit Einbaumaßen und Lasten endgültig auszuwählen. Die folgende Beschreibung bleibt die zusammenpassende 20-mm-Referenzausführung.

## Kraftfluss und Abmessungen

NEMA-34-Motor → 20T-Riemenscheibe → HTD-5M-Riemen → 40T-Riemenscheibe → 20-mm-Hauptachse → Flansch-Klemmnabe → Armplatte → Kunststoffrohr → Wagen.

Die beiden UCFL204-Lager werden auf zwei festen, parallelen Tragebenen montiert. Ihre Achsen fluchten; geplanter Mittenabstand etwa 80–120 mm. Die Hauptachse steht senkrecht. Die Riemenräder liegen in derselben Ebene, ihre Achsen sind parallel. Der Rohrarm sitzt oberhalb der Lagerung. Der Wagen trägt die Spinne; die Lagerung trägt Rohrkräfte und Riemenzug.

Vorgesehen sind eine ungefähr 200 mm lange Welle und eine verschiebbare Motoraufnahme. **200 mm sind ein Planmaß**, kein bereits überprüfter Zuschnitt: Lagerbreiten, Riemennabe, Sicherungsringe und Armnabe zunächst übereinander aufzeichnen. Ebenso beziehen sich die 118 mm des Motors auf die Gehäuselänge; Welle, Riemenscheibe und Montage benötigen zusätzlichen Raum. Eine Gesamthöhe unter 150 mm ist damit noch nicht nachgewiesen.

## Riemengeometrie

| Größe | Wert |
|---|---:|
| Motor / Hauptachse | 20 / 40 Zähne |
| Teilung / Breite | 5 / 15 mm |
| Riemen | geschlossen, HTD 450-5M-15, 90 Zähne |
| Teilkreisdurchmesser | 31,83 / 63,66 mm |
| Rechnerischer Achsabstand | ca. 149,15 mm |
| Geplanter Einstellbereich | ungefähr 140–160 mm |

Eigene Näherungsrechnung für einen offenen Riemen: `L = 2a + π(D+d)/2 + (D-d)²/(4a)`, mit `D = 40×5/π`, `d = 20×5/π`, `L = 450 mm`. Das ist ein Layoutwert. Die konkrete Scheibenform, Riemenfreigabe und Spannung müssen beim Aufbau geprüft werden. Langlöcher ersetzen einen zusätzlichen Riemenspanner. Nicht übermäßig vorspannen; die Motorlager müssen den verbleibenden Riemenzug trotzdem aufnehmen.

## Welle-Nabe-Verbindungen

- Motorseitig: 14-mm-Bohrung mit zur Motorwelle passender Passfedernut. Nut und Passfeder am gelieferten Motor messen; Scheibenbreite inklusive Nabe muss auf die nutzbare Wellenlänge passen.
- Hauptachse: 40T-Scheibe mit 20-mm-Bohrung und Passfedernut. Dafür ist eine **bearbeitbare Stahlwelle mit passender Nut** vorgesehen, keine ungeprüft gehärtete Linearführungswelle. Nut und Passfeder gemeinsam mit der Scheibe festlegen.
- Armaufnahme: geschlitzte Flansch-Klemmnabe für 20-mm-Welle, dokumentiertes übertragbares Moment mindestens 20 Nm. Keine nur lose aufgesteckte Flanschnabe. Das ist eine Beschaffungsspezifikation; ein konkretes günstiges Modell wurde noch nicht verifiziert.
- Zwei geteilte Klemmringe sichern die Welle axial; nur am rotierenden Lagerinnenring anlegen, nicht am feststehenden Gehäuse schleifen lassen. Lagerbefestigung und axiale Sicherung nach Herstellerangaben.
- Preiswerte Alu-Riemenscheiben bleiben vorgesehen. Die gefundenen Händlerangebote belegen Variantenmaße, aber keine belastbare Drehmomentfreigabe. Die frühere Aussage „billige Teile reichen sicher“ ist deshalb keine technische Abnahme.

## Wagen und Rohr

Zwei gepolsterte Rohrschellen auf der Armplatte, mit Abstand gegeneinander, halten das Kunststoffrohr. Rohr nicht quetschen. Auf der Wagenseite eine befestigte, bei Bedarf gelenkige Aufnahme mit gesichertem Bolzen vorsehen; Unebenheiten dürfen den Wagen nicht am Rohr hochheben. Rohrdurchmesser, Wanddicke, Material und Befestigungshöhe fehlen noch.

Die sechs Rollen müssen zur Kreisbahn passen: frei schwenkbare Rollen oder eine geeignete tangentiale Ausrichtung. Sechs beliebig parallele Bockrollen würden seitlich schieben und den Antrieb stark belasten. Auf dem tatsächlichen Boden mit einer Federwaage den nötigen Zug messen: `M_Hauptachse ≈ F_Zug × Radius`. Beschleunigung und Verluste kommen hinzu. Haltemoment des Motors allein beweist keine ausreichende Fahrleistung.

## Vor Zuschnitt und Bestellung zu klären

| Offenes Maß / Merkmal | Davon abhängige Teile |
|---|---|
| Rohr-Außendurchmesser, Wanddicke, Material | Rohrschellen, Polsterung, Wagenaufnahme |
| Wagenmaß, Rollentyp, Boden | Wagenplatte, Rollen, benötigte Zugkraft |
| Nabenmaße und Nuten der gekauften Scheiben | Wellenbearbeitung, Passfedern, Wellenlänge |
| Lager- und Nabenbreiten | Lagerbock, Höhen, Distanzteile |
| Montageort, verfügbarer Platz | Grundplatte, Abdeckung, Verankerung |

Der ganze Schwenkbereich einschließlich Wagenüberstand muss frei und gegen Betreten abgegrenzt sein. Riemen und Scheiben erhalten eine feste Abdeckung. Der Grundrahmen wird gegen Wandern und Kippen verankert. Erst ohne Arm, danach ohne Spinne und zuletzt mit Gesamtlast testen.
