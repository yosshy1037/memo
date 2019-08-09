from django.conf.urls import url
from .memoSearch import views,resultListPost
from . import postgres

urlpatterns = [
    url(r'^memo/$', views.memo, name='memo'),
    url(r'^dataList/$', resultListPost.resultListView, name='resultListView'),
    url(r'^postgres/$', postgres.db_test, name='db_test'),
]