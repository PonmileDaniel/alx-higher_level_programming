#!/bin/bash
# Sends a request and display the size 
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2