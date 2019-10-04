from django.shortcuts import render, redirect
from django.views.generic import View
import traceback
from ...common import dbMainClass,const,constDef,formValidateClass,sessionClass,commonFuncClass,exceptionClass,logClass
from ...memoDetail import detailForms,detailDb

## 詳細画面
class memoDetail(View):
  # initMethod
  def __init__(self, **kwargs):
  
    # インスタンス用変数
    self.__ses = sessionClass.session()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__db = dbMainClass.dbMain()
    self.__ddSql = detailDb.detailSql()
    self.errMes = {}
    self.__detailForm = "";
    self.__css = 'detail.css'
    self.__js = ''
    self.__listJs = ''
    self.__veiwUrl = 'memo/memoDetailView.html'
    self.__logoutAtag = '<a class="logout" id="logoutNormal" href="#">ログアウト</a>'
    self.__updateButton = '<input type="submit" value="更新" class="update" />'
    self.__deleteButton = '<input type="submit" value="削除" class="delete" />'
    
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
      self.__detailForm = detailForms.detailForm(None);
      
      # フォーム値設定
      self.__initVal()
    
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
    
    # 詳細画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__detailForm,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
      'updateButton' : self.__updateButton,
      'deleteButton' : self.__deleteButton
    }
    return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    # request情報を格納
    self.__ses.request = request
    
    try:
      
      # フォーム生成
      self.__detailForm = detailForms.detailForm(request.POST);
    
      # フォーム値設定
      self.__initVal()
    
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
      return redirect("error")
    except Exception as e:
      # Exception処理
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
      return redirect("error")
    
    # 詳細画面を描画する処理
    d = {
      'logout' : self.__logoutAtag,
      'form': self.__detailForm,
      'css' : self.__css,
      'disp_js' : self.__js,
      'resutList_js' : self.__listJs,
      'updateButton' : self.__updateButton,
      'deleteButton' : self.__deleteButton
    }
    return render(request, self.__veiwUrl, d)

  # フォーム初期状態取得処理
  def __initVal(self):
    self.__db.dbConnection()
    self.__ddSql.detailNum = self.__ses.request.GET.get('detailNum')
    self.__ddSql.detailSelectSql()
    self.__db.execute(self.__ddSql.sql,const.sel,const.fetchModeTwo)
    self.__db.dbClose()

    self.__detailForm.fields['detailPart'].initial = self.__db.result[0][1]
    self.__detailForm.fields['detailName'].initial = self.__db.result[0][2]
    self.__detailForm.fields['detailContents'].initial = self.__db.result[0][3]
    self.__detailForm.fields['detailBiko'].initial = self.__db.result[0][4]
    
    # 更新ボタン制御
    self.__com.userRoleDispos(self.__ses.request, self.__updateButton)
    self.__updateButton = self.__com.result
    
    # 削除ボタン制御
    self.__com.userRoleDispos(self.__ses.request, self.__deleteButton)
    self.__deleteButton = self.__com.result