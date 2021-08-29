import subprocess


def RunCommand(command_name):
    cmd = command_name
    executed_cmd = subprocess.run(["ls"])
    if(executed_cmd.returncode == 0):
        print('Command executed succesfully')
        # print(executed_cmd)
