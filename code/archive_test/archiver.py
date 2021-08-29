import os
import subprocess

# The directory in which all the files that require compression are placed into
content_directory = os.getcwd()

for meta_file in os.listdir(content_directory):
    current_path = meta_file
    if(os.path.isdir(current_path)):
        print(current_path)
