from django.shortcuts import render
from django.views.generic import View
from ...common import const,constDef,sessionClass

## エラー画面
class error(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__ses = sessionClass.session()
    self.__css = 'error.css'
    self.__js = ''
    self.__listJs = ''
    self.__veiwUrl = 'memo/memoErrorView.html'
    self.__logoutAtag = ''
    
  # GetMethod
  def get(self, request, *args, **kwargs):
    self.__ses = sessionClass.session()
    self.__ses.request = request
    # セッション情報削除
    self.__ses.logout()

    d = {
      'logout' : self.__logoutAtag,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
    }
    return render(self.__ses.request, self.__veiwUrl, d)
  
  # PostMethod
  def post(self, request, *args, **kwargs):
    self.__ses = sessionClass.session()
    self.__ses.request = request
    # セッション情報削除
    self.__ses.logout()