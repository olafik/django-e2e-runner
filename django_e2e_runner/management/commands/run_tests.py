import argparse

from django.core.management.base import BaseCommand, CommandParser

from django_e2e_runner.database import setup_database
from django_e2e_runner.server import DjangoTestServer
from django_e2e_runner.test_runner import start_test_runner


DJANGO_SETTINGS_MODULE = 'GabinetProject.settings_testing'
KEEP_DB = True
THREADED_SERVER = False


class Command(BaseCommand):
    help = 'Run the tests: start the Django test server, setup ' \
           'the test database and invoke the e2e test runner specified ' \
           'in settings (e.g. Cypress, TestCafe)'

    def add_arguments(self, parser):
        cmd = self

        class SubParser(CommandParser):
            def __init__(self, **kwargs):
                super(SubParser, self).__init__(cmd, **kwargs)

        parser.add_argument('-runner',
                            nargs=argparse.REMAINDER,
                            help='All remaining arguments will be '
                                 'forwarded to the test runner')

    def handle(self, *args, **options):
        # TODO consider adding setup_test_environment() from Django runners.
        #      Shouldn't this whole script be a Django test runner?

        # Setup the test database
        database = setup_database()

        # Run Django test server
        self.stdout.write('Starting Django test server... ', ending='')
        server = DjangoTestServer(use_threading=THREADED_SERVER)
        try:
            if not server.start():
                self.stdout.write(self.style.ERROR('FAILED'))
                return

            self.stdout.write(self.style.SUCCESS('DONE'))

            # Run the test suite
            self.stdout.write('Starting test runner...')
            runner_args = options.get('runner') or []
            test_runner = start_test_runner(runner_args)
        finally:
            # Stop the server and teardown the test database
            self.stdout.write('Shutting down Django server... ', ending='')
            server.terminate()
            self.stdout.write(self.style.SUCCESS('DONE'))
            database.teardown()
