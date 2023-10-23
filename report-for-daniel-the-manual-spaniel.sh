#!/usr/bin/env bash

## Simple script to quickly review which pages have expired and which are due
## to expire in next three weeks.

function check_dependencies () {

  if ! command -v ag; then
    echo -e "\nThe silver searcher is required to run this script"
    echo -e "https://github.com/ggreer/the_silver_searcher \n"
    exit 1
  fi

  if ! command -v datediff >/dev/null 2>&1; then
    echo -e "\ndatediff is required to run this script"
    echo "it is part of 'dateutils' - install with brew or os package manager"
    echo -e "https://github.com/hroptatyr/dateutils \n"
    exit 1
  fi
}

function readlines () {
    local N="$1"
    local line
    local rc="1"

    # Read at most N lines
    for i in $(seq 1 $N)
    do
        # Try reading a single line
        read line
        if [ $? -eq 0 ]
        then
            # Output line
            echo $line
            rc="0"
        else
            break
        fi
    done

    # Return 1 if no lines where read
    return $rc
}

run_report () {
  local report
  local today
  local expiring_pages
  local expired_pages

  local last_reviewed_on
  local review_in
  local expiry
  local expiry_diff

  report=$(ag last_reviewed_on -A 1 --ignore "*.txt" --ignore "*.sh" --group)
  today=$(date '+%Y-%m-%d')
  expiring_pages="Following pages expiring in next 3 weeks:\n"
  expired_pages="Following pages have expired:\n"

  while chunk=$(readlines 4)
  do
      echo "******************************************************************************************"
      echo "$chunk"
      echo ""

      last_reviewed_on="$(echo "$chunk" | grep "last_reviewed_on" | cut -d " " -f 2)"
      echo "last_reviewed_on: ${last_reviewed_on}"

      review_in="$(echo "$chunk" | grep "review_in" | cut -d " " -f 2)"
      echo "review_in: ${review_in}"

      review_in_days=$(expr ${review_in} \* 30)
      echo "review_in_days: ${review_in_days}"

      expiry=$(date -d "${last_reviewed_on}+${review_in_days}days" '+%Y-%m-%d')
      echo "expiry: ${expiry}"

      expiry_diff=$(datediff ${today} ${expiry})
      echo "expiry_diff: ${expiry_diff}"

      page="$(echo "$chunk" | grep "source" | cut -d "/" -f1-)"

      if [[ ${expiry_diff} -gt 0 ]];then
        echo "****** fine ${page}  *****"

        if [[ ${expiry_diff} -lt 21 ]];then
          echo "****** due ${page}  *****"
          expiring_pages+="$(echo -e "\nExpiring in ${expiry_diff} days: ${page}")"
        fi
      else
        echo "****** review ${page}  *****"
        expired_pages+="$(echo -e "\nExpired ${expiry_diff} days ago: ${page}")"
      fi

      echo "******************************************************************************************"
      echo ""
      echo ""
  done  <<<"${report}"

  echo ""
  echo ""
  echo -e "${expiring_pages}"

  echo ""
  echo ""
  echo -e "${expired_pages}"
  echo ""
  echo ""
}

main() {
  check_dependencies
  run_report
}

main
