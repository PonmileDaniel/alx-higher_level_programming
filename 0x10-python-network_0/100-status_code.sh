#!/bin/bash
# Script that sends a request to url passed
curl -so /dev/null -w "%{http_code}" "$1"
