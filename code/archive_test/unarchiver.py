from genericpath import isdir
import os
import shutil
import subprocess

import commands
import archiver


def PackCommand(cmd_name, cmd_args):

    if(len(cmd_args) == 0):
        print('Running the cat process without any extra flags...')

    packed_cmd = [cmd_name]

    for xarg in cmd_args:
        packed_cmd.append(xarg)

    return packed_cmd


def CatProcess(copied_directory, archive_name):
    """
    Define the cat command which packs the zipped chunks into a single file.
    The cat command takes the chunks and creates a single "gem" within a pre-configured location
    """

    packed_gem = "unpacked.zip"

    cat_cmd = f'cat {archive_name}.z* > {copied_directory}{packed_gem}'
    cat_xargs = []

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
    commands.RunCommand(cat_cmd, cat_xargs, True)


if __name__ == '__main__':
    CatProcess(archiver.copied_directory, archiver.archive_name)
    archiver.CleanArchives(archiver.current_directory, archiver.archive_name)
