from django.http.response import HttpResponse,Http404
from django.views.generic import View
from ...memoRegist import registDb,registModel
from ...common import dbMainClass,const,constDef,formValidateClass,exceptionClass,logClass,commonFuncClass
import json,traceback

## 登録処理のクラス
class registPost(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__model = registModel.registModel()
    self.__validate = formValidateClass.formValidate()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__db = dbMainClass.dbMain()
    self.__riSql = registDb.insertSql()

  # GetMethod
  def get(self, request, *args, **kwargs):
    raise Http404
  
  # POSTMethod
  def post(self, request, *args, **kwargs):
    successMes = ""
    
    try:
      # DB接続
      self.__db.dbConnection()
      
      # モデルセット
      self.__model.request = request
      self.__model.json = json
      
      # 値生成
      self.__model.collumList = ['part','name','contents','biko']
      self.__model.collumAddList = ['regist_date','regist_name','update_date','update_name','delete_date','delete_name','delete_flg']
      self.__model.valueListCreate()
      
      # 値チェック
      self.__validate.collumList = self.__model.Tmp
      self.__validate.valueList = self.__model.valueList
      self.__validate.validateCheck()
      if len(self.__validate.messageList) > 0:
        response = json.dumps({'result':'すべて入力してください。','err':self.__validate.messageList})
        return HttpResponse(response)
      
      # DB登録処理
      self.__riSql.valueList = self.__model.valueList
      # 登録SQL用意
      self.__riSql.registInsert()
      self.__db.bindVal = self.__riSql.bindVal
      self.__db.execute(self.__riSql.sql,const.ins,'')
      self.__db.dbCommit()
      self.__db.dbClose()

      successMes = '登録完了'

    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__db.dbRollback()
      self.__db.dbClose()
      successMes = self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc(), '登録失敗')
    except Exception as e:
      # Exception処理
      self.__db.dbRollback()
      self.__db.dbClose()
      successMes = self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc(), '登録失敗')

    # レスポンス返却
    response = json.dumps({'result':successMes})
    return HttpResponse(response)