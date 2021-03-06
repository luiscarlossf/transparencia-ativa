"""
ASGI config for transparencia project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transparencia.settings')

project_folder = os.path.expanduser('../')
load_dotenv(os.path.join(project_folder, '.env'))

application = get_asgi_application()
