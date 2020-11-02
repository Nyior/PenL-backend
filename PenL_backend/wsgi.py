"""
WSGI config for PenL_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import socketio

from apps.game_room.api.views import sio

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PenL_backend.settings')

application = get_wsgi_application()
# application = socketio.WSGIApp(sio, django_app)
