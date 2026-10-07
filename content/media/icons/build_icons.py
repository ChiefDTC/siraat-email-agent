"""Siraat line-icon set. 24px grid, 1.75 stroke, round caps and joins.
Run: python3 build_icons.py  (writes svg/<color>/<name>.svg), then node render_icons.js for PNGs."""
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))
COLORS = {"brick": "#AC3B19", "ink": "#282828"}

def star(cx, cy, ro, ri, n=5):
    pts = []
    for i in range(n * 2):
        r = ro if i % 2 == 0 else ri
        a = -math.pi / 2 + i * math.pi / n
        pts.append(f"{cx + r*math.cos(a):.2f} {cy + r*math.sin(a):.2f}")
    return "M" + "L".join(pts) + "Z"

def P(d, extra=""):
    return f'<path d="{d}"{extra}/>'
def C(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'

ICONS = {
 "no-duties": [C(12,12,9.25), P("M2.75 12h18.5"), P("M12 2.75c2.5 2.6 3.75 5.7 3.75 9.25S14.5 18.65 12 21.25"), P("M12 2.75C9.5 5.35 8.25 8.45 8.25 12S9.5 18.65 12 21.25")],
 "deadline": [C(12,13,8.25), P("M12 8.75V13l2.75 1.75"), P("M9.5 2.75h5"), P("M12 2.75v2")],
 "discount-tag": [P("M3.75 4.75v6.6a1 1 0 0 0 .3.7l8.4 8.4a1 1 0 0 0 1.4 0l6.6-6.6a1 1 0 0 0 0-1.4l-8.4-8.4a1 1 0 0 0-.7-.3h-6.6a1 1 0 0 0-1 1z"), C(7.75,8.25,1.25), P("m10.5 15.5 5-5")],
 "free-shipping": [P("M5 17.25H2.75V6.75a1 1 0 0 1 1-1h9.5a1 1 0 0 1 1 1v10.5"), P("M9 17.25h6.5"),
                   P("M14.25 9.25h3.45a1 1 0 0 1 .8.4l2.3 3.05a1 1 0 0 1 .2.6v3.95H19.5"), C(7,17.25,2), C(17.5,17.25,2)],
 "returns-30-day": [P("M3.5 12a8.5 8.5 0 1 0 2.5-6L3.5 8.5"), P("M3.5 3.5v5h5"), P("m10.25 9.25-2.5 2.5 2.5 2.5"), P("M7.75 11.75h5.5a2.5 2.5 0 0 1 0 5H12")],
 "warranty-75-year": [P("M12 2.75 4.75 5.5v5.75c0 4.6 3.05 8.4 7.25 9.75 4.2-1.35 7.25-5.15 7.25-9.75V5.5z"),
                      P("m8.75 12 2.25 2.25 4.5-4.5")],
 "pfas-tested": [P("M9.25 2.75h5.5"), P("M10 2.75v6.1L4.6 18.2a2 2 0 0 0 1.73 3.05h11.34a2 2 0 0 0 1.73-3.05L14 8.85V2.75"),
                 P("M7.1 14.25h9.8"), P("M10.5 17.5h.01"), P("M13.5 18.25h.01")],
 "no-coating": [C(10,12,7.25), C(10,12,4.25), P("M17.25 12h4"), P("M8.75 11h.01"), P("M11.25 10.5h.01"), P("M10 13.25h.01")],
 "metal-utensil-safe": [f'<g transform="rotate(40 12 12)">' + P("M8.5 1.75h7a1 1 0 0 1 1 1v7.5a2 2 0 0 1-2 2h-5a2 2 0 0 1-2-2v-7.5a1 1 0 0 1 1-1z")
                        + P("M10.75 4.5v5") + P("M13.25 4.5v5") + P("M12 12.25v10") + '</g>'],
 "dishwasher-safe": [P("M4.75 2.75h14.5a1 1 0 0 1 1 1v16.5a1 1 0 0 1-1 1H4.75a1 1 0 0 1-1-1V3.75a1 1 0 0 1 1-1z"),
                     P("M3.75 7.25h16.5"), P("M7 5h.01"), P("M9.5 5h.01"), C(12,14.25,4.25),
                     P("M9.5 14.75c.85-.65 1.65-.65 2.5 0s1.65.65 2.5 0")],
 "induction-ready": [P("M3 8.75h18"), P("M4 14c1.25-2.5 2.75-2.5 4 0s2.75 2.5 4 0 2.75-2.5 4 0 2.75 2.5 4 0"), P("M3 19.25h18")],
 "oven-safe": [P("M4.75 3.75h14.5a1 1 0 0 1 1 1v14.5a1 1 0 0 1-1 1H4.75a1 1 0 0 1-1-1V4.75a1 1 0 0 1 1-1z"),
               P("M3.75 8.25h16.5"), P("M7 6h.01"), P("M10 6h.01"), P("M8.25 11.25h7.5a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-7.5a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1z")],
 "gift": [P("M4.25 8.25h15.5a1 1 0 0 1 1 1v1.5a1 1 0 0 1-1 1H4.25a1 1 0 0 1-1-1v-1.5a1 1 0 0 1 1-1z"),
          P("M4.75 11.75v8.5a1 1 0 0 0 1 1h12.5a1 1 0 0 0 1-1v-8.5"), P("M12 8.25v13"),
          P("M12 8.25C10.5 4 6.75 3.25 6.75 5.6c0 1.6 2.4 2.65 5.25 2.65"), P("M12 8.25c1.5-4.25 5.25-5 5.25-2.65 0 1.6-2.4 2.65-5.25 2.65")],
 "mystery-gift": [P("M4.25 4.75h15.5a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1H4.25a1 1 0 0 1-1-1v-1a1 1 0 0 1 1-1z"),
                  P("M4.75 7.75v12.5a1 1 0 0 0 1 1h12.5a1 1 0 0 0 1-1V7.75"),
                  P("M10 12.25a2 2 0 1 1 2.75 1.85c-.45.2-.75.6-.75 1.1v.55"), P("M12 18.25h.01")],
 "e-book": [P("M12 6.5c-1.8-1.5-4.5-2-8.25-1.75v13c3.75-.25 6.45.25 8.25 1.75 1.8-1.5 4.5-2 8.25-1.75v-13C16.5 4.5 13.8 5 12 6.5z"),
            P("M12 6.5v13")],
 "water-filter": [P("M12 2.75s-6.25 6.9-6.25 11.25a6.25 6.25 0 0 0 12.5 0C18.25 9.65 12 2.75 12 2.75z"), P("M9.25 14.5a2.75 2.75 0 0 0 2.25 2.6")],
 "secure-checkout": [P("M5.75 10.75h12.5a1 1 0 0 1 1 1v8.5a1 1 0 0 1-1 1H5.75a1 1 0 0 1-1-1v-8.5a1 1 0 0 1 1-1z"),
                     P("M8 10.75V7.5a4 4 0 0 1 8 0v3.25"), P("M12 15v2.25")],
 "customers-100k": [C(9,8,3.25), P("M3 20.25v-1a5 5 0 0 1 5-5h2a5 5 0 0 1 5 5v1"), P("M15.5 4.9a3.25 3.25 0 0 1 0 6.2"),
                    P("M17.75 14.4a5 5 0 0 1 3.25 4.6v1.25")],
 "original-since-2024": [C(12,9.25,6.5), P(star(12,9.25,3.1,1.35)), P("M8.6 14.8 7.25 21.25l4.75-2.25 4.75 2.25-1.35-6.45")],
}

def svg(name, color):
    body = "".join(ICONS[name])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
            f'<title>{name}</title>{body}</svg>\n')

if __name__ == "__main__":
    for cname, hexv in COLORS.items():
        os.makedirs(os.path.join(HERE, "svg", cname), exist_ok=True)
        for n in ICONS:
            open(os.path.join(HERE, "svg", cname, n + ".svg"), "w").write(svg(n, hexv))
    print(len(ICONS), "icons x", len(COLORS), "colors")
