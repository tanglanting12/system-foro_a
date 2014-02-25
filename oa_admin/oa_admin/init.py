#coding=utf-8

import sys, os

def init_django_settings():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oa_admin.settings")
    reload(sys)
    sys.setdefaultencoding('utf-8')