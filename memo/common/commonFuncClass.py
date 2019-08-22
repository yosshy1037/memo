from . import const,constDef

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
    
  # リクエスト
  @property
  def request(self):
    return self.__request

  @request.setter
  def request(self,request):
    self.__request = request