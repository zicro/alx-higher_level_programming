#!/usr/bin/python3
"""Sends a POST req to URL with an email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    v = {"email": sys.argv[2]}
    d = urllib.parse.urlencode(v).encode("ascii")

    request = urllib.request.Request(url, d)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
