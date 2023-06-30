#!/bin/bash
# A script that displays the size of the body of the response
curl -s -o /dev/null -w "%{http_code}\n" "$1" | [ "$(cat)" = "200" ] && curl -s "$1"
