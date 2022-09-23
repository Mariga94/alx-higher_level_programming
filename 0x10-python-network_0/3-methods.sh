#!/bin/bash
# displays all http methods
curl -sI $1 | grep "Allow"
