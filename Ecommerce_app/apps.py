from django.apps import AppConfig


class EcommerceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ecommerce_app'

    def ready(self) -> None:
        import Ecommerce_app.signals 