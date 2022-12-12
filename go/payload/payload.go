package main

import (
    "fmt"
    "net"
    "time"
)

func main() {
    // Create the packet data
    data := []byte("Hello, world!")
    // Create a connection to the gateway
    gatewayAddr := net.ParseIP("1.2.3.4")
    conn, err := net.Dial("ip:tcp", gatewayAddr.String())
    if err != nil {
        fmt.Println(err)
        return
    }
    defer conn.Close()
    // Set a deadline for writing the packet
    err = conn.SetWriteDeadline(time.Now().Add(time.Second))
    if err != nil {
        fmt.Println(err)
        return
    }
    // Write the packet to the connection, specifying the forged IP address
    forgedAddr := net.ParseIP("5.6.7.8")
    _, err = conn.WriteTo(data, &net.IPAddr{IP: forgedAddr})
    if err != nil {
        fmt.Println(err)
    }
}
