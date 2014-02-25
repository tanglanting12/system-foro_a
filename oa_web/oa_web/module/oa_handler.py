#coding=utf-8

from tornado.web import RequestHandler
import os
from oa_web.config import ConfigCommon
import urlparse

def get_img_url(path):
    return urlparse.urljoin(ConfigCommon.img_http_prefix, path)

class OaHandler(RequestHandler):

    default_template_path = 'web'
    controller_path = 'controller'

    def __init__(self, *args, **kwargs):
        RequestHandler.__init__(self, *args, **kwargs)

    def get_template_path(self):
        return os.path.join(self.application.settings.get("template_path"), self.default_template_path)

    def prepare(self, *args, **kwargs):
        self.const = {
            'get_img_url': get_img_url,
        }
        super(OaHandler, self).prepare(*args, **kwargs)

    def get_int(self, name, default=0):
        try:
            return int(self.get_argument(name))
        except:
            return default