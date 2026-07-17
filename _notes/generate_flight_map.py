#!/usr/bin/env python3
"""Generate the direct-flight route map for the Transportation page.

Usage:
    python3 _notes/generate_flight_map.py <ne_110m_land.geojson> <output.svg>

- World map: Natural Earth 110m land (public domain), equirectangular
  projection centred on 150E so Australia sits mid-frame.
- Routes: great-circle arcs from each non-stop origin to Melbourne.
  Solid = year-round; dashed = seasonal / launching late 2026.
- Update the CITIES/SPECIAL lists below when routes change (keep in sync
  with _pages/transportation.md and _notes/transportation-sources.md).
"""
import json
import math
import sys

CENTER_LON = 150.0          # map centre (deg E)
LAT_TOP, LAT_BOT = 75.0, -57.0
W = 1000.0                  # SVG width
H = (LAT_TOP - LAT_BOT) / 360.0 * W

MEL = ("Melbourne", -37.67, 144.84)

# (name, lat, lon, airlines, label_anchor or None, label_dx, label_dy)
CITIES = [
    ("Beijing", 39.90, 116.40, "Air China", "end", -6, -2),
    ("Shanghai", 31.23, 121.47, "China Eastern Airlines, Juneyao Air", "start", 6, 2),
    ("Guangzhou", 23.13, 113.26, "China Southern Airlines", None, 0, 0),
    ("Shenzhen", 22.54, 114.06, "Shenzhen Airlines", None, 0, 0),
    ("Chengdu", 30.57, 104.07, "Sichuan Airlines", "end", -6, -2),
    ("Xiamen", 24.48, 118.09, "Xiamen Airlines", None, 0, 0),
    ("Hangzhou", 30.27, 120.16, "Beijing Capital Airlines", None, 0, 0),
    ("Qingdao", 36.07, 120.38, "Beijing Capital Airlines", None, 0, 0),
    ("Nanjing", 32.06, 118.80, "China Eastern Airlines", None, 0, 0),
    ("Haikou", 20.04, 110.34, "Hainan Airlines", None, 0, 0),
    ("Hong Kong", 22.31, 113.92, "Cathay Pacific, Qantas", None, 0, 0),
    ("Taipei", 25.08, 121.23, "China Airlines", "start", 6, 2),
    ("Tokyo (Narita)", 35.77, 140.39, "Japan Airlines, Qantas", "start", 7, 0),
    ("Singapore", 1.36, 103.99, "Singapore Airlines, Qantas, Jetstar, Scoot", "start", 7, 3),
    ("Kuala Lumpur", 2.75, 101.71, "Malaysia Airlines, AirAsia X", "end", -6, 0),
    ("Bangkok", 13.69, 100.75, "Thai Airways, Jetstar", "end", -6, -2),
    ("Ho Chi Minh City", 10.82, 106.65, "Vietnam Airlines, Vietjet Air, Jetstar", None, 0, 0),
    ("Hanoi", 21.22, 105.81, "Vietnam Airlines", None, 0, 0),
    ("Jakarta", -6.13, 106.66, "Garuda Indonesia", "end", -6, 2),
    ("Denpasar (Bali)", -8.75, 115.17, "Jetstar, Qantas, Virgin Australia, Garuda Indonesia, Batik Air", None, 0, 0),
    ("Manila", 14.51, 121.02, "Philippine Airlines, Cebu Pacific", "start", 7, 0),
    ("Bandar Seri Begawan", 4.94, 114.93, "Royal Brunei Airlines", None, 0, 0),
    ("Delhi", 28.56, 77.10, "Air India; Qantas (seasonal)", "end", -7, 0),
    ("Colombo", 7.18, 79.88, "SriLankan Airlines, Jetstar", "end", -7, 2),
    ("Doha", 25.27, 51.61, "Qatar Airways", "end", -7, -2),
    ("Dubai", 25.25, 55.36, "Emirates", "start", 6, 6),
    ("Abu Dhabi", 24.43, 54.65, "Etihad Airways", None, 0, 0),
    ("Los Angeles", 33.94, -118.41, "Qantas, United Airlines, Delta Air Lines", "start", 7, 0),
    ("San Francisco", 37.62, -122.38, "United Airlines", "end", -7, -3),
    ("Dallas/Fort Worth", 32.90, -97.04, "Qantas", "start", 4, 13),
    ("Auckland", -37.01, 174.79, "Air New Zealand, Qantas, Jetstar", "start", 7, 0),
    ("Christchurch", -43.49, 172.53, "Air New Zealand, Qantas, Jetstar", None, 0, 0),
    ("Wellington", -41.33, 174.81, "Air New Zealand, Qantas", None, 0, 0),
    ("Queenstown", -45.02, 168.74, "Air New Zealand, Qantas, Jetstar, Virgin Australia", None, 0, 0),
    ("Nadi (Fiji)", -17.76, 177.44, "Fiji Airways, Virgin Australia, Jetstar", "start", 7, 0),
    ("Santiago de Chile", -33.39, -70.79, "LATAM Airlines", "end", -7, -3),
]

# dashed: seasonal or launching before the conference
SPECIAL = [
    ("Seoul (Incheon)", 37.46, 126.44, "Asiana Airlines — seasonal, approx. late Oct to Mar", "start", 8, -12),
    ("London (Heathrow)", 51.47, -0.45, "Qantas — from late October 2026", "start", 7, 0),
]


def shift_lon(lon):
    x = lon - CENTER_LON
    while x < -180.0:
        x += 360.0
    while x > 180.0:
        x -= 360.0
    return x


def px(lon_s, lat):
    return ((lon_s + 180.0) / 360.0 * W, (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * H)


def clip_poly(pts, edge):
    """Sutherland-Hodgman against one edge: ('x>=',v) ('x<=',v) ('y>=',v) ('y<=',v)."""
    kind, v = edge
    def inside(p):
        if kind == 'x>=':
            return p[0] >= v
        if kind == 'x<=':
            return p[0] <= v
        if kind == 'y>=':
            return p[1] >= v
        return p[1] <= v
    def intersect(a, b):
        ax, ay = a
        bx, by = b
        if kind.startswith('x'):
            t = (v - ax) / (bx - ax)
            return (v, ay + t * (by - ay))
        t = (v - ay) / (by - ay)
        return (ax + t * (bx - ax), v)
    out = []
    n = len(pts)
    for i in range(n):
        cur, prev = pts[i], pts[i - 1]
        if inside(cur):
            if not inside(prev):
                out.append(intersect(prev, cur))
            out.append(cur)
        elif inside(prev):
            out.append(intersect(prev, cur))
    return out


def clip_rect(pts):
    for e in (('x>=', -180.0), ('x<=', 180.0), ('y>=', LAT_BOT), ('y<=', LAT_TOP)):
        pts = clip_poly(pts, e)
        if len(pts) < 3:
            return []
    return pts


def ring_to_paths(ring):
    """Continuously shift ring lons, then clip 3 translated copies to frame."""
    pts = []
    prev = None
    for lon, lat in ring:
        x = shift_lon(lon)
        if prev is not None:
            while x - prev > 180.0:
                x -= 360.0
            while x - prev < -180.0:
                x += 360.0
        pts.append((x, lat))
        prev = x
    paths = []
    for dx in (-360.0, 0.0, 360.0):
        clipped = clip_rect([(x + dx, y) for x, y in pts])
        if clipped:
            paths.append(clipped)
    return paths


def gc_arc(a, b, n=72):
    """Great-circle points from (lat,lon) a to b."""
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    v1 = (math.cos(la1) * math.cos(lo1), math.cos(la1) * math.sin(lo1), math.sin(la1))
    v2 = (math.cos(la2) * math.cos(lo2), math.cos(la2) * math.sin(lo2), math.sin(la2))
    dot = max(-1.0, min(1.0, sum(p * q for p, q in zip(v1, v2))))
    ang = math.acos(dot)
    pts = []
    for i in range(n + 1):
        t = i / n
        if ang < 1e-9:
            v = v1
        else:
            f1 = math.sin((1 - t) * ang) / math.sin(ang)
            f2 = math.sin(t * ang) / math.sin(ang)
            v = tuple(f1 * p + f2 * q for p, q in zip(v1, v2))
        lat = math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))
        lon = math.degrees(math.atan2(v[1], v[0]))
        pts.append((lat, lon))
    return pts


def stylized_arc(dest, dip, n=72):
    """Aesthetic southern arc (sine dip) for routes whose true great circle
    would leave the frame (e.g. Santiago, GC min lat ~ -67)."""
    la1, lo1 = MEL[1], shift_lon(MEL[2])
    la2, lo2 = dest[0], shift_lon(dest[1])
    while lo2 - lo1 > 180.0:
        lo2 -= 360.0
    while lo2 - lo1 < -180.0:
        lo2 += 360.0
    pts = []
    for i in range(n + 1):
        t = i / n
        lat = (1 - t) * la1 + t * la2 - dip * math.sin(math.pi * t)
        lon = (1 - t) * lo1 + t * lo2
        pts.append((lat, lon))
    d = []
    for i, (lat, lon) in enumerate(pts):
        X, Y = px(lon, lat)
        d.append(('M' if i == 0 else 'L') + f'{X:.1f},{Y:.1f}')
    return ' '.join(d)


# routes drawn stylized instead of true great-circle: name -> southward dip (deg)
STYLIZED = {"Santiago de Chile": 17.0}


def arc_path(dest, name=None):
    """SVG path for Melbourne->dest great circle, continuous across frame."""
    if name in STYLIZED:
        return stylized_arc(dest, STYLIZED[name])
    pts = gc_arc((MEL[1], MEL[2]), (dest[0], dest[1]))
    xs = []
    prev = None
    for lat, lon in pts:
        x = shift_lon(lon)
        if prev is not None:
            while x - prev > 180.0:
                x -= 360.0
            while x - prev < -180.0:
                x += 360.0
        xs.append((x, lat))
        prev = x
    d = []
    for i, (x, lat) in enumerate(xs):
        X, Y = px(x, lat)
        d.append(('M' if i == 0 else 'L') + f'{X:.1f},{Y:.1f}')
    return ' '.join(d)


def main():
    geo_path, out_path = sys.argv[1], sys.argv[2]
    with open(geo_path) as f:
        geo = json.load(f)

    land_d = []
    for feat in geo['features']:
        g = feat['geometry']
        polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
        for poly in polys:
            for ring in poly:
                for piece in ring_to_paths(ring):
                    seg = []
                    for i, (x, y) in enumerate(piece):
                        X, Y = px(x, y)
                        seg.append(('M' if i == 0 else 'L') + f'{X:.1f},{Y:.1f}')
                    land_d.append(' '.join(seg) + ' Z')

    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
             f'font-family="Helvetica,Arial,sans-serif" role="img" '
             f'aria-label="Map of non-stop flight routes to Melbourne">')
    s.append('<title>Non-stop flight routes to Melbourne</title>')
    s.append(f'<rect width="{W:.0f}" height="{H:.0f}" fill="#eef4f9"/>')
    s.append('<path d="' + ' '.join(land_d) +
             '" fill="#ccd9e4" stroke="#a9bfd0" stroke-width="0.5" fill-rule="evenodd"/>')

    # routes
    s.append('<g fill="none" stroke="#b7332f" stroke-width="1.3" opacity="0.75">')
    for c in CITIES:
        s.append(f'<path d="{arc_path((c[1], c[2]), c[0])}"><title>Melbourne – {c[0]}: {c[3]}</title></path>')
    s.append('</g>')
    s.append('<g fill="none" stroke="#b7332f" stroke-width="1.3" opacity="0.75" stroke-dasharray="6,4">')
    for c in SPECIAL:
        s.append(f'<path d="{arc_path((c[1], c[2]), c[0])}"><title>Melbourne – {c[0]}: {c[3]}</title></path>')
    s.append('</g>')

    # city dots + labels
    s.append('<g>')
    for c in CITIES + SPECIAL:
        x, y = px(shift_lon(c[2]), c[1])
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#1f3b5b" stroke="#ffffff" '
                 f'stroke-width="0.9"><title>{c[0]}: {c[3]}</title></circle>')
        if c[4]:
            s.append(f'<text x="{x + c[5]:.1f}" y="{y + c[6] + 3:.1f}" text-anchor="{c[4]}" '
                     f'font-size="10.5" fill="#1f3b5b">{c[0]}</text>')
    s.append('</g>')

    # Melbourne
    mx, my = px(shift_lon(MEL[2]), MEL[1])
    s.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="5.5" fill="#c8102e" stroke="#ffffff" stroke-width="1.6">'
             f'<title>Melbourne (MEL)</title></circle>')
    s.append(f'<text x="{mx - 12:.1f}" y="{my + 16:.1f}" text-anchor="end" font-size="13" '
             f'font-weight="bold" fill="#c8102e">MELBOURNE</text>')

    # legend
    lx, ly = 18.0, H - 52.0
    s.append(f'<g font-size="11" fill="#1f3b5b">')
    s.append(f'<rect x="{lx - 8:.0f}" y="{ly - 16:.0f}" width="240" height="46" rx="4" '
             f'fill="#ffffff" opacity="0.85" stroke="#a9bfd0" stroke-width="0.5"/>')
    s.append(f'<line x1="{lx:.0f}" y1="{ly - 3:.0f}" x2="{lx + 34:.0f}" y2="{ly - 3:.0f}" '
             f'stroke="#b7332f" stroke-width="1.6"/>')
    s.append(f'<text x="{lx + 42:.0f}" y="{ly:.0f}">Non-stop, year-round</text>')
    s.append(f'<line x1="{lx:.0f}" y1="{ly + 15:.0f}" x2="{lx + 34:.0f}" y2="{ly + 15:.0f}" '
             f'stroke="#b7332f" stroke-width="1.6" stroke-dasharray="6,4"/>')
    s.append(f'<text x="{lx + 42:.0f}" y="{ly + 18:.0f}">Seasonal / from late 2026</text>')
    s.append('</g>')

    s.append(f'<text x="{W - 8:.0f}" y="{H - 6:.0f}" text-anchor="end" font-size="8.5" '
             f'fill="#8296ab">Map data: Natural Earth (public domain) · Routes as of July 2026</text>')
    s.append('</svg>')

    with open(out_path, 'w') as f:
        f.write('\n'.join(s))
    print(f'wrote {out_path} ({len("".join(s)) // 1024} KB)')


if __name__ == '__main__':
    main()
