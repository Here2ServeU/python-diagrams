import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os

# Define SRE stages and corresponding icon filenames
stages = [
    ("1. Monitoring", "monitoring.png"),
    ("2. Incident Response", "incident.png"),
    ("3. Postmortems", "postmortem.png"),
    ("4. Automation", "automation.png"),
    ("5. Capacity Planning", "capacity.png"),
    ("6. SLI/SLO Definition", "sli_slo.png"),
    ("7. Change Mgmt", "change.png"),
    ("8. Release Mgmt", "release.png"),
    ("9. Chaos Engineering", "chaos.png"),
    ("10. Runbooks", "runbook.png")
]

# Create a directed graph and connect circularly
G = nx.DiGraph()
for i in range(len(stages)):
    G.add_edge(stages[i][0], stages[(i + 1) % len(stages)][0])

# Generate circular layout
pos = nx.circular_layout(G)
for key in pos:
    pos[key] *= 1.3  # Slightly spread out for clarity

# Create figure
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_title("SRE Lifecycle (Circular Layout)", fontsize=18, fontweight='bold')
ax.axis('off')

# Draw edges (arrows only)
nx.draw_networkx_edges(G, pos, ax=ax, arrows=True, arrowsize=20, edge_color='gray')

# Draw icons and bold text labels
for label, icon_file in stages:
    x, y = pos[label]
    icon_path = os.path.join("icons", icon_file)
    if os.path.exists(icon_path):
        img = plt.imread(icon_path)
        imagebox = OffsetImage(img, zoom=0.12)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
    # Draw bold text under icon
    ax.text(x, y - 0.25, label, fontsize=10, fontweight='bold', ha='center', va='top')

# Save and show
plt.tight_layout()
plt.savefig("sre_lifecycle_circular_with_icons.png", dpi=300)
plt.show()