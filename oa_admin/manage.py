#!/usr/bin/env python
import os
import sys
from oa_admin.init import init_django_settings

if __name__ == "__main__":
    init_django_settings()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oa_admin.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
