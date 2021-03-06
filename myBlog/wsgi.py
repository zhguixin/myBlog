"""
WSGI config for myBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/usr/local/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myBlog.settings")

application = get_wsgi_application()
