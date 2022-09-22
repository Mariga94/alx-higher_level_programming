#!/usr/bin/bash
# Takes in a URL, sends a request to the URL
# and displays the size of the body of the response
curl -s -w "%{http_code}\n" $1 ;
