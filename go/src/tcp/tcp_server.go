package tcp

import (
	"bufio"
	"bytes"
	"fmt"
	"github.com/golang/protobuf/proto"
	"github.com/palmergs/protobuf-in-ruby/bmore"
	"log"
	"net"
	"time"
)

type Client struct {
	conn   net.Conn
	Server *server
}

type server struct {
	address                  string
	context                  *bmore.Context
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
			total += count
			buffer.Write(tmp)
		}

		// NOTE: this simple server has a nasty bug... if the length of the sent
		// data is exactly 4096 bytes then it will assume there's more data to read
		// and will hang while it waits.
		if err != nil || count < 4096 {
			if buffer.Len() > 0 {
				// process the message (truncated to the actual number of bytes received)
				c.Server.onNewMessage(c, buffer.Bytes()[:total])
			}
			return
		}
	}
}

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

func New(context *bmore.Context) *server {
	address := fmt.Sprintf("%s:%d", "localhost", 35678)
	log.Printf("Creating server with address: %v\n", address)
	server := &server{context: context, address: address}
	server.OnNewClient(func(c *Client) {
	})

	server.OnClientConnectionClosed(func(c *Client, err error) {
	})

	server.OnNewMessage(func(c *Client, bytes []byte) {

		message := &bmore.Activity{}
		err := proto.Unmarshal(bytes, message)
		if err != nil {
			fmt.Printf("Couldn't unmarshal message! %v\n", err)
		}

		switch message.Event.(type) {
		case *bmore.Activity_Request:
			handleHttpRequest(c, message.GetRequest())
		case *bmore.Activity_Chat:
			handleChat(c, message.GetChat())
		default:
			fmt.Println("Unknown message from agent!")
		}

		c.conn.Close()
		c.Server.onClientConnectionClosed(c, nil)
	})

	return server
}

func handleHttpRequest(c *Client, request *bmore.HttpRequest) {
	firewall := bmore.Block(request)
	marshalled, err := proto.Marshal(firewall)
	if err != nil {
		fmt.Println("Unable to send response back to agent: %v\n", err)
	} else {
		writeAndFlush(c, marshalled)
	}
}

func handleChat(c *Client, chat *bmore.Chat) {
	conversation := &bmore.Conversation{SentAt: (time.Now().UnixNano() / 1000000)}
	marshalled, err := proto.Marshal(conversation)
	if err != nil {
		fmt.Println("Unable to send conversation back to agent: %v\n", err)
	} else {
		writeAndFlush(c, marshalled)
	}
}

func writeAndFlush(c *Client, bytes []byte) {
	writer := bufio.NewWriter(c.conn)
	_, err := writer.Write(bytes)
	if err != nil {
		fmt.Println("Unable to write response to buffered writer: %v\n", err)
	} else {
		writer.Flush()
	}
}
