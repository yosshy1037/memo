from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from ..common import const,constDef
from datetime import datetime
import copy

class registSearchModel():

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
    self.__postData = {}
    self.__num = 0
    
    self.Tmp = []

  # 値配列作成処理
  def valueListCreate(self):
    self.__valueList = {}
    self.__collumList.extend(self.__collumAddList)
    for col in self.__collumList:
      value = ''
      init = ''
      type = 'str'
      if col == "regist_date":
        type = 'date'
        value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      elif col == "regist_name":
        value = str(self.__request.session['ADLOGINUSER'])
      elif col == "update_date":
        type = 'date'
        value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      elif col == "update_name":
        value = str(self.__request.session['ADLOGINUSER'])
      elif col == "delete_date":
        type = 'date'
        value = '1999-01-01 00:00:00'
      elif col == "delete_name":
        value = ''
      elif col == "delete_flg":
        type = 'int'
        value = 0
      elif col == "id":
        type = 'int'
        value = str(self.__postData[col])
      else:
        value = str(self.__postData[col])
      self.__valueList[col.upper()] = [type,value]
  # 一覧表示用値整形
  def viewListCreate(self):
    # ループして取得
    for row in self.__result:
      self.__dataResult["ID"] = row[0]
      self.__dataResult["LOGINUSERID"] = row[1]
      self.__dataResult["REGISTID"] = row[2]
      self.__dateRow[self.__num] = self.__dataResult
      self.__dataResult = {}
      self.__num += 1

  # カラム配列
  @property
  def collumList(self):
    return self.__collumList

  @collumList.setter
  def collumList(self,collumList):
    self.__collumList = []
    self.__collumList = collumList
    self.Tmp = copy.deepcopy(collumList)
    
  # カラム配列(時刻と実行者)
  @property
  def collumAddList(self):
    return self.__collumAddList

  @collumList.setter
  def collumAddList(self,collumAddList):
    self.__collumAddList = []
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
    
  # 整形後配列
  @property
  def postData(self):
    return self.__postData

  @postData.setter
  def postData(self,postData):
    self.__postData = postData

  # DB値取得
  @property
  def result(self):
    return self.__result

  @result.setter
  def result(self,result):
    self.__result = result

  # 一覧表示用値
  @property
  def dateRow(self):
    return self.__dateRow

  @dateRow.setter
  def dateRow(self,dateRow):
    self.__dateRow = dateRow