#!/usr/bin/env python3
"""Zeichnet die zwei Schaltplanblätter als eigenständige SVGs, ohne Zusatzpakete."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Gleiche Geräte tragen auf jedem Blatt dieselbe Bezeichnung.
DEVICES = {
    'U1': 'Arduino Uno R3',
    'U2': 'SN74HCT14N',
    'U3': 'DM860T V3.0',
    'B1': 'HC-SR501-Bauform',
    'M1': '34HS46-6004S1',
    'PS1': 'LRS-350-48',
    'PS2': 'USB-Netzteil',
    'J1': 'RJ45-Klemmenadapter',
    'J2': 'RJ45-Klemmenadapter',
}

def device(ref):
    return f'{ref} · {DEVICES[ref]}'

class Plan:
    def __init__(self, title, height):
        self.h = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="{height}" viewBox="0 0 1800 {height}">',
            '<style>text{font-family:DejaVu Sans,Arial,sans-serif;fill:#152536} .wire{fill:none;stroke:#253b50;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}</style>',
            f'<rect width="1800" height="{height}" fill="white"/>']
        self.text(35, 46, title, 29, bold=True)
        self.text(35, 79, 'Halloween-Spinne · Revision A · 26.09.2026 · Entwurf, noch nicht aufgebaut oder geprüft', 18)
        self.text(35, 108, 'Gleiche Netznamen sind verbunden. Punkte = Verbindung. Kreuzungen ohne Punkt = keine Verbindung.', 17)

    def text(self, x, y, s, size=18, bold=False, color=None):
        attr = (' font-weight="bold"' if bold else '') + (f' style="fill:{color}"' if color else '')
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}"{attr}>{escape(s)}</text>')

    def lines(self, x, y, lines, size=17, step=27):
        for i, s in enumerate(lines): self.text(x, y+i*step, s, size)

    def box(self, x, y, w, h, title=None, fill='#f5f8fb'):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="#8ca0b3" stroke-width="1.5"/>')
        if title: self.text(x+16, y+30, title, 21, True)

    def wire(self, *pts, color=None, dash=False):
        attrs = (f' style="stroke:{color}"' if color else '') + (' stroke-dasharray="7 5"' if dash else '')
        self.parts.append('<polyline class="wire" points="'+' '.join(f'{x},{y}' for x,y in pts)+f'"{attrs}/>')

    def dot(self, x, y):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#253b50"/>')

    def resistor(self, x, y, label, vertical=False):
        if vertical:
            self.wire((x,y),(x,y+10)); self.parts.append(f'<rect x="{x-8}" y="{y+10}" width="16" height="40" fill="white" stroke="#253b50" stroke-width="2"/>'); self.wire((x,y+50),(x,y+60)); self.text(x+16,y+35,label,16)
        else:
            self.wire((x,y),(x+10,y)); self.parts.append(f'<rect x="{x+10}" y="{y-8}" width="70" height="16" fill="white" stroke="#253b50" stroke-width="2"/>'); self.wire((x+80,y),(x+90,y)); self.text(x,y-22,label,17)

    def cap(self, x, y, label, polar=False):
        self.wire((x,y),(x,y+22)); self.wire((x-15,y+22),(x+15,y+22)); self.wire((x-15,y+32),(x+15,y+32)); self.wire((x,y+32),(x,y+60)); self.text(x+22,y+33,label,16)
        if polar: self.text(x-28,y+16,'+',18)

    def gnd(self, x, y):
        self.wire((x,y),(x,y+10)); self.wire((x-16,y+10),(x+16,y+10)); self.wire((x-10,y+17),(x+10,y+17)); self.wire((x-4,y+24),(x+4,y+24)); self.text(x-21,y+47,'GND',16)

    def gate(self, x,y,label,pins):
        self.parts.append(f'<path d="M{x},{y-30} L{x},{y+30} L{x+60},{y} Z" fill="white" stroke="#253b50" stroke-width="2"/>')
        self.parts.append(f'<circle cx="{x+67}" cy="{y}" r="7" fill="white" stroke="#253b50" stroke-width="2"/>')
        self.text(x+6,y+6,'H',16); self.text(x-5,y-68,label,19,True)
        self.text(x-5,y-46,DEVICES['U2'],15)
        self.text(x-22,y-10,str(pins[0]),16); self.text(x+76,y-10,str(pins[1]),16)

    def save(self, name):
        self.wire((35,self.h-70),(1765,self.h-70))
        self.text(35,self.h-42,'Verbindliche Verbindungstabellen, Bauteilwerte und Aufbauhinweise: docs/elektronik.md',18)
        self.text(35,self.h-16,'Kein Verdrahten unter Spannung. 230-V-Baugruppe durch Elektrofachperson aufbauen und prüfen.',17)
        (ROOT/'docs'/name).write_text('\n'.join(self.parts+['</svg>'])+'\n',encoding='utf-8')

p=Plan('Blatt 2 / 2 — Steuerung, STEP/DIR und PIR-Sensor',1500)
p.box(30,130,1740,365,f'A · PIR über RJ45, bis 3 m; {device("U2")} (DIP-14), nicht 74HC14')
p.box(55,190,190,240,fill='white');p.text(55,188,device('B1'),16,True)
for y, label in [(235,'VCC'),(310,'OUT'),(400,'GND')]:
    p.text(175,y-9,label,17); p.wire((245,y),(340,y))
p.text(70,273,'PIR-Sensor',17);p.text(70,299,'Bewegung',17)
p.text(65,457,'B1-Pinreihenfolge am eigenen Modul prüfen!',16)
p.box(340,200,105,225,fill='white');p.box(640,200,105,225,fill='white')
p.text(340,188,device('J2'),16,True);p.text(640,188,device('J1'),16,True)
for y,label in [(235,'5'),(310,'1'),(400,'2+4')]:
    p.text(356,y-8,label,17);p.text(653,y-8,label,17);p.wire((445,y),(640,y))
p.text(455,210,'W3 · Patchkabel 1:1',16,True)
p.text(462,268,'weiß/blau: +5V',16)
p.text(457,343,'weiß/orange: OUT',16)
p.text(454,435,'orange + blau: GND',16)
p.wire((745,235),(820,235));p.text(775,218,'+5V',18,True)
p.wire((745,400),(810,400));p.gnd(810,400)
p.wire((745,310),(815,310));p.resistor(815,310,'R5 · 1 kΩ')
p.wire((905,310),(1090,310));p.dot(950,310);p.dot(1020,310)
p.wire((950,310),(950,345));p.resistor(950,345,'',True);p.gnd(950,405)
p.wire((1020,310),(1020,345));p.cap(1020,345,'');p.gnd(1020,405)
p.text(863,480,'R6 · 100 kΩ',16);p.text(1010,480,'C5 · 100 nF',16)
p.gate(1090,310,'U2A',(1,2));p.wire((1164,310),(1270,310));p.gate(1270,310,'U2B',(3,4))
p.wire((1344,310),(1695,310));p.text(1400,285,'PIR_5V → J0.6 → U1 D7',20,True)
p.lines(1400,355,['HIGH = Bewegung','LOW bei abgezogenem Kabel','U2A/U2B: Teile desselben U2','Versorgung/übrige Pins: Feld E'],17)

def stage(x,title,pin,q,r,pd,jminus,jplus,minus,plus):
    p.box(x,520,855,360,title)
    p.text(x+25,600,device('U1'),19,True)
    p.text(x+25,642,pin,21,True)
    p.wire((x+100,650),(x+135,650));p.resistor(x+135,650,f'{r} · 1 kΩ')
    p.wire((x+225,650),(x+330,650));p.dot(x+270,650)
    p.wire((x+270,650),(x+270,700));p.resistor(x+270,700,'',True);p.gnd(x+270,760);p.text(x+145,737,f'{pd} · 100 kΩ',16)
    p.wire((x+330,620),(x+330,680));p.wire((x+330,635),(x+380,605),(x+380,580))
    p.wire((x+330,665),(x+380,700),(x+380,760))
    p.parts.append(f'<path d="M{x+363},681 L{x+369},694 L{x+354},690 Z" fill="#253b50"/>')
    p.gnd(x+380,760);p.text(x+400,685,f'{q} · 2N3904',18,True)
    p.text(x+302,608,'B',15);p.text(x+386,612,'C',15);p.text(x+385,729,'E',15)
    p.box(x+650,565,180,210,fill='white')
    p.text(x+661,593,device('U3'),16,True)
    p.text(x+661,616,'Steuereingang',15)
    p.wire((x+380,580),(x+585,580),(x+585,630),(x+650,630))
    p.text(x+440,564,f'J3.{jminus}',16);p.text(x+675,637,minus,20,True)
    p.wire((x+570,720),(x+650,720));p.text(x+485,727,'+5V',20,True);p.text(x+583,704,f'J3.{jplus}',16);p.text(x+675,727,plus,20,True)
    p.text(x+25,853,'HIGH am Uno aktiviert den Optokoppler. GND bleibt auf der Steuerungsseite.',16)
stage(30,'B · Schrittimpulse, Common-Anode','D2','Q1','R1','R3',2,1,'PUL−','PUL+')
stage(915,'C · Richtung, Common-Anode','D3','Q2','R2','R4',4,3,'DIR−','DIR+')

p.box(30,910,410,390,f'D · {device("U1")}')
p.lines(48,973,['USB-B ← W2 / PS2 (Blatt 1)','J0.1 ↔ 5V → Netz +5V','J0.2 ↔ GND → Netz GND','J0.3 ↔ D2 → R1 (Feld B)','J0.4 ↔ D3 → R2 (Feld C)','J0.5 ↔ D4 → S1 / R7','J0.6 ↔ D7 ← U2.4 (Feld A)','D8, VIN, Hohlbuchse: frei','D13: eingebaute Status-LED'],18,32)

p.box(460,910,365,390,'S1 · Freigabe EIN/AUS')
p.text(495,975,'+5V',19,True);p.wire((520,985),(520,1000));p.resistor(520,1000,'R7 · 10 kΩ',True)
p.wire((520,1060),(520,1090),(740,1090));p.dot(520,1090)
p.text(543,1078,'D4 / J0.5',18,True)
p.wire((520,1090),(520,1140));p.dot(520,1140);p.dot(520,1200)
p.wire((520,1200),(545,1150));p.gnd(520,1200)
p.text(562,1147,'J4.1',17);p.text(562,1207,'J4.2',17)
p.text(570,1249,'EIN = geschlossen',16)
p.text(478,1280,'Softwarefunktion, kein Not-Halt.',16)

p.box(845,910,455,390,f'E · {device("U2")}')
p.text(865,970,'+5V → U2.14    GND → U2.7',18,True)
p.wire((890,1000),(1135,1000));p.text(865,992,'+5V',16)
p.cap(890,1020,'C1 · 100 nF');p.wire((890,1000),(890,1020));p.gnd(890,1080)
p.cap(1135,1020,'C2 · 10 µF',True);p.wire((1135,1000),(1135,1020));p.gnd(1135,1080)
p.lines(865,1170,['C1 direkt an U2.14 / U2.7.','U2.5 / .9 / .11 / .13 → GND','U2.6 / .8 / .10 / .12 → offen','U2.2 mit U2.3 verbinden.'],17,30)

p.box(1320,910,450,390,f'F · {device("B1")}')
p.wire((1370,1000),(1600,1000));p.text(1342,980,'B1 VCC / J2.5',18,True)
p.cap(1370,1020,'C3 · 100 nF');p.wire((1370,1000),(1370,1020));p.gnd(1370,1080)
p.cap(1600,1020,'C4 · 10 µF',True);p.wire((1600,1000),(1600,1020));p.gnd(1600,1080)
p.lines(1340,1170,['GND = B1 GND / J2.2 + J2.4','C2/C4: 16 V oder höher, Polarität!','C1/C3/C5: 25 V oder höher.','RJ45.3/.6/.7/.8: beidseitig frei.'],17,30)
p.text(35,1334,'W4 · STEP/DIR-Kabel: J3 → U3, 2 geschirmte Paare. ENA±/ALM±/BRK± offen. GND, M48− und PE getrennt.',18,True)
p.text(35,1370,'J0 · Arduino-Anschlussleiste   |   J3 · STEP/DIR-Klemmenleiste   |   J4 · Freigabeschalter-Klemmenleiste',18)
p.text(35,1400,'Kennzeichen · Bauteilbezeichnung; z. B. U3 · DM860T V3.0. J3.2 bedeutet Anschluss 2 der Klemmenleiste J3.',17)
p.save('schaltplan-steuerung.svg')

p=Plan('Blatt 1 / 2 — Netzversorgung, 48-V-Motorversorgung und Schutzleiter',1540)
p.box(30,130,1740,285,'Steckübersicht Schweiz · zwei Netzteile an derselben Mehrfachsteckdose')
p.box(55,190,300,170,'CH-Wandsteckdose','white')
p.lines(72,250,['230 V / 50 Hz · Typ 13','30-mA-FI/RCD vorhanden','E45 nur bei fehlendem RCD'],17,30)
p.wire((355,275),(505,275));p.text(372,257,'CH-Stecker',16)
p.box(505,175,480,215,'S0 · CH-Mehrfachsteckdose','white')
p.lines(525,243,['Typ-13-Buchsen · 10 A gesamt','Gemeinsamer EIN/AUS-Schalter','L/N zweipolig, PE durchverbunden'],17,33)
# Zwei schematische Steckplätze; Leitungen hier als ganze Kabel dargestellt.
for y,number in [(245,'1'),(350,'2')]:
    p.parts.append(f'<circle cx="955" cy="{y}" r="19" fill="white" stroke="#253b50" stroke-width="2"/>')
    p.text(949,y+6,number,17,True)
    p.wire((974,y),(1260,y))
p.text(1005,223,'W1 · CH-Typ-12-Stecker',17,True)
p.text(1005,272,'3-adrige Netzleitung',16)
p.box(1260,205,485,85,device('PS1'),'white')
p.text(1276,268,'Motornetzteil · Klemmenanschluss unten',17)
p.text(1005,328,'PS2 direkt einstecken',17,True)
p.text(1005,377,'CH-/Eurostecker',16)
p.box(1260,310,485,85,device('PS2'),'white')
p.text(1276,373,'5 V → W2 USB-Kabel → U1 Arduino Uno R3',17)
p.parts.append('<g transform="translate(0,330)">')
p.box(30,135,1740,475,'Leistungsteil · 230 V nur im geschlossenen Netzbereich; Motorverdrahtung nicht auf Lochraster')
p.box(55,198,225,335,fill='white');p.text(72,228,'S0 · Steckplatz 1',18,True)
p.lines(72,270,['CH-Mehrfachsteckdose','W1 eingesteckt:','CH-Typ-12-Stecker','L / N / PE'],16,30)
p.lines(72,429,['Detail zur Übersicht','Keine Leiste öffnen','PE durchverbunden'],16,29)
for y,label in [(250,'L_SW'),(330,'N_SW'),(410,'PE')]:
    p.wire((280,y),(375,y));p.text(289,y-12,label,17,True)
p.resistor(375,250,'F1 · T6,3 A');p.wire((465,250),(595,250));p.text(485,231,'W1 L',16)
p.wire((375,330),(595,330));p.text(488,310,'W1 N',16)
p.wire((375,410),(595,410),color='#36813f');p.dot(425,410);p.text(456,388,'XPE',18,True)
p.box(595,195,300,330,device('PS1'),'white')
for y,label in [(250,'L'),(330,'N'),(410,'PE')]:p.text(610,y+7,label,21,True)
p.lines(690,325,['Eingang: 230 V','Wahlschalter','auf 230 V!'],18,30)
p.text(834,257,'+V',20,True);p.text(834,442,'−V',20,True)
p.wire((895,250),(970,250));p.resistor(970,250,'');p.text(944,204,'F2 · T8 A / 63 VDC',18);p.wire((1060,250),(1210,250))
p.wire((385,250),(455,250));p.wire((980,250),(1050,250))
p.wire((895,435),(1130,435),(1130,330),(1210,330));p.text(929,418,'M48−',19,True)
p.text(1090,231,'+48 V',19,True)
p.box(1210,195,280,365,device('U3'),'white')
p.text(1228,257,'AC (1)',19,True);p.text(1228,337,'AC (2)',19,True)
p.lines(1228,395,['48 VDC an AC/AC','Bei V3.0 zulässig.','Andere Version:','Belegung neu prüfen!'],17,29)
p.box(1580,195,170,365,fill='white');p.text(1593,220,device('M1'),13,True);p.text(1594,545,'NEMA 34',17)
for y,label,col in [(250,'A+ schwarz','#253b50'),(330,'A− grün','#36813f'),(410,'B+ rot','#b33333'),(490,'B− blau','#2463af')]:
    p.wire((1490,y),(1580,y),color=col);p.text(1500,y-13,label,14);p.text(1593,y+8,label[:2],19,True)
p.text(60,578,'F1/F2: 6,3×32 mm, eigene berührungsgeschützte Halter. Leistungslitzen 1,5 mm²; Motor mit mitgeliefertem Kabel.',18)

p.box(30,635,540,330,'XPE · Schutzleiterverteilung')
p.wire((425,410),(555,410),(555,690),(500,690),color='#36813f')
p.lines(53,712,['W1 PE → XPE → PS1 PE','XPE → Metallgehäuse','XPE → Metall-Montageplatte','XPE → leitfähiger Deckel (flexible Brücke)','XPE → Motorrahmen / Motorgehäuse','J3-Kabelschirm → PE am Gehäuseeintritt'],18,35)
p.text(53,942,'Eigene gesicherte PE-Anschlüsse, grün-gelb.',18,True)

p.box(595,635,1175,330,'5-V-Versorgung · PS2 direkt in Steckplatz 2 derselben CH-Mehrfachsteckdose S0')
p.box(625,708,270,170,device('PS2'),'white')
p.text(640,770,'230 V ← S0, Steckplatz 2',17)
p.text(640,813,'5 V / ≥1 A, geschlossen',18)
p.wire((895,790),(1160,790));p.text(936,765,'W2 · USB-A/B',19,True)
p.box(1160,708,265,170,device('U1'),'white')
p.text(1176,799,'USB-B',20,True)
p.wire((1425,752),(1705,752));p.text(1475,731,'5V → +5V (Blatt 2)',18,True)
p.wire((1425,837),(1705,837));p.text(1475,821,'GND → GND (Blatt 2)',18,True)
p.text(620,925,'Beim Programmieren: Motor aus, USB-Kabel von PS2 auf Rechner umstecken. VIN bleibt frei.',18)

p.box(30,990,1740,130,'Betriebsgrenzen und Zuordnung')
p.lines(50,1050,['M48−, Steuer-GND und PE nicht miteinander brücken. Die Treibereingänge bleiben optisch getrennt.',
    'U3-Signale PUL± / DIR±: Blatt 2. ENA± / ALM± / BRK± offen. S0 ist Netzabschaltung, kein nachgewiesener Not-Halt.',
    'Schwenkbereich abgrenzen. Nachlauf und Verlust des Haltemoments nach Abschaltung berücksichtigen.'],18,27)
p.parts.append('</g>')
p.save('schaltplan-versorgung.svg')
print('Zwei SVG-Schaltplanblätter erzeugt.')
