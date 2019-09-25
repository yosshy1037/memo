from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
from ...common import const,constDef,sessionClass,commonFuncClass,exceptionClass,logClass
from ...memoSearch import searchForms

## 一覧画面
class memoSearch(View):
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
    self.__css = 'search.css'
    self.__js = '<script src="/static/js/jquery.search.js"></script>'
    self.__listJs = '<script src="/static/js/jquery.listResult.js"></script>'
    self.__veiwUrl = 'memo/memoSearchView.html'
    self.__logoutAtag = '<a class="logout" id="logoutNormal" href="#">ログアウト</a>'
    self.__registButton = '<input type="submit" value="新規登録" class="registPage" />'
  
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
      self.__form = searchForms.searchForm(None);
      
      # 登録ボタン制御
      self.__com.userRoleDispos(self.__ses.request, self.__registButton)
      self.__registButton = self.__com.result
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # 検索画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
      'registButton' : self.__registButton
    }
    return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    try:
      # フォーム生成
      self.__form = searchForms.searchForm(request.POST);
      
      # 登録ボタン制御
      self.__com.userRoleDispos(request, self.__registButton)
      self.__registButton = self.__com.result
      
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
      
    # 検索画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
      'registButton' : self.__registButton
    }
    return render(request, self.__veiwUrl, d)