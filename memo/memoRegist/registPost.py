from django.http.response import HttpResponse,Http404
from django.shortcuts import render
from . import registDb,registModel
from ..common import dbMainClass,const,constDef,formValidateClass
from datetime import datetime
import math,json

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
    db.dbConnection()
    
    sql = registDb.registInsert(None,model.valueList)
    db.execute(sql,const.ins,'')
    db.dbCommitOrRollback()
    db.dbClose()

    response = json.dumps({'result':'登録完了'})
    return HttpResponse(response)
    
  else:
    raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも