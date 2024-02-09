import os
import platform

from django.conf import settings


DATABASE_CLASS = 'django_e2e_runner.database.DjangoTestDatabase'
KEEP_DATABASE = True
TEST_DATA_MANAGER = 'django_e2e_runner.database.GlobalTransaction'
FIXTURE_LOADER = 'django_e2e_runner.database.ScriptFixtureLoader'

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8001

E2E_TEST_RUNNER_CLASS = 'django_e2e_runner.test_runner.cypress.Cypress'
E2E_TEST_RUNNER_BASE_DIR = os.path.join(settings.BASE_DIR, 'tests/e2e/')
E2E_TEST_RUNNER_EXECUTABLE = os.path.join(
    settings.BASE_DIR,
    'tests/e2e/node_modules/.bin/cypress'
    + ('.cmd' if platform.system() == 'Windows' else '')
)
E2E_TEST_RUNNER_DOCKER_IMAGE = 'cypress/included:12.17.1'
