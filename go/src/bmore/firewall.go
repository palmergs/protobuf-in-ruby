package bmore

import (
	"fmt"
)

func Block(request *HttpRequest) *Firewall {
	if whitelisted(request) {
		return &Firewall{BlockIt: false}
	}

	if blockByIp(request) {
		return &Firewall{BlockIt: true}
	}

	if blockByParam(request) {
		return &Firewall{BlockIt: true}
	}

	fmt.Println("No firewall rules matched")
	return &Firewall{BlockIt: false}
}

func whitelisted(request *HttpRequest) bool {
	fmt.Printf("checking for whitelisted path :: %v\n", request.Path)
	return request.Path == "/secure"
}

func blockByIp(request *HttpRequest) bool {
	fmt.Printf("checking for blacklisted ip :: %v\n", request.Ip)
	return request.Ip == "123.123.123.123"
}

func blockByParam(request *HttpRequest) bool {
	fmt.Println("checking for blacklisted parameter")
  fmt.Printf("Parameters are %v\n", request.Parameters)
	pair := request.Parameters["malware"]
	if pair != nil {
		for _, value := range pair.Value {
      fmt.Printf("  examining %v (%v)\n", pair, value)
			if value == "true" {
				return true
			}
		}
	}
	return false
}
