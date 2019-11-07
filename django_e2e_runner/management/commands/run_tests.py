import argparse

from django.core.management.base import BaseCommand, CommandParser

from django_e2e_runner import settings
from django_e2e_runner.database import setup_database
from django_e2e_runner.server import DjangoTestServer
from django_e2e_runner.test_runner import start_test_runner


# TODO move to command line arg/settings file; enforce with global_transaction
from django_e2e_runner.utils import parse_command_line_bool_arg

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

        parser.add_argument(
            '-k', '--keepdb', dest='keepdb',
            default=settings.KEEP_DATABASE,
            help='Preserves the test DB between runs.'
        )
        parser.add_argument(
            '-runner', nargs=argparse.REMAINDER,
            help='All remaining arguments will be forwarded to the test runner'
        )

    def handle(self, *args, **options):
        # TODO consider adding setup_test_environment() from Django runners.
        #      Shouldn't this whole script be a Django test runner?

        # Setup the test database
        keepdb = parse_command_line_bool_arg(options.get('keepdb'))
        database = setup_database(keepdb=keepdb)

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
            database.teardown(keepdb)
