#!/usr/bin/env python3
"""Praktische Anschlussblätter für Revision B, ausschließlich Standardbibliothek."""
from html import escape
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DEVICES = {'U1':'Arduino Uno R3','U3':'DM860T V3.0','U4':'Adafruit MOSFET #5648','U5':'Adafruit MOSFET #5648','B1':'PIR · HC-SR501-Bauform','M1':'34HS46-6004S1','PS1':'Mean Well GST220A48-R7B','PS2':'Goobay 44952 · USB-Netzteil','S0':'CH-Mehrfachsteckdose','J1':'DFRobot FIT0849','J2':'DFRobot FIT0849'}
class Sheet:
    def __init__(self,title,h):
        self.h=h
        self.out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="{h}" viewBox="0 0 1800 {h}">', '<rect width="100%" height="100%" fill="white"/>', '<style>text{font-family:Arial,DejaVu Sans,sans-serif;fill:#152331;font-size:24px} .title{font-size:37px;font-weight:bold}.head{font-size:27px;font-weight:bold}.small{font-size:22px}</style>']
        self.text(55,65,title,'title');self.text(55,105,'04.10.2026 · Revision B · Entwurf, noch nicht aufgebaut/getestet','small')
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
    s.device('PS1',850,225,870,200,['W1: Typ-12-Stecker ↔ IEC-C13-Buchse, aus Bestand','Netzteileingang: IEC-C14','Ausgang: 48 V / 4,6 A · 4-poliger Power-DIN-R7B'])
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
    s.box(900,1270,820,185,'Vor dem Einschalten',['PS1 separat, trocken und belüftet aufstellen.','48-V-Rückleiter X2 nicht an Arduino-GND brücken.','W5-Steckerzuordnung messen; nie nach Farben raten.'])
    s.text(65,1495,'Beide AC-Klemmen akzeptieren 48 V DC nur für die hier bezeichnete U3-Version.','small')
    s.save('docs/schaltplan-versorgung.svg')

def control():
    s=Sheet('Blatt 2 · Uno direkt, fertige Signalmodule und PIR',2540)
    s.panel(140,'A · 5 V und GND verteilen · zwei separate WAGO-Klemmen · kein Anschluss-Shield')
    s.device('U1',65,230,485,230,['5V → X3.1','Erster GND nach 5V → X4.1','Zweiter GND nach 5V → J1.4','Power-Leiste: VIN bleibt frei'])
    s.box(700,230,460,270,'X3 · WAGO 221-415 · +5 V',['1 ← Uno 5V','2 → U4 V+ (rote E55-Buchse)','3 → U5 V+ (rote E55-Buchse)','4 → J1.5 (+5 V für PIR)','5: frei'])
    s.box(1250,230,490,270,'X4 · WAGO 221-415 · GND',['1 ← Uno erster Power-GND','2 → U4 GND (schwarze E55-Buchse)','3 → U5 GND (schwarze E55-Buchse)','4 → J1.2 (GND für PIR)','5 ← W4-Schirm, nur Steuerungsende'])
    s.wire([(550,308),(700,308)],'#bd2734')
    s.wire([(550,344),(610,344),(610,545),(1210,545),(1210,308),(1250,308)])
    s.text(65,590,'E24: Header-Stecker am Uno / in E55-Buchse; an WAGO nur freie abisolierte Leiter.','small')
    s.text(65,630,'X3 und X4 getrennt halten. WAGO: 11 mm abisolieren; passende Leiter, kein Metallstift.','small')
    for y,ref,pin,rail,out,color,title in [(665,'U4','D2','2','PUL','#c26311','B · STEP: D2 schaltet das Schritt-Signal'),(1165,'U5','D3','3','DIR','#7357ad','C · DIR: D3 schaltet die Richtung')]:
        s.panel(y,title)
        s.device('U1',65,y+85,470,140,[pin+' → weiße E55-Buchse','E24: Stecker/Stecker-Leitung'])
        s.device(ref,900,y+85,840,285,['STEMMA In ← '+pin+' über weiße E55-Buchse','STEMMA V+ ← X3.'+rail+' über rote E55-Buchse','STEMMA GND ← X4.'+rail+' über schwarze E55-Buchse','Ausgang + → U3 '+out+'+','Ausgang − → U3 '+out+'−'])
        s.wire([(535,y+163),(900,y+163)],color)
        s.text(565,y+145,'Signal über E24 / E55','small')
        s.text(565,y+235,'X3.'+rail+' · +5 V','small')
        s.wire([(795,y+235),(830,y+235),(830,y+199),(900,y+199)],'#bd2734')
        s.text(565,y+295,'X4.'+rail+' · GND','small')
        s.wire([(795,y+295),(850,y+295),(850,y+235),(900,y+235)])
        s.device('U3',65,y+320,690,145,[out+'+ ← '+ref+' Ausgang +; S2 auf 5 V',out+'− ← '+ref+' Ausgang −; keine GND-Brücke'])
        s.wire([(1740,y+271),(1770,y+271),(1770,y+398),(755,y+398)],color)
        s.wire([(1740,y+307),(1755,y+307),(1755,y+434),(755,y+434)],color)
        s.text(900,y+455,'W4: '+out+'+ / '+out+'− als ein verdrilltes Paar','small')
    s.panel(1670,'D · PIR: drei elektrische Netze über vier RJ45-Adern · KEIN LAN / PoE')
    s.device('U1',65,1760,640,150,['A0 → J1.1 (OUT)','Zweiter Power-GND → J1.4'])
    s.text(80,1940,'X4.4 → J1.2 · GND','small')
    s.text(80,1995,'X3.4 → J1.5 · +5 V','small')
    s.device('J1',850,1760,400,250,['1: OUT','4: GND vom Uno','2: GND von X4.4','5: +5 V von X3.4'])
    s.box(1370,1760,370,285,'W3 · Patchkabel ≤ 3 m',['1 ↔ 1: OUT','4 ↔ 4: GND','2 ↔ 2: GND','5 ↔ 5: +5 V','1/2 und 4/5 sind Paare','Alle acht Adern 1:1'])
    for j,c in enumerate(['#18836b','#556779','#556779','#bd2734']):
        if j < 2:
            s.wire([(705,1838+j*36),(850,1838+j*36)],c)
        else:
            start_y=1940 if j==2 else 1995
            s.wire([(360,start_y),(760+j*20,start_y),(760+j*20,1838+j*36),(850,1838+j*36)],c)
        s.wire([(1250,1838+j*36),(1370,1838+j*36)],c)
    s.device('J2',65,2150,650,250,['1 → B1 OUT','2 → B1 GND','4 → Brücke an J2.2','5 → B1 VCC (+5 V)'])
    s.wire([(1510,2045),(1510,2090),(380,2090),(380,2150)])
    s.device('B1',1240,2150,500,250,['Vorhandener Sensor','OUT ← J2.1','GND ← J2.2','VCC ← J2.5','Pinfolge am eigenen Sensor prüfen'])
    s.wire([(715,2228),(1240,2264)],'#18836b')
    s.wire([(715,2264),(1000,2264),(1000,2300),(1240,2300)])
    s.wire([(715,2336),(1240,2336)],'#bd2734')
    s.text(65,2450,'E23/E24 aus Bestand; 2 × E55 Adafruit #3894 unverändert lassen. Keine 48 V an X3/X4/U4/U5.','small')
    s.save('docs/schaltplan-steuerung.svg')

if __name__=='__main__':
    supply();control();print('Schaltplanblätter Revision B erzeugt.')
