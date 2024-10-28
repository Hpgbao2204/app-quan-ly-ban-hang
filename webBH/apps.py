from django.apps import AppConfig


class WebbhConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webBH'

    # Tích hopwj signals vào
    def ready(self):
        import webBH.signals
