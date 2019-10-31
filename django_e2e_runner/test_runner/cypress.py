import subprocess

from django_e2e_runner import settings


class Cypress(object):
    def start(self, runner_args):
        if len(runner_args) == 0:
            runner_args = ['run']
        runner_args.insert(0, settings.E2E_TEST_RUNNER['executable_path'])
        p_cypress = subprocess.Popen(
            runner_args,
            cwd=settings.E2E_TEST_RUNNER['base_dir'],
        )
        p_cypress.wait()
