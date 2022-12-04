package main

import (
    "flag"
    "log"
    "math/rand"
    "net"
    "sync"
    "time"
)

var (
    // Address and port of the VPN gateway server to use
    serverAddr = flag.String("server", "vpn_gateway_server:port", "vpn gateway server address and port")
    // Duration of the stress test in seconds
    duration = flag.Int("duration", 60, "stress test duration in seconds")
    // Maximum number of concurrent connections
    maxConns = flag.Int("maxconns", 100, "maximum number of concurrent connections")
    // Number of threads to use
    numThreads = flag.Int("threads", 10, "number of threads to use")
)

func main() {
    flag.Parse()

    // Create a channel for the connections
    conns := make(chan net.Conn, *maxConns)

    // Create a wait group for the threads
    var wg sync.WaitGroup

    // Start the threads
    for i := 0; i < *numThreads; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
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
    }

    // Perform the stress test for the specified duration
    endTime := time.Now().Add(time.Duration(*duration) * time.Second)
    for {
        // If the connection channel is not empty, send SYN packets on the connected sockets
        if len(conns) > 0 {
            select {
            case conn := <-conns:
                // Generate a random source port
                rand.Seed(time.Now().UnixNano())
                srcPort := rand.Intn(65536)
                // Construct the SYN packet
                syn := &net.IP{
                    Version: 4,
                    TOS:     0,
                    ID:      0,
                    Flags:   0,
                    FragOff: 0,
                    TTL:     64,
                    Protocol: 6,
                    Src:     net.IP{},
                    Dst:     net.IP{},
                }
                syn.Src = conn.LocalAddr().(*net.TCPAddr).IP
				syn.Dst = conn.RemoteAddr().(*net.TCPAddr).IP
				syn.Tcp = &net.TCP{
					SrcPort: srcPort,
					DstPort: conn.RemoteAddr().(*net.TCPAddr).Port,
					Seq:     0,
					Ack:     0,
					DataOff: 5,
					Flags:   0x02, // SYN
					Window:  0,
					Urg:     0,
					Payload: []byte{},
				}
				// Encode the SYN packet
				synEncoded, err := syn.Marshal()
				if err != nil {
					log.Println(err)
					continue
				}
				// Send the SYN packet
				_, err = conn.Write(synEncoded)
				if err != nil {
					log.Println(err)
					continue
				}
			}
		}
	}
}

// go run stress_test.go -server vpn.example.com:8080 -duration 60 -maxconns 100 -threads 10
