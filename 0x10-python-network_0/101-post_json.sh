#!/bin/bash
# Script that send a JSON POST request
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
