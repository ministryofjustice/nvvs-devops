#!/bin/bash

environment=$1
name=$2
value=$3

aws ssm put-parameter --name "/<parameter-path>/$environment/$name" \
  --value "$value" \
  --type String \
  --overwrite
