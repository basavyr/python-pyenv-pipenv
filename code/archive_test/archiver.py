from genericpath import isfile
import os
from posixpath import dirname
import subprocess


import shutil
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
copied_directory = "copied_content/"


required_xargs = [split_mode, split_size, ignore_mode, ignore_file,
                  recurring_mode, archive_name + archive_type, folder_name]

# cmd.RunCommand(required_command, required_xargs)


def PrepareDirectory(folder_name):
    """removes the macOS specific DS_Store file before creating the splitted archive"""
    items = os.listdir(folder_name)
    ds_store_check = [item for item in items if '.DS_Store' in item]
    # print(items)
    if(len(ds_store_check) > 0):
        print('Found DS_Store file...')
        ds_store = items[0]
        items.remove(ds_store)  # removes from the list of files
        os.remove(folder_name + ds_store)
    else:
        print('Found NO DS_Store file...')


def CleanDirectory(current_path):
    """cleans the directory in which the files required for archiving are stored"""
    archive_name = 'content_archived'
    files = [x for x in os.listdir(current_path) if f'{archive_name}' in x]
    if(len(files) == 0):
        print('No archives found...')
    for x_file in files:
        if(os.path.isfile(x_file)):
            # print(f'would remove -> {x_file}')
            os.remove(x_file)


def PurgeDirectory(dir_path):
    files = [x for x in os.listdir(dir_path) if os.path.isfile(x)]
    dirs = [x for x in os.listdir(dir_path) if os.path.isdir(x)]
    # step 1 -> remove the files
    print(files)
    for file in files:
        try:
            os.remove(f'{dir_path}/{file}')
        except OSError as err:
            print(err)
            pass
    # step 2 -> remove the dirs
    print(dirs)
    for cdir in dirs:
        try:
            # os.remove(cdir)
            shutil.rmtree(f'{dir_path}/{cdir}')
        except OSError as err:
            print(err)
            pass


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
# cmd.RunCommand(required_command, required_xargs)
# CleanDirectory(content_directory)
PurgeDirectory(copied_directory)
