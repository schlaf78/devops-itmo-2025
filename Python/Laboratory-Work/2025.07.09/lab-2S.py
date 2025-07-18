import paramiko
from getpass import getpass

def get_config_via_ssh(hostname, username, password, command="uname -a", port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    result = stdout.read().decode()
    client.close()
    return result

if __name__ == "__main__":
    host = "localhost"
    user = input("Enter username: ")
    password = getpass("Enter password: ")

    commands = ["cat /etc/os-release", "sw_vers", "whoami", "ifconfig", "df -H"]
    full_output = ""

    for cmd in commands:
        output = get_config_via_ssh(host, user, password, command=cmd)
    print (f"Device inventory of {cmd}':\n{output}")
    #print("\nКонфигурация устройства (localhost):\n")
    #print(output)

    with open("localhost_config.txt", "w") as f:
        f.write(output)
