# TODO Reconsider if this abstract class is that useful...
class BaseDatabase(object):
    def setup(self, *args, **kwargs):
        raise NotImplementedError(
            'subclasses of BaseDatabase may require a setup() method'
        )

    def teardown(self, *args, **kwargs):
        raise NotImplementedError(
            'subclasses of BaseDatabase may require a teardown() method'
        )

    @classmethod
    def connect_to_test_database(cls, *args, **kwargs):
        raise NotImplementedError(
            'subclasses of BaseDatabase may require '
            'a connect_to_test_database() method'
        )

    @classmethod
    def allows_multiple_connections(cls, *args, **kwargs):
        raise NotImplementedError(
            'subclasses of BaseDatabase may require '
            'a allows_multiple_connections() method'
        )


class BaseDataManager(object):
    def pre_load_setup(self):
        raise NotImplementedError(
            'subclasses of BaseDataManager may require '
            'a pre_load_setup() method'
        )

    def rollback(self):
        raise NotImplementedError(
            'subclasses of BaseDataManager may require a rollback() method'
        )
