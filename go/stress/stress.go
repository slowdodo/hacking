package main

import (
    "flag"
    "fmt"
    "log"
    "math/rand"
    "net"
    "time"
)

var (
    // Address and port of the VPN gateway server to use
    serverAddr = flag.String("server", "vpn_gateway_server:port", "vpn gateway server address and port")
    // Duration of the stress test in seconds
    duration = flag.Int("duration", 60, "stress test duration in seconds")
    // Maximum number of concurrent connections
    maxConns = flag.Int("maxconns", 100, "maximum number of concurrent connections")
)

func main() {
    flag.Parse()

    // Create a channel for the connections
    conns := make(chan net.Conn, *maxConns)

    // Start a goroutine to wait for new connections
    go func() {
        for {
            // Connect to the VPN gateway server
            conn, err := net.Dial("tcp", *serverAddr)
            if err != nil {
                log.Println(err)
                continue
            }
            // Add the new connection to the channel
            conns <- conn
        }
    }()

    // Perform the stress test for the specified duration
    endTime := time.Now().Add(time.Duration(*duration) * time.Second)
    for {
        // If the connection channel is not empty, send data on the connected sockets
        if len(conns) > 0 {
            select {
            case conn := <-conns:
                // Generate a random string
                rand.Seed(time.Now().UnixNano())
                data := fmt.Sprintf("test-%d\n", rand.Int())
                // Send the string on the socket
                conn.Write([]byte(data))
            default:
                // Do nothing
            }
        }

        // End the test if the specified duration has passed
        if time.Now().After(endTime) {
            break
        }
    }
}
// 