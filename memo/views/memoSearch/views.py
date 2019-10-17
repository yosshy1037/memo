from django.shortcuts import render, redirect
from django.views.generic import View
from datetime import datetime
from dateutil.relativedelta import relativedelta
import traceback,ast
from ...common import const,constDef,sessionClass,commonFuncClass,exceptionClass,logClass,tempFileClass
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
    self.__temp = tempFileClass.tempFile()
    self.errMes = {}
    self.__form = "";
    self.__dict = {};
    self.__css = 'search.css'
    self.__js = '<script src="/static/js/jquery.search.js"></script>'
    self.__listJs = '<script src="/static/js/jquery.listResult.js"></script>'
    self.__veiwUrl = 'memo/memoSearchView.html'
    self.__logoutAtag = '<a class="logout" id="logoutNormal" href="#">ログアウト</a>'
    self.__registButton = '<input type="submit" value="新規登録" class="registPage" />'
    self.__tempData = ""
  
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
      
      # 値設定
      self.__initVal('search')
      
      # tempデータ取得
      self.__temp.tempFileRead()
      self.__tempData = self.__temp.readData
      if self.__tempData != "":
        self.__dict = ast.literal_eval(self.__tempData)
        self.__initVal()
        temp = ""
        ct = 0
        for col in self.__dict:
          if ct == 0:
            temp += str(self.__dict[col][1])
          else:
            temp += ',' + str(self.__dict[col][1])
          ct += 1
        self.__tempData = temp
      
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
      'registButton' : self.__registButton,
      'tempData' : self.__tempData,
    }
    return render(self.__ses.request, self.__veiwUrl, d)

  # POSTMethod
  def post(self, request, *args, **kwargs):
    
    # request情報を格納
    self.__ses.request = request
    
    try:
      # フォーム生成
      self.__form = searchForms.searchForm(None);
      
      # 値設定
      self.__initVal('search')
      
      # tempデータ取得
      self.__temp.tempFileRead()
      self.__tempData = self.__temp.readData
      if self.__tempData != "":
        self.__dict = ast.literal_eval(self.__tempData)
        # 値設定
        self.__initVal('regist')
        temp = ""
        ct = 0
        for col in self.__dict:
          if ct == 0:
            temp += str(self.__dict[col][1])
          else:
            temp += ',' + str(self.__dict[col][1])
          ct += 1
        self.__tempData = temp
      
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
      'registButton' : self.__registButton,
      'tempData' : self.__tempData,
    }
    return render(request, self.__veiwUrl, d)
  
  # フォーム初期状態取得処理
  def __initVal(self , disp):
    if disp == 'search':
      # 検索画面よりPOST時処理
      if 'part' in self.__ses.request.POST and 'name' in self.__ses.request.POST and 'registStartDate' in self.__ses.request.POST and 'registEndDate' in self.__ses.request.POST and 'keyWord' in self.__ses.request.POST:
        self.__form.fields['part'].initial = self.__ses.request.POST.get('part')
        self.__form.fields['name'].initial = self.__ses.request.POST.get('name')
        self.__form.fields['registStartDate'].initial = self.__ses.request.POST.get('registStartDate')
        self.__form.fields['registEndDate'].initial = self.__ses.request.POST.get('registEndDate')
        self.__form.fields['keyWord'].initial = self.__ses.request.POST.get('keyWord')
      else:
        # 検索画面ロード時
        self.__form.fields['part'].initial = ""
        self.__form.fields['name'].initial = ""
        retentionPeriodNow = datetime.today() - relativedelta(years=0)
        retentionPeriodAgo = datetime.today() - relativedelta(years=2)
        self.__form.fields['registStartDate'].initial = datetime.strftime(retentionPeriodAgo,"%Y-%m-%d")
        self.__form.fields['registEndDate'].initial = datetime.strftime(retentionPeriodNow,"%Y-%m-%d")
      
    elif disp == 'regist':
      # 登録画面よりPOST時処理
      if 'registPart' in self.__ses.request.POST and 'registName' in self.__ses.request.POST:
        self.__form.fields['part'].initial = self.__dict['PART'][1]
        self.__form.fields['name'].initial = self.__dict['NAME'][1]
        self.__form.fields['registStartDate'].initial = self.__dict['REGISTSTARTDATE'][1]
        self.__form.fields['registEndDate'].initial = self.__dict['REGISTENDDATE'][1]
        self.__form.fields['keyWord'].initial = self.__dict['KEYWORD'][1]