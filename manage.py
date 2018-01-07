# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import os
import sys
'''
python -m django --version
此命令用户查看Django版本
'''
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myBlog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)
