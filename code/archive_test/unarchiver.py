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
    define the cat command which packs the zipped chunks into a single file
    """

    cat_cmd = f'cat {archive_name}.z* > {copied_directory}'
    cat_xargs = []

    # use a True shell state in order to consider the wildcard * when packing multiple chunks with the same name
    commands.RunCommand(cat_cmd, cat_xargs, True)


CatProcess(archiver.copied_directory, archiver.archive_name)
