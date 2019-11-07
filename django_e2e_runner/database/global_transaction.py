from django.db import DEFAULT_DB_ALIAS, transaction
from django.db.transaction import get_connection

from django_e2e_runner.database.base import BaseDataManager


atomic = None


class GlobalTransaction(BaseDataManager):
    def pre_load_setup(self):
        connection = get_connection()
        connection.settings_dict['AUTOCOMMIT'] = False  # TODO
        connection.settings_dict["CONN_MAX_AGE"] = None

        global atomic
        atomic = transaction.atomic(using=DEFAULT_DB_ALIAS)
        atomic.__enter__()

    def rollback(self):
        global atomic
        transaction.set_rollback(True, using=DEFAULT_DB_ALIAS)
        atomic.__exit__(None, None, None)
