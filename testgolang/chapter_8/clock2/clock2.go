//clock2 is a TCP server that periodically writes the time
package main

import (
	"io"
	"log"
	"net"
	"time"
)

func handleConn(c net.Conn) {
	defer c.Close()
	for {
		_, err := io.WriteString(c, time.Now().Format("15:04:05\n"))
		if err != nil {
			return //e.g, client disconnected
		}
		time.Sleep(1 * time.Second) //goroutine休眠1s
	}
}

func main() {
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Print(err) //e.g, connection aborted
		}
		go handleConn(conn) //go 并发
	}
}
