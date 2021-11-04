# Ministry of Justice Cloud Operations team repository

## About this Repository

This is the Ministry of Justice [Cloud Operations teams](https://ministryofjustice.github.io/cloud-operations) public repository for our documentation.


### Core repositories
| Name | Description |
|-|-|
| [Cloud Operations teams](https://ministryofjustice.github.io/cloud-operations) (this one) | Our repository for documentation, scripts and ways of working |

### Shared Services

| Name | Description |
|-|-|
| [shared-services-infrastructure](https://github.com/ministryofjustice/staff-device-shared-services-infrastructure) | Create infrastructure from the main AWS shared account into Development, Pre Production and Production via AWS CodePipelines. |
| [staff-device-docker-base-images](https://github.com/ministryofjustice/staff-device-docker-base-images) | Repository for base container images used across multiple services. Created as the solution to DockerHub rate limits as suggested by AWS. |

### DHCP / DNS

| Name | Description |
|-|-|
| [staff-device-dhcp-server](https://github.com/ministryofjustice/staff-device-dhcp-server) | This repository contains the Dockerfile to create the ISC Kea DHCP server docker image. The configuration for this server is managed in the Admin Portal. |
| [staff-device-dns-server](https://github.com/ministryofjustice/staff-device-dns-server) | This repository contains the Dockerfile to create the BIND DNS server Docker image. The configuration for this server is managed in the Admin Portal. |
| [staff-device-dns-dhcp-admin](https://github.com/ministryofjustice/staff-device-dns-dhcp-admin) | Portal for managing staff device site dhcp and dns. |
| [staff-device-dns-dhcp-disaster-recovery](https://github.com/ministryofjustice/staff-device-dns-dhcp-disaster-recovery) | This repo contains an interactive script which can be used to roll back a corrupt config file for the DNS or DHCP services. |
| [staff-device-logging-dns-dhcp-integration-tests](ministryofjustice/staff-device-logging-dns-dhcp-integration-tests) | These scripts emulate UDP traffic for both DHCP and Syslog requests. They are run from the Corsham VM to test the services over the network. |

### Infrastructure Monitoring and Alerting Platform
| Name | Description |
|-|-|
| [staff-infrastructure-monitoring-app-reachability](https://github.com/ministryofjustice/staff-infrastructure-monitoring-app-reachability) | Container to remote write blackbox http application prometheus metrics 
| [staff-infrastructure-monitoring-blackbox-exporter](https://github.com/ministryofjustice/staff-infrastructure-monitoring-blackbox-exporter) | To probe endpoints over HTTP, HTTPS, DNS, TCP and ICMP
| [staff-infrastructure-monitoring-dns-reachability](https://github.com/ministryofjustice/staff-infrastructure-monitoring-dns-reachability) | Container to remote write blackbox DNS prometheus metrics
| [staff-infrastructure-monitoring-config](https://github.com/ministryofjustice/staff-infrastructure-monitoring-config) | To provision data sources for the IMA Platform
| [staff-infrastructure-monitoring-deployments](https://github.com/ministryofjustice/staff-infrastructure-monitoring-deployments) | To deploy helm charts to EKS
| [staff-infrastructure-monitoring](https://github.com/ministryofjustice/staff-infrastructure-monitoring) | Terraform module that deploys the staff infrastructure monitoring solution. It has support for components like: Grafana, Prometheus, etc.
| [staff-infrastructure-metric-aggregation-server](https://github.com/ministryofjustice/staff-infrastructure-metric-aggregation-server) | Prometheus ECS
| [staff-infrastructure-metric-aggregator-cloud](https://github.com/ministryofjustice/staff-infrastructure-metric-aggregator-cloud) | Prometheus EKS
| [staff-device-private-dns-zone](https://github.com/ministryofjustice/staff-device-private-dns-zone) | Add private DNS zones into Route53
| [staff-infrastructure-monitoring-snmpexporter](https://github.com/ministryofjustice/staff-infrastructure-monitoring-snmpexporter) | To scrape data from physical devices (Docker image)

### Security Log Aggregation and Shipping
| Name | Description |
|-|-|
| [ministryofjustice/staff-device-logging-infrastructure](https://github.com/ministryofjustice/staff-device-logging-infrastructure) | Log shipping to infrastructure > OST
| [staff-device-logging-syslog-to-cloudwatch](https://github.com/ministryofjustice/staff-device-logging-syslog-to-cloudwatch) | Syslog to aws cloudwatch > OST

### SMTP Relay Service
| Name | Description |
|-|-|
| [staff-infrastructure-smtp-relay-server](https://github.com/ministryofjustice/staff-infrastructure-smtp-relay-server) | Mail relay based on POSTFIX
| [staff-infrastructure-network-services](https://github.com/ministryofjustice/staff-infrastructure-network-services) | Infrastructure deployment

## Website

This repository is published via Github Pages [here](https://ministryofjustice.github.io/cloud-operations/#cloud-operations)

To update, edit files in [this directory](https://github.com/ministryofjustice/cloud-operations/tree/main/source).

Filenames must be `[something].html.md.erb`