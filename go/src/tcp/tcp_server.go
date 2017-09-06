package tcp

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"net"
)

type Client struct {
	conn   net.Conn
	Server *server
}

type server struct {
	address                  string
	onNewClientCallback      func(c *Client)
	onClientConnectionClosed func(c *Client, err error)
	onNewMessage             func(c *Client, message []byte)
}

func (c *Client) listen() {
	reader := bufio.NewReader(c.conn)
	total := 0
	tmp := make([]byte, 4096)
	var buffer bytes.Buffer
	for {
		count, err := reader.Read(tmp)
		if count > 0 {
			fmt.Printf("Read %d bytes...\n", count)
			total += count
			buffer.Write(tmp)
		}

		if err != nil {
			if buffer.Len() > 0 {
				// process the message (truncated to the actual number of bytes received)
				c.Server.onNewMessage(c, buffer.Bytes()[:total])
			}
			return
		}
	}
}

//func (c *Client) Send(message string) error {
//	_, err := c.conn.Write([]byte(message))
//	return err
//}

//func (c *Client) SendBytes(b []byte) error {
//	_, err := c.conn.Write(b)
//	return err
//}

func (c *Client) Conn() net.Conn {
	return c.conn
}

func (c *Client) Close() error {
	return c.conn.Close()
}

func (s *server) OnNewClient(callback func(c *Client)) {
	s.onNewClientCallback = callback
}

func (s *server) OnClientConnectionClosed(callback func(c *Client, err error)) {
	s.onClientConnectionClosed = callback
}

func (s *server) OnNewMessage(callback func(c *Client, message []byte)) {
	s.onNewMessage = callback
}

func (s *server) Listen() {
	listener, err := net.Listen("tcp", s.address)
	if err != nil {
		log.Fatal("Error starting TCP service")
	}
	defer listener.Close()

	for {
		conn, _ := listener.Accept()
		client := &Client{conn: conn, Server: s}
		go client.listen()
		s.onNewClientCallback(client)
	}
}

func New() *server {
	address := fmt.Sprintf("%s:%d", "localhost", 35555)
	log.Printf("Creating server with address: %v\n", address)
	server := &server{address: address}
	server.OnNewClient(func(c *Client) {
		fmt.Println("A new client connected!")
	})

	server.OnClientConnectionClosed(func(c *Client, err error) {
		fmt.Printf("A client connection was closed! err=%v\n", err)
	})

	server.OnNewMessage(func(c *Client, bytes []byte) {
		fmt.Printf("Message received: %v [%d]\n", bytes[0:10], len(bytes))

		// message := &bmore.Message{}
		// err := proto.Unmarshal(bytes, message)
		// if err != nil {
		// 	fmt.Printf("Couldn't unmarshal message! %v\n", err)
		// }

		c.conn.Close()
		c.Server.onClientConnectionClosed(c, nil)
	})

	return server
}
