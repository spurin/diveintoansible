#!/bin/bash

# Capture inputs, these are passed as a file to the module
source $1 >/dev/null 2>&1

# Set our variables, set default if not assigned
TARGET=${target:-127.0.0.1}

ping -c 1 ${TARGET} >/dev/null 2>/dev/null

if [ $? == 0 ];
  then
  echo "{\"changed\": true, \"rc\": 0}"
else
  echo "{\"failed\": true, \"msg\": \"failed to ping\", \"rc\": 1}"
fi
