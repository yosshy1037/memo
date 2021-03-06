from . import commonFuncClass,pathControlClass
from datetime import datetime, timedelta
import logging,os

# ロガークラス
class logger():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__logfile = ""
    self.__logging = ""
    self.__pathCon = pathControlClass.pathControl()
    self.__open()
    self.__com = commonFuncClass.commonFunc()
    self.__value = ""
    self.__level = ""
    self.__dir = ""
  
  # ログファイル選択
  def __open(self):
    self.__pathCon.status = "log"
    self.__pathCon.pathCrearte()
    try:
      # 過去ログ削除
      for day in range(3, 11):
        retentionPeriod = datetime.now() - timedelta(day)
        deleteLog = self.__pathCon.dirPath + "memo_" + retentionPeriod.strftime("%Y%m%d") +  ".log"
        if os.path.exists(deleteLog) == True:
          os.remove(deleteLog)
      
      # ログディレクトリ作成
      if os.path.exists(self.__pathCon.dirPath) == False:
        os.mkdir(self.__pathCon.dirPath)
      # オープン処理
      self.__logfile = self.__pathCon.dirPath + "memo_" + datetime.now().strftime("%Y%m%d") +  ".log"
      self.__logging = logging
      self.__logging.basicConfig(
        filename=self.__logfile,
        format = '%(asctime)s %(levelname)s %(message)s',
        level=logging.DEBUG,
        filemode = 'a'
      )
    except:
     pass
  
  # ログ書き込み処理
  def write(self,level):
    self.__level = level
    
    # ログファイルOPEN成功した場合
    if self.__logging != "":
      if self.__level == 'debug':
        self.__logging.debug(self.__value)
      elif self.__level == 'info':
        self.__logging.info(self.__value)
      elif self.__level == 'warning':
        self.__logging.warning(self.__value)
      elif self.__level == 'error':
        self.__logging.error(self.__value)
      elif self.__level == 'critical':
        self.__logging.critical(self.__value)
      
  # 値setter・getter
  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,value):
    self.__value = value
    
  # levelsetter・getter
  @property
  def level(self):
    return self.__level

  @level.setter
  def level(self,level):
    self.__level = level
    
  # comsetter・getter
  @property
  def com(self):
    return self.__com

  @com.setter
  def com(self,com):
    self.__com = com