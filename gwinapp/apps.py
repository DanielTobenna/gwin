from django.apps import AppConfig


class GwinappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gwinapp'

    def ready(self):
    	import gwinapp.signals
