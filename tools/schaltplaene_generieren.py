#!/usr/bin/env python3
"""Praktische Anschlussblätter für Revision B, ausschließlich Standardbibliothek."""
from html import escape
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DEVICES = {'U1':'Arduino Uno R3','U3':'DM860T V3.0','U4':'Adafruit MOSFET #5648','U5':'Adafruit MOSFET #5648','U6':'DFRobot DFR0265','B1':'PIR · HC-SR501-Bauform','M1':'34HS46-6004S1','PS1':'Mean Well GST220A48-R7B','PS2':'Goobay 44952 · USB-Netzteil','S0':'CH-Mehrfachsteckdose','J1':'DFRobot FIT0849','J2':'DFRobot FIT0849'}
class Sheet:
    def __init__(self,title,h):
        self.h=h
        self.out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="{h}" viewBox="0 0 1800 {h}">', '<rect width="100%" height="100%" fill="white"/>', '<style>text{font-family:Arial,DejaVu Sans,sans-serif;fill:#152331;font-size:24px} .title{font-size:37px;font-weight:bold}.head{font-size:27px;font-weight:bold}.small{font-size:22px}</style>']
        self.text(55,65,title,'title');self.text(55,105,'03.10.2026 · Revision B · Entwurf, noch nicht aufgebaut/getestet','small')
    def text(self,x,y,t,cls=''):
        self.out.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(t)}</text>')
    def box(self,x,y,w,h,title,lines=()):
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#f4f7fa" stroke="#354b60" stroke-width="2"/>')
        self.text(x+16,y+37,title,'head')
        for i,l in enumerate(lines):self.text(x+16,y+78+36*i,l,'small')
    def device(self,ref,x,y,w,h,lines=()):self.box(x,y,w,h,ref+' · '+DEVICES[ref],lines)
    def wire(self,pts,color='#556779'):
        self.out.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="4"/>')
    def dot(self,x,y):self.out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#152331"/>')
    def panel(self,y,title):
        self.wire([(55,y),(1745,y)],'#c3ced8');self.text(55,y+42,title,'head')
    def save(self,path):
        self.text(55,self.h-35,'Maßgebliche Pinliste und Aufbaufolge: docs/elektronik.md · Nur spannungslos verdrahten.','small')
        (ROOT/path).write_text('\n'.join(self.out+['</svg>'])+'\n',encoding='utf-8')

def supply():
    s=Sheet('Blatt 1 · Versorgung und Motor',1590)
    s.panel(140,'A · Beide fertigen Netzteile in die vorhandene Schweizer Mehrfachsteckdose stecken')
    s.device('S0',65,225,485,220,['Typ-13-Buchsen · gemeinsamer Schalter','Steckplatz 1 → W1 → PS1','Steckplatz 2 → PS2','Vorhanden; beide Netzteile gemeinsam aus'])
    s.device('PS1',850,225,870,200,['W1: Typ-12-Stecker ↔ IEC-C13-Buchse, 1,8 m','Netzteileingang: IEC-C14','Ausgang: 48 V / 4,6 A · 4-poliger Power-DIN-R7B'])
    s.wire([(550,300),(850,300)]);s.text(585,280,'W1 · fertiges Netzkabel','small')
    s.device('PS2',65,520,670,155,['Steckt direkt in Steckplatz 2 von S0','USB-A-Ausgang: nominal 5 V'])
    s.wire([(290,445),(290,520)])
    s.device('U1',1170,520,550,155,['W2 in USB-B-Buchse stecken','5-V-Verteilung siehe Blatt 2'])
    s.wire([(735,600),(1170,600)],'#bd2734');s.text(780,580,'W2 · USB-A ↔ USB-B','small')
    s.panel(735,'B · 48-V-Anschluss über W5; keine Arbeiten am Netzteilkabel oder an 230 V')
    s.box(65,825,750,230,'W5 · GlobTek KPPX4124641M0KPJX4(R)',['Power-DIN-Buchse auf unveränderten PS1-Stecker','Nur männliches Ende der Verlängerung abschneiden','Vier AWG-18-Adern: 2 × +48 V, 2 × Rückleiter','Kontaktlage durchmessen; Schirm am Schnitt isolieren'])
    s.wire([(1720,350),(1760,350),(1760,800),(440,800),(440,825)],'#bd2734')
    s.box(900,825,330,100,'X1 · WAGO 221-413',['1 / 2: beide +48-V-Adern'])
    s.box(900,985,330,100,'X2 · WAGO 221-413',['1 / 2: beide Rückleiter'])
    s.wire([(815,900),(900,900)],'#bd2734');s.wire([(815,1035),(900,1035)])
    s.device('U3',1360,825,360,300,['AC (erste Klemme)','AC (zweite Klemme)','A+ / A− / B+ / B−','Signale: Blatt 2','ENA / ALM / BRK frei'])
    s.wire([(1230,900),(1360,900)],'#bd2734');s.text(1240,880,'X1.3','small')
    s.wire([(1230,1035),(1305,1035),(1305,936),(1360,936)]);s.text(1240,1015,'X2.3','small')
    s.text(890,1160,'X1.3 / X2.3 → U3 AC/AC: je kurze 1,5-mm²-Kupferlitze','small')
    s.device('M1',65,1190,750,230,['Motorlieferkabel, 1 m; keine Verlängerung vorgesehen','Schwarz → A+       Grün → A−','Rot → B+               Blau → B−','Wicklungspaare vor Anschluss durchmessen'])
    s.wire([(1530,1125),(1530,1230),(815,1230)],'#895821');s.text(875,1210,'Vier Motoradern → U3 A+/A−/B+/B−','small')
    s.box(900,1270,820,185,'Vor dem Einschalten',['PS1 trocken und belüftet außerhalb der Steuerbox.','48-V-Rückleiter X2 nicht an Arduino-GND brücken.','W5-Steckerzuordnung messen; nie nach Farben raten.'])
    s.text(65,1495,'Beide AC-Klemmen akzeptieren 48 V DC nur für die hier bezeichnete U3-Version.','small')
    s.save('docs/schaltplan-versorgung.svg')

def control():
    s=Sheet('Blatt 2 · Arduino, fertige Signalmodule und PIR',2290)
    for y,ref,pin,power,out,color,title in [(140,'U4','D2','A1','PUL','#c26311','A · STEP: D2 schaltet das Schritt-Signal'),(670,'U5','D3','A2','DIR','#7357ad','B · DIR: D3 schaltet die Richtung')]:
        s.panel(y,title)
        s.device('U1',65,y+95,390,130,[pin+' → aufgestecktes U6','5 V / GND → U6'])
        s.device('U6',530,y+95,600,250,[pin+' grüner Signalstift → In',power+' roter +V-Stift → V+',power+' schwarzer GND-Stift → GND','Jumper 5V/3.3V auf 5 V','Rote digitale D-Versorgungsreihe frei'])
        s.wire([(455,y+170),(530,y+170)],color)
        s.device(ref,1240,y+95,500,270,['STEMMA In ← weiße Leitung','STEMMA V+ ← rote Leitung','STEMMA GND ← schwarze Leitung','Ausgang + → '+out+'+','Ausgang − → '+out+'−'])
        for j,c in enumerate([color,'#bd2734','#556779']):s.wire([(1130,y+173+j*36),(1240,y+173+j*36)],c)
        s.device('U3',65,y+365,1065,140,[out+'− ← '+ref+' Ausgang −; keine zusätzliche GND-Brücke',out+'+ ← '+ref+' Ausgang +; S2 auf 5 V'])
        s.wire([(1740,y+281),(1770,y+281),(1770,y+479),(1130,y+479)],color)
        s.wire([(1740,y+317),(1755,y+317),(1755,y+443),(1130,y+443)],color)
        s.text(1240,y+410,'W4 · '+out+'+ / '+out+'−: ein verdrilltes Paar','small')
    s.panel(1200,'C · PIR: drei elektrische Netze über vier RJ45-Adern · KEIN LAN / PoE')
    s.device('U1',65,1300,650,120,['U6 wird auf die Uno-Buchsenleisten gesteckt.','Versorgung weiterhin über W2 an USB-B.'])
    s.device('U6',65,1500,650,260,['A0 blauer Signalstift → J1.1 (OUT)','A0 schwarzer GND-Stift → J1.2','A3 schwarzer GND-Stift → J1.4','A0 roter +V-Stift → J1.5 (+5 V)','Jumper auf 5 V; A3-Signalstift bleibt frei'])
    s.wire([(380,1420),(380,1500)])
    s.device('J1',850,1500,400,260,['1: OUT','2: GND','4: GND','5: +5 V'])
    s.box(1370,1500,370,260,'W3 · Patchkabel ≤ 3 m',['1 ↔ 1: OUT','2 ↔ 2: GND','4 ↔ 4: GND','5 ↔ 5: +5 V','1/2 und 4/5 sind Paare'])
    for j,c in enumerate(['#18836b','#556779','#556779','#bd2734']):
        s.wire([(715,1578+j*36),(850,1578+j*36)],c)
        s.wire([(1250,1578+j*36),(1370,1578+j*36)],c)
    s.device('J2',65,1860,650,260,['Sensor','1 → B1 OUT','2 → B1 GND','4 → Brücke an J2.2','5 → B1 VCC (+5 V)'])
    s.wire([(1510,1760),(1510,1800),(380,1800),(380,1860)])
    s.device('B1',1240,1860,500,260,['Vorhandener Sensor','OUT: an J2.1','GND: an J2.2','VCC: an J2.5','Pinfolge am eigenen Sensor prüfen'])
    s.wire([(715,1974),(1240,1974)],'#18836b')
    s.wire([(715,2010),(1240,2010)])
    s.wire([(715,2082),(1060,2082),(1060,2046),(1240,2046)],'#bd2734')
    s.text(780,2140,'E23/E24: vorhandene Header-Kabel; Modul-Eingänge: 2 × Adafruit #3894','small')
    s.text(65,2190,'W4-Schirm → U6 SERVO_PWR-GND; Plus dort frei. PWR_IN frei. Keine 48 V an U6/U4/U5.','small')
    s.save('docs/schaltplan-steuerung.svg')

if __name__=='__main__':
    supply();control();print('Schaltplanblätter Revision B erzeugt.')
