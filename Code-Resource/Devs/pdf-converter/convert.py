#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path


subprocess.run(["python", "--version"], capture_output=False)

current_path = os.getcwd()

folders = [x for x in os.listdir(current_path) if os.path.isdir(x)]

for dir in folders:
    content = os.listdir(dir)
    current_dir_path = os.path.join(
        os.path.relpath(os.getcwd()), os.path.relpath(dir))
    # print(current_dir_path)

    pdf_files = [pdf for pdf in content if ".pdf" in pdf]
    pdf_file_paths = [os.path.join(
        str(current_dir_path), str(pdf_file)) for pdf_file in pdf_files]
    for path in pdf_file_paths:
        print(path)
        # subprocess.run(["python", "convert.py", path], capture_output=False)
    # for pdf_file in pdf_files:
    # print(os.path.join(str(current_dir_path), str(pdf_file)))


def Get_PDF_Files(directory):
    print("this is a pdf file")
