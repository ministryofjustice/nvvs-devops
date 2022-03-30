  3. Use AWS Elastic Container Service for DHCP DNS
  Date: 2020-05-27

  Status
  ✅ Accepted

  ## Context

We will need to run our [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) (Dynamic Host Configuration Protocol), [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) (Domain Name System) and Monitoring systems somewhere that support both TCP and UDP load balancing.

  ## Decision

Use AWS Elastic Container Services. 
ECS is a fully managed container service that supports TCP and UDP network traffic.

  ## Consequences

  ### Advantages

  Less management overhead than running virtual machines e.g. EC2 and less complexity than EKS.

  ### Disadvantages

Provisioning and deployment e.g. CI/CD responsibilities, documentation and forever maintaining those things. Duplication of work, increased cloud costs.