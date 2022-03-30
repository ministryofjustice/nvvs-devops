  # 3. Use AWS Elastic Container Service for DHCP DNS
  Date: 2020-05-27

  ## Status
  ✅ Accepted

  ## Context

We will need to run our [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) (Dynamic Host Configuration Protocol), [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) (Domain Name System) somewhere that support both TCP and UDP load balancing.

  ## Decision

We have decided to use AWS Elastic Container Services. ECS is a fully managed container service. There is support for TCP and UDP network traffic with AWS load balancers.

  ## Consequences

  ### Advantages

  Less administrative overhead than running virtual machines e.g. EC2 and less complexity than EKS.



  ### Disadvantages

Still need to provision the service and will need CI/CD tooling, operational documentation and forever maintaining those things.