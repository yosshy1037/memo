from django.http.response import HttpResponse,Http404
from . import registDb,registModel
from ..common import dbMainClass,const,constDef,formValidateClass
import json

def registList(request):
  if request.method == 'POST':
    
    # モデルへ値格納
    model = registModel.registModel()
    model.request = request
    model.collumList = ['part','name','gender','contents','biko']
    model.collumAddList = ['regist_date','regist_name','update_date','update_name','delete_date','delete_name','delete_flg']
    model.valueListCreate()
    
    # 値チェック
    validate = formValidateClass.formValidate()
    validate.collumList = model.Tmp
    validate.valueList = model.valueList
    validate.validateCheck()
    if len(validate.messageList) > 0:
      response = json.dumps({'result':'すべて入力してください。','err':validate.messageList})
      return HttpResponse(response)
    
    
    # DB登録処理
    db = dbMainClass.dbMain()
    riSql = registDb.insertSql()
    db.dbConnection()
    
    riSql.valueList = model.valueList
    riSql.registInsert()
    db.bindVal = riSql.bindVal
    db.execute(riSql.sql,const.ins,'')
    db.dbCommitOrRollback()
    db.dbClose()

    # レスポンス返却
    response = json.dumps({'result':'登録完了'})
    return HttpResponse(response)
    
  else:
    raise Http404