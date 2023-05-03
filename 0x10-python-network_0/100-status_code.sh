#!/bin/bash
# Sends a request to '$1' and displays only the status code
curl -sLw "%{http_code}" -o /dev/null "$1"
