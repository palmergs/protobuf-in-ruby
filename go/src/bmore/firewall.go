package bmore

import (
	"fmt"
)

func Block(request *HttpRequest) *Firewall {
	printRequest(request)

	if whitelisted(request) {
		fmt.Println("SAFE (whitelist)")
		return &Firewall{BlockIt: false}
	}

	if blockByIp(request) {
		fmt.Println("BLOCKED (ip)")
		return &Firewall{BlockIt: true}
	}

	if blockByParam(request) {
		fmt.Println("BLOCKED (param)")
		return &Firewall{BlockIt: true}
	}

	fmt.Println("SAFE")
	return &Firewall{BlockIt: false}
}

func printRequest(request *HttpRequest) {
	fmt.Printf("ip:%v host:%v port:%v method:%v script:%v path:%v => ",
		request.Ip,
		request.Host,
		request.Port,
		request.RequestMethod,
		request.Script,
		request.Path)
}

func whitelisted(request *HttpRequest) bool {
	return request.Path == "/secure"
}

func blockByIp(request *HttpRequest) bool {
	return request.Ip == "123.123.123.123"
}

func blockByParam(request *HttpRequest) bool {
	pair := request.Parameters["malware"]
	if pair != nil {
		for _, value := range pair.Value {
			if value == "true" {
				return true
			}
		}
	}
	return false
}
