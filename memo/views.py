from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from html import unescape
from .common import const,constDef,formValidateClass,sessionClass
from .memoLogin import loginForms,loginModel
from .memoSearch import searchForms
from .memoRegist import registForms

## ログイン画面
def memo(request):
  ses = sessionClass.session()
  ses.request = request
  # ログイン情報チェック
  ses.loginCheckSession()
  if ses.loginFlg == True:
     return redirect("memoSearch")

  # モデルへ値格納
  model = loginModel.loginModel()
  model.request = request
  model.collumList = ['loginUser','loginPassword']
  model.valueListCreate()
  
  # ログインチェック
  errMes = {}
  mes = ""
  if request.method == 'POST':
    validate = formValidateClass.formValidate()
    validate.collumList = model.collumList
    validate.valueList = model.valueList
    validate.validateCheck()
    if len(validate.messageList) > 0:
      errMes = validate.messageList
      mes = errMes['LOGINUSER_ERR']
    else:
      ses.valueList = model.valueList
      # ログイン情報をセッションへ格納
      ses.setSession()
      return redirect("memoSearch")
  
  form = loginForms.loginForm(request.POST or None);
  css = 'login.css'
  d = {
    'css' : css,
    'form': form,
    'errMes' : "<tr><th></th><td class='errMes'>" + mes + "</td></tr>" ,
  }
  return render(request, 'memo/memoLoginView.html', d )

## 一覧画面
def memoSearch(request):
  ses = sessionClass.session()
  ses.request = request
  # ログイン情報チェック
  ses.loginCheckSession()
  if ses.loginFlg == False:
     return redirect("memo")
  
  part = ""
  name = ""
  pageNum = 1
  if request.method == 'POST':
    part = request.POST.get('part');
    name = request.POST.get('name');

    if request.POST.get('pageNum') == None:
      part = "";
    else:
      part = request.POST.get('part');
      
    if request.POST.get('name') == None:
      name = "";
    else:
      name = request.POST.get('name');
    
    if request.POST.get('pageNum') == None:
      pageNum = 1;
    else:
      pageNum = request.POST.get('pageNum');

  if part=="":
    message = '入力してください'
  else:
    message = ''
  
  form = searchForms.searchForm(request.POST or None);
  css = 'search.css'
  js = '<script src="/static/js/jquery.search.js"></script>'
  listJs = '<script src="/static/js/jquery.listResult.js"></script>'
  
  d = {
    'logout' : '<a class="logout" href="#">ログアウト</a>',
    'form': form,
    'css' : css,
    'disp_js' : js,
    'resutList_js' : listJs,
    'partErr' : message,
    'pageNum' : pageNum,
    'part' : part,
    'name' : name,
  }
  return render(request, 'memo/memoSearchView.html', d )

## 登録画面
def memoRegist(request):
  ses = sessionClass.session()
  ses.request = request
  # ログイン情報チェック
  ses.loginCheckSession()
  if ses.loginFlg == False:
     return redirect("memo")

  part = ""
  name = ""
  pageNum = 1
  if request.method == 'POST':
    part = request.POST.get('part');
    name = request.POST.get('name');
    
    if request.POST.get('pageNum') == None:
      part = "";
    else:
      part = request.POST.get('part');
      
    if request.POST.get('name') == None:
      name = "";
    else:
      name = request.POST.get('name');
    
    if request.POST.get('pageNum') == None:
      pageNum = 1;
    else:
      pageNum = request.POST.get('pageNum');

  if part=="":
    message = '入力してください'
  else:
    message = ''
  
  form = registForms.registForm(request.POST or None);
  
  d = {
    'logout' : '<a class="logout" href="#">ログアウト</a>',
    'form': form,
    'css' : "regist.css",
    'disp_js' : '',
    'resutList_js' : '',
    'partErr' : message,
    'pageNum' : pageNum,
    'part' : part,
    'name' : name,
  }
  return render(request, 'memo/memoRegistView.html', d )
  
## ログアウト
def logout(request):
  ses = sessionClass.session()
  ses.request = request
  # セッション情報削除
  ses.logout()
  return redirect("memo")