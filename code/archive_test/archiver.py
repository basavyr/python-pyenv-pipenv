from genericpath import isfile
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
folder_name = "content/"  # folder in which the files must be stored

required_xargs = [split_mode, split_size, ignore_mode, ignore_file,
                  recurring_mode, archive_name + archive_type, folder_name]

# cmd.RunCommand(required_command, required_xargs)


def PrepareDirectory(folder_name):
    """removes the macOS specific DS_Store file before creating the splitted archive"""
    x = os.listdir(folder_name)
    print(x)
    if('DS' in x[0]):
        ds_store = x[0]
        x.remove(ds_store)
    print(x)


def CleanDirectory(current_path):
    """cleans the directory in which the files required for archiving are stored"""
    archive_name = 'content_archived'
    files = [x for x in os.listdir(current_path) if f'{archive_name}' in x]
    if(len(files) == 0):
        print('No archives found...')
    for x_file in files:
        if(os.path.isfile(x_file)):
            print(f'would remove -> {x_file}')
            os.remove(x_file)


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


# PrepareDirectory(folder_name)
CleanDirectory(os.getcwd())
