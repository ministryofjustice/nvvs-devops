# 11. Use GitHub Actions for CI/CD
Date: 2021-03-22

## Status
🤔 Proposed

## Context
A generic library of GitHub actions which the team uses are stored in the [cloud-operations-github-actions](https://github.com/ministryofjustice/cloud-operations-github-actions) repository.
 
## Decision
It has been decided that we use GitHub Actions for any new CI/CD pipelines, create issues to migrate existing AWS CodePipelines if required.

## Consequences
- we centralise our code and our CI/CD in one place.
- we reduce our costs as actions are free on public repositories
- we align with other teams in the MoJ as they move to GitHub Actions.

### Advantages
 - Ability to deploy in `test` environment even before merging to main, so that developers have the option to go back and fix before merging to main.
 - CI Pipelines live close to the code and provides a badge for the `README` so that it is easy to read the status of the pipeline.
 - GH CI Pipelines use short-lived AWS credentials using OIDC connection, so no need to store any AWS credentials anywhere.

### Disadvantages
 - Dependencies coupled with a single vendor (vendor locked)