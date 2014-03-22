#
#!/usr/bin/env python
import os
import sys
 
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from oa_admin.init import init_django_settings
init_django_settings()
 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
 
define('port', type=int, default=8088)
 
def main():
    parse_command_line()
 
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())
 
    tornado_app = tornado.web.Application(
        [('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == '__main__':
    main()
