import os
import subprocess

import commands as cmd

# The directory in which all the files that require compression are placed into
content_directory = os.getcwd()


# Declare the required commands and parameters for creating the archive
required_command = "zip"
recurring_mode = "-r"
ignore_mode = "-x"
ignore_file = "\"*.DS_Store\""
split_mode = "-s"
split_size = "5m"
archive_name = "content_archived"
archive_type = ".zip"
folder_name = "content/"

required_xargs = [split_mode, split_size, ignore_mode, ignore_file,
                  recurring_mode, archive_name + archive_type, folder_name]

# cmd.RunCommand(required_command, required_xargs)


def DeleteArchive(archive):
    cmd_name = "rm"
    cmd_xargs = ["-rf", f'{archive}.z*']
    packed_cmd = cmd.Pack_Command(cmd_name, cmd_xargs)
    print(packed_cmd)
    cmd.RunCommand(cmd_name,cmd_xargs)


DeleteArchive(archive_name)


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
