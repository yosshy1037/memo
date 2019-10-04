import tempfile,os
from . import pathControlClass
from . import const

## Tempデータを操作するクラス
class tempFile():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__pathCon = pathControlClass.pathControl()
    self.__temp = "";
    self.__write_path = ""
    self.__fp = ""
    self.__ses = ""
    self.__writeData = {}
    self.__readData = ""
  
  # tempFile書き込み処理呼び出し
  def tempFileCreate(self):
    self.__tempFileInit()
    self.__tempFileOpen('w')
    self.__tempFileWrite()
    self.__tempFileClose()
    
  # tempFile読み込み処理呼び出し
  def tempFileRead(self):
    # Tempファイルパス取得
    self.__tempFileInit()
    # Tempファイル存在チェック
    if os.path.exists(self.__write_path):
      self.__tempFileOpen('r')
      self.__tempFileRead()
      self.__tempFileClose()
      self.__tempFileDelete()
  
  # tempFile初期処理
  def __tempFileInit(self):
    self.__pathCon.status = "tmpFile"
    self.__pathCon.pathCrearte()
    self.__write_path = self.__pathCon.dirPath + 'temp.txt'
    
  # tempFile作成
  def __tempFileOpen(self,status):
    self.__fp = open(self.__write_path, status)
    
  # tempFile書き込み
  def __tempFileWrite(self):
    self.__fp.write(str(self.__writeData))
    
  # tempFile読み込み処理
  def __tempFileRead(self):
    self.__fp.seek(0)
    self.__readData = self.__fp.read()

  # tempFile削除
  def __tempFileDelete(self):
    os.remove(self.__write_path)
    
  # tempFile終了
  def __tempFileClose(self):
    self.__fp.close()
    
  # 書き込み値
  @property
  def writeData(self):
    return self.__writeData

  @writeData.setter
  def writeData(self,writeData):
    self.__writeData = writeData

  # 読み込み値
  @property
  def readData(self):
    return self.__readData

  @readData.setter
  def readData(self,readData):
    self.__readData = readData