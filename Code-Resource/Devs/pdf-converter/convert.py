#!/usr/bin/env python3
import os
import subprocess

subprocess.run(["python", "--version"], capture_output=False)

current_path = os.getcwd()

folders = [x for x in os.listdir(current_path) if os.path.isdir(x)]

print(folders)

for dir in folders:
    content = os.listdir(dir)
    print(content)
