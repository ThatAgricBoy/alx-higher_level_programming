#!/bin/bash
# A script that displays status code of response
curl -w "$1" -s -o /dev/null
