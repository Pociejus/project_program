from django.apps import AppConfig


class ProgramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'program'

    def ready(self):
        from .signals import create_profile, save_profile
