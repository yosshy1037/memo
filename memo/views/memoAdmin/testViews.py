from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
from ...common import const,constDef,sessionClass,commonFuncClass,exceptionClass,logClass,unitTestClass

## テスト処理
class memoTest(View):
  # initMethod
  def __init__(self, **kwargs):
  
    # インスタンス用変数
    self.__ses = sessionClass.session()
    self.__model = ""
    self.__com = commonFuncClass.commonFunc()
    self.__unit = unitTestClass.unitTest()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.errMes = {}
    self.__form = "";
    self.__css = 'test.css'
    self.__js = '<script src="/static/js/jquery.unitTest.js"></script>'
    self.__veiwUrl = 'memo/admin/memoAdminTest.html'
    self.__logoutAtag = ''
  
  # GetMethod
  def get(self, request, *args, **kwargs):
  
    # request情報を格納
    self.__unit.request = request
    
    try:
      
      # ログイン実施テスト
      self.__unit.loginTest()
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      print(traceback.format_exc())
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # テスト完了画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'disp_js' : self.__js,
    }
    return render(request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    self.__unit.request = request
    
    try:
      
      # ログイン実施テスト
      self.__unit.loginTest()
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      print(traceback.format_exc())
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # テスト完了画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'disp_js' : self.__js,
    }
    return render(request, self.__veiwUrl, d)