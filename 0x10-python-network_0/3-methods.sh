#!/bin/bash
# script that displays all HTTP methods the server will accept.
curl -si -X OPTIONS "$1" | grep -i "allow" | cut -c 8-
