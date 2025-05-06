from diagrams import Diagram, Edge
from diagrams.custom import Custom
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.iac import Terraform
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.analytics import Tableau
from diagrams.programming.language import Python

with Diagram("How to Use the DevOps Infrastructure Checklist", show=True, direction="LR"):

    # Step 1: Audit
    audit = Custom("Audit Infrastructure", "./assets/audit.png")

    # Step 2: Standardize
    standardize = Custom("Standardize Environments", "./assets/dev_stage_prod.png")

    # Step 3: Prioritize
    prioritize = Custom("Prioritize High-Impact", "./assets/prioritize.png")

    # Step 4: Onboard
    onboard = Python("Onboarding Docs")

    # Step 5: Review & Update
    review = Tableau("Quarterly Review")

    # Step 6: Automate
    cicd = Jenkins("CI/CD")
    iac = Terraform("IaC")
    observability = Prometheus("Monitoring") >> Grafana("Dashboards")

    # Flow connections
    audit >> Edge(label="Identify gaps") >> standardize
    standardize >> Edge(label="Apply principles") >> prioritize
    prioritize >> Edge(label="Focus areas") >> onboard
    onboard >> Edge(label="Documentation") >> review
    review >> Edge(label="Continuous Improvement") >> [cicd, iac, observability]
