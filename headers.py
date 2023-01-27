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

'''This module contains methods to generate the headers and pages that are sent to the client.'''

from pages import *

def get_http_date():
    '''Returns the current date in the format required by HTTP.'''
    import time
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())

def get_200_header(content, type):
    return f"""HTTP/1.1 200 OK\r
Date: {get_http_date()}\r
Server: MyCoolCMPUT404Server/1.0\r
Content-Type: {type}; charset=UTF-8\r
Content-Length: {len(content)}\r

{content}"""


def get_404_header():
    return f"""HTTP/1.1 404 Not Found\r
Date: {get_http_date()}\r
Server: MyCoolCMPUT404Server/1.0\r
Content-Type: text/html; charset=UTF-8\r
Content-Length: {len(PAGE404)}\r

{PAGE404}"""

def get_405_header():
    return f"""HTTP/1.1 405 Method Not Allowed\r
Date: {get_http_date()}\r
Server: MyCoolCMPUT404Server/1.0\r
Content-Type: text/html; charset=UTF-8\r
Content-Length: {len(PAGE405)}\r

{PAGE405}"""

def get_301_location(host, original_url):
    '''Returns the location of the 301 redirect.'''
    return host + original_url + "/"

def get_301_header(host, original_url):
    return f"""HTTP/1.1 301 Moved Permanently\r
Location: http://{get_301_location(host, original_url)}\r
"""

def get_400_header():
    return f"""HTTP/1.1 400 Bad Request\r
Date: {get_http_date()}\r
Server: MyCoolCMPUT404Server/1.0\r
Content-Type: text/html; charset=UTF-8\r
Content-Length: {len(PAGE400)}\r

{PAGE400}"""