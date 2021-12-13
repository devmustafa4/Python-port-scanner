#!/bin/python

import sys
import socket
from datetime import datetime

# function to check if the entered ip address is valid


def valid(ip):
    # checks if every octect in the ip address is in the range of 0-255
    octects = [int(x) for x in ip.split(".")]

    if len(octects) != 4:
        return False

    for x in octects:
        if 0 > x or x > 255:
            return False

    return True


# variable to keep track of whether the entered ip address is valid or not
valid_ip = False
# Defining the target
if len(sys.argv) == 2:
    ip = sys.argv[1]
    if (valid(ip)):
        valid_ip = True
        target = socket.gethostbyname(ip)  # translate hostname to IPv4
    else:
        print("Invalid IP address.")
else:
    print("Invalid amount of arguments.")
    print("The syntax is: python3 scanner.py <ip>")

if (valid_ip):
    # Get the min and max ports to scan
    min_port = int(input("Enter the min port no. to scan: "))
    max_port = int(input("Enter the max port no. to scan: "))

    # Printing messages
    print("Scanning target "+target)
    print("Time started: "+str(datetime.now()))

    if 0 <= min_port <= 65535 and 0 <= max_port <= 65535:
        try:
            for port in range(min_port,max_port+1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # set the default time out for connect request
                # if the response is not recieved in 1 second then stop waiting
                socket.setdefaulttimeout(1)
                # try to connect to the IP address and port
                result = s.connect_ex((target, port)) # if the port is open it returns 0 else throws an error
                if result == 0:
                    print("Port "+ str(port) +" is open")
                s.close()
            print("Time ended: "+str(datetime.now()))

        except KeyboardInterrupt:
            # when ctrl+c is pressed
            print("\nThe program has been terminated")
            sys.exit()

        except socket.gaierror:
            # if DNS fails to resolve the DNS
            print("Hostname could not be resolved")
            sys.exit()

        except socket.error:
            # if we cannot connect to the IP address
            print("Could not connect to server.")
            sys.exit()
