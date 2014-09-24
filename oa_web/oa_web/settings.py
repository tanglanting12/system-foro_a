#!/usr/bin/python
#coding=utf8

import os, sys
from oa_admin.init import init_django_settings
from oa_web.controller import init_controllers
from oa_web.config import ConfigCommon
init_django_settings()

#import allmoudles which directory under the settings'path   include decorated function
init_controllers()
from controller.web.modelshtml import *

PYWEB_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(PYWEB_PATH)
sys.path.insert(0, PROJECT_PATH)

settings = {
    "debug": ConfigCommon.debug,
    "static_path": os.path.join(PYWEB_PATH, "resource"),
    'static_url_prefix': '/resource/',
    'img_http_prefix': ConfigCommon.img_http_prefix,
    "gzip": False,
    'autoescape': 'xhtml_escape',
    'root_path': PYWEB_PATH,
    'template_path': os.path.join(PYWEB_PATH, "templates"),
    'xsrf_cookies': ConfigCommon.is_xsrf_cookies,
    'cookie_secret': ConfigCommon.cookie_secret,
    'login_url': '/login',



}

'''
 'ui_modules': {'AskForLeave': AskForLeave,'Askforout':Askforout,'Default_detail':Default_detail,\
                   'Wait_for_confirm':Wait_for_confirm,'Confirm':Confirm,'Changepwd':Changepwd,\
                   'Perdetail':Perdetail,'Statistic':Statistic,'ComfirmForOther':ComfirmForOther,\
                   'UncomfirmForOther':UncomfirmForOther,'Attendanceexceptiondata':Attendanceexceptiondata,\
                   'Attendanceexceptionalldata':Attendanceexceptionalldata,'UploadAbsenceFile':UploadAbsenceFile},

'''