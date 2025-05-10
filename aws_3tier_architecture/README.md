
# t2s-app: AWS 3-Tier Architecture Diagram

This project uses the [Diagrams](https://diagrams.mingrammer.com/) Python library to generate a horizontal diagram of a basic **AWS 3-Tier Architecture**. It visually represents a production-ready infrastructure using key AWS components like Route53, WAF, ELB, EC2 instances, and RDS.

---

## Architecture Overview

**Three Tiers:**
1. **Web Tier** – Handles incoming traffic (via Load Balancer and EC2 Web servers)
2. **App Tier** – Processes application logic (EC2 App servers)
3. **Data Tier** – Stores data securely (Amazon RDS)

---

## Prerequisites

- macOS or Linux (tested)
- Python 3.8+
- [Homebrew](https://brew.sh/) installed for macOS users

---

## Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/t2s-app-aws-diagram.git
cd t2s-app-aws-diagram
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Python Packages

```bash
pip install diagrams
```

### 4. Install Graphviz (required for rendering diagrams)

```bash
brew install graphviz     # macOS
# OR
sudo apt install graphviz # Debian/Ubuntu
```

---

## Run the Script

```bash
python t2s-app_aws_3tier_architecture.py
```

- This will generate an image file: `t2s-app_aws_3tier_architecture.png`
- It will also automatically open a preview window if `show=True`

---

## Code Explanation

```python
from diagrams import Diagram, Cluster
```
- Import core classes for creating diagrams and logical grouping.

```python
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.security import WAF
```
- Import AWS-specific nodes to represent various services.

```python
with Diagram("t2s-app: AWS 3-Tier Architecture", show=True, filename="t2s-app_aws_3tier_architecture", direction="LR"):
```
- Start the diagram context.
- `show=True` auto-opens the file.
- `filename=...` sets the output file name.
- `direction="LR"` arranges elements **Left to Right**.

```python
    dns = Route53("Route53 DNS")
    waf = WAF("AWS WAF")
    lb = ELB("Elastic Load Balancer")
```
- Define the **edge layer** for DNS resolution, security firewall, and traffic routing.

```python
    dns >> waf >> lb
```
- Show directional flow from Route53 → WAF → Load Balancer.

```python
    with Cluster("Web Tier"):
        web_servers = [EC2("Web1"), EC2("Web2")]
```
- Group EC2 Web instances inside the "Web Tier" cluster.

```python
    with Cluster("App Tier"):
        app_servers = [EC2("t2s-App1"), EC2("t2s-App2")]
```
- Group EC2 App instances inside the "App Tier".

```python
    with Cluster("Data Tier"):
        db = RDS("Amazon RDS")
```
- Define the database node inside the "Data Tier".

```python
    lb >> web_servers
```
- Load balancer forwards traffic to Web servers.

```python
    for web in web_servers:
        web >> app_servers
```
- Each Web server connects to all App servers.

```python
    for app in app_servers:
        app >> db
```
- Each App server connects to the RDS database.

---

## Clean Up

When you're done:

### 1. Deactivate Virtual Environment
```bash
deactivate
```

### 2. Remove Environment and Artifacts
```bash
rm -rf venv
rm t2s-app_aws_3tier_architecture.png
```

---

## Output Preview

- `t2s-app_aws_3tier_architecture.png` is the horizontal diagram generated.
- The diagram includes:
  - Route53 → WAF → ELB → EC2 Web Instances → EC2 App Instances → RDS

---

## Contact

**Emmanuel Naweji**  
Founder, Transformed 2 Succeed LLC  
📧 emmanuel@transformed2succeed.com  
🌐 [GitHub](https://github.com/Here2ServeU) | [LinkedIn](https://linkedin.com/in/ready2assist)

---

© 2025 Transformed 2 Succeed LLC. All rights reserved.

