# Django E2E Runner

## Installation
Install using pip. From command line:
```
$ pip install git+https://github.com/LekSeek/django-e2e-runner@v0.1.0-alpha
```
Or add to your project's requirements.txt:
```
Django==1.11.22
(...)
git+git://github.com/LekSeek/django-e2e-runner@v0.1.0-alpha#egg=django-e2e-runner
```
and run
```pip install -r requirements.txt```

Add `django_e2e_runner` to `INSTALLED_APPS`

```
INSTALLED_APPS = [
    (...)
    'django_e2e_runner',
]
```

## Usage
```
$ python manage.py run_tests [options]
```
Optional `options` include everything you can pass to Django's
`manage.py` (e.g. `--settings`) and:

`--keepdb=<True/False>`: preserve the test database between runs;
defaults to `True`

`--server-output=<True/False>`: print Django server output to stdout;
defaults to `False`

`-runner <arguments>`: passes along *all the remaining* arguments to the
test runner (e.g. Cypress)

Examples:
```
$ python manage.py run_tests
$ python manage.py run_tests --settings=project.settings_e2e
$ python manage.py run_tests --server-output=true -runner run --headed
```
