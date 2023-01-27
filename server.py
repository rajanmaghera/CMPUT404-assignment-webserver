#  coding: utf-8
import os
import socketserver
from headers import *

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# Copyright 2023 Rajan Maghera
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):

    def handle_request_extension(self):
        '''Gets the extension of the file requested and saves
        it into self.extension.'''

        self.url_bits = self.url.split("/")
        self.extension = self.url_bits[len(self.url_bits)-1].split(".")
        if len(self.extension) > 1:
            self.extension = self.extension[len(self.extension) - 1]
        else:
            self.extension = None

    def handle_request_url(self):
        '''Gets the url of the file requested and saves
        it into self.url.'''

        self.url = self.data.split()[1]
        self.url = self.url.decode('utf-8')

    def handle_request_host(self):
        '''Gets the host of the file requested and saves
        it into self.host.'''

        lines = self.data.splitlines()
        self.host = None
        for line in lines:
            if line.startswith(b"Host:"):
                self.host = line.split()[1]
                self.host = self.host.decode('utf-8')
                break


    def handle_request_type(self):
        '''Gets the type of the request and saves
        it into self.type.'''

        self.type = self.data.split()[0]

    def try_send_page(self, path_ending=False):
        '''Tries to send the page requested. If the page is not found,
        it sends a 404. If the page is found, it sends the page.'''

        if path_ending:
            self.url = self.url + "index.html"
            self.extension = "html"

        if self.extension != "css" and self.extension != "html":
            self.content_type = "application/octet-stream"
        else:
            self.content_type = "text/" + self.extension

        try:
            file = open("www" + self.url, "r")
            content = file.read()
            file.close()
            self.request.sendall(bytearray(get_200_header(content, self.content_type),'utf-8'))
        except:
            self.send_404()

    def find_file_from_url(self):
        '''Finds the file on the disk from the url. This is used to
        later determine if a 301 should be served or a 404.'''

        # if the url is a directory that has a trailing slash, look for index.html
        if self.url[len(self.url) -1] == "/":
            self.url = self.url + "index.html"

        # if the url is a directory that doesn't have a trailing slash AND has a file existing there, send 301
        if self.url[len(self.url) -1] != "/" and os.path.isdir("www" + self.url):
            self.send_301()
            return False

        # otherwise, the file is a real file, so look for it like normal
        return True


    def handle(self):
        '''Handles the request from the client. This is the main
        function that is called when the server is run.'''

        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)

        self.handle_request_type()

        if self.type != b"GET":
            self.send_405()
            return

        self.handle_request_url()

        # no relative paths are allowed in the url, this is a security risk
        split_url = self.url.split("/")
        if ".." in split_url or "." in split_url:
            # Note: I would normally send 400 here, but the tests don't like it
            self.send_404()
            return

        self.handle_request_host()
        if self.host is None:
            self.send_400()
            return

        # TODO read through questions on eClass

        if not self.find_file_from_url():
            return

        self.handle_request_extension()

        self.try_send_page()

    '''The following functions are used to send the appropriate
    HTTP response to the client.'''

    def send_404(self):
        self.request.sendall(bytearray(get_404_header(),'utf-8'))

    def send_405(self):
        self.request.sendall(bytearray(get_405_header(),'utf-8'))

    def send_400(self):
        self.request.sendall(bytearray(get_400_header(),'utf-8'))

    def send_301(self):
        self.request.sendall(bytearray(get_301_header(self.host, self.url),'utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
