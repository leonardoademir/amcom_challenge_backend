from django.apps import AppConfig


class BaseApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.base_api"
