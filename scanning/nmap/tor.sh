#!/usr/bin/env nmap

# This nmap script performs a scan using the tor gateway.

# Check for IP address
if [ -z "$1" ]; then
  echo "Please specify an IP address"
  exit
fi

# Set the tor gateway
gateway="127.0.0.1"

# Perform the scan using the tor gateway
nmap -A -O -sS --proxies http:$gateway:9050 $1