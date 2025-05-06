# DevOps Infrastructure Checklist Flow (with Diagrams Python)

This project uses the [Diagrams](https://diagrams.mingrammer.com/) Python library to visually represent a structured checklist for DevOps infrastructure. It guides users from auditing infrastructure to full automation using modern tooling.

---

## Flow Overview

The diagram represents six key stages in DevOps infrastructure maturity:

1. **Audit Infrastructure**
2. **Standardize Environments**
3. **Prioritize High-Impact Areas**
4. **Onboard Engineers**
5. **Review & Update**
6. **Automate with CI/CD, IaC, and Monitoring**

---

## How to Run

### Step 1: Set up your environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install diagrams
brew install graphviz  # Or sudo apt install graphviz on Linux
```

### Step 2: Run the script

```bash
python3 checklist_flow_diagram.py
```

This generates a PNG diagram named:
`How to Use the DevOps Infrastructure Checklist.png`

---

## Line-by-Line Script Breakdown
- Using **checklist_flow_diagram.py**
```python
from diagrams import Diagram, Edge
```
- `Diagram`: Creates a canvas for your architecture diagram.
- `Edge`: Used to draw directional arrows between components.

```python
from diagrams.custom import Custom
```
- Allows using custom icons from PNG files in your assets folder.

```python
from diagrams.onprem.devops import Gitlab
from diagrams.onprem.iac import Terraform
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.network import Nginx
from diagrams.programming.language import Python
from diagrams.saas.collaboration import Notion
from diagrams.onprem.compute import Server
from diagrams.onprem.analytics import Tableau
```
- These imports pull components from Diagrams' icon libraries representing on-prem, SaaS, or language tools. They allow you to create labeled nodes.

```python
with Diagram("How to Use the DevOps Infrastructure Checklist", show=True, direction="LR"):
```
- Starts a new diagram called `"How to Use the DevOps Infrastructure Checklist"`.
- `direction="LR"` arranges nodes from **left to right**.
- `show=True` opens the diagram file after it's generated.

---

### Step Nodes

```python
audit = Custom("Audit Infrastructure", "./assets/audit.png")
```
- Represents the first step: auditing current systems. Uses a custom PNG icon.

```python
standardize = Custom("Standardize Environments", "./assets/dev_stage_prod.png")
```
- Highlights the need for consistency across dev, staging, and prod.

```python
prioritize = Custom("Prioritize High-Impact", "./assets/prioritize.png")
```
- Guides teams to address security, availability, and cost before enhancements.

```python
onboard = Notion("Onboarding Docs")
```
- Suggests using collaborative tools (like Notion) for team onboarding docs.

```python
review = Tableau("Quarterly Review")
```
- Visualizes quarterly retrospectives using a BI tool like Tableau.

```python
cicd = Jenkins("CI/CD")
iac = Terraform("IaC")
observability = Prometheus("Monitoring") >> Grafana("Dashboards")
```
- Shows the automation layer:
  - Jenkins handles build/deploy pipelines.
  - Terraform for infrastructure provisioning.
  - Prometheus and Grafana for observability and alerting.

---

### Workflow Arrows

```python
audit >> Edge(label="Identify gaps") >> standardize
```
- From audit → standardization step, labeled as "Identify gaps"

```python
standardize >> Edge(label="Apply principles") >> prioritize
prioritize >> Edge(label="Focus areas") >> onboard
onboard >> Edge(label="Documentation") >> review
review >> Edge(label="Continuous Improvement") >> [cicd, iac, observability]
```
- Each arrow shows a logical progression in infrastructure maturity.

---

## Author

**Emmanuel Naweji**  
Cloud & DevOps Solutions Architect  
- [LinkedIn](https://www.linkedin.com/in/ready2assist/)  
- [Book a Call](https://here4you.setmore.com)

---

## License

MIT License © 2025 Emmanuel Naweji
