from django.conf.urls import url
from .memoSearch import views,resultListPost

urlpatterns = [
    url(r'^$', views.memo, name='memo'),
    url(r'^dataList/$', resultListPost.resultListView, name='resultListView'),
]