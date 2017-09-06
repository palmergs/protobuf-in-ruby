package main

import (
	//	"chat/bmore"
	"chat/tcp"
	"fmt"
)

func main() {
	fmt.Println("Starting up a new service...")
	server := tcp.New()
	server.Listen()
}
