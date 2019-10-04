from django.http.response import HttpResponse,Http404
from django.views.generic import View
from ...memoSearch import searchDb,searchModel
from ...common import dbMainClass,const,constDef,formValidateClass,exceptionClass,logClass,commonFuncClass
import math,json,traceback

## 検索処理のクラス
class searchListPost(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__model = searchModel.searchModel()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__db = dbMainClass.dbMain()
    self.__ssSql = searchDb.searchSql()

  # GetMethod
  def get(self, request, *args, **kwargs):
    raise Http404
    
  # POSTMethod
  def post(self, request, *args, **kwargs):
    successMes = ""
    tag = ""
    atag = ""
    
    try:
      #-- モデルへ値格納
      self.__model.request = request
      self.__model.json = json
      self.__model.collumList = ['part','name','registStartDate','registEndDate','keyWord','pageNum']
      self.__model.valueListCreate()
      
      startPos = 0
      endPos = 0
      pageNum = self.__model.valueList['PAGENUM'][1]
      
      #-- DB処理
      self.__db.dbConnection()
      
      #-- 件数取得クエリ
      self.__ssSql.request = request
      self.__ssSql.valueList = self.__model.valueList
      self.__ssSql.searchSelectCountSql()
      self.__db.bindVal = self.__ssSql.bindVal
      self.__db.execute(self.__ssSql.sql,const.sel,const.fetchModeOne)
      pageFull = self.__db.result[0]
      if pageFull == 0:
        pageNum = 1
      
      # 全ページ数取得
      pageAll = math.ceil(int(pageFull)/const.intervalPageNum)
      if pageAll == 0:
        pageAll = 1
      
      # 自ページの制御
      if int(pageNum) > int(pageAll):
        pageNum = pageAll
        self.__model.valueList['PAGENUM'][1] = pageAll
      
      #-- 値取得クエリ
      self.__ssSql.searchSelectSql()
      self.__db.bindVal = self.__ssSql.bindVal
      self.__db.execute(self.__ssSql.sql,const.sel,const.fetchModeTwo)
      
      #-- DB閉じる
      self.__db.dbClose()
      
      # 一覧表示用値整形
      self.__model.com = self.__com
      self.__model.result = self.__db.result
      self.__model.viewListCreate()
      
      #-- aタグ作成
      atag = ''
      startATag = ''
      endATag = ''

      
      #-- aタグ制御
      # 1ページ目処理
      if int(pageNum) == 1:
        startPos = 1
      else:
        startPos = int(pageNum) - 1
        startATag = '<a href="#" class="pager" data-link="1" onClick="pager(1,'')" >&laquo;</a>'
      
      # 選択ページ=最終ページ
      if int(pageNum) == int(pageAll):
        endPos = int(pageAll) + 1
      elif const.intervalPageNum > int(pageAll):
        endPos = int(pageAll) + 1
        endATag = '<a href="#" class="pager" data-link="' + str(pageAll) + '"  onClick="pager(' + str(pageAll) + ','')" >&raquo;</a>'
      else:
        endPos = int(pageAll) + 1
        endATag = '<a href="#" class="pager" data-link="' + str(pageAll) + '" onClick="pager(' + str(pageAll) + ','')" >&raquo;</a>'
      
      #-- aタグ生成
      atag = startATag
      
      # ページ作成
      for i in range(startPos,endPos):
        if int(pageNum) == i:
          atag += '<a href="#" class="pager clicked" data-link="' + str(i) + '" onClick="pager(' + str(i) + ','')" >' + str(i) + '</a>';
        else:
          atag += '<a href="#" class="pager" data-link="' + str(i) + '" onClick="pager(' + str(i) + ','')" >' + str(i) + '</a>';
      
      atag += endATag

      #-- 一覧作成
      tag = '<table>'
      
      tag += '<tr>'
      tag += '  <th class="partHeader">タイトル</th>'
      tag += '  <th class="nameHeader">名称（人名）</th>'
      tag += '  <th class="registDateHeader">登録日</th>'
      tag += '  <th class="contentsHeader">内容</th>'
      tag += '  <th class="bikoHeader">備考</th>'
      tag += '  <th class="detailedConfirmHeader"></th>'
      tag += '</tr>'

      for row in self.__model.dateRow:
        tag += '    <tr>'
        tag += '      <td>' + str(self.__model.dateRow[row]["PART"]) + '</td>'
        tag += '      <td>' + str(self.__model.dateRow[row]["NAME"]) + '</td>'
        tag += '      <td>' + str(self.__model.dateRow[row]["REGIST_DATE"]) + '</td>'
        tag += '      <td>' + str(self.__model.dateRow[row]["CONTENTS"]) + '</td>'
        tag += '      <td>' + str(self.__model.dateRow[row]["BIKO"]) + '</td>'
        tag += '      <td>'
        tag += '        <input type="submit" value="詳細" class="detailedConfirm" onClick="detailSend(' + str(self.__model.dateRow[row]["ID"]) + ')" />'
        tag += '      </td>'
        tag += '    </tr>'
      
      tag += '</table>'

    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__db.dbClose()
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
    except Exception as e:
      # Exception処理
      self.__db.dbClose()
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
    
    # レスポンス返却
    response = json.dumps({'result':tag,'atag':atag})
    return HttpResponse(response)