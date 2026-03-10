#!/bin/bash
URL="http://localhost:4499"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS" -eq 200 ]; then
  echo "APP STATUS: UP (200 OK)"
else
  echo "APP STATUS: DOWN (Status: $STATUS)"
fi