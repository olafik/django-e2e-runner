from django.test.utils import setup_databases, teardown_databases

from django_e2e_runner import settings
from django_e2e_runner.database import BaseDatabase


class DjangoTestDatabase(BaseDatabase):
    def __init__(self):
        self.old_config = {}

    def setup(self):
        self.old_config = setup_databases(1, False,
                                          keepdb=settings.KEEP_DATABASE)

    def teardown(self):
        teardown_databases(self.old_config, 1, keepdb=settings.KEEP_DATABASE)
