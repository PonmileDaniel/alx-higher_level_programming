#!/bin/bash
#Sends a request and display the size 
curl -s "$1" | wc -c
