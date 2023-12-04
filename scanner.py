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
# create a banner

print("-" * 50)
print("Scanning running: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} " is open)
        s.close()

except KeyboardInterrupt:
    print("\nExiting")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect.")
