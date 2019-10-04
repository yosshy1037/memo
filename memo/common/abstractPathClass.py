from abc import ABCMeta
from abc import abstractmethod
from memoProject.settings import BASE_DIR

## 抽象クラス abstractPathの定義
class abstractPath(metaclass = ABCMeta):

  # コンストラクタ
  def __init__(self):
  
    # baseURL
    self.__basePath = BASE_DIR
    # 処理の名称
    self.__status = ""
    # logのディレクトリパス
    self.__logPath = ""
    # ディレクトリパス
    self.__dirPath = ""

  # メイン処理
  @abstractmethod
  def pathCrearte(self):
    if self.__status == "tmpFile":
      self.__dirPath = self.__basePath + '\\tmp\\'
    elif self.__status == "log":
      # プロジェクトフォルダを絶対パスから除去
      tmpPath = self.__basePath.replace('memoProject', '')
      self.__dirPath = tmpPath + '\\logs\\'
    else:
      self.__dirPath = self.__basePath

  @property
  def status(self):
    return self.__status

  @status.setter
  def status(self,status):
    self.__status = status
    
  @property
  def dirPath(self):
    return self.__dirPath