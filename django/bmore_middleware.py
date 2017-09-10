import socket
import select
import os
import io
import sys
from chat.bmore.messages_pb2 import Activity, HttpRequest, KeyValue, Firewall
from cgi import parse_qs, escape
from django.http import HttpResponse

class BmoreMiddleware(object):
    def __init__(self, app):
        print("In BmoreMiddleware init...")
        self.app = app


    def __call__(self, environ, start_response):
        print("In BmoreMiddleware call...")
        message = self.build_message_from(environ)
        response = self.send_message(message)
        if response.block_it:
            start_response("403 Not Permitted", [("content-type", "text/plain")])
            return [ b'BOOM!' ]
        else:
            return self.app(environ, start_response)

    def build_message_from(self, environ):
        activity = Activity()
        activity.request.request_method = environ.get('REQUEST_METHOD', "GET")
        activity.request.host = environ.get('SERVER_NAME', "")
        activity.request.port = 8000 # int(environ.get('SERVER_PORT', "0"))
        activity.request.script = environ.get('SCRIPT_NAME', "")
        activity.request.path = environ.get("PATH_INFO", "")
        activity.request.ip = environ.get('REMOTE_ADDR', "")
        
        d = parse_qs(environ['QUERY_STRING'])
        for key in d:
            activity.request.parameters[key].key = key
            for v in d[key]:
                activity.request.parameters[key].value.append(v)

        return activity

    def send_message(self, message):
        print(message)        
        
        packed = message.SerializeToString()
        try:
            sock = self.generate_socket()
            count = sock.send(packed)
            print("I think I sent...", count)
            received = self.receive_data(sock)

            firewall = Firewall()
            firewall.ParseFromString(received)
            print(firewall)
            return firewall
        finally:
            if sock is not None:
                sock.close()
        
    def receive_data(self, sock):
        print("In receive data...")
        buf = bytearray()
        byte_count = sock.recv_into(buf)
        print(byte_count)
        return buf

    def generate_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 35678))
        sock.setblocking(True)
        return sock



