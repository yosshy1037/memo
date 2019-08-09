from django.conf.urls import url
from . import views
from . import db
from . import dbSelect

urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
    url(r'^template/$', views.hello_template, name='hello_template'),
    url(r'^get/$', views.hello_get_query, name='hello_get_query'),
    url(r'^forms/$', views.hello_forms, name='hello_forms'),
    url(r'^form_samples/$', views.hello_forms2, name='hello_forms2'),
    url(r'^db/$', db.db_test, name='db_test'),
    url(r'^dbSelect/$', dbSelect.db_test_select, name='db_test_select'),
    url(r'^models/$', views.hello_models, name='hello_models'),
]