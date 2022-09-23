#!/bin/bash
# Takes in a URL, sends a request to the URL
curl -s "$1" | wc -c ;
