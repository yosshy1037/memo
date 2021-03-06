from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
from ...common import const,constDef,formValidateClass,sessionClass,commonFuncClass,exceptionClass,logClass,tempFileClass
from ...memoRegist import registForms,registModel
import json

## 登録画面
class memoRegist(View):
  # initMethod
  def __init__(self, **kwargs):
  
    # インスタンス用変数
    self.__model = registModel.registModel()
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__temp = tempFileClass.tempFile()
    self.errMes = {}
    self.__registForm = "";
    self.__css = 'regist.css'
    self.__js = ''
    self.__listJs = ''
    self.__veiwUrl = 'memo/memoRegistView.html'
    self.__logoutAtag = '<a class="logout" id="logoutNormal" href="#">ログアウト</a>'
    self.__registButton = '<input type="submit" value="登録" class="regist" />'

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
      'registButton' : self.__registButton,
    }
    return render(self.__ses.request, self.__veiwUrl, d)
  
  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    try:
    
      # モデルセット
      self.__model.request = request
      self.__model.json = json
    
      # 値生成
      self.__model.collumList = ['part','name','registStartDate','registEndDate','keyWord','pageNum']
      self.__model.valueListCreate()
    
      # フォーム生成
      self.__registForm = registForms.registForm(request.POST);
      
      # 登録ボタン制御
      self.__com.userRoleDispos(self.__model.request, self.__registButton , 'disabled')
      self.__registButton = self.__com.result
      
      # tempデータ書き込み
      self.__temp.writeData = self.__model.valueList
      self.__temp.tempFileCreate()
      
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
      'registButton' : self.__registButton,
    }
    return render(request, self.__veiwUrl, d)