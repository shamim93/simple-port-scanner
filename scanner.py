#!/bin/python3
import sys
import socket
from datetime import datetime


#  define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip address>")
