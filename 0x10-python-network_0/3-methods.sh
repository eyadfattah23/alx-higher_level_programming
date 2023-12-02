#!/bin/bash
# script that displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i "allow" | cut -c 8-
