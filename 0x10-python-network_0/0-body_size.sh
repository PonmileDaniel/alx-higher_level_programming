#!/bin/bash
# Sends a request and display the size 
curl -sI "$1" | wc -c