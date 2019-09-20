from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from ..common import const,constDef
from datetime import datetime
import copy

class detailModel():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__request = ""
    self.__json = ""
    self.__collumList = []
    self.__collumAddList = []
    self.__valueList = {}
    
    self.Tmp = []

  # 値配列作成処理
  def valueListCreate(self):
    self.__collumList.extend(self.__collumAddList)
    for col in self.__collumList:
      value = ''
      init = ''
      type = 'str'
      if col == "regist_date":
        type = 'date'
        value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      elif col == "regist_name":
        value = str(self.__request.session['LOGINUSER'])
      elif col == "update_date":
        type = 'date'
        value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
      elif col == "update_name":
        value = str(self.__request.session['LOGINUSER'])
      elif col == "delete_date":
        type = 'date'
        value = '1999-01-01 00:00:00'
      elif col == "delete_name":
        value = ''
      elif col == "delete_flg":
        type = 'int'
        value = 0
      else:
        postData = self.__json.loads(self.__request.POST.get('postData'))
        value = postData[col]
      self.__valueList[col.upper()] = [type,value]
  
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

  # JSON
  @property
  def json(self):
    return self.__json

  @json.setter
  def json(self,json):
    self.__json = json
  
  # 整形後配列
  @property
  def valueList(self):
    return self.__valueList

  @valueList.setter
  def valueList(self,valueList):
    self.__valueList = valueList