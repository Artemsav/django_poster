"""
WSGI config for where_to_go project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'where_to_go.settings')

application = get_wsgi_application()

project_folder = os.path.expanduser('~/hisp.pythonanywhere.com')
load_dotenv(os.path.join(project_folder, '.env'))
