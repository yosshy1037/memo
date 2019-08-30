from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from . import const,constDef
import psycopg2

class dbMain():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__conn = ""
    self.__cur = ""
    self.__sql = ""
    self.__result = ""
    self.__bindVal = []
    self.__host = "ec2-50-19-222-129.compute-1.amazonaws.com"
    self.__port = "5432"
    self.__dbname = "d55hlkoc8p6llk"
    self.__user = "mpwwqumdjipwfw"
    self.__password = "60162450ab1fb5baf5c9c260b6fbde5823f0cb24a584b89be0ce2443bf9f855f"

  # メイン処理
  def execute(self,sql,sqlMode,fetchStatus):

    self.__sql = sql
    
    self.__dbCursor()
    if sqlMode == const.sel:
      self.__cur.execute(self.__sql)
      if fetchStatus == const.fetchModeOne:
        self.__result = self.dbFetchOne()
      elif fetchStatus == const.fetchModeTwo:
        self.__result = self.dbFetchAll()
    elif sqlMode == const.ins:
      self.__cur.execute(self.__sql)
    elif sqlMode == const.upd:
      self.__cur.execute(self.__sql,self.__bindVal)
      
    self.__cur.close()

  # DB接続
  def dbConnection(self):
    try:
      self.__conn = psycopg2.connect("host=" + self.__host + " port=" + self.__port + " dbname=" + self.__dbname + " user=" + self.__user + " password=" + self.__password + "")
    
      self.__conn.autocommit = False
      
    except psycopg2.Error as e:
      print('psycopg2.Error occurred:', e.args[0])

  # コミット
  def dbCommitOrRollback(self):
    try:
      self.__conn.commit()
    
    except psycopg2.Error as e:
      self.__conn.rollback()

  # DBカーソル
  def __dbCursor(self):
    try:
      self.__cur = self.__conn.cursor()
    
    except psycopg2.Error as e:
      print('psycopg2.Error occurred:', e.args[0])

  # fetchOne
  def dbFetchOne(self):
    try:
      return self.__cur.fetchone()
    
    except psycopg2.Error as e:
      print('psycopg2.Error occurred:', e.args[0])

  # fetchAll
  def dbFetchAll(self):
    try:
      return self.__cur.fetchall()
    
    except psycopg2.Error as e:
      print('psycopg2.Error occurred:', e.args[0])

  # DBクローズ
  def dbClose(self):
    try:
      self.__conn.close()
      
    except psycopg2.Error as e:
      print('psycopg2.Error occurred:', e.args[0])

  @property
  def conn(self):
    return self.__conn
    
  @property
  def result(self):
    return self.__result
    
  @property
  def bindVal(self):
    return self.__bindVal

  @bindVal.setter
  def bindVal(self,bindVal):
    self.__bindVal = bindVal