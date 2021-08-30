import subprocess


def Pack_Command(cmd, xargs):
    """
    Uses the command name and the extra arguments to create a proper shell command that will be executed within the terminal.
    """
    packed = [cmd]
    for xarg in xargs:
        packed.append(xarg)
    return packed


def RunCommand(command_name, command_xargs):
    """
    Executes the command via terminal.
    """
    cmd = command_name
    xargs = command_xargs

    packed_cmd = Pack_Command(cmd, xargs)
    print(packed_cmd)

    executed_cmd = subprocess.run(packed_cmd)

    if(executed_cmd.returncode == 0):
        print('Command executed succseffully!')
