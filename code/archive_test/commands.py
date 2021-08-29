import subprocess


def Unpack_Command(cmd, xargs):
    unpacked = [cmd]
    for xarg in xargs:
        unpacked.append(xarg)
    return unpacked


def RunCommand(command_name, command_xargs):
    cmd = command_name
    xargs = command_xargs
    executed_cmd = subprocess.run([cmd])
    # if(len(xargs) == 0):
    if(executed_cmd.returncode == 0):
        print('Command executed succesfully')
