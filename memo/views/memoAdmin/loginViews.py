from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
from ...common import const,constDef,formValidateClass,sessionClass,commonFuncClass,exceptionClass,logClass
from ...memoAdmin import adminLoginForms,adminLoginModel

## 管理画面
class loginView(View):
  # initMethod
  def __init__(self, **kwargs):
  
    # インスタンス用変数
    self.__validate = formValidateClass.formValidate()
    self.__ses = sessionClass.session()
    self.__model = adminLoginModel.loginModel()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    # エラーメッセージ用変数
    self.__errMes = {}
    self.__mes = ""
    self.__errMesHtml = ""
    self.__css = 'adminLogin.css'
    self.__veiwUrl = 'memo/admin/memoAdminLogin.html'
  
  # GetMethod
  def get(self, request, *args, **kwargs):
  
    # request情報を格納
    self.__ses.request = request
    # フォーム生成
    self.__form = adminLoginForms.adminLoginForm(None);
    
    try:
    
      # ログイン情報チェック
      self.__ses.loginCheckSession()
      # ログイン情報が存在しない場合
      #if self.__ses.loginFlg == False:
      #  return redirect("adLoginView")

    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # ログイン画面を描画する処理
    d = {
      'errMes' : self.__errMesHtml,
      'form': self.__form,
      'css' : self.__css,
    }
    return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    # request情報を格納
    self.__ses.request = request
    self.__form = adminLoginForms.adminLoginForm(request.POST);
    
    try:
    
      # モデルへ値格納
      self.__model.request = self.__ses.request
      self.__model.collumList = ['adLoginUser','adLoginPassword']
      self.__model.valueListCreate()
      
      # ログイン情報の存在チェック
      self.__validate.collumList = self.__model.collumList
      self.__validate.valueList = self.__model.valueList
      self.__validate.adminValidateCheck()
      if len(self.__validate.messageList) > 0:
        # ログイン情報に不備あり
        self.__errMes = self.__validate.messageList
        self.__mes = self.__errMes['ADLOGINUSER_ERR']
      else:
        # ログイン情報チェックOKの場合
        self.__ses.valueList = self.__model.valueList
        self.__ses.setSession()
        # 検索画面へ遷移
        return redirect("adSsearchView")
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # ログイン画面を描画する処理
    self.__errMesHtml = "<tr><th></th><td class='errMes'>" + self.__mes + "</td></tr>"
    
    d = {
      'errMes' : self.__errMesHtml,
      'form': self.__form,
      'css' : self.__css,
    }
    return render(request, self.__veiwUrl, d)