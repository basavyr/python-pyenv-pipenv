#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path


subprocess.run(["python", "--version"], capture_output=False)

current_path = os.getcwd()

folders = [x for x in os.listdir(current_path) if os.path.isdir(x)]

id = 0

for dir in folders:
    content = os.listdir(dir)
    current_dir_path = os.path.join(
        os.path.relpath(os.getcwd()), os.path.relpath(dir))
    # print(current_dir_path)

    file_type = ".md"

    pdf_files = [pdf for pdf in content if ".pdf" in pdf]
    md_files = [md for md in content if file_type in md]

    pdf_file_paths = [os.path.join(
        str(current_dir_path), str(pdf_file)) for pdf_file in pdf_files]
    md_file_paths = [os.path.join(
        str(current_dir_path), str(md_file)) for md_file in md_files]

    for path in md_file_paths:
        print(path)
        subprocess.run(["pandoc", path, f"-o file{id+1}.pdf"])
        id += 1


def Get_PDF_Files(directory):
    print("this is a pdf file")
