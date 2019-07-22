#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browse    r using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

allMessage = []
class MessageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        htmlFile = open("Messageboard.html", 'r')
        outString=htmlFile.read()
        htmlFile.close()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(outString.encode())
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        # 2. Read the correct amount of data from the request.
        # 3. Extract the "message" field from the request data.
        # Send the "message" field back as the response.
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', '/') #This will navigate to the original page
        self.end_headers()
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len).decode()
        msg=parse_qs(post_body).get('message','')[0]
        allMessage.append(msg)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
