from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
from ...common import const,constDef,sessionClass,commonFuncClass,exceptionClass,logClass
from ...memoAdmin import adminSearchForms

## メニュー画面
class menuView(View):
  # initMethod
  def __init__(self, **kwargs):
  
    # インスタンス用変数
    self.__ses = sessionClass.session()
    self.__model = ""
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.errMes = {}
    self.__form = "";
    self.__css = 'adminMenu.css'
    self.__js = '<script src="/static/js/admin/jquery.adminMenu.js"></script>'
    self.__veiwUrl = 'memo/admin/memoAdminMenu.html'
    self.__logoutAtag = '<a class="logout" id="logoutAdmin" href="#">ログアウト</a>'
  
  # GetMethod
  def get(self, request, *args, **kwargs):
  
    # request情報を格納
    self.__ses.request = request
    
    try:
    
      # ログイン情報チェック
      self.__ses.adminLoginCheckSession()
      # ログイン情報が存在しない場合
      if self.__ses.loginFlg == False:
        return redirect("adLoginView")

      # フォーム生成
      self.__form = adminSearchForms.adminForm(None);
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # メニュー画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'js' : self.__js,
    }
    return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    try:
      # フォーム生成
      self.__form = adminSearchForms.adminForm(request.POST);
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # メニュー画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'js' : self.__js,
    }
    return render(request, self.__veiwUrl, d)