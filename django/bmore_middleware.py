import socket
import select
import os
import sys
from chat.bmore.messages_pb2 import HttpRequest, KeyValue, Firewall
from cgi import parse_qs, escape
from django.http import HttpResponse

class BmoreMiddleware(object):
    def __init__(self, app):
        print("In BmoreMiddleware init...")
        self.app = app


    def __call__(self, environ, start_response):
        print("In BmoreMiddleware call...")
        http_request = self.build_http_request(environ)
        response = self.send_message(http_request)
        if response.block_it:
            start_response("403 Not Permitted", [("content-type", "text/plain")])
            return [ b'BOOM!' ]
        else:
            return self.app(environ, start_response)

    def build_http_request(self, environ):
        print(environ)
        req = HttpRequest()
        req.request_method = environ.get('REQUEST_METHOD', 'GET')
        req.host = environ.get('SERVER_NAME', '')
        req.port = int(environ.get('SERVER_PORT', '0'))
        req.script = environ.get('SCRIPT_NAME', '')
        req.path = environ.get('PATH_INFO', '')
        req.ip = environ.get('REMOTE_ADDR', '')
        
        d = parse_qs(environ['QUERY_STRING'])
        for key in d:
            req.parameters[key].key = key
            for v in d[key]:
                req.parameters[key].value.append(v)

        return req

    def send_message(self, message):
        packed = message.SerializeToString()
        print(packed)
        firewall = Firewall()
        firewall.block_it = True
        return firewall

    def generate_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 35678))
        sock.setblocking(True)
        return sock



