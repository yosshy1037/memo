from django.http.response import HttpResponse,Http404
from django.views.generic import View
from ...memoDetail import detailDb,detailModel
from ...common import dbMainClass,const,constDef,formValidateClass,exceptionClass,logClass,commonFuncClass
import json,traceback

## 詳細更新処理のクラス
class detailPost(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__model = detailModel.detailModel()
    self.__validate = formValidateClass.formValidate()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__db = dbMainClass.dbMain()
    self.__ddSql = detailDb.detailSql()
  
  # GetMethod
  def get(self, request, *args, **kwargs):
    raise Http404
  
  # POSTMethod
  def post(self, request, *args, **kwargs):
    successMes = ""
    
    try:
      # DB接続
      self.__db.dbConnection()

      # モデルへ値格納
      self.__model.request = request
      self.__model.json = json
      
      # 更新処理
      if str(json.loads(request.POST.get('postData'))['status']) == const.upd:
        # 値生成
        self.__model.collumList = ['part','name','contents','biko']
        self.__model.collumAddList = ['update_date','update_name','delete_flg','detailQuery']
        self.__model.valueListCreate()
        
        # 値チェック
        self.__validate.collumList = self.__model.Tmp
        self.__validate.valueList = self.__model.valueList
        self.__validate.validateCheck()
        if len(self.__validate.messageList) > 0:
          response = json.dumps({'result':'すべて入力してください。','err':self.__validate.messageList})
          return HttpResponse(response)
        
        # 更新実行
        self.__ddSql.valueList = self.__model.valueList
        self.__db.bindVal = self.__ddSql.bindVal
        self.__ddSql.detailUpdateSql()
        self.__db.execute(self.__ddSql.sql,const.upd,'')
        
        # コミット処理
        self.__db.dbCommit()
        
        successMes = '<p class="mes">更新処理 ' + str(self.__db.resultCount) + '件正常終了しました。</p>'
        
      else:
      # 削除処理
        
        # 値生成
        self.__model.collumList = ['update_date','update_name','delete_date','delete_name','delete_flg','detailQuery']
        self.__model.valueListCreate()
        
        # 削除実行
        self.__ddSql.valueList = self.__model.valueList
        self.__db.bindVal = self.__ddSql.bindVal
        self.__ddSql.detailUpdDeleteSql()
        self.__db.execute(self.__ddSql.sql,const.upd,'')
        
        # コミット処理
        self.__db.dbCommit()
        
        successMes = '<p class="mes">削除処理 ' + str(self.__db.resultCount) + '件正常終了しました。</p>'
    
      # DB閉脚
      self.__db.dbClose()
    
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__db.dbRollback()
      self.__db.dbClose()
      successMes = self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc(), '<p class="mes">更新処理 異常終了しました。</p>')
    except Exception as e:
      # Exception処理
      self.__db.dbRollback()
      self.__db.dbClose()
      successMes = self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc(), '<p class="mes">更新処理 異常終了しました。</p>')

    # レスポンス返却
    response = json.dumps({'result':successMes})
    return HttpResponse(response)
