#!/bin/bash
# displays only the status code
curl -s -w '%{http_code}' $1;
