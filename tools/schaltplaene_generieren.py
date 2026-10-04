#!/usr/bin/env python3
"""Praktische Anschlussblätter mit expliziten Leitungsenden; nur Standardbibliothek."""
from dataclasses import dataclass
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = {
    'U1': 'Arduino Uno R3', 'U3': 'DM860T V3.0',
    'U4': 'Adafruit MOSFET #5648', 'U5': 'Adafruit MOSFET #5648',
    'B1': 'PIR · HC-SR501-Bauform', 'M1': '34HS46-6004S1',
    'PS1': 'Mean Well GST220A48-R7B', 'PS2': 'Goobay 44952 · USB-Netzteil',
    'S0': 'CH-Mehrfachsteckdose', 'J1': 'DFRobot FIT0849', 'J2': 'DFRobot FIT0849',
    'X1': 'WAGO 221-413', 'X2': 'WAGO 221-413',
    'X3': 'WAGO 221-415', 'X4': 'WAGO 221-415',
    'W5': 'GlobTek KPPX4124641M0KPJX4(R)',
}
RED = '#bd2734'
GROUND = '#48596b'
GREEN = '#13816c'
STEP = '#c0640c'
STEP_MINUS = '#84500e'
DIR = '#7654bd'
DIR_MINUS = '#433278'


@dataclass(frozen=True)
class Pin:
    key: str
    x: int
    y: int


class Sheet:
    def __init__(self, title, h):
        self.h = h
        self.w = 2200
        self.out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{h}" viewBox="0 0 {self.w} {h}">',
            '<rect width="100%" height="100%" fill="white"/>',
            '<style>text{font-family:Arial,DejaVu Sans,sans-serif;fill:#152331;font-size:24px}'
            '.title{font-size:36px;font-weight:bold}.head{font-size:28px;font-weight:bold}'
            '.small{font-size:22px}.note{font-size:20px}.pinlabel{font-size:22px;font-weight:bold}</style>',
        ]
        self.text(60, 60, title, 'title')
        self.text(60, 100, '04.10.2026 · Revision B · Entwurf, noch nicht aufgebaut/getestet', 'small')
        self.text(60, 136, 'Jede Linie endet an einem beschrifteten Anschluss. Gleiche Geräte-Nummer = dasselbe Gerät.', 'small')

    def text(self, x, y, value, cls='', anchor='start', size=None):
        style = f' style="font-size:{size}px"' if size else ''
        self.out.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{style}>{escape(value)}</text>')

    def box(self, x, y, w, h, title, fill='#f4f7fa'):
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#354b60" stroke-width="2"/>')
        size = min(26, int((w - 32) / (max(1, len(title)) * .56)))
        self.text(x + 16, y + 38, title, 'head', size=size)
        return x, y, w, h

    def device(self, ref, x, y, w, h):
        return self.box(x, y, w, h, ref + ' · ' + DEVICES[ref])

    def pin(self, box, ref, name, side, position, label=None):
        x, y, w, h = box
        if side == 'left':
            px, py = x, position
            tx, ty, anchor = x + 17, py - 12, 'start'
        elif side == 'right':
            px, py = x + w, position
            tx, ty, anchor = x + w - 17, py - 12, 'end'
        elif side == 'top':
            px, py = position, y
            tx, ty, anchor = px + 14, py - 13, 'start'
        else:
            px, py = position, y + h
            tx, ty, anchor = px, py - 15, 'middle'
        key = ref + '.' + name
        self.out.append(f'<g data-pin="{escape(key)}" data-x="{px}" data-y="{py}">')
        self.text(tx, ty, label if label is not None else name, 'pinlabel', anchor)
        self.out.append(f'<circle cx="{px}" cy="{py}" r="7" fill="white" stroke="#152331" stroke-width="3"/>')
        self.out.append('</g>')
        return Pin(key, px, py)

    def line(self, points, color=GROUND, width=4, attrs=''):
        self.out.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in points)
                        + f'" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" {attrs}/>')

    def connect(self, start, end, color=GROUND, via=(), kind='wire', label=None):
        points = [(start.x, start.y), *via, (end.x, end.y)]
        attrs = f'data-from="{escape(start.key)}" data-to="{escape(end.key)}" data-kind="{kind}"'
        self.line(points, color, 4 if kind != 'plug' else 7, attrs)
        if label:
            self.text(*label[:2], label[2], 'note')

    def dot(self, x, y, color=GROUND):
        self.out.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/>')

    def panel(self, y, title):
        self.line([(60, y), (2140, y)], '#c3ced8', 2)
        self.text(60, y + 44, title, 'head')

    def wago(self, ref, x, y, w, h, ports, rail):
        box = self.device(ref, x, y, w, h)
        self.text(x + 16, y + 72, rail, 'small')
        pins = {str(number): self.pin(box, ref, str(number), side, py, str(number))
                for number, side, py in ports}
        bus_x = x + w // 2
        ys = [p.y for p in pins.values()]
        self.line([(bus_x, min(ys)), (bus_x, max(ys))], '#697889', 6)
        for p in pins.values():
            self.line([(p.x, p.y), (bus_x, p.y)], '#697889', 3)
            self.dot(bus_x, p.y)
        self.text(x + 16, y + h - 20, 'Alle Plätze intern verbunden', 'note')
        return pins

    def save(self, path):
        self.text(60, self.h - 68, 'Anschlussdarstellung, keine maßstäbliche Geräteansicht. WAGO-Plätze von links nach rechts selbst nummerieren.', 'note')
        self.text(60, self.h - 32, 'Nur spannungslos verdrahten · Vollständige Aufbaufolge und Einstellungen: docs/elektronik.md', 'note')
        (ROOT / path).write_text('\n'.join(self.out + ['</svg>']) + '\n', encoding='utf-8')


def supply():
    s = Sheet('Blatt 1 · Netzanschlüsse, 48-V-Versorgung und Motor', 3170)
    s.panel(170, 'A · Fertige Stecker und Kabel verbinden')
    wall_box = s.box(70, 250, 470, 145, 'Schweizer Wandsteckdose')
    wall = s.pin(wall_box, 'Haus', 'Typ13', 'bottom', 305, 'Typ 13 · 230 V')
    strip_box = s.device('S0', 70, 500, 470, 330)
    strip_in = s.pin(strip_box, 'S0', 'Netzstecker', 'top', 305)
    slot1 = s.pin(strip_box, 'S0', 'Steckplatz1', 'right', 620, 'Steckplatz 1 · 230 V')
    slot2 = s.pin(strip_box, 'S0', 'Steckplatz2', 'right', 770, 'Steckplatz 2 · 230 V')
    s.connect(wall, strip_in, kind='plug')
    s.text(340, 458, 'Leiste einstecken', 'note')
    ps1 = s.device('PS1', 1350, 500, 790, 330)
    ps1_ac = s.pin(ps1, 'PS1', 'IEC-C14', 'left', 620, 'IEC-C14-Netzeingang')
    s.connect(slot1, ps1_ac, '#8a5c36', kind='plug', label=(640, 594, 'W1 · fertiges CH-Stecker / IEC-C13-Kabel aus Bestand'))
    s.text(1366, 715, 'Geschlossenes Netzteil · 48 V / 4,6 A', 'small')
    s.text(1366, 760, '48-V-Ausgang: Anschlussbereich B unten', 'note')
    ps2 = s.device('PS2', 1350, 925, 790, 260)
    ps2_ac = s.pin(ps2, 'PS2', 'Netzstecker', 'left', 1035, 'Euro-Netzstecker · 230 V')
    ps2_usb = s.pin(ps2, 'PS2', 'USB-A', 'left', 1140, 'USB-A-Buchse · 5 V')
    s.connect(slot2, ps2_ac, '#8a5c36', via=[(1100, 770), (1100, 1035)], kind='plug')
    s.text(650, 813, 'PS2 direkt in Steckplatz 2 einstecken', 'note')
    uno = s.device('U1', 70, 925, 470, 260)
    uno_usb = s.pin(uno, 'U1', 'USB-B', 'right', 1140, 'USB-B-Buchse')
    s.connect(ps2_usb, uno_usb, RED, kind='plug', label=(640, 1112, 'W2 · vorhandenes USB-A/B-Kabel, ca. 2 m'))
    s.text(86, 1010, 'Versorgung über USB', 'note')
    s.text(86, 1050, '5-V-Anschlüsse: Blatt 2', 'note')

    s.panel(1250, 'B · Vier identifizierte 48-V-Adern und vier Motoradern einzeln anschließen')
    ps1_dc_box = s.device('PS1', 70, 1360, 660, 215)
    ps1_dc = s.pin(ps1_dc_box, 'PS1', 'Power-DIN', 'right', 1480, '4-poliger Power-DIN-Stecker')
    s.text(86, 1535, 'Originalkabel unverändert lassen', 'note')
    extension = s.device('W5', 890, 1360, 590, 900)
    ext_in = s.pin(extension, 'W5', 'Power-DIN-Buchse', 'left', 1480, 'Power-DIN-Buchse')
    s.connect(ps1_dc, ext_in, RED, kind='plug', label=(744, 1444, 'einstecken'))
    s.text(906, 1542, 'Nur das andere, männliche Ende abschneiden.', 'note')
    pos_a = s.pin(extension, 'W5', '+48V_A', 'right', 1640, 'Identifizierte Ader +48 V · A')
    pos_b = s.pin(extension, 'W5', '+48V_B', 'right', 1720, 'Identifizierte Ader +48 V · B')
    neg_a = s.pin(extension, 'W5', 'Rueckleiter_A', 'right', 1990, 'Identifizierte Rückleiter-Ader · A')
    neg_b = s.pin(extension, 'W5', 'Rueckleiter_B', 'right', 2070, 'Identifizierte Rückleiter-Ader · B')
    s.text(906, 2180, 'Adern durchmessen; Farben sind nicht festgelegt.', 'note')
    s.text(906, 2220, 'Schirm am abgeschnittenen Ende einzeln isolieren.', 'note')
    x1 = s.wago('X1', 1660, 1510, 480, 340,
                [(1, 'left', 1640), (2, 'left', 1720), (3, 'right', 1790)], '+48 V · drei Klemmplätze')
    x2 = s.wago('X2', 1660, 1860, 480, 380,
                [(1, 'left', 1990), (2, 'left', 2070), (3, 'right', 2160)], '48-V-Rückleiter · drei Klemmplätze')
    for src, dst, color in [(pos_a, x1['1'], RED), (pos_b, x1['2'], RED),
                            (neg_a, x2['1'], GROUND), (neg_b, x2['2'], GROUND)]:
        s.connect(src, dst, color)

    # Kontaktansicht am unveränderten Netzteilstecker; keine GlobTek-Pinnummern übernehmen.
    sketch = s.box(70, 1740, 660, 520, 'Kontaktseite: PS1-Netzteilstecker')
    s.text(400, 1834, 'Führungsnase oben', 'small', 'middle')
    s.out.append('<circle cx="400" cy="2015" r="140" fill="white" stroke="#354b60" stroke-width="3"/>')
    s.out.append('<rect x="378" y="1865" width="44" height="26" fill="#354b60"/>')
    for x, y, color in [(340, 1960, GROUND), (460, 1960, GROUND), (340, 2070, RED), (460, 2070, RED)]:
        s.out.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{color}"/>')
    s.text(400, 1918, 'beide oben: Rückleiter', 'note', 'middle')
    s.text(400, 2133, 'beide unten: +48 V', 'note', 'middle')
    s.text(86, 2206, 'Gegenstecker ist gespiegelt. W5-Zuordnung messen.', 'note')

    driver = s.device('U3', 1660, 2430, 480, 590)
    ac1 = s.pin(driver, 'U3', 'AC1', 'top', 1750, 'AC · 1. Klemme')
    ac2 = s.pin(driver, 'U3', 'AC2', 'top', 1950, 'AC · 2. Klemme')
    s.connect(x1['3'], ac1, RED, via=[(2170, 1790), (2170, 2330), (1750, 2330)])
    s.connect(x2['3'], ac2, GROUND, via=[(2195, 2160), (2195, 2365), (1950, 2365)])
    s.text(905, 2332, 'X1/X2 → Treiber: je kurze 1,5-mm²-Leitung', 'note')
    motor = s.device('M1', 70, 2510, 890, 440)
    s.text(86, 2590, 'Motorlieferkabel · 1 m', 'small')
    for color_name, pin_name, py, color in [('schwarz', 'A+', 2650, '#18212c'),
                                           ('grün', 'A-', 2730, '#138b44'),
                                           ('rot', 'B+', 2810, RED),
                                           ('blau', 'B-', 2890, '#286fca')]:
        mp = s.pin(motor, 'M1', color_name, 'right', py, color_name.capitalize() + 'e Motorader')
        dp = s.pin(driver, 'U3', pin_name, 'left', py, pin_name.replace('-', '−'))
        s.connect(mp, dp, color)
    s.text(1676, 2970, 'Signalanschlüsse: Blatt 2', 'note')
    s.text(70, 3044, 'X2 (48-V-Rückleiter) nicht mit Arduino-GND verbinden. Motorwicklungen vor Anschluss durchmessen.', 'small')
    s.save('docs/schaltplan-versorgung.svg')


def distribution(s, y, ref, source_name, source_label, color, outputs):
    s.panel(y, 'A · 5 V verteilen' if ref == 'X3' else 'B · Masse (GND) verteilen')
    uno = s.device('U1', 70, y + 110, 470, 230)
    source = s.pin(uno, 'U1', source_name, 'right', y + 210, source_label)
    s.text(86, y + 297, 'Buchsen der Power-Leiste verwenden', 'note')
    if ref == 'X4':
        s.text(86, y + 329, 'GND direkt neben der 5V-Buchse', 'note')
    ports = [(1, 'left', y + 210)] + [(i, 'right', y + 210 + (i - 2) * 130) for i in range(2, 6)]
    pins = s.wago(ref, 740, y + 90, 470, 660, ports, '+5 V' if ref == 'X3' else 'Signal-GND / Masse')
    s.connect(source, pins['1'], color)
    for index, (dest_ref, dest_pin, label) in enumerate(outputs, 2):
        py = y + 210 + (index - 2) * 130
        if dest_ref == 'W4':
            box = s.box(1440, py - 90, 700, 115, 'W4 · Steuerkabel zum Motortreiber')
        else:
            box = s.device(dest_ref, 1440, py - 90, 700, 115)
        target = s.pin(box, dest_ref, dest_pin, 'left', py, label)
        s.connect(pins[str(index)], target, color)
        if dest_ref == 'W4':
            s.text(1456, py + 65, 'Anderes Schirmende am Treiber: isolieren, nicht anschließen.', 'note')
    if ref == 'X3':
        s.text(1250, pins['5'].y + 8, 'Platz 5 bleibt frei', 'note')
    s.text(70, y + 797, 'In WAGO nur abisolierte Leiter klemmen. Header-Kabel aus Bestand; STEMMA-Kabel #3894 gesteckt lassen.', 'note')


def control():
    s = Sheet('Blatt 2 · Arduino, Signalmodule und PIR: Anschluss für Anschluss', 3540)
    distribution(s, 175, 'X3', '5V', '5V', RED,
                 [('U4', 'V+', 'V+ · rote Leitung am STEMMA-Kabel'),
                  ('U5', 'V+', 'V+ · rote Leitung am STEMMA-Kabel'),
                  ('J1', '5', 'Schraubklemme 5 · PIR-Versorgung')])
    distribution(s, 1035, 'X4', 'GND1', 'GND · erster Anschluss nach 5V', GROUND,
                 [('U4', 'GND', 'GND · schwarze Leitung am STEMMA-Kabel'),
                  ('U5', 'GND', 'GND · schwarze Leitung am STEMMA-Kabel'),
                  ('J1', '2', 'Schraubklemme 2 · Sensor-Masse'),
                  ('W4', 'Schirm', 'Schirm / Beidraht am Steuerungsende')])

    s.panel(1895, 'C · Schritt-Signal (STEP) und Drehrichtung (DIR)')
    uno = s.device('U1', 70, 1995, 470, 425)
    d2 = s.pin(uno, 'U1', 'D2', 'right', 2105)
    d3 = s.pin(uno, 'U1', 'D3', 'right', 2325)
    s.text(86, 2400, 'Zwei Stecker/Stecker-Kabel aus Bestand', 'note')
    driver = s.device('U3', 1710, 1995, 430, 510)
    s.text(1726, 2420, 'S2-Schalter auf 5 V', 'small')
    s.text(1726, 2467, 'ENA / ALM / BRK bleiben frei', 'note')
    for ref, pin, yy, prefix, c1, c2 in [('U4', d2, 1995, 'PUL', STEP, STEP_MINUS),
                                       ('U5', d3, 2215, 'DIR', DIR, DIR_MINUS)]:
        mod = s.device(ref, 740, yy, 640, 205)
        inp = s.pin(mod, ref, 'In', 'left', yy + 110, 'In · weiße STEMMA-Leitung')
        plus = s.pin(mod, ref, 'Out+', 'right', yy + 85, '+ · Ausgangsklemme')
        minus = s.pin(mod, ref, 'Out-', 'right', yy + 155, '− · Ausgangsklemme')
        dp = s.pin(driver, 'U3', prefix + '+', 'left', yy + 85)
        dm = s.pin(driver, 'U3', prefix + '-', 'left', yy + 155, prefix + '−')
        s.connect(pin, inp, c1)
        s.connect(plus, dp, c1)
        s.connect(minus, dm, c2)
        s.text(1410, yy + 49, 'W4 · ' + ('Paar 1' if ref == 'U4' else 'Paar 2'), 'note')
    s.text(70, 2550, 'Versorgung der Module: Bereiche A und B. Die Ausgangsklemme „−“ nur mit PUL− bzw. DIR− verbinden.', 'note')

    s.panel(2600, 'D · PIR-Sensor und RJ45-Patchkabel · Kein Anschluss an LAN oder PoE')
    # Reihen sind Anschlussausschnitte, keine behauptete physische Pinreihenfolge.
    uno = s.device('U1', 70, 2695, 410, 235)
    a0 = s.pin(uno, 'U1', 'A0', 'right', 2780)
    gnd2 = s.pin(uno, 'U1', 'GND2', 'right', 2870, 'GND · zweiter Anschluss nach 5V')
    x4 = s.device('X4', 70, 2995, 410, 120)
    x4_4 = s.pin(x4, 'X4', '4', 'right', 3080, 'Klemmplatz 4')
    x3 = s.device('X3', 70, 3190, 410, 120)
    x3_4 = s.pin(x3, 'X3', '4', 'right', 3275, 'Klemmplatz 4')
    j1 = s.device('J1', 690, 2670, 300, 690)
    j2 = s.device('J2', 1260, 2670, 300, 690)
    s.text(706, 2740, 'Klemme', 'note'); s.text(974, 2740, 'RJ45', 'note', 'end')
    s.text(1276, 2740, 'RJ45', 'note'); s.text(1544, 2740, 'Klemme', 'note', 'end')
    s.text(1057, 2718, 'W3 · Patchkabel', 'note')
    s.text(1057, 2751, 'bis 3 m · 1:1', 'note')
    b1 = s.device('B1', 1750, 2695, 390, 665)
    s.text(1766, 2980, 'OUT / GND / VCC:', 'note')
    s.text(1766, 3015, 'Pinfolge am Sensor prüfen', 'note')
    sensor = {name: s.pin(b1, 'B1', name, 'left', py, label)
              for name, py, label in [('OUT', 2780, 'OUT · Bewegungssignal'),
                                       ('GND', 3080, 'GND · Masse'),
                                       ('VCC', 3275, 'VCC · +5 V')]}
    terminal2 = {}
    sources = {1: a0, 4: gnd2, 2: x4_4, 5: x3_4}
    for num, py, color in [(1, 2780, GREEN), (4, 2870, GROUND), (2, 3080, GROUND), (5, 3275, RED)]:
        t1 = s.pin(j1, 'J1', str(num), 'left', py)
        r1 = s.pin(j1, 'J1', 'RJ45.' + str(num), 'right', py, str(num))
        r2 = s.pin(j2, 'J2', 'RJ45.' + str(num), 'left', py, str(num))
        t2 = s.pin(j2, 'J2', str(num), 'right', py)
        terminal2[num] = t2
        s.connect(sources[num], t1, color)
        s.connect(t1, r1, '#8c9aaa', kind='internal')
        s.connect(r1, r2, color, kind='patch')
        s.connect(r2, t2, '#8c9aaa', kind='internal')
    s.connect(terminal2[1], sensor['OUT'], GREEN)
    s.connect(terminal2[2], sensor['GND'], GROUND)
    s.connect(terminal2[5], sensor['VCC'], RED)
    s.connect(terminal2[4], terminal2[2], GROUND, via=[(1650, 2870), (1650, 3080)])
    s.dot(1650, 3080)
    s.text(1585, 2980, 'Brücke', 'note')
    s.text(706, 3325, '3 / 6 / 7 / 8: frei', 'note')
    s.text(1276, 3325, '3 / 6 / 7 / 8: frei', 'note')
    s.text(70, 3420, 'An J2 sind Klemme 4 und 2 verbunden; Klemme 2 führt zusätzlich zum Sensor-GND. X3/X4 bekommen niemals 48 V.', 'note')
    s.save('docs/schaltplan-steuerung.svg')


if __name__ == '__main__':
    supply()
    control()
    print('Schaltplanblätter Revision B mit expliziten Anschlüssen erzeugt.')
