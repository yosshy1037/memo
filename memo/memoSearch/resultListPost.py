from django.http.response import HttpResponse,Http404
from django.shortcuts import render
from . import database
import datetime
import math

def resultListView(request):
  import json
  
  if request.method == 'POST':
    
    startPos = 0
    endPos = 0
    pageNum = request.POST.get('pageNum',None)
    partVal = request.POST.get('partVal',None)
    nameVal = request.POST.get('nameVal',None)
    result = database.memoSearchSelect(None,pageNum,partVal,nameVal);
    
    # aタグ作成
    atag = ''
    startATag = ''
    endATag = ''
    pageAll = math.ceil(int(result[1][0])/3)
    
    # aタグ制御
    if int(pageNum) == 1:
      startPos = 1
    else:
      startPos = int(pageNum) - 1
      startATag = '<a href="#" class="pager" onClick="pager(1,'"+ partVal +"',0)" >&laquo;</a>'
    
    if int(pageNum) == int(pageAll):
      endPos = int(pageAll) + 1
    else:
      endPos = (int(pageNum) - 1) + 3
      endATag = '<a href="#" class="pager"  onClick="pager(' + str(pageAll) + ','"+ partVal +"',0)" >&raquo;</a>'
    
    # aタグ生成
    atag = startATag
    
    for i in range(startPos,endPos):
      if int(pageNum) == i:
        atag += '<a href="#" class="pager clicked" onClick="pager(' + str(i) + ','"+ partVal +"',0)" >' + str(i) + '</a>';
      else:
        atag += '<a href="#" class="pager" onClick="pager(' + str(i) + ','"+ partVal +"',0)" >' + str(i) + '</a>';
    
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
    
    for row in result[0]:
      tag += '    <tr>'
      tag += '      <td>' + row[1] + '</td>'
      tag += '      <td>' + row[2] + '</td>'
      tag += '      <td>' + str(row[6]) + '</td>'
      tag += '      <td>' + row[4] + '</td>'
      tag += '      <td>' + row[5] + '</td>'
      tag += '      <td>'
      tag += '        <input type="submit" value="詳細確認" class="detailedConfirm" />'
      tag += '      </td>'
      tag += '    </tr>'
    
    tag += '</table>'
    
    response = json.dumps({'result':tag,'atag':atag})
        
    return HttpResponse(response)
    
  else:
    raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも