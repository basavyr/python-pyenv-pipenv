#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path


subprocess.run(["python", "--version"], capture_output=False)

current_path = os.getcwd()

folders = [x for x in os.listdir(current_path) if os.path.isdir(x)]

for dir in folders:
    content = os.listdir(dir)
    current_dir_path = os.path.abspath(dir)
    for file in content:
        print(os.path.join(str(current_dir_path), str(file)))

    # pdf_files = [pdf for pdf in content if ".pdf" in pdf]
    # for pdf in pdf_files:
    # print("FilePath:", Path(pdf).parent.absolute())
    # print(os.path.abspath(pdf))


def Get_PDF_Files(directory):
    print("this is a pdf file")
