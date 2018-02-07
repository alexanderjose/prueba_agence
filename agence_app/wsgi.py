"""
WSGI config for agence_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

# path = '/home/agalindez/prueba_agence'
# if path not in sys.path:
#     sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agence_app.settings")

application = get_wsgi_application()
# application = DjangoWhiteNoise(get_wsgi_application())
