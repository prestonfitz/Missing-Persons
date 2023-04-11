# Michael Underwood, Michael Hutchings, Preston Fitzgerald, Elliot Pi, Lily Pettit, Noelle Burton

from django.apps import AppConfig

# create class
class BasefolderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basefolder'
