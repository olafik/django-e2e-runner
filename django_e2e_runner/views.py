from django.http import JsonResponse
from django.utils.module_loading import import_string

from django_e2e_runner import settings
from gabinet.constants import OK_JS_CODE


def load_test_data(request, fixture_name):
    data_manager = import_string(settings.TEST_DATA_MANAGER)()
    data_manager.pre_load_setup()

    fixture_loader = import_string(settings.FIXTURE_LOADER)()
    fixture_loader.load(fixture_name)

    return JsonResponse({'status': OK_JS_CODE})


def rollback_test_data(request):
    data_manager = import_string(settings.TEST_DATA_MANAGER)()
    data_manager.rollback()
    return JsonResponse({'status': OK_JS_CODE})
