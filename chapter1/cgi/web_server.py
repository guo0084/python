#!/usr/bin/python3.5
"""
Use python to implement one HTTP web server, it knows how to run cgi script on server;
It provides files and scripts from current direction, python script must saved on webdir\cgi-bin or webdir\htbin.
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port   = 12306

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
