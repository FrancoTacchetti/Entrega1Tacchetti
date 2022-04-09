from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "entrega1tacchetti.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import entrega1tacchetti.users.signals  # noqa F401
        except ImportError:
            pass
