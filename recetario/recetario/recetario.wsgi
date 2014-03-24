import os
import sys
sys.path = ["/var/www/recetario"] = sys.path
os.environ["DJANGO_SETTINGS_MODULE"]="recetario.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

