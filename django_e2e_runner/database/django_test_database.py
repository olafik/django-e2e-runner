from django.db import connection
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

    @classmethod
    def connect_to_test_database(cls):
        test_database_name = connection.creation._get_test_db_name()
        connection.close()
        settings.DATABASES[connection.alias]["NAME"] = test_database_name
        connection.settings_dict["NAME"] = test_database_name
        connection.ensure_connection()

    @classmethod
    def allows_multiple_connections(cls):
        return connection.features.test_db_allows_multiple_connections
