# Ministry of Justice NVVS DevOps team repository
[![repo standards badge](https://img.shields.io/badge/dynamic/json?color=blue&style=flat&logo=github&labelColor=32393F&label=MoJ%20Compliant&query=%24.result&url=https%3A%2F%2Foperations-engineering-reports.cloud-platform.service.justice.gov.uk%2Fapi%2Fv1%2Fcompliant_public_repositories%2Fcloud-operations)](https://operations-engineering-reports.cloud-platform.service.justice.gov.uk/public-github-repositories.html#cloud-operations "Link to report")

## About this Repository

This is the Ministry of Justice [NVVS DevOps teams](https://ministryofjustice.github.io/cloud-operations) public repository for our documentation.

## Contents
- [Architecture Decision Record (ADR)](architecture-decision-record) A record of the technical decisions made by the team.

### Core repositories
| Name | Description |
|-|-|
| [NVVS DevOps team](https://github.com/ministryofjustice/cloud-operations) | Our repository for documentation, scripts and ways of working (this repository) |

### Shared Services
| Name | Description |
|-|-|
| [GitHub actions](https://github.com/ministryofjustice/cloud-operations-github-actions) | Central configuration repository for [GitHub Actions Workflows](https://docs.github.com/en/actions/using-workflows/about-workflows), which can be called from our other repositories. |
| [Shared services infrastructure](https://github.com/ministryofjustice/staff-device-shared-services-infrastructure) | Creates infrastructure in the shared services account, including continuous integration and delivery pipelines |
| [Technology Services GitHub Teams](https://github.com/ministryofjustice/staff-technology-services-github-teams) | Terraform repository to define and maintain GitHub Teams for Technology Services. |
| [Tech docs monitor](https://github.com/ministryofjustice/tech-docs-monitor) | Technical Documentation expiry monitor and notifier |
| [AWS OIDC](https://github.com/ministryofjustice/mojo-aws-github-oidc-provider) |To manage GitHub AWS OpenID Connector provider on MoJO AWS Shared Services account.|



### Certificate Services
| Name | Description |
|-|-|
| [Certificate Services](https://github.com/ministryofjustice/staff-infrastructure-certificate-services) | Public Key Infrastructure(PKI) for devices and users. This repository is used to redeploy the EC2 instances on which Entrust builds the managed service. |

### DHCP / DNS
| Name | Description |
|-|-|
| [DHCP DNS infrastructure](https://github.com/ministryofjustice/staff-device-dns-dhcp-infrastructure) | This repository contains the Terraform code to build the AWS infrastructure for the Ministry of Justice's DNS and DHCP platform. |
| [DHCP DNS admin portal](https://github.com/ministryofjustice/staff-device-dns-dhcp-admin) | Portal for managing staff device site DHCP and DNS. |
| [DHCP server config](https://github.com/ministryofjustice/staff-device-dhcp-server) | This repository contains the Dockerfile to create the ISC Kea DHCP server docker image. The configuration for this server is managed in the Admin Portal. |
| [DNS server config](https://github.com/ministryofjustice/staff-device-dns-server) | This repository contains the Dockerfile to create the BIND DNS server Docker image. The configuration for this server is managed in the Admin Portal. |
| [DNS route53 zones](https://github.com/ministryofjustice/staff-device-private-dns-zone) | DNS Zones hosted in Route53, the internal zones are used by MoJO-DNS |
| [DHCP DNS disaster recovery](https://github.com/ministryofjustice/staff-device-dns-dhcp-disaster-recovery) | This repo contains an interactive script which can be used to roll back a corrupt config file for the DNS or DHCP services. |
| [DHCP DNS integration tests](https://github.com/ministryofjustice/staff-device-logging-dns-dhcp-integration-tests) | These scripts emulate UDP traffic for both DHCP and Syslog requests. They are run from the Corsham VM to test the services over the network. |

### Infrastructure Monitoring and Alerting Platform
| Name | Description |
|-|-|
| [App reachability](https://github.com/ministryofjustice/staff-infrastructure-monitoring-app-reachability) | Container to remote write blackbox http application prometheus metrics |
| [Blackbox exporter](https://github.com/ministryofjustice/staff-infrastructure-monitoring-blackbox-exporter) | To probe endpoints over HTTP, HTTPS, DNS, TCP and ICMP |
| [DNS reachability](https://github.com/ministryofjustice/staff-infrastructure-monitoring-dns-reachability) | Container to remote write blackbox DNS prometheus metrics
| [Helm Deployment](https://github.com/ministryofjustice/staff-infrastructure-monitoring-deployments) | To deploy helm charts to EKS
| [IMAP infrastructure](https://github.com/ministryofjustice/staff-infrastructure-monitoring) | Terraform module that deploys the staff infrastructure monitoring solution including Grafana and Prometheus.
| [SNMP exporter](https://github.com/ministryofjustice/staff-infrastructure-monitoring-snmpexporter) | To scrape data from physical devices (Docker image) |
| [IMAP configuration](https://github.com/ministryofjustice/staff-infrastructure-monitoring-config) | To provision data sources dashboards and alerts 
| [Prometheus ECS](https://github.com/ministryofjustice/staff-infrastructure-metric-aggregation-server) | Prometheus ECS
| [Prometheus EKS](https://github.com/ministryofjustice/staff-infrastructure-metric-aggregator-cloud) | Prometheus EKS

### Security Log Aggregation and Shipping
| Name | Description |
|-|-|
| [Log shipping infrastructure](https://github.com/ministryofjustice/staff-device-logging-infrastructure) | Log shipping to infrastructure > OST
| [Syslog to CloudWatch](https://github.com/ministryofjustice/staff-device-logging-syslog-to-cloudwatch) | Syslog to aws cloudwatch > OST

### SMTP Relay Service
| Name | Description |
|-|-|
| [SMTP infrastructure](https://github.com/ministryofjustice/staff-infrastructure-network-services) | Infrastructure deployment for networking services including SMTP |
| [SMTP relay server](https://github.com/ministryofjustice/staff-infrastructure-smtp-relay-server) | Internal mail relay based on POSTFIX

### Network Access Control (NACS)

| Name | Description |
|-|-|
| [Network access control admin](https://github.com/ministryofjustice/network-access-control-admin) | Web Frontend for managing Network Access Control |
| [Network access control disaster recovery](https://github.com/ministryofjustice/network-access-control-disaster-recovery) | Disaster Recovery |
| [Network access control infrastructure](https://github.com/ministryofjustice/network-access-control-infrastructure) | NACS Infrastructure |
| [Network access control integration tests](https://github.com/ministryofjustice/network-access-control-integration-tests) | NACS Integrations Tests |
| [Network access control server ](https://github.com/ministryofjustice/network-access-control-server ) | NACS Radius Server Configuration |

## About this Website

This repository is published via Github Pages [here](https://ministryofjustice.github.io/cloud-operations/#cloud-operations)

To update, edit files in [this directory](https://github.com/ministryofjustice/cloud-operations/tree/main/source).

Filenames must be `[something].html.md.erb`
