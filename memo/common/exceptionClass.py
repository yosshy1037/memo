from . import const,constDef
from django.shortcuts import redirect

# Exception継承クラス
class OriginException(Exception):
  # コンストラクタ
  def __init__(self, value):
  
    # プライベート変数
    self.__e = ""
    self.__mes = ""
    self.__log = ""

  # メイン処理
  def dispatch(self, e ,traceback):
    self.__e = e
    
    self.__e  = str(self.__e) + "\n\r"
    
    # ログ書き込み
    self.__log.value = str(self.__e) + traceback
    self.__log.write('error')

  @property
  def e(self):
    return self.__e

  @e.setter
  def e(self,e):
    self.__e = e

  @property
  def log(self):
    return self.__log

  @log.setter
  def log(self,log):
    self.__log = log

# Exception処理振り分けクラス
class dispatchException():
  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__e = ""
    self.__errType = ""
    self.__mes = ""
    self.__log = ""

  # 振り分け処理
  def dispatch(self, e ,traceback):
    self.__errType = str(type(e)).split("'")
    
    # 振り分け処理
    if str(self.__errType[1]) == 'AssertionError':
      self.__mes  = "assert文が失敗エラー"
    elif str(self.__errType[1]) == 'AttributeError':
      self.__mes  = "存在しない属性を参照したエラー"
    elif str(self.__errType[1]) == 'NameError':
      self.__mes  = "存在しない名前を参照したエラー"
    elif str(self.__errType[1]) == 'SyntaxError':
      self.__mes  = "解析できないソースコード参照エラー"
    elif str(self.__errType[1]) == 'TypeError':
      self.__mes  = "データ型誤りエラー"
    elif str(self.__errType[1]) == 'ValueError':
      self.__mes  = "不正な値エラー"
    elif str(self.__errType[1]) == 'ZeroDivisionError':
      self.__mes  = "ゼロ除算エラー"
    else:
      self.__mes  = str(self.__errType[1])
      
    if self.__mes != "":
      self.__mes  = str(self.__errType[1]) + " | " + self.__mes + "\n\r"
    else:
      self.__mes  = self.__mes + "\n\r"
    
    # ログ書き込み
    self.__log.value = self.__mes + traceback
    self.__log.write('error')

  @property
  def e(self):
    return self.__e

  @e.setter
  def e(self,e):
    self.__e = e
    
  @property
  def log(self):
    return self.__log

  @log.setter
  def log(self,log):
    self.__log = log