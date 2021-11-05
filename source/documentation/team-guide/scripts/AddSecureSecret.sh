#!/bin/bash

environment=$1
name=$2
value=$3

aws ssm put-parameter --name "/<parameter-path>/$environment/$name" \
  --value "$value" \
  --type SecureString \
  --key-id '<shared-services-account-ID/the-custom-AWS KMS-key>' \
  --overwrite
