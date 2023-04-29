#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept
curl "$1" -sH "X-School-User-Id: 98"
