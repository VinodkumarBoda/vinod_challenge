#!/bin/bash
DOMAINS=("www.demo.com")

LEN=${#DOMAINS[@]}
echo "1..${LEN}" >results.tap
for (( i=0; i<${LEN}; i++ ));
do
  echo Testing ${DOMAINS[$i]}
  DIG=$("curl")
  if [[ "$DIG" == "200" ]]; then
    echo "$DIG  Working"
  else
    echo "$DIG Not Working"
  fi
done
