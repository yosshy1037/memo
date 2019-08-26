from django.http.response import HttpResponse,Http404
from . import searchDb,searchModel
from ..common import dbMainClass,const,constDef,commonFuncClass
import datetime,math,json

def resultListView(request):
  if request.method == 'POST':
    com = commonFuncClass.commonFunc()
    model = searchModel.searchModel()
    
    # モデルへ値格納
    model.request = request
    model.collumList = ['part','name','registStartDate','registEndDate','gender','keyWord','pageNum']
    model.valueListCreate()
    
    startPos = 0
    endPos = 0
    pageNum = model.valueList['PAGENUM'][1]
    
    # DB処理
    db = dbMainClass.dbMain()
    db.dbConnection()
    
    sqlct = searchDb.searchSelectCountSql(model.valueList)
    db.execute(sqlct,const.sel,const.fetchModeOne)
    pageFull = db.result[0]
    if pageFull == 0:
      pageNum = 1
    
    sql = searchDb.searchSelectSql(model.valueList)
    db.execute(sql,const.sel,const.fetchModeTwo)
    db.dbClose()
    
    dateRow = {}
    dataResult = {}
    num = 0
    
    # ループして取得
    for row in db.result:
       dataResult["ID"] = row[0]
       dataResult["PART"] = row[1]
       dataResult["NAME"] = row[2]
       dataResult["GENDER"] = row[3]
       contents = row[4].replace('\n','<br>')
       if len(contents) > 30:
         contents_tmp = com.mid(contents,1,30) + "・・・"
       else:
         contents_tmp = contents
       dataResult["CONTENTS"] = contents_tmp
       biko = row[5].replace('\n','<br>')
       if len(biko) > 35:
         biko_tmp = com.mid(biko,1,35) + "・・・"
       else:
         biko_tmp = biko
       dataResult["BIKO"] = biko_tmp
       registDate = row[6].strftime("%Y/%m/%d %H:%M:%S")
       
       dataResult["REGIST_DATE"] = registDate
       dateRow[num] = dataResult
       dataResult = {}
       num += 1
    
    # aタグ作成
    atag = ''
    startATag = ''
    endATag = ''
    pageAll = math.ceil(int(pageFull)/3)
    if pageAll == 0:
      pageAll = 1
    
    # aタグ制御
    if int(pageNum) == 1:
      startPos = 1
    else:
      startPos = int(pageNum) - 1
      startATag = '<a href="#" class="pager" onClick="pager(1)" >&laquo;</a>'
    
    if int(pageNum) == int(pageAll):
      endPos = int(pageAll) + 1
    else:
      endPos = (int(pageNum) - 1) + 3
      endATag = '<a href="#" class="pager"  onClick="pager(' + str(pageAll) + ')" >&raquo;</a>'
    
    # aタグ生成
    atag = startATag
    
    for i in range(startPos,endPos):
      if int(pageNum) == i:
        atag += '<a href="#" class="pager clicked" onClick="pager(' + str(i) + ')" >' + str(i) + '</a>';
      else:
        atag += '<a href="#" class="pager" onClick="pager(' + str(i) + ')" >' + str(i) + '</a>';
    
    atag += endATag
    
    # 一覧作成
    tag = '<table>'
    
    tag += '<tr>'
    tag += '  <th class="partHeader">役割</th>'
    tag += '  <th class="nameHeader">名称（人名）</th>'
    tag += '  <th class="registDateHeader">登録日</th>'
    tag += '  <th class="contentsHeader">内容</th>'
    tag += '  <th class="bikoHeader">備考</th>'
    tag += '  <th class="detailedConfirmHeader"></th>'
    tag += '</tr>'
    
    for row in dateRow:
      tag += '    <tr>'
      tag += '      <td>' + str(dateRow[row]["PART"]) + '</td>'
      tag += '      <td>' + str(dateRow[row]["NAME"]) + '</td>'
      tag += '      <td>' + str(dateRow[row]["REGIST_DATE"]) + '</td>'
      tag += '      <td>' + str(dateRow[row]["CONTENTS"]) + '</td>'
      tag += '      <td>' + str(dateRow[row]["BIKO"]) + '</td>'
      tag += '      <td>'
      tag += '        <input type="submit" value="詳細" class="detailedConfirm" onClick="detailSend(' + str(dateRow[row]["ID"]) + ')" />'
      tag += '      </td>'
      tag += '    </tr>'
    
    tag += '</table>'
    
    response = json.dumps({'result':tag,'atag':atag})
        
    return HttpResponse(response)
    
  else:
    raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも