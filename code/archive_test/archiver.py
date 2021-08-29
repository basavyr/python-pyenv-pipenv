import os
import subprocess

import commands as cmd

archive_name = "py_content_archived.zip"
folder_name = "content/"
recurring_mode = "-r"

required_command = "zip"
required_xargs = [recurring_mode, archive_name, folder_name]

cmd.RunCommand(required_command, required_xargs)

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
