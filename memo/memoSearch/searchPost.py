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
    ssSql = searchDb.searchSql()
    db.dbConnection()
    
    ssSql.valueList = model.valueList
    ssSql.searchSelectCountSql()
    db.bindVal = ssSql.bindVal
    
    # 件数取得クエリ実行
    db.execute(ssSql.sql,const.sel,const.fetchModeOne)
    pageFull = db.result[0]
    if pageFull == 0:
      pageNum = 1
    
    ssSql.searchSelectSql()
    db.bindVal = ssSql.bindVal
    
    # 値取得クエリ実行
    db.execute(ssSql.sql,const.sel,const.fetchModeTwo)
    
    # DB閉じる
    db.dbClose()
    
    # 一覧表示用値整形
    model.com = com
    model.result = db.result
    model.viewListCreate()
    
    # aタグ作成
    atag = ''
    startATag = ''
    endATag = ''
    pageAll = math.ceil(int(pageFull)/const.intervalPageNum)
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
    elif const.intervalPageNum > int(pageAll):
      endPos = int(pageAll) + 1
      endATag = '<a href="#" class="pager"  onClick="pager(' + str(pageAll) + ')" >&raquo;</a>'
    else:
      endPos = int(pageAll) + 1
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
    
    for row in model.dateRow:
      tag += '    <tr>'
      tag += '      <td>' + str(model.dateRow[row]["PART"]) + '</td>'
      tag += '      <td>' + str(model.dateRow[row]["NAME"]) + '</td>'
      tag += '      <td>' + str(model.dateRow[row]["REGIST_DATE"]) + '</td>'
      tag += '      <td>' + str(model.dateRow[row]["CONTENTS"]) + '</td>'
      tag += '      <td>' + str(model.dateRow[row]["BIKO"]) + '</td>'
      tag += '      <td>'
      tag += '        <input type="submit" value="詳細" class="detailedConfirm" onClick="detailSend(' + str(model.dateRow[row]["ID"]) + ')" />'
      tag += '      </td>'
      tag += '    </tr>'
    
    tag += '</table>'
    
    response = json.dumps({'result':tag,'atag':atag})
        
    return HttpResponse(response)
    
  else:
    raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも