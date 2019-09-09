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
    self.__host = const.dbHost
    self.__port = const.dbPort
    self.__dbname = const.dbName
    self.__user = const.dbUser
    self.__password = const.dbPassword

  # メイン処理
  def execute(self,sql,sqlMode,fetchStatus):

    self.__sql = sql
    
    self.__dbCursor()
    if sqlMode == const.sel:
      self.__cur.execute(self.__sql,self.__bindVal)
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