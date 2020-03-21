import subprocess

from django_e2e_runner import settings


class Cypress(object):
    def start(self, runner_args):
        if len(runner_args) == 0:
            runner_args = ['run']
        runner_args.insert(0, settings.E2E_TEST_RUNNER_EXECUTABLE)
        p_cypress = subprocess.Popen(
            runner_args,
            cwd=settings.E2E_TEST_RUNNER_BASE_DIR,
        )
        p_cypress.wait()
        return p_cypress.returncode
