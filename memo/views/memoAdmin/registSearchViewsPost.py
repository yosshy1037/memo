from django.http.response import HttpResponse,Http404
from django.views.generic import View
from ...memoAdmin import adminRegistSearchDb,adminRegistSearchModel
from ...common import dbMainClass,const,constDef,formValidateClass,exceptionClass,logClass,commonFuncClass
import math,json,traceback

## 作成者処理のクラス
class adRegistSearchViewsPost(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__model = adminRegistSearchModel.registSearchModel()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__db = dbMainClass.dbMain()
    self.__arcSql = adminRegistSearchDb.registConnectSql()
    self.__proc = ""

  # GetMethod
  def get(self, request, *args, **kwargs):
    raise Http404
    
  # POSTMethod
  def post(self, request, *args, **kwargs):
    successMes = ""
    tag = ""
    atag = ""
    resultCt = 0
    
    try:
      # postData存在
      if request.POST.get('postData') is not None:
        postData = json.loads(request.POST.get('postData'))
        
        # DB処理
        self.__db.dbConnection()
        
        # モデルへ値格納
        self.__model = adminRegistSearchModel.registSearchModel()
        self.__model.request = request
        self.__model.postData = postData
        
        # 登録処理
        if postData['status'] == 'regist':
          
          # 値生成
          self.__model.collumList = ['loginUserId','registId','resultLoginUserId','resultRegistId']
          self.__model.collumAddList = ['update_date','update_name','delete_date','delete_name','delete_flg']
          self.__model.valueListCreate()
          
          # DB登録処理
          self.__arcSql.valueList = self.__model.valueList
          # 登録SQL用意
          self.__arcSql.registInsertSql()
          self.__db.bindVal = self.__arcSql.bindVal
          self.__db.execute(self.__arcSql.sql,const.ins,'')
          self.__proc = '登録処理'
        
        # 更新処理
        elif postData['status'] == 'update':
          
          # 値生成
          self.__model.collumList = ['id']
          self.__model.valueListCreate()
          
          # 作成者取得
          self.__arcSql.valueList = self.__model.valueList
          self.__arcSql.registSearchSql()
          self.__db.bindVal = self.__arcSql.bindVal
          self.__db.execute(self.__arcSql.sql,const.sel,const.fetchModeTwo)
          
          self.__model.collumList = ['loginUserId','registId','id']
          self.__model.collumAddList = ['update_date','update_name']
          self.__model.valueListCreate()
          
          self.__model.valueList['LOGINUSERID'][1] = self.__db.result[0][1]
          # 選択した作成者格納
          for col in postData:
            if 'resultLoginUserIdSelect_' in col:
              self.__model.valueList['REGISTID'][1] = postData[col]
          
          # 更新実行
          self.__arcSql.valueList = self.__model.valueList
          self.__arcSql.registUpdateSql()
          self.__db.bindVal = self.__arcSql.bindVal
          self.__db.execute(self.__arcSql.sql,const.upd,'')
          self.__proc = '更新処理'
          
        # 削除処理
        elif postData['status'] == 'delete':
          # 値生成
          if postData['loginUserId'] != '':
            self.__model.collumList = ['loginUserId','id']
          else:
            self.__model.collumList = ['id']
          self.__model.valueListCreate()
          
          # 削除実行
          self.__arcSql.valueList = self.__model.valueList
          self.__arcSql.registDeleteSql()
          self.__db.bindVal = self.__arcSql.bindVal
          self.__db.execute(self.__arcSql.sql,const.ins,'')
          self.__proc = '削除処理'
        
        # コミット
        self.__db.dbCommit()
        
        # 値生成
        self.__model.collumList = ['loginUserId','registId']
        self.__model.collumAddList = ['update_date','update_name','delete_date','delete_name','delete_flg']
        self.__model.valueListCreate()
          
        # 値取得クエリ
        self.__arcSql.valueList = self.__model.valueList
        self.__arcSql.registSearchSql()
        self.__db.bindVal = self.__arcSql.bindVal
        self.__db.execute(self.__arcSql.sql,const.sel,const.fetchModeTwo)
        
        # DB閉じる
        self.__db.dbClose()
        
        # 完了メッセージ
        if self.__proc != "":
          successMes = '<p class="mes">' + str(self.__proc) + str(self.__db.resultCount) + '件正常終了しました。</p>'
        # 一覧表示用値整形
        self.__model.com = self.__com
        self.__model.result = self.__db.result
        self.__model.viewListCreate()

        # 一覧作成
        tag = '<table>'

        # 登録エリア
        tag += '<tr>'
        tag += '  <th class="loginUserId">ログインユーザID</th>'
        tag += '  <th class="registId">作成者ID</th>'
        tag += '</tr>'
        
        tag += '    <tr>'
        tag += '      <td><input type"text" name="resultLoginUserId" class="resultLoginUserId" /></td>'
        tag += '      <td><input type"text" name="resultRegistId" class="resultRegistId" /></td>'
        tag += '    </tr>'
        tag += '    <tr>'
        tag += '      <td>'
        tag += '        <input type="submit" value="登録" class="registIdRegist" onclick="registIdRegist(); return false;" />'
        tag += '      </td>'
        tag += '    </tr>'

        
        # 更新エリア
        tag += '<tr>'
        tag += '  <th class="loginUserId">ログインユーザID</th>'
        tag += '  <th class="registUserId">作成者ID</th>'
        tag += '  <th class="registUpdateButton"></th>'
        tag += '</tr>'
        for row in self.__model.dateRow:
          tag += '    <tr>'
          tag += '      <td>'
          tag += str(self.__model.dateRow[row]["LOGINUSERID"])
          tag += '      </td>'
          tag += '      <td>'
          tag += '        <select name="resultLoginUserIdSelect_' + str(self.__model.dateRow[row]["ID"]) + '" class="resultLoginUserIdSelect">'
          # プルダウンメニュー生成
          pullDown = ""
          for rowOption in self.__model.dateRow:
            if str(self.__model.dateRow[row]["REGISTID"]) == str(self.__model.dateRow[rowOption]["REGISTID"]):
              pullDown += '<option value="' + str(self.__model.dateRow[rowOption]["REGISTID"]) + '" selected>'
              pullDown += str(self.__model.dateRow[rowOption]["REGISTID"]) + '</option>'
            else:
              pullDown += '<option value="' + str(self.__model.dateRow[rowOption]["REGISTID"]) + '">'
              pullDown += str(self.__model.dateRow[rowOption]["REGISTID"]) + '</option>'
          tag += pullDown
          tag += '        </select>'
          tag += '      </td>'
          tag += '      <td>'
          tag += '        <input type="submit" value="更新" class="registIdUpdate" onclick="registIdUpdate(' + str(self.__model.dateRow[row]["ID"]) + '); return false;" />'
          tag += '        <input type="submit" value="削除" class="registIdDelete" onclick="registIdDelete(' + str(self.__model.dateRow[row]["ID"]) + '); return false;" />'
          tag += '      </td>'
          tag += '    </tr>'
        
        tag += '</table>'
   
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__db.dbRollback()
      self.__db.dbClose()
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
    except Exception as e:
      # Exception処理
      self.__db.dbRollback()
      self.__db.dbClose()
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
    
    # レスポンス返却
    response = json.dumps({'result':tag,'status':successMes})
    return HttpResponse(response)