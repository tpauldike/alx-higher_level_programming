#!/bin/bash
# Script sends a JSON POST request to the URL ($1) and displays the body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
