from pages import *

def get_http_date():
    import time
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())

def get_200_header(content, type):
    return f"""HTTP/1.1 200 OK\r
Date: {get_http_date()}\r
Server: MyCoolCMPUT404Server/1.0\r
Content-Type: text/{type}; charset=UTF-8\r
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