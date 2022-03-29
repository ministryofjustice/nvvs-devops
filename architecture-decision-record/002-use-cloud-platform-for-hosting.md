2. Use Cloud Platform for hosting
Date: 2020-05-22

## Status 
❌ Rejected

## Context

We will need to run our [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) (Dynamic Host Configuration Protocol), [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) (Domain Name System) and Monitoring systems somewhere. [MoJ Technical Guidance](https://technical-guidance.service.justice.gov.uk/documentation/standards/hosting.html#how-to-host-services) states you must use [Cloud Platform](https://user-guide.cloud-platform.service.justice.gov.uk/) by default.

## Decision

After investigations by Cloud Platform team (see GitHub issue [here](https://github.com/ministryofjustice/cloud-platform/issues/1897#issuecomment-632592093)), there are [issues]((https://github.com/kubernetes/kubernetes/issues/79523#issuecomment-595405745)) with Network Load Balancers passing both UDP and TCP, this is a requirement for running DHCP and DNS services.

## Consequences

- We will need to build and run our own infrastructure to host these services.
