from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.security import WAF

with Diagram("t2s-app: AWS 3-Tier Architecture", show=True, filename="t2s-app_aws_3tier_architecture", direction="LR"):

    dns = Route53("Route53 DNS")
    waf = WAF("AWS WAF")
    lb = ELB("Elastic Load Balancer")

    dns >> waf >> lb

    with Cluster("Web Tier"):
        web_servers = [EC2("Web1"), EC2("Web2")]

    with Cluster("App Tier"):
        app_servers = [EC2("t2s-App1"), EC2("t2s-App2")]

    with Cluster("Data Tier"):
        db = RDS("Amazon RDS")

    lb >> web_servers

    for web in web_servers:
        web >> app_servers

    for app in app_servers:
        app >> db
