from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from ..memoLogin import loginDb
from . import dbMainClass,const,constDef

class formValidate():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__valueList = ""
    self.__collumList = []
    self.__messageList = {}

  # チェック処理
  def validateCheck(self):
    for col in self.__collumList:
      if col.upper() == "LOGINUSER" and self.__valueList[col.upper()][1] != '':
        # ログイン情報確認
        db = dbMainClass.dbMain()
        db.dbConnection()
        sqlct = loginDb.loginSelectSql(None,self.__collumList,self.__valueList)
        db.execute(sqlct,const.sel,const.fetchModeOne)
        loginCt = db.result[0]
        db.dbClose()
        
        if loginCt == 0:
          self.__messageList[col.upper() + "_ERR"] = 'ログイン情報が存在しません'
      elif self.__valueList[col.upper()][0] == 'str' and self.__valueList[col.upper()][1] == '':
        self.__messageList[col.upper() + "_ERR"] = '文字を入力してください'
      elif self.__valueList[col.upper()][0] == 'int' and self.__valueList[col.upper()][1] == '':
        self.__messageList[col.upper() + "_ERR"] = '選択してください。'

  @property
  def collumList(self):
    return self.__collumList

  @collumList.setter
  def collumList(self,collumList):
    self.__collumList = collumList

  @property
  def valueList(self):
    return self.__valueList

  @valueList.setter
  def valueList(self,valueList):
    self.__valueList = valueList

  # エラーメッセージ
  @property
  def messageList(self):
    return self.__messageList

  @messageList.setter
  def messageList(self,messageList):
    self.__messageList = messageList