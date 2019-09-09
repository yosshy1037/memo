from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
import logging
from ...common import const,constDef,formValidateClass,sessionClass,commonFuncClass,exceptionClass,logClass
from ...memoLogin import loginForms,loginModel

## ログイン画面
class memoLogin(View):
  # initMethod
  def __init__(self, **kwargs):
    
    # インスタンス用変数
    self.__validate = formValidateClass.formValidate()
    self.__model = loginModel.loginModel()
    self.__com = commonFuncClass.commonFunc()
    self.__ses = sessionClass.session()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    # エラーメッセージ用変数
    self.__errMes = {}
    self.__mes = ""
    self.__errMesHtml = ""
    self.__requestMethod = None
    self.__searchForm = loginForms.loginForm(self.__requestMethod);
    self.__css = 'login.css'
    self.__veiwUrl = 'memo/memoLoginView.html'
    
  # GetMethod
  def get(self, request, *args, **kwargs):
    
    try:
      self.__ses.request = request
      
      # ログイン情報(session)チェック
      self.__ses.loginCheckSession()
      if self.__ses.loginFlg == True:
         return redirect("memoSearch")
      else:
        # ログイン情報が存在しない場合
        d = {
          'css' : self.__css,
          'form': self.__searchForm,
          'errMes' : self.__errMesHtml,
        }
        return render(self.__ses.request, self.__veiwUrl, d)

    except exceptionClass.parentException as e:
      print(e.value)
      
    # ログイン情報が存在しない場合
    d = {
      'css' : self.__css,
      'form': self.__searchForm,
      'errMes' : self.__errMesHtml,
    }
    return render(self.__ses.request, self.__veiwUrl, d)
  
  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    # request情報を格納
    self.__ses.request = request
    self.__requestMethod = request.POST
    self.__searchForm = loginForms.loginForm(self.__requestMethod);
  
    try:
      
      # モデルへ値格納
      self.__model.request = self.__ses.request
      self.__model.collumList = ['loginUser','loginPassword']
      self.__model.valueListCreate()

      # ログイン情報の存在チェック
      self.__validate.collumList = self.__model.collumList
      self.__validate.valueList = self.__model.valueList
      self.__validate.validateCheck()
      # ログイン情報に不備あり
      if len(self.__validate.messageList) > 0:
        self.__errMes = self.__validate.messageList
        self.__mes = self.__errMes['LOGINUSER_ERR']
      else:
        # ログイン情報チェックOKの場合
        self.__ses.valueList = self.__model.valueList
        self.__ses.setSession()
        # 検索画面へ遷移
        return redirect("memoSearch")
    
    # エラー処理
    except (NameError, SyntaxError, TypeError, ValueError, ZeroDivisionError, IndexError) as e:
      self.__exc.log = self.__log
      self.__exc.dispatch(e, traceback.format_exc())
      
    except exceptionClass.parentException as e:
      e.errMes = e.value
      e.logOutput()

    # ログイン画面を描画する前処理
    self.__errMesHtml = "<tr><th></th><td class='errMes'>" + self.__mes + "</td></tr>"
    
    d = {
      'css' : self.__css,
      'form': self.__searchForm,
      'errMes' : self.__errMesHtml,
    }
    return render(self.__ses.request, self.__veiwUrl, d)