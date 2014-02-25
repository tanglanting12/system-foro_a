#!/usr/bin/python
#coding=utf8
from oa_web.settings import settings
import tornado.web, tornado.httpserver
from tornado.options import define, parse_command_line, options
from oa_web.module.route import Route
from oa_web.libs.log import add_tornado_log_handler
from oa_web.config import ConfigCommon


define("port", type=int, default=9000,
       help="the server port")
define("address", type=str, default='127.0.0.1',
       help="the server address")
parse_command_line()

add_tornado_log_handler(ConfigCommon.log_path, ConfigCommon.log_level)
urls = Route.routes()

application = tornado.web.Application(urls, **settings)
app_server = tornado.httpserver.HTTPServer(application, xheaders=True)
app_server.listen(options.port, options.address)
tornado.ioloop.IOLoop.instance().start()
