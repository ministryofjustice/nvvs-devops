2. Use BIND DNS for device name resolution
Date: 2020-05-14

Status
✅ Accepted

## Context

Staff devices while connected to our network will require DNS or Domain Naming Services. This service will be responsible for resolving both internal and external DNS queries for staff devices connected at a site or remotely. Any requests not dealt with by the MoJ DNS service are required to be forwarded to the National Cyber Security Centre (NCSC) Protective DNS [PDNS](https://www.ncsc.gov.uk/information/pdns) service for resolution.

There is a requirement that this service is able to automatically scale (both up and down) to cope with varying load levels during the course of the day.

There is a limitation around using the fully managed AWS Route53 DNS service as it does not support DNS forwarding.  

**Dec 2021 Update** Route53 can now forward DNS requests e.g. [PDNS](https://www.ncsc.gov.uk/information/pdns)

## Decision

- We have decided to use ISC (Internet Systems Consortium) [BIND](https://www.isc.org/bind/) (Berkeley Internet Name Domain) for our [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) (Domain Name System)
- BIND is the industry standard software for running DNS servers. It is open source and easily installed using package managers. It can be containerised and can fit into the many hosting options within MoJ.

## Consequences

### General consequences
- we will need to run our own infrastructure rather than using a managed DNS service, due limitations in the managed Route53 service with forwarding requests.
- since the BIND9 DNS service has no user interface, we will need to provide a way for onsite support engineers to add new Zones to the service.
### Advantages
- BIND9 provides a lot of customisation and flexibility that may fill requirements as this service is used further in MoJ.
### Disadvantages
  - need to build, operate and maintain the service somewhere
