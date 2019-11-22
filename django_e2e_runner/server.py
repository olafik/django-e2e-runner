from multiprocessing import Process

from django.core.management import call_command
from django.db import connection
from django.test.utils import override_settings

from django_e2e_runner import settings
from django_e2e_runner.utils import wrap_subprocess, wait_net_service


class DjangoTestServer(object):
    def __init__(self, use_threading=False, verbose=False):
        self.address = settings.SERVER_IP
        self.port = settings.SERVER_PORT
        self.use_threading = use_threading \
            and connection.features.test_db_allows_multiple_connections
        self.server_process = None
        self.verbose = verbose

    @property
    def addrport(self):
        return '{}:{}'.format(self.address, str(self.port))

    def start(self):
        self.server_process = Process(
            target=wrap_subprocess(call_command, verbose=self.verbose),
            args=('runserver',),
            kwargs={
                'addrport': self.addrport,
                # TODO allow use_reloader=True, one possible solution might
                # be to wrap all the code (from run_tests.py) before and after
                # the server setup in a `if os.environ.get('RUN_MAIN', False):`
                # See: https://code.djangoproject.com/ticket/8085
                # https://chase-seibert.github.io/blog/2013/10/24/django-subclass-runserver.html
                # https://stackoverflow.com/questions/28489863/why-is-run-called-twice-in-the-django-dev-server
                'use_reloader': False,
                'use_threading': self.use_threading,
            },
        )

        with override_settings(ROOT_URLCONF='django_e2e_runner.urls',
                               ORIG_ROOT_URLCONF=settings.ROOT_URLCONF):
            self.server_process.start()

        if not wait_net_service(self.address, self.port, timeout=10):
            self.terminate()
            return False

        return True

    def terminate(self):
        if self.server_process.is_alive():
            self.server_process.terminate()
