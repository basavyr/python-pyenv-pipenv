import subprocess
import operator


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

    print(f'Running the command -> {packed_cmd}')

    executed_cmd = subprocess.run(packed_cmd, capture_output=True, text=True)

    error_in_zip_cmd = operator.contains(executed_cmd.stdout, 'error')
    warning_in_zip_cmd = operator.contains(executed_cmd.stdout, 'warning')

    if(error_in_zip_cmd == True or warning_in_zip_cmd == True):
        print('Zipping encountered issues')

    if(executed_cmd.stderr == ''):
        print('Command executed successfully!')
