from . import const,constDef
import os

class commonFunc():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__request = ""
    self.__result = ""

  # ajax処理exception発生時の処理
  def postExceptDispos(self, exp, self_log, e, traceback, mes):
    exp.log = self_log
    exp.dispatch(e, traceback)
    return mes
    
  # ajax処理exception発生時の処理(オーバーロード)
  def postExceptDispos(self, exp, self_log, e, traceback):
    exp.log = self_log
    exp.dispatch(e, traceback)
    
  # ユーザ権限の制御処理
  def userRoleDispos(self, request, tag, formStatus):
    tagTmp = ''
    self.__result = ''
    if 'ROLE' in request.session:
      if request.session['ROLE'] == 'a':
        self.__result = tag
      elif request.session['ROLE'] == 'rw':
        self.__result = tag
      else:
        if formStatus == 'disabled':
          tagTmp = tag.split("/")
          self.__result += tagTmp[0] + 'disabled="disabled" /' + tagTmp[1]
        else:
          self.__result = ''
    else:
      self.__result = ''

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
    
  # 結果
  @property
  def result(self):
    return self.__result

  @result.setter
  def result(self,result):
    self.__result = result