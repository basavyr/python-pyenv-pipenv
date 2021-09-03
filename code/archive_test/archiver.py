from genericpath import isfile
import os
from posixpath import dirname
import subprocess


import shutil
import commands as cmd

# The directory in which all the files that require compression are placed into
current_directory = os.getcwd()

# Declare the required commands and parameters for creating the archive
required_command = "zip"
recurring_mode = "-r"
ignore_mode = "-x"
ignore_file = "\"*.DS_Store\""
split_mode = "-s"
split_size = "10m"  # change the size accordingly
archive_name = "content_archived"
archive_type = ".zip"


# folder in which the files are be stored
content_directory = "content/"


# folder in which copies of the splitted archives are stored
copied_directory = "copied_content/"


# add all the required flags into a list of x_arguments
required_xargs = [split_mode, split_size, ignore_mode, ignore_file,
                  recurring_mode, archive_name + archive_type, content_directory]

move_cmd = f'mv {archive_name}.z* {copied_directory}'
move_args = []  # use the flags within the command itself, since the subprocess.run command can't except *


cat_cmd = f'cat {archive_name}.z* > {copied_directory}arch.zip'
cat_args = []  # use the flags within the command itself, since the subprocess.run command can't except *


def PrepareDirectory(folder_name):
    """removes the macOS specific DS_Store file before creating the splitted archive"""
    items = os.listdir(folder_name)
    ds_store_check = [item for item in items if '.DS_Store' in item]
    # print(items)
    if(len(ds_store_check) > 0):
        # print('Found DS_Store file...')
        ds_store = items[0]
        items.remove(ds_store)  # removes from the list of files
        os.remove(folder_name + ds_store)
    else:
        pass
        # print('Found NO DS_Store file...')


def CleanArchives(dir_path, arhive_name):
    """cleans a directory from the splitted zip archives"""
    files = [x for x in os.listdir(dir_path) if f'{archive_name}' in x]
    if(len(files) == 0):
        print('No archives found...')

    for cfile in files:
        os.remove(os.path.abspath(cfile))
        # if(os.path.isfile(f'{dir_path}{cfile}')):
        #     os.remove(f'{dir_path}{cfile}')


def PurgeDirectory(dir_path):
    # removing content within a directory -> https://careerkarma.com/blog/python-delete-file/

    files = [x for x in os.listdir(
        dir_path) if os.path.isfile(f'{dir_path}/{x}')]
    # print(files)

    dirs = [x for x in os.listdir(
        dir_path) if os.path.isdir(f'{dir_path}/{x}')]
    # print(dirs)

    # step 1 -> remove the files
    for cfile in files:
        try:
            # print(f'will remove -> {dir_path}{cfile}')
            os.remove(f'{dir_path}{cfile}')
        except OSError as err:
            print(err)
            pass

    # step 2 -> remove the dirs
    for cdir in dirs:
        try:
            # print(f'will remove -> {dir_path}{cdir}')
            shutil.rmtree(f'{dir_path}{cdir}')
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


if __name__ == '__main__':
    # Step 1
    # Delete the .DS_Store file within the content directory
    PrepareDirectory(content_directory)

    # Step 2
    # Run the zip command for splitting the content directory into small chunks
    cmd.RunCommand(required_command, required_xargs, False)

    # Step 3
    # After the splitting procedure finished, pack all the chunks into a single .zip file, within a new location
    # (!!!) This procedure is moved into a separate python script
    # cmd.RunCommand(cat_cmd, cat_cmd, True)

    # Step 4
    # Remove any remaining small chunks
    # CleanArchives(current_directory, archive_name)

    # Step 5
    # Remove the copied content after the testing procedure has finished
    # PurgeDirectory(copied_directory)
