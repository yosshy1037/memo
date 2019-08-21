from django.conf.urls import url
from . import views
from .memoSearch import searchPost
from .memoRegist import registPost

urlpatterns = [
    url(r'^$', views.memo, name='memo'),
    url(r'^memoSearch/$', views.memoSearch, name='memoSearch'),
    url(r'^dataList/$', searchPost.resultListView, name='resultListView'),
    url(r'^memoRegist/$', views.memoRegist, name='memoRegist'),
    url(r'^regist/$', registPost.registList, name='registList'),
    url(r'^logout/$', views.logout, name='logout'),
]