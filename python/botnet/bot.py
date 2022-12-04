import paramiko

# 접속할 컴퓨터의 IP 주소 및 SSH 접속 정보
hosts = [
    {"hostname": "192.168.0.1", "username": "user1", "password": "password1"},
    {"hostname": "192.168.0.2", "username": "user2", "password": "password2"},
    {"hostname": "192.168.0.3", "username": "user3", "password": "password3"},
]

# 수행할 명령어
command = "ls -al"

# 컴퓨터를 반복하여 접속하고 명령어를 실행합니다.
for host in hosts:
    # SSH 접속을 시도합니다.
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())