import subprocess

from django_e2e_runner import settings


class Cypress(object):
    def start(self, runner_args, run_in_docker=False, docker_image=None):
        if len(runner_args) == 0:
            runner_args = ['run']
        if run_in_docker:
            run_cmd = (
                'docker run --net=host '
                '-v {base_dir}:/e2e '
                '-w /e2e '
                '{image}'
            ).format(
                base_dir=settings.E2E_TEST_RUNNER_BASE_DIR,
                image=docker_image,
            ).split() + runner_args
        else:
            run_cmd = [settings.E2E_TEST_RUNNER_EXECUTABLE] + runner_args
        p_cypress = subprocess.Popen(
            run_cmd,
            cwd=settings.E2E_TEST_RUNNER_BASE_DIR,
        )
        p_cypress.wait()
        return p_cypress.returncode
