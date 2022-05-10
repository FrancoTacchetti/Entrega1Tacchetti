from distutils.log import error
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "entrega1tacchetti.users"
    verbose_name = _("Users")

    def ready(self):
        import entrega1tacchetti.users.signals



