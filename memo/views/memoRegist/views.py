from django.shortcuts import render, redirect
from django.views.generic import View
from ...common import const,constDef,formValidateClass,sessionClass,commonFuncClass
from ...memoRegist import registForms

## 登録画面
class memoRegist(View):
  # initMethod
  def __init__(self, **kwargs):
  
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.errMes = {}
    self.__requestMethod = None
    self.__registForm = registForms.registForm(self.__requestMethod);

    self.__css = 'regist.css'
    self.__js = ''
    self.__listJs = ''
    self.__veiwUrl = 'memo/memoRegistView.html'
    self.__logoutAtag = '<a class="logout" href="#">ログアウト</a>'

  # GetMethod
  def get(self, request, *args, **kwargs):
    self.__ses.request = request
    # ログイン情報チェック
    self.__ses.loginCheckSession()
    # ログイン情報が存在しない場合
    if self.__ses.loginFlg == False:
      return redirect("memo")
    else:
      d = {
        'logout' : self.__logoutAtag,
        'form': self.__registForm,
        'css' : self.__css,
        'disp_js' : self.__js,
        'resutList_js' : self.__listJs,
      }
      return render(self.__ses.request, self.__veiwUrl, d)
  
  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__requestMethod = request.POST
    self.__registForm = registForms.registForm(self.__requestMethod);
    
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__registForm,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
    }
    return render(request, self.__veiwUrl, d)