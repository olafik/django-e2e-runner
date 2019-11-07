from django.test.utils import setup_databases, teardown_databases

from django_e2e_runner import settings
from django_e2e_runner.database import BaseDatabase


class DjangoTestDatabase(BaseDatabase):
    def __init__(self):
        self.old_config = {}

    def setup(self, keepdb=settings.KEEP_DATABASE):
        self.old_config = setup_databases(1, False,
                                          keepdb=keepdb)

    def teardown(self, keepdb=settings.KEEP_DATABASE):
        teardown_databases(self.old_config, 1, keepdb=keepdb)
