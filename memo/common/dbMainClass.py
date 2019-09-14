from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction
from . import logClass,const,constDef
import psycopg2
from psycopg2.extensions import STATUS_BEGIN, STATUS_READY

class dbMain():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__conn = ""
    self.__cur = ""
    self.__sql = ""
    self.__result = ""
    self.__log = logClass.logger()
    self.__bindVal = []
    self.__host = const.dbHost
    self.__port = const.dbPort
    self.__dbname = const.dbName
    self.__user = const.dbUser
    self.__password = const.dbPassword

  # メイン処理
  def execute(self,sql,sqlMode,fetchStatus):

    self.__sql = sql
    
    # カーソルOPEN
    self.__dbCursorOpen()
    try:
      # 実行
      self.__cur.execute(self.__sql,self.__bindVal)
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')
      
    
    # 選択/登録/更新別の処理
    if sqlMode == const.sel:
      if fetchStatus == const.fetchModeOne:
        self.__result = self.dbFetchOne()
      elif fetchStatus == const.fetchModeTwo:
        self.__result = self.dbFetchAll()
    # カーソルCLOSE
    self.__dbCursorClose()
    
    # ログ書き込み
    self.__log.value = self.__sql
    self.__log.write('info')

  # DB接続
  def dbConnection(self):
    try:
      if self.__host != "" and self.__port != "":
        self.__conn = psycopg2.connect("host=" + self.__host + " port=" + self.__port + " dbname=" + self.__dbname + " user=" + self.__user + " password=" + self.__password + "")
      else:
        self.__conn = psycopg2.connect("dbname=" + self.__dbname + " user=" + self.__user + " password=" + self.__password + "")
    
      self.__conn.autocommit = False
      
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

  # DBカーソルOPEN
  def __dbCursorOpen(self):
    try:
      if self.__conn != "":
        self.__cur = self.__conn.cursor()
    
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

  # DBカーソルCLOSE
  def __dbCursorClose(self):
    try:
      if self.__cur != "":
        self.__cur.close()
    
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

  # コミット
  def dbCommit(self):
    try:
      if self.__conn != "" and self.__conn.status == STATUS_BEGIN:
        self.__conn.commit()
    
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')
      
  # ロールバック
  def dbRollback(self):
    try:
      if self.__conn != "" and self.__conn.status == STATUS_BEGIN:
        self.__conn.rollback()
    
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

  # fetchOne
  def dbFetchOne(self):
    try:
      if self.__cur != "":
        return self.__cur.fetchone()
      else:
        return ""
        
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

  # fetchAll
  def dbFetchAll(self):
    try:
      if self.__cur != "":
        return self.__cur.fetchall()
      else:
        return ""
    
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

  # DBクローズ
  def dbClose(self):
    try:
      if self.__conn != "":
        self.__conn.close()
      
    except psycopg2.Error as e:
      self.__log.value = 'psycopg2.Error occurred:' + e.args[0]
      self.__log.write('error')

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