from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from html import unescape
from .common import dbMainClass,const,constDef,formValidateClass,sessionClass,commonFuncClass
from .memoLogin import loginForms,loginModel
from .memoSearch import searchForms
from .memoRegist import registForms
from .memoDetail import detailForms,detailDb

## ログイン画面
class memoLogin(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__ses = ""
    self.__validate = ""
    self.__model = ""
    self.__com = ""
    self.errMes = {}
    self.__errMesHtml = ""
    self.__requestMethod = None
    self.__searchForm = loginForms.loginForm(self.__requestMethod);
    self.__css = 'login.css'
    self.__veiwUrl = 'memo/memoLoginView.html'
    
    self.__com = commonFuncClass.commonFunc()
    self.__ses = sessionClass.session()
    
  # GetMethod
  def get(self, request, *args, **kwargs):
    self.__ses.request = request
    
    # ログイン情報チェック
    self.__ses.loginCheckSession()
    if self.__ses.loginFlg == True:
       return redirect("memoSearch")
    else:
      d = {
        'css' : self.__css,
        'form': self.__searchForm,
        'errMes' : self.__errMesHtml,
      }
      return render(self.__ses.request, self.__veiwUrl, d)
  
  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__ses.request = request
    self.__requestMethod = request.POST
    self.__searchForm = loginForms.loginForm(self.__requestMethod);
  
    # モデルへ値格納
    self.__model = loginModel.loginModel()
    self.__model.request = self.__ses.request
    self.__model.collumList = ['loginUser','loginPassword']
    self.__model.valueListCreate()

    # ログインチェック
    self.__validate = formValidateClass.formValidate()
    self.__validate.collumList = self.__model.collumList
    self.__validate.valueList = self.__model.valueList
    self.__validate.validateCheck()
    if len(self.__validate.messageList) > 0:
      self.errMes = self.__validate.messageList
      self.mes = self.errMes['LOGINUSER_ERR']
    else:
      self.__ses.valueList = self.__model.valueList
      # ログイン情報をセッションへ格納
      self.__ses.setSession()
      return redirect("memoSearch")
    
    self.__errMesHtml = "<tr><th></th><td class='errMes'>" + self.mes + "</td></tr>"
    
    d = {
      'css' : self.__css,
      'form': self.__searchForm,
      'errMes' : self.__errMesHtml,
    }
    return render(self.__ses.request, self.__veiwUrl, d)
    
## 一覧画面
class memoSearch(View):
  # initMethod
  def __init__(self, **kwargs):
  
    self.__ses = sessionClass.session()
    self.__model = ""
    self.__com = commonFuncClass.commonFunc()
    self.errMes = {}
    self.__requestMethod = None
    self.__form = searchForms.searchForm(self.__requestMethod);
    self.__css = 'search.css'
    self.__js = '<script src="/static/js/jquery.search.js"></script>'
    self.__listJs = '<script src="/static/js/jquery.listResult.js"></script>'
    self.__veiwUrl = 'memo/memoSearchView.html'
    self.__logoutAtag = '<a class="logout" href="#">ログアウト</a>'
  
  # GetMethod
  def get(self, request, *args, **kwargs):
    self.__ses.request = request
    # ログイン情報チェック
    self.__ses.loginCheckSession()
    if self.__ses.loginFlg == False:
      return redirect("memo")
    else:
      d = {
        'logout' : self.__logoutAtag,
        'form': self.__form,
        'css' : self.__css,
        'disp_js' : self.__js,
        'resutList_js' : self.__listJs,
      }
      return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__requestMethod = request.POST
    self.__form = searchForms.searchForm(self.__requestMethod);
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__form,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
    }
    return render(request, self.__veiwUrl, d)

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
  
## 詳細画面
class memoDetail(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.__db = dbMainClass.dbMain()
    self.errMes = {}
    self.__detailForm = "";
    self.__css = 'detail.css'
    self.__js = ''
    self.__listJs = ''
    self.__veiwUrl = 'memo/memoDetailView.html'
    self.__logoutAtag = '<a class="logout" href="#">ログアウト</a>'
    
  # GetMethod
  def get(self, request, *args, **kwargs):
    self.__ses.request = request
    self.__detailForm = detailForms.detailForm(None);
    # DB取得処理
    sql = detailDb.detailSelect(request.GET.get('detailNum'))
    self.__detailForm = self.__initVal(sql)
    
    # ログイン情報チェック
    self.__ses.loginCheckSession()
    if self.__ses.loginFlg == False:
      return redirect("memo")
    else:
      d = {
        'logout' : self.__logoutAtag,
        'form': self.__detailForm,
        'css' : self.__css,
        'disp_js' : self.__js,
        'resutList_js' : self.__listJs,
      }
      return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__ses.request = request
    self.__detailForm = detailForms.detailForm(request.POST);
    
    # DB取得処理
    sql = detailDb.detailSelect(request.GET.get('detailNum'))
    self.__detailForm = self.__initVal(sql)
    
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__detailForm,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
    }
    return render(request, self.__veiwUrl, d)

  # DB初期値取得
  def __initVal(self,sql):
    self.__db.dbConnection()
    sql = detailDb.detailSelect(self.__ses.request.GET.get('detailNum'))
    self.__db.execute(sql,const.sel,const.fetchModeTwo)
    self.__db.dbClose()

    self.__detailForm.fields['detailPart'].initial = self.__db.result[0][1]
    self.__detailForm.fields['detailName'].initial = self.__db.result[0][2]
    self.__detailForm.fields['detailGender'].initial = self.__db.result[0][3]
    self.__detailForm.fields['detailContents'].initial = self.__db.result[0][4]
    self.__detailForm.fields['detailBiko'].initial = self.__db.result[0][5]
    
    print(self.__ses.request.POST.get('detailPart'))
    return self.__detailForm

## ログアウト
class logout(View):
  # POSTMethod
  def post(self, request, *args, **kwargs):
    self.__ses = sessionClass.session()
    self.__ses.request = request
    # セッション情報削除
    self.__ses.logout()
    return redirect("memo")