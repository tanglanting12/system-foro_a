#coding=utf-8

from oa_web.module.oa_handler import OaHandler
from oa_web.module.route import Route

@Route('/test/(\w+)/?')
class TestPage(OaHandler):

    def get(self, name):

        return self.render(template_name='test.html', name=name)
