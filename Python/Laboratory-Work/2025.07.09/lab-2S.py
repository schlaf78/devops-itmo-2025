import paramiko
from getpass import getpass
import os

def get_config_via_ssh(hostname, username, password, command="uname -a", port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command(command)
    result = stdout.read().decode()
    client.close()
    return result

if __name__ == "__main__":
    host = "localhost"
    user = input("Enter username: ")
    password = getpass("Enter password: ")

    commands = [
        "cat /etc/os-release",
        "sw_vers",
        "whoami",
        "ifconfig",
        "df -H"
    ]

    results = []

    for cmd in commands:
        output = get_config_via_ssh(host, user, password, command=cmd)
        results.append(f"\n===== {cmd} =====\n{output.strip()}")

    full_output = "\n".join(results)

    file_path = os.path.join(os.getcwd(), f"{host}_config.txt")
    with open(file_path, "w") as f:
        f.write(full_output)

    print(f"\n Инвентаризация {host} сохранена в: {file_path}")
