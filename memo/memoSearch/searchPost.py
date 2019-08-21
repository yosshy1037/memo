from django.http.response import HttpResponse,Http404
from django.shortcuts import render
from . import searchDb
from ..common import dbMainClass,const,constDef
import datetime
import math

def resultListView(request):
  import json
  
  if request.method == 'POST':
    
    startPos = 0
    endPos = 0
    pageNum = request.POST.get('pageNum',0)
    partVal = request.POST.get('partVal','')
    nameVal = request.POST.get('nameVal','')
    
    # DB処理
    db = dbMainClass.dbMain()
    db.dbConnection()
    
    sqlct = searchDb.searchSelectCountSql(None,pageNum,partVal,nameVal)
    db.execute(sqlct,const.sel,const.fetchModeOne)
    pageFull = db.result[0]
    
    sql = searchDb.searchSelectSql(None,pageNum,partVal,nameVal)
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
       dataResult["CONTENTS"] = contents
       biko = row[5].replace('\n','<br>')
       dataResult["BIKO"] = biko
       dataResult["REGIST_DATE"] = row[6]
       dateRow[num] = dataResult
       dataResult = {}
       num += 1
    
    # aタグ作成
    atag = ''
    startATag = ''
    endATag = ''
    pageAll = math.ceil(int(pageFull)/3)
    
    # aタグ制御
    if int(pageNum) == 1:
      startPos = 1
    else:
      startPos = int(pageNum) - 1
      startATag = '<a href="#" class="pager" onClick="pager(1,\'' + partVal + '\',0)" >&laquo;</a>'
    
    if int(pageNum) == int(pageAll):
      endPos = int(pageAll) + 1
    else:
      endPos = (int(pageNum) - 1) + 3
      endATag = '<a href="#" class="pager"  onClick="pager(' + str(pageAll) + ',\'' + partVal + '\',0)" >&raquo;</a>'
    
    # aタグ生成
    atag = startATag
    
    for i in range(startPos,endPos):
      if int(pageNum) == i:
        atag += '<a href="#" class="pager clicked" onClick="pager(' + str(i) + ',\'' + partVal + '\',0)" >' + str(i) + '</a>';
      else:
        atag += '<a href="#" class="pager" onClick="pager(' + str(i) + ',\'' + partVal + '\',0)" >' + str(i) + '</a>';
    
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
      tag += '        <input type="submit" value="詳細確認" class="detailedConfirm" />'
      tag += '      </td>'
      tag += '    </tr>'
    
    tag += '</table>'
    
    response = json.dumps({'result':tag,'atag':atag})
        
    return HttpResponse(response)
    
  else:
    raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも