import paramiko as pmiko
import csv
from api_lesson.utilities.configuration import *


# Start Connection
username = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['Server']['port']
ssh = pmiko.SSHClient()
ssh.set_missing_host_key_policy(pmiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# Run Commands
# stdin, stdout, stderr = ssh.exec_command("ls -a")
stdin, stdout, stderr = ssh.exec_command("cat demofile")
lines = stdout.readlines()
# print(lines[1])

# Upload files to the linux server

# script file
sftp = ssh.open_sftp()
destination_path = "script.py"
local_path = "D:/Selenium_Python/pythonProject/api_lesson/batch_files/script.py"
sftp.put(local_path, destination_path)

# csv file
destination_path = "loanasa.csv"
local_path = "D:/Selenium_Python/pythonProject/api_lesson/batch_files/loanasa.csv"
sftp.put(local_path, destination_path)

# Execute python command for the script file
ssh.exec_command("python script.py")

# Download the file to the local system
sftp.get("loanasa.csv", "output_files/loanasa.csv")

# Parse the output csv file
with open("D:/Selenium_Python/pythonProject/api_lesson/output_files/loanasa.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] == "32321":
            assert row[1] == 'approved'

ssh.close()
