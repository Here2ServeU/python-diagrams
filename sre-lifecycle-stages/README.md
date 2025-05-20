# SRE Lifecycle Circular Diagram

This project generates a circular diagram of the Site Reliability Engineering (SRE) lifecycle using Python. Each stage of the lifecycle is represented by a labeled icon, and directional arrows illustrate the continuous nature of the lifecycle.

## Features

- Circular layout using polar coordinates
- Ten standard stages of the SRE lifecycle
- Arrows connecting each phase in a loop
- Custom icons for visual clarity
- Saves and displays the diagram as an image

## Requirements

Install the required Python libraries:

```bash
pip install matplotlib networkx pillow
```

## Folder Structure

```
project/
├── sre_lifecycle_circular_popup.py
└── icons/
    ├── monitoring.png
    ├── incident.png
    ├── postmortem.png
    ├── automation.png
    ├── capacity.png
    ├── sli_slo.png
    ├── change.png
    ├── release.png
    ├── chaos.png
    └── runbook.png
```

## How to Run

To generate and view the diagram:

```bash
python3 sre_lifecycle_circular_popup.py
```

This will:
- Display the diagram in a popup window
- Save the file as `sre_lifecycle_circular_final.png` in the current directory

## Code Explanation

- **Graph Construction:** The script builds a directed graph using `networkx.DiGraph`, linking each SRE phase in a loop.
- **Circular Layout:** A custom layout positions each node around a circle using polar coordinates to ensure even distribution.
- **Image Rendering:** Icons are loaded using PIL and placed with `matplotlib.offsetbox`.
- **Arrow Routing:** Edges are slightly offset to avoid overlapping the icons, and arrows are drawn using `annotate`.
- **Output:** The final diagram is saved as a PNG and displayed using `plt.show()`.

## SRE Lifecycle Stages Covered

1. Monitoring  
2. Incident Response  
3. Postmortems  
4. Automation  
5. Capacity Planning  
6. SLI/SLO Definition  
7. Change Management  
8. Release Management  
9. Chaos Engineering  
10. Runbooks and Playbooks

## Use of the Diagram

This diagram is useful for:
- Presenting the full SRE lifecycle in engineering or operational meetings
- Training new team members on the sequence and feedback loops in reliability work
- Including in documentation, process diagrams, or dashboards to visualize responsibility areas

## Credits

Created by Emmanuel Naweji.  
Based on industry-recognized SRE best practices.
