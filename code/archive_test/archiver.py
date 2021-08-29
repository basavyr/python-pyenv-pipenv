import os
import subprocess

import commands as cmd

required_command = "zip"

required_xargs = ["--v"]

cmd.RunCommand(required_command, required_xargs)

print(cmd.Unpack_Command(required_command, required_xargs))

# The directory in which all the files that require compression are placed into
content_directory = os.getcwd()


def ListDirectories(current_path):
    meta_files = [x for x in os.listdir(current_path)]

    dirs = [x for x in meta_files if os.path.isdir(x)]

    if(len(dirs)):
        return dirs
    else:
        return 'Dirs -> ', -1


def ListFiles(current_path):
    meta_files = [x for x in os.listdir(current_path)]

    files = [x for x in meta_files if os.path.isfile(x)]

    if(len(files)):
        return files
    else:
        return 'Files', -1


# print(ListDirectories(content_directory))
# print(ListFiles(content_directory))
