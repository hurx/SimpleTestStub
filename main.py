# -*-encoding:utf-8-*-

import BaseHTTPServer
from httpserverhandler.httpserver import HTTPServerHandler


if __name__ == "__main__":
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('127.0.0.1', 8083), HTTPServerHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
