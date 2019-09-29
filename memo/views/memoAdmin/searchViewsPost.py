from django.http.response import HttpResponse,Http404
from django.views.generic import View
from ...memoSearch import searchDb,searchModel
from ...memoAdmin import adminSearchDb
from ...common import dbMainClass,const,constDef,formValidateClass,exceptionClass,logClass,commonFuncClass
import math,json,traceback

## 検索処理のクラス
class adSearchListPost(View):
  # initMethod
  def __init__(self, **kwargs):
    self.__model = searchModel.searchModel()
    self.__com = commonFuncClass.commonFunc()
    self.__log = logClass.logger()
    self.__exc = exceptionClass.dispatchException()
    self.__db = dbMainClass.dbMain()
    self.__ssSql = searchDb.searchSql()
    self.__auSql = adminSearchDb.updateSql()

  # GetMethod
  def get(self, request, *args, **kwargs):
    raise Http404
    
  # POSTMethod
  def post(self, request, *args, **kwargs):
    successMes = ""
    tag = ""
    atag = ""
    resultCt = 0
    
    try:
      # postDataが存在する
      if request.POST.get('postData') is not None:
        postData = json.loads(request.POST.get('postData'))
        
        # DB処理
        self.__db.dbConnection()
        
        # モデルへ値格納
        self.__model = searchModel.searchModel()
        self.__model.request = request
        self.__model.json = json
        
        # 複数処理
        if postData['status'] == 'multiOpe':
          self.__model.collumList = ['update_date','update_name','delete_date','delete_name','delete_flg']
          self.__model.valueListCreate()
          # ID毎に復帰
          for id in postData['list']:
            resultCt += 1;
            self.__auSql.valueList = self.__model.valueList
            self.__auSql.detailUpdRefSql(id)
            self.__db.bindVal = self.__auSql.bindVal
            self.__db.execute(self.__auSql.sql,const.upd,'')
            
          # コミット処理
          self.__db.dbCommit()
          
          # 完了メッセージ
          successMes = '<p class="mes">復帰処理 ' + str(resultCt) + '件正常終了しました。</p>'
        
        # 表示処理
        self.__model.collumList = ['registStartDate','registEndDate','keyWord','pageNum']
        self.__model.valueListCreate()
        
        startPos = 0
        endPos = 0
        pageNum = self.__model.valueList['PAGENUM'][1]
        
        # 件数取得クエリ
        self.__ssSql.request = request
        self.__ssSql.valueList = self.__model.valueList
        self.__ssSql.searchSelectCountSql()
        self.__db.bindVal = self.__ssSql.bindVal
        self.__db.execute(self.__ssSql.sql,const.sel,const.fetchModeOne)
        pageFull = self.__db.result[0]
        if pageFull == 0:
          pageNum = 1
        
        # 値取得クエリ
        self.__ssSql.searchSelectSql()
        self.__db.bindVal = self.__ssSql.bindVal
        self.__db.execute(self.__ssSql.sql,const.sel,const.fetchModeTwo)
        
        # DB閉じる
        self.__db.dbClose()
        
        # 一覧表示用値整形
        self.__model.com = self.__com
        self.__model.result = self.__db.result
        self.__model.viewListCreate()
        
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
        tag += '  <th class="partHeader">タイトル</th>'
        tag += '  <th class="registDateHeader">削除日</th>'
        tag += '  <th class="contentsHeader">内容</th>'
        tag += '  <th class="bikoHeader">備考</th>'
        tag += '  <th class="detailedConfirmHeader"></th>'
        tag += '</tr>'
        
        for row in self.__model.dateRow:
          tag += '    <tr>'
          tag += '      <td>' + str(self.__model.dateRow[row]["PART"]) + '</td>'
          tag += '      <td>' + str(self.__model.dateRow[row]["DELETE_DATE"]) + '</td>'
          tag += '      <td>' + str(self.__model.dateRow[row]["CONTENTS"]) + '</td>'
          tag += '      <td>' + str(self.__model.dateRow[row]["BIKO"]) + '</td>'
          tag += '      <td>'
          tag += '        <input type="checkbox" value="' + str(self.__model.dateRow[row]["ID"]) + '" class="detailedConfirm" />'
          tag += '      </td>'
          tag += '    </tr>'
        
        tag += '</table>'
   
    except exceptionClass.OriginException as e:
      # Exception継承処理
      self.__db.dbClose()
      self.__com.postExceptDispos(e, self.__log, e, traceback.format_exc())
    except Exception as e:
      print(str(traceback.format_exc()));
      # Exception処理
      self.__db.dbClose()
      self.__com.postExceptDispos(self.__exc, self.__log, e, traceback.format_exc())
    
    # レスポンス返却
    response = json.dumps({'result':tag,'atag':atag,'status':successMes})
    return HttpResponse(response)