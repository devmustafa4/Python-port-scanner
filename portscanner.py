#!/bin/python

import sys 
import socket
from datetime import datetime

# function to check if the entered ip address is valid
def valid(ip):
    # checks if every octect in the ip address is in the range of 0-255
    octects = [int (x) for x in ip.split(".")]
    for x in octects:
        if 0 > x or x > 255:
            return False;
    return True;

# variable to keep track of whether the entered ip address is valid or not
valid_ip = False;
#Defining the target
if len(sys.argv) == 2:
    ip = sys.argv[1]
    if (valid(ip)):
        valid_ip = True
        target = socket.gethostbyname(ip) # translate hostname to IPv4
    else:
        print("Invalid IP address.")
else:
    print("Invalid amount of arguments.")
    print("The syntax is: python3 scanner.py <ip>")

if (valid_ip):
    # Printing messages
    print("Scanning target "+target)
    print("Time started: "+str(datetime.now()))

    try:
        for port in range(0,1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # set the default time out for connect request
            # if the response is not recieved in 1 second then stop waiting
            socket.setdefaulttimeout(1)
            # try to connect to the IP address and port
            result = s.connect_ex((target, port)) # if the port is open it returns 0 else throws an error
            if result == 0:
                print("Port "+ port +" is open")
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
