from ..common import const,constDef
from datetime import datetime
import copy

class searchModel():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__request = ""
    self.__collumList = []
    self.__collumAddList = []
    self.__valueList = {}
    
    self.__com = ""
    self.__result = ""
    self.__dateRow = {}
    self.__dataResult = {}
    self.__num = 0
    
    self.Tmp = []

  # 値配列作成処理
  def valueListCreate(self):
    self.__collumList.extend(self.__collumAddList)
    for col in self.__collumList:
      value = ''
      init = ''
      type = 'str'
      if col == "registStartDate":
        type = 'date'
        init = '1999-01-01 00:00:00'
        postData = self.__json.loads(self.__request.POST.get('postData'))
        value = postData[col]
      elif col == "registEndDate":
        type = 'date'
        init = '1999-01-01 00:00:00'
        postData = self.__json.loads(self.__request.POST.get('postData'))
        value = postData[col]
      elif col == "regist_date":
        type = 'date'
        value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      elif col == "regist_name":
        if 'LOGINUSER' in self.__request.session:
          value = str(self.__request.session['LOGINUSER'])
        else:
          value = str(self.__request.session['ADLOGINUSER'])
      elif col == "update_date":
        type = 'date'
        value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      elif col == "update_name":
        if 'LOGINUSER' in self.__request.session:
          value = str(self.__request.session['LOGINUSER'])
        else:
          value = str(self.__request.session['ADLOGINUSER'])
      elif col == "delete_date":
        type = 'date'
        value = '1999-01-01 00:00:00'
      elif col == "delete_name":
        value = ''
      elif col == "delete_flg":
        type = 'int'
        value = 0
      elif col == "pageNum":
        type = 'int'
        init = 0
        postData = self.__json.loads(self.__request.POST.get('postData'))
        value = postData[col]
      else:
        postData = self.__json.loads(self.__request.POST.get('postData'))
        value = postData[col]
      self.__valueList[col.upper()] = [type,value]
  
  # 一覧表示用値整形
  def viewListCreate(self):
    # ループして取得
    for row in self.__result:
      self.__dataResult["ID"] = row[0]
      self.__dataResult["PART"] = row[1]
      self.__dataResult["NAME"] = row[2]
      contents = row[3].replace('\n','<br>')
      if len(contents) > 30:
        contents_tmp = self.__com.mid(contents,1,30) + "・・・"
      else:
        contents_tmp = contents
      self.__dataResult["CONTENTS"] = contents_tmp
      biko = row[4].replace('\n','<br>')
      if len(biko) > 35:
        biko_tmp = self.__com.mid(biko,1,35) + "・・・"
      else:
        biko_tmp = biko
      self.__dataResult["BIKO"] = biko_tmp
      registDate = row[5].strftime("%Y/%m/%d %H:%M:%S")
      self.__dataResult["REGIST_DATE"] = registDate
      self.__dataResult["DELETE_DATE"] = row[6].strftime("%Y/%m/%d %H:%M:%S")
      self.__dateRow[self.__num] = self.__dataResult
      self.__dataResult = {}
      self.__num += 1
  
  # カラム配列
  @property
  def collumList(self):
    return self.__collumList

  @collumList.setter
  def collumList(self,collumList):
    self.__collumList = collumList
    self.Tmp = copy.deepcopy(collumList)
    
  # カラム配列(時刻と実行者)
  @property
  def collumAddList(self):
    return self.__collumAddList

  @collumList.setter
  def collumAddList(self,collumAddList):
    self.__collumAddList = collumAddList
  
  # リクエスト
  @property
  def request(self):
    return self.__request

  @request.setter
  def request(self,request):
    self.__request = request
  
  # 整形後配列
  @property
  def valueList(self):
    return self.__valueList

  @valueList.setter
  def valueList(self,valueList):
    self.__valueList = valueList

  # 共通関数インスタンス
  @property
  def com(self):
    return self.__com

  @com.setter
  def com(self,com):
    self.__com = com

  # DB値取得
  @property
  def result(self):
    return self.__result

  @result.setter
  def result(self,result):
    self.__result = result
    
  # JSON
  @property
  def json(self):
    return self.__json

  @json.setter
  def json(self,json):
    self.__json = json
    
  # 一覧表示用値
  @property
  def dateRow(self):
    return self.__dateRow

  @dateRow.setter
  def dateRow(self,dateRow):
    self.__dateRow = dateRow