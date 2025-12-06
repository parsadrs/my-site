from math import atan2, pi
import math
import matplotlib.pyplot as plt

vertices = list(range(5))
hyperedge_codes = [
    "10000",
    "01000",
    "00100",
    "00010",
    "00001",
    "11000",
    "10101",
    "11111",
]

R = 1.5
angles = [2*pi*i/5 for i in range(5)]
coords = [(R * (0.9 * math.cos(a)), R * (0.9 * math.sin(a))) for a in angles]

fig, ax = plt.subplots(figsize=(7,7))
ax.set_aspect('equal')
ax.axis('off')

for code in hyperedge_codes:
    members = [i for i, bit in enumerate(code) if bit == '1']
    if not members:
        continue
    pts = [coords[i] for i in members]
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    pts_sorted = sorted(pts, key=lambda p: atan2(p[1]-cy, p[0]-cx))
    xs = [p[0] for p in pts_sorted]; ys = [p[1] for p in pts_sorted]
    xs.append(xs[0]); ys.append(ys[0])
    ax.fill(xs, ys, alpha=0.25)
    ax.text(cx, cy, code, ha='center', va='center', fontsize=9, fontweight='bold')

for i, (x, y) in enumerate(coords):
    circle = plt.Circle((x, y), 0.08, fill=True)
    ax.add_patch(circle)
    ax.text(x, y-0.18, f"v{i}", ha='center', va='center')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
plt.title("5-bit hypergraph — hyperedges shown by binary codes", fontsize=12)
plt.savefig("hypergraph_5bit_fixed.png", dpi=200, bbox_inches='tight')
plt.close(fig)
