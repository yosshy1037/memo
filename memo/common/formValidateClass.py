from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from ..memoLogin import loginDb
from ..memoAdmin import adminLoginDb
from . import dbMainClass,const,constDef

## 入力値チェック用クラス ##
class formValidate():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__valueList = {}
    self.__collumList = []
    self.__messageList = {}
    self.__db = dbMainClass.dbMain()
    self.__llSql = loginDb.loginSelectSql()
    self.__aaSql = adminLoginDb.adLoginSelectSql()

  # チェック処理
  def validateCheck(self):
    for col in self.__collumList:
      if col.upper() == "LOGINUSER" and self.__valueList[col.upper()][1] != '':
        # ログイン情報確認
        self.__db.dbConnection()
        
        self.__llSql.valueList = self.__valueList
        self.__llSql.collumList = self.__collumList
        self.__llSql.loginSelect();
        self.__db.bindVal = self.__llSql.bindVal
        self.__db.execute(self.__llSql.sql,const.sel,const.fetchModeOne)
        if self.__db.result == None:
          loginCt = 0
        else:
          loginCt = self.__db.result[0]
          # 権限取得
          self.__valueList['ROLE'] = ['str',str(self.__db.result[1])]
        self.__db.dbClose()
        
        if loginCt == 0:
          self.__messageList[col.upper() + "_ERR"] = 'ログイン情報が存在しません'
      elif self.__valueList[col.upper()][0] == 'str' and self.__valueList[col.upper()][1] == '':
        self.__messageList[col.upper() + "_ERR"] = '文字を入力してください'
      elif self.__valueList[col.upper()][0] == 'int' and self.__valueList[col.upper()][1] == '':
        self.__messageList[col.upper() + "_ERR"] = '選択してください。'

  # 管理情報チェック処理
  def adminValidateCheck(self):
    for col in self.__collumList:
      if col.upper() == "ADLOGINUSER" and self.__valueList[col.upper()][1] != '':
        # 管理用ログイン情報確認
        self.__db.dbConnection()
        
        self.__aaSql.valueList = self.__valueList
        self.__aaSql.collumList = self.__collumList
        self.__aaSql.loginSelect();
        self.__db.bindVal = self.__aaSql.bindVal
        self.__db.execute(self.__aaSql.sql,const.sel,const.fetchModeOne)
        if self.__db.result == None:
          loginCt = 0
        else:
          loginCt = self.__db.result[0]
          # 権限取得
          self.__valueList['ROLE'] = ['str',str(self.__db.result[1])]
        self.__db.dbClose()
        
        if loginCt == 0:
          self.__messageList[col.upper() + "_ERR"] = '管理者ログイン情報が存在しません'

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