  # 8. Use AWS SSO for AWS Account Access
  Date: 2021-05-01

  ## Status
  ✅ Accepted

  ## Context

We need to use Single Sign On to access all our AWS accounts. We currently use AzureAD to secure our user facing services portals.

  ## Decision

We will use the [Modernisation Platforms](https://github.com/ministryofjustice/modernisation-platform) implementation of  [AWS Single Sign On](https://user-guide.modernisation-platform.service.justice.gov.uk/concepts/environments/single-sign-on.html#single-sign-on). It requires the use of a MoJ Org GitHub account but that requirement only further facilitates the use of deploymening infrastructure as code within our AWS accounts.

### Alternative Considerations: 
#### AzureAD
AzureAD is currently managed externally, this means that automations of group and accounts are not possible.