#!/bin/bash
#Get content-length of http headers
curl -s "$1" | wc -c
