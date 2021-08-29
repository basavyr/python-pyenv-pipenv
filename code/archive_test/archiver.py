import os
import subprocess

# The directory in which all the files that require compression are placed into
content_directory = os.getcwd()


def ListDirectories(current_path):
    meta_files = [x for x in os.listdir(current_path)]
    if(len(meta_files)):
        return meta_files
    else:
        return 'Dirs', -1


def ListFiles(current_path):
    meta_files = [x for x in os.listdir(current_path)]
    if(len(meta_files)):
        return meta_files
    else:
        return 'Files', -1

print(ListDirectories(content_directory))
print(ListFiles(content_directory))
