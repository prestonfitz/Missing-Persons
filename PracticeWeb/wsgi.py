# Michael Underwood, Michael Hutchings, Preston Fitzgerald, Elliot Pi, Lily Pettit, Noelle Burton

"""
WSGI config for PracticeWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
# import stuff
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PracticeWeb.settings')

application = get_wsgi_application()
