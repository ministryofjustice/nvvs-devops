[![repo standards badge](https://img.shields.io/badge/dynamic/json?color=blue&style=for-the-badge&logo=github&label=MoJ%20Compliant&query=%24.data%5B%3F%28%40.name%20%3D%3D%20%22modernisation-platform%22%29%5D.status&url=https%3A%2F%2Foperations-engineering-reports.cloud-platform.service.justice.gov.uk%2Fgithub_repositories)](https://operations-engineering-reports.cloud-platform.service.justice.gov.uk/github_repositories#modernisation-platform "Link to report")

# Ministry of Justice Cloud Operations team repository

## About this Repository

This is the Ministry of Justice [Cloud Operations teams](https://ministryofjustice.github.io/cloud-operations) public repository for our documentation.

## Contents
- [Architecture Decision Record (ADR)](architecture-decision-record) A record of the technical decisions made by the team.

### Core repositories
| Name | Description |
|-|-|
| [cloud-operations-team](https://github.com/ministryofjustice/cloud-operations) | Our repository for documentation, scripts and ways of working (this repository) |

### Shared Services
| Name | Description |
|-|-|
| [shared-services-infrastructure](https://github.com/ministryofjustice/staff-device-shared-services-infrastructure) | Creates infrastructure in the shared services account, including continuous integration and delivery pipelines |
| [docker-base-images](https://github.com/ministryofjustice/staff-device-docker-base-images) | Repository for base container images used across multiple services. Created as the solution to DockerHub rate limits as suggested by AWS. |

### Certificate Services
| Name | Description |
|-|-|
| [infra-certificate-services](https://github.com/ministryofjustice/staff-infrastructure-certificate-services) | Public Key Infrastructure for devices and users. This repository is used to redeploy the EC2 instances which Entrust build their managed service on. |

### DHCP / DNS
| Name | Description |
|-|-|
| [infra-dhcp-dns](https://github.com/ministryofjustice/staff-device-dns-dhcp-infrastructure) | This repository contains the Terraform code to build the AWS infrastructure for the Ministry of Justice's DNS and DHCP platform. |
| [dns-dhcp-admin](https://github.com/ministryofjustice/staff-device-dns-dhcp-admin) | Portal for managing staff device site dhcp and dns. |
| [dhcp-server](https://github.com/ministryofjustice/staff-device-dhcp-server) | This repository contains the Dockerfile to create the ISC Kea DHCP server docker image. The configuration for this server is managed in the Admin Portal. |
| [dns-server](https://github.com/ministryofjustice/staff-device-dns-server) | This repository contains the Dockerfile to create the BIND DNS server Docker image. The configuration for this server is managed in the Admin Portal. |
| [private-dns-zone](https://github.com/ministryofjustice/staff-device-private-dns-zone) | Add private DNS zones into Route53 |
| [disaster-recovery](https://github.com/ministryofjustice/staff-device-dns-dhcp-disaster-recovery) | This repo contains an interactive script which can be used to roll back a corrupt config file for the DNS or DHCP services. |
| [logging-integration-tests](ministryofjustice/staff-device-logging-dns-dhcp-integration-tests) | These scripts emulate UDP traffic for both DHCP and Syslog requests. They are run from the Corsham VM to test the services over the network. |

### Infrastructure Monitoring and Alerting Platform
| Name | Description |
|-|-|
| [infra-imap](https://github.com/ministryofjustice/staff-infrastructure-monitoring) | Terraform module that deploys the staff infrastructure monitoring solution. It has support for components like: Grafana, Prometheus, etc.
| [app-reachability](https://github.com/ministryofjustice/staff-infrastructure-monitoring-app-reachability) | Container to remote write blackbox http application prometheus metrics |
| [blackbox-exporter](https://github.com/ministryofjustice/staff-infrastructure-monitoring-blackbox-exporter) | To probe endpoints over HTTP, HTTPS, DNS, TCP and ICMP |
| [snmp-exporter](https://github.com/ministryofjustice/staff-infrastructure-monitoring-snmpexporter) | To scrape data from physical devices (Docker image) |
| [dns-reachability](https://github.com/ministryofjustice/staff-infrastructure-monitoring-dns-reachability) | Container to remote write blackbox DNS prometheus metrics
| [imap-config](https://github.com/ministryofjustice/staff-infrastructure-monitoring-config) | To provision data sources for the IMA Platform
| [deployments](https://github.com/ministryofjustice/staff-infrastructure-monitoring-deployments) | To deploy helm charts to EKS
| [metric-aggregation-server](https://github.com/ministryofjustice/staff-infrastructure-metric-aggregation-server) | Prometheus ECS
| [metric-aggregator-cloud](https://github.com/ministryofjustice/staff-infrastructure-metric-aggregator-cloud) | Prometheus EKS

### Security Log Aggregation and Shipping
| Name | Description |
|-|-|
| [infra-log-shipping](https://github.com/ministryofjustice/staff-device-logging-infrastructure) | Log shipping to infrastructure > OST
| [syslog-to-cloudwatch](https://github.com/ministryofjustice/staff-device-logging-syslog-to-cloudwatch) | Syslog to aws cloudwatch > OST

### SMTP Relay Service
| Name | Description |
|-|-|
| [infra-smtp](https://github.com/ministryofjustice/staff-infrastructure-network-services) | Infrastructure deployment for networking services including SMTP |
| [smtp-relay-server](https://github.com/ministryofjustice/staff-infrastructure-smtp-relay-server) | Internal mail relay based on POSTFIX

## About this Website

This repository is published via Github Pages [here](https://ministryofjustice.github.io/cloud-operations/#cloud-operations)

To update, edit files in [this directory](https://github.com/ministryofjustice/cloud-operations/tree/main/source).

Filenames must be `[something].html.md.erb`
