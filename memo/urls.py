from django.conf.urls import url
from .views import memoLogin,memoSearch,memoRegist,memoDetail,logout
from .memoSearch import searchPost
from .memoRegist import registPost
from .memoDetail import detailPost

urlpatterns = [
    url(r'^$', memoLogin.as_view(), name='memo'),
    url(r'^memoSearch/$', memoSearch.as_view(), name='memoSearch'),
    url(r'^dataList/$', searchPost.resultListView, name='resultListView'),
    url(r'^memoRegist/$', memoRegist.as_view(), name='memoRegist'),
    url(r'^regist/$', registPost.registList, name='registList'),
    url(r'^memoDetail/$', memoDetail.as_view(), name='memoDetail'),
    url(r'^update/$', detailPost.detailList, name='detailList'),
    url(r'^logout/$', logout.as_view(), name='logout'),
]