#!/usr/bin/env python

import paramiko

# SSH 접속 정보
hosts = ['host1', 'host2', 'host3']
username = 'user'
password = 'pass'

# 원격 컴퓨터에서 수행할 명령어
command = 'ls -al'

# SSH 접속 및 명령어 수행
for host in hosts:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())
    client.close()