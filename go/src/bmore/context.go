package bmore

import (
	"fmt"
)

type Context struct {
}

func New() (*Context, error) {
	fmt.Println("Creating context...")
	context := &Context{}
	return context, nil
}
