from django.shortcuts import render, redirect
from django.views.generic import View
from ...common import const,constDef,formValidateClass,sessionClass,commonFuncClass,exceptionClass,logClass
from ...memoRegist import registForms

## 登録画面
class memoRegist(View):
  # initMethod
  def __init__(self, **kwargs):
  
    # インスタンス用変数
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.errMes = {}
    self.__registForm = "";
    self.__css = 'regist.css'
    self.__js = ''
    self.__listJs = ''
    self.__veiwUrl = 'memo/memoRegistView.html'
    self.__logoutAtag = '<a class="logout" href="#">ログアウト</a>'

  # GetMethod
  def get(self, request, *args, **kwargs):
    
    # request情報を格納
    self.__ses.request = request
    
    try:
    
      # ログイン情報チェック
      self.__ses.loginCheckSession()
      # ログイン情報が存在しない場合
      if self.__ses.loginFlg == False:
        return redirect("memo")
      
      # フォーム生成
      self.__registForm = registForms.registForm(None);

    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")

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
    
    try:
      # フォーム生成
      self.__registForm = registForms.registForm(request.POST);

    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__registForm,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
    }
    return render(request, self.__veiwUrl, d)