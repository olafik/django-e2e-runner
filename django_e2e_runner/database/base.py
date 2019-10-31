class BaseDatabase(object):
    def setup(self):
        raise NotImplementedError(
            'subclasses of BaseDatabase may require a setup() method'
        )

    def teardown(self):
        raise NotImplementedError(
            'subclasses of BaseDatabase may require a teardown() method'
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
