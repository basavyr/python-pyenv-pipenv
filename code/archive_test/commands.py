import subprocess


def Pack_Command(cmd, xargs):
    unpacked = [cmd]
    for xarg in xargs:
        unpacked.append(xarg)
    return unpacked


def RunCommand(command_name, command_xargs):
    cmd = command_name
    xargs = command_xargs

    packed_cmd = Pack_Command(cmd, xargs)
    print(packed_cmd)

    executed_cmd = subprocess.run(packed_cmd)

    # return executed_cmd.returncode
