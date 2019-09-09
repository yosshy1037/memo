from . import const,constDef
import os

class commonFunc():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__request = ""

  # 文字分割処理
  def left(self,text, n):
    return text[:n]

  def right(self,text, n):
    return text[-n:]

  def mid(self,text, n, m):
    return text[n-1:n+m-1]
  
  # ディレクトリサイズ取得
  def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

  # ファイル存在チェック
  def fileExists(path):
    return os.path.exists(path)

  def fileDelete(self,path):
    return os.remove(path)

  # リクエスト
  @property
  def request(self):
    return self.__request

  @request.setter
  def request(self,request):
    self.__request = request