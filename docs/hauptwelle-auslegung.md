# Hauptwelle: Vorprüfung 15 mm gegenüber 20 mm

Stand: 26. September 2026. **Rechnerische Vorprüfung, kein abgeschlossener Festigkeits- oder Lebensdauernachweis.**

## Ergebnis

**20 mm sind kein nachgewiesener Mindestdurchmesser. Eine 15-mm-Stahlwelle ist eine plausible Alternative, wenn die Riemenscheibe nahe am Lager sitzt.** Die bisherige 20-mm-Ausführung bietet deutlich mehr Reserve gegen Biegung und Verdrehung. Ob diese Reserve nötig ist, lässt sich erst mit den tatsächlichen Einbaumaßen, Riemenkräften und Welle-Nabe-Verbindungen entscheiden.

Für den nächsten Konstruktionsschritt 15 mm als Alternative untersuchen: zwei Lager, kurzer Abstand zwischen Riemenmitte und nächster Lagermitte, kurze Armnabe oberhalb des oberen Lagers. Ein Überhang von 20 mm ist unten ein günstiges Rechenbeispiel, keine pauschale Freigabegrenze. Ob er mit den Lager- und Nabenbreiten erreichbar ist, muss die Maßzeichnung zeigen. Eine Scheibe zwischen den Lagern kann ebenfalls sinnvoll sein; sie benötigt eine eigene Berechnung mit ihrer tatsächlichen Position.

Die bisher betrachtete 20-mm-Referenzausführung bleibt vorläufiger Projektkontext. Die aktuelle Stück- und Bestellliste umfasst ausschließlich Elektronik; die früheren Mechanikpositionen M03, M05, M06, M07, M08 und M10 sind dort nicht mehr enthalten. Eine spätere Durchmesseränderung betrifft gemeinsam Riemenscheibe, Welle, Lager, Klemmringe, Armnabe und Passfeder.

## Gesicherte Ausgangsdaten und offene Lasten

- Der Wagen trägt die ungefähr 5 kg auf Rollen. Daraus entsteht **kein** ständig frei auskragendes Gewichtsmoment von `5 kg × 9,81 m/s² × 1 m` an der Hauptwelle.
- Der [34HS46-6004S1](https://www.omc-stepperonline.com/fr/moteur-pas-a-pas-nema-34-serie-s-8-5nm-1203-94oz-in-14mm-arbre-a-cle-cable-1m-34hs46-6004s1) hat laut Hersteller 8,5 Nm Haltemoment. Mit 20T/40T ergibt sich ohne Verluste eine **Rechengröße von 17 Nm** an der Hauptwelle. Das ist weder zugesichertes Fahrmoment noch eine Begrenzung äußerer Stoßlasten.
- Die 40T-Scheibe hat bei 5 mm Teilung einen Teilkreisradius `r = 40 × 5 / (2π) = 31,83 mm`.
- Damit beträgt die Differenz der Zugkräfte beider Riemenstränge bei 17 Nm bereits `ΔF = T/r = 534 N`. Die Lagerbelastung hängt hingegen von der vektoriellen Summe beider Strangkräfte ab, einschließlich Vorspannung. Sie ist nicht einfach mit 534 N gleichzusetzen.
- Reale Vorspannung, Wagenzugkraft, Beschleunigung, Rohrgewicht, Verbindungen und Hindernisstöße sind bisher nicht gemessen. Auch das Eigengewicht des Rohrarms kann ein Biegemoment verursachen, obwohl der Wagen auf Rollen steht.

## Vergleichsrechnung für eine auskragende Riemenscheibe

Modell: gleichmäßig dicke, massive Stahlwelle, zwei idealisierte radiale Lager, Riemenscheibe unterhalb des unteren Lagers. `a` bezeichnet den Abstand von der **Lagermitte zur Riemenmitte**, nicht den freien Spalt zwischen Gehäuse und Scheibe.

Für diesen Vergleich werden **700 N resultierende Riemenkraft angenommen**. Dieser Wert ist ein Szenario, keine Herstellerangabe oder nachgewiesene Obergrenze. Er dient dazu, den Einfluss von Durchmesser und Überhang zu zeigen. Weitere Arm- und Gewichtslasten sind in dieser Tabelle noch nicht enthalten; sie sind bei der endgültigen Auslegung mit ihren Angriffspunkten zu ergänzen.

Mit Drehmoment `T = 17 000 Nmm`, Biegemoment am unteren Lager `M = F × a` und Durchmesser `d` in mm:

```text
Schubspannung:          τ = 16 T / (π d³)
Biegespannung:           σ = 32 M / (π d³)
Vergleichsspannung:      σv = √(σ² + 3 τ²)
```

Die Tabelle kombiniert volle Torsion und maximale Riemenbiegung als Vergleichshülle. Ob beide am selben kritischen Querschnitt wirken, hängt von Naben- und Nutlage ab. Werte beziehen sich auf einen glatten Vollquerschnitt, ohne Kerben.

| Überhang a | Biegemoment | Vergleichsspannung 15 mm | Vergleichsspannung 20 mm |
|---|---:|---:|---:|
| 20 mm | 14 Nm | 61 MPa | 26 MPa |
| 30 mm | 21 Nm | 77 MPa | 33 MPa |
| 50 mm | 35 Nm | 115 MPa | 48 MPa |

Bei gleichem Lastfall hat die 15-mm-Welle **2,37-mal so hohe Spannungen** wie die 20-mm-Welle. Allein durch das Drehmoment beträgt ihre Schubspannung rund 26 MPa; der Riemenzug ist daher ein wesentlicher Teil der Auslegung.

Zum Einordnen könnte eine konkret spezifizierte C45-Ausführung mit mindestens 300 MPa Streckgrenze dienen. Das ist eine **Anforderung an das spätere Material**, keine Eigenschaft jeder beliebigen Stahlstange. Das [Ovako-Datenblatt zu C45](https://steelnavigator.ovako.com/steel-grades/c45/) zeigt unterschiedliche Festigkeiten je nach Variante und Lieferzustand. Aus dem Abstand der obigen Spannungen zur Streckgrenze folgt noch keine ausreichende Sicherheit der fertigen Welle.

### Empfindlichkeit gegenüber Kerben und Stößen

Eine Passfedernut erhöht lokale Spannungen. Nur als Sensitivitätsbeispiel: Würden Kerben beide Spannungskomponenten um Faktor 2 erhöhen und gleichzeitig Drehmoment und Riemenkraft durch einen Stoß auf das Doppelte steigen, würden die Tabellenwerte insgesamt vervierfacht. Bei 15 mm und 30 mm Überhang wären das etwa **310 MPa**, gegenüber etwa **131 MPa** bei 20 mm.

Diese beiden Faktoren sind **keine ermittelten Last- oder Kerbfaktoren** und keine normgerechte Bemessung. Das Beispiel zeigt, weshalb eine glatte 15-mm-Welle im ruhigen Lastfall plausibel sein kann, ohne dass damit eine genutete Welle bei Blockade freigegeben wäre. Auch 20 mm sind damit nicht für beliebige Stöße nachgewiesen. Die bestehende Beschaffungsvorgabe von mindestens 20 Nm für die Armnabe deckt das Beispiel mit 34 Nm nicht ab.

## Verdrehung

Für eine angenommene wirksame Torsionslänge von **150 mm zwischen den Krafteinleitungen der beiden Naben**, 17 Nm und `G = 80 000 N/mm²`:

```text
J = π d⁴ / 32
φ = T L / (G J)        [Radiant]
```

| Durchmesser | Elastische Verdrehung | Entsprechender Weg bei 1 m Arm |
|---|---:|---:|
| 15 mm | 0,37° | 6,4 mm |
| 20 mm | 0,12° | 2,0 mm |

Das ist die elastische Verformung unter diesem Drehmoment, kein bleibender Positionsfehler. Bei kleinerem Moment sinkt sie proportional. Riemen, Kunststoffrohr, Nuten und Naben bringen weitere Verformung beziehungsweise Spiel mit. Der Materialwert stammt aus dem oben verlinkten Ovako-Datenblatt.

## Was die endgültige Entscheidung benötigt

1. Bemaßte Seitenansicht: Lagermittenabstand, Riemenmitte, Armanschluss, Nabenbreiten und Nutlage. Referenz bisher 80–120 mm Lagerabstand; das allein bestimmt den Überhang nicht.
2. Konkrete Welle mit Werkstoff/Lieferzustand, Nutgeometrie und Oberflächenzustand. Bei wiederholtem Schwenken entstehen wechselnde Spannungen; Ermüdung ist hier noch nicht nachgewiesen.
3. Tatsächliche Riemenspannung und Wagenzugkraft auf dem vorgesehenen Boden, ergänzt um Beschleunigung und Rohrkräfte. Übermäßige Vorspannung vermeiden; [Gates weist auf Schäden an Wellen und Lagern durch zu hohe Spannung hin](https://www.gates.com/content/dam/documents-library/catalogs/powergrip-gt3-drive-design-manual-en.pdf). Daraus werden keine GT3-Spannwerte für unseren HTD-Riemen übernommen.
4. Nachweise für Passfeder, Alu-Scheibennabe, Arm-Klemmnabe, Lager und Lagerträger. Ein stärkerer Wellendurchmesser ersetzt diese nicht. Lager mit 15-mm-Bohrung existieren, beispielsweise [JTEKT UCFL202](https://koyo.jtekt.co.jp/en/products/detail/?pno=UCFL202); Tragfähigkeit und Einbaumaße gelten jeweils für das konkrete Fabrikat.

**Planungsentscheidung:** 15 mm bleiben eine ernsthafte Alternative. 20 mm sind eine vorläufige Ausführung mit größerer Reserve, keine berechnete Mindestanforderung. Die nächste sinnvolle Arbeit ist die bemaßte Lager-/Nabenanordnung; erst damit lässt sich die kleinere Variante verbindlich auswählen.
