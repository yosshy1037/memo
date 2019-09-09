from django.http.response import HttpResponse,Http404
from . import detailDb,detailModel
from ..common import dbMainClass,const,constDef,formValidateClass,exceptionClass
import json

def detailList(request):
  if request.method == 'POST':
    
    try:
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
      ddSql = detailDb.detailSql()
      db.dbConnection()
      
      # 更新クエリ
      ddSql.valueList = model.valueList
      db.bindVal = ddSql.bindVal
      ddSql.detailUpdateSql()
      db.execute(ddSql.sql,const.upd,'')
      
      # コミットorロールバック処理
      db.dbCommitOrRollback()
      db.dbClose()
    
    except ZeroDivisionError as e:
      print(e.message)
      
    except exceptionClass.originalException as e:
      e.errMes = e.message
      e.logOutput()
      return HttpResponse(response)

    finally:
      # レスポンス返却
      response = json.dumps({'result':'更新完了'})
      return HttpResponse(response)
    
  else:
    raise Http404 
