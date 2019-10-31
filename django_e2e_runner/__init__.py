from django.conf import settings as user_settings
from django_e2e_runner import settings as default_settings


class Settings(object):
    def __getattr__(self, name):
        if hasattr(user_settings, name):
            return getattr(user_settings, name)

        if hasattr(default_settings, name):
            return getattr(default_settings, name)

        raise AttributeError("'Settings' object has no attribute '%s'" % name)


settings = Settings()
