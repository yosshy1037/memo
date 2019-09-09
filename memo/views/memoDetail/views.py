from django.shortcuts import render, redirect
from django.views.generic import View
from ...common import dbMainClass,const,constDef,formValidateClass,sessionClass,commonFuncClass
from ...memoDetail import detailForms,detailDb

## 詳細画面
class memoDetail(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.__db = dbMainClass.dbMain()
    self.__ddSql = detailDb.detailSql()
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
    self.__initVal()
    
    # ログイン情報チェック
    self.__ses.loginCheckSession()
    # ログイン情報が存在しない場合
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
    self.__initVal()
    
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__detailForm,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
    }
    return render(request, self.__veiwUrl, d)

  # DB初期値取得
  def __initVal(self):
    self.__db.dbConnection()
    self.__ddSql.detailNum = self.__ses.request.GET.get('detailNum')
    self.__ddSql.detailSelectSql()
    self.__db.execute(self.__ddSql.sql,const.sel,const.fetchModeTwo)
    self.__db.dbClose()

    self.__detailForm.fields['detailPart'].initial = self.__db.result[0][1]
    self.__detailForm.fields['detailName'].initial = self.__db.result[0][2]
    self.__detailForm.fields['detailGender'].initial = self.__db.result[0][3]
    self.__detailForm.fields['detailContents'].initial = self.__db.result[0][4]
    self.__detailForm.fields['detailBiko'].initial = self.__db.result[0][5]