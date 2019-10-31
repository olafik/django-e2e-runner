from django.conf.urls import url, include

from django_e2e_runner.views import load_test_data, rollback_test_data

urlpatterns = [
    url(r'^', include('GabinetProject.urls')),
    url(r'^load_test_data/(?P<fixture_name>[\w_.]+)/$', load_test_data),
    url(r'^rollback_test_data/$', rollback_test_data),
]
