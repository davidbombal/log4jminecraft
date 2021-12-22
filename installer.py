import subprocess
from os import path

#1. Update Kali
print("**Updating Kali!**\n")
subprocess.run(["sudo", "apt", "update"])

#2. Install Maven
# Check if Maven is installed
try:
    mvn_check = subprocess.run(["mvn", "--version"], capture_output=True)
    print("\n**Apache Maven already installed! Continuing!\n**")
except:
    print("\n**Installing Maven!**\n")
    subprocess.run(["sudo", "apt", "install", "maven"])

#3. Download JDK-8u181
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

#4. Install JDK
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

#5. Get MarshalSec repo
subprocess.run(["git", "clone", "https://github.com/mbechler/marshalsec.git"])