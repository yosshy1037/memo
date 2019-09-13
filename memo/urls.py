from django.conf.urls import url
from .views.memoLogin.views import memoLogin
from .views.memoSearch.views import memoSearch
from .views.memoRegist.views import memoRegist
from .views.memoDetail.views import memoDetail
from .views.memoDetail.viewsDetailPost import detailPost
from .views.memoRegist.viewsRegistPost import registPost
from .views.memoSearch.viewsSearchPost import searchListPost
from .views.logout.views import logout
from .views.error.views import error

urlpatterns = [
    url(r'^$', memoLogin.as_view(), name='memo'),
    url(r'^memoSearch/$', memoSearch.as_view(), name='memoSearch'),
    url(r'^dataList/$', searchListPost.as_view(), name='searchListPost'),
    url(r'^memoRegist/$', memoRegist.as_view(), name='memoRegist'),
    url(r'^regist/$', registPost.as_view(), name='registPost'),
    url(r'^memoDetail/$', memoDetail.as_view(), name='memoDetail'),
    url(r'^update/$', detailPost.as_view(), name='detailPost'),
    url(r'^logout/$', logout.as_view(), name='logout'),
    url(r'^error/$', error.as_view(), name='error'),
]