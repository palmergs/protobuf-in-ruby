package main

import (
	"github.com/palmergs/protobuf-in-ruby/bmore"
	"github.com/palmergs/protobuf-in-ruby/tcp"
	"fmt"
	"log"
)

func main() {
	fmt.Println("Building context...")
	context, err := bmore.New()
	if err != nil {
		log.Fatalf("Unable to build new context :: %v", err)
	}

	fmt.Println("Starting up a new service...")
	server := tcp.New(context)
	server.Listen()
}
