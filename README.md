# Python Diagrams for DevOps & Cloud Architecture

This repository showcases how to generate architecture diagrams using Python to visualize and document real-world Cloud/DevOps systems.

## Diagrams Included In These Respective Directories
- `devops-checklist`: Visual DevOps maturity flow
- `aws-3tier-architecture`: Scalable 3-tier AWS setup
- `eks-observability-stack`: EKS monitoring stack

## Setup Instructions

- Move into the desired directory: 
```bash
cd devops-checklist
```

- Run the following commands

```bash
python3 -m venv venv
source venv/bin/activate
pip install diagrams
brew install graphviz  # or: sudo apt install graphviz
python3 checklist_flow_diagram.py
```

## Author
**Emmanuel Naweji** - [LinkedIn](https://www.linkedin.com/in/ready2assist) • [Book a Call](https://here4you.setmore.com)
