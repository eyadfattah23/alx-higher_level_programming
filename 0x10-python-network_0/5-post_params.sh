#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -s "$1"
