from . import const,constDef

# Exception発生クラス
class parentException(Exception):
  # コンストラクタ
  def __init__(self, value):
  
    # プライベート変数
    self.__value = value

  # メイン処理
  def logOutput(self):
    print('%s' % self.__value)

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,value):
    self.__value = value

# Exception処理振り分けクラス
class dispatchException():
  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__e = ""
    self.__mes = ""
    self.__log = ""

  # 振り分け処理
  def dispatch(self, e ,traceback):
    self.__e = e
    
    # 振り分け処理
    if str(self.__e) == 'division by zero':
      self.__mes  = "ゼロで割り算のエラー"
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