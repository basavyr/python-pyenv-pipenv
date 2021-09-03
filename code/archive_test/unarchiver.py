from genericpath import isdir, isfile
import os
import shutil
import subprocess

import commands
import archiver


def Unzip(copied_directory, archive_name):
    unzip_cmd = "unzip"
    unzip_args = [f'{copied_directory}{archive_name}']

    # packed_unzip = PackCommand(unzip_cmd, unzip_args)
    commands.RunCommand(unzip_cmd, unzip_args, True)


def PackCommand(cmd_name, cmd_args):

    if(len(cmd_args) == 0):
        print('Running the cat process without any extra flags...')

    packed_cmd = [cmd_name]

    for xarg in cmd_args:
        packed_cmd.append(xarg)

    return packed_cmd


def CatProcess(copied_directory, archive_name, packed_gem):
    """
    Define the cat command which packs the zipped chunks into a single file.
    The cat command takes the chunks and creates a single "gem" within a pre-configured location
    """

    cat_cmd = f'cat {archive_name}.z* > {copied_directory}{packed_gem}'
    cat_xargs = []

    files = [x for x in os.listdir(os.getcwd()) if os.path.isfile(x)]
    print(files)

    # checks wether there are chunks present within the current working directory
    check_chunks = archiver.archive_name + archiver.archive_type in files
    print(f'Chunk presence -> {check_chunks}')

    # check if the copied directory exists or not
    dirs = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]
    if (copied_directory in dirs):
        pass
        # print('copied folder exists')
    else:
        # print('copied folder does not exist')
        try:
            os.mkdir(copied_directory)
        except FileExistsError:
            pass

    # use a True shell state in order to consider the wildcard * when packing multiple chunks with the same name
    if(check_chunks):
        commands.RunCommand(cat_cmd, cat_xargs, True)


if __name__ == '__main__':
    CatProcess(archiver.copied_directory,
               archiver.archive_name, archiver.packed_gem)
    # archiver.CleanArchives(archiver.current_directory, archiver.archive_name)
    # Unzip(archiver.copied_directory, archiver.packed_gem)
    # archiver.PurgeDirectory(archiver.copied_directory)
