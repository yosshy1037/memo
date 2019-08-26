from django.http.response import HttpResponse,Http404
from django.shortcuts import render
from . import detailDb,detailModel
from ..common import dbMainClass,const,constDef,formValidateClass
from datetime import datetime
import math,json

def detailList(request):
  if request.method == 'POST':
    # モデルへ値格納
    model = detailModel.detailModel()
    model.request = request
    model.collumList = ['part','name','gender','contents','biko']
    model.collumAddList = ['update_date','update_name','delete_flg','detailQuery']
    model.valueListCreate()
    
    # 値チェック
    validate = formValidateClass.formValidate()
    validate.collumList = model.Tmp
    validate.valueList = model.valueList
    validate.validateCheck()
    if len(validate.messageList) > 0:
      response = json.dumps({'result':'すべて入力してください。','err':validate.messageList})
      return HttpResponse(response)
    
    # DB更新処理
    db = dbMainClass.dbMain()
    db.dbConnection()
    
    sql = detailDb.detailUpdate(None,model.valueList)
    db.execute(sql,const.upd,'')
    db.dbCommitOrRollback()
    db.dbClose()

    response = json.dumps({'result':'更新完了'})
    return HttpResponse(response)
    
  else:
    raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも