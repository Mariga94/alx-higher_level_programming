#!/usr/bin/bash
# Takes in a URL, sends a request to the URL
# and displays the size of the body of the response
curl -sb -H "Accept: application/json" -r 0-15000  $1 ;
