import subprocess


def RunCommand(command_name):
    cmd = command_name
    executed_cmd = subprocess.run(["zip", "-v"])
    print(executed_cmd.stdout)
