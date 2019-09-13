## ログイン情報存在チェック ##
class loginSelectSql():

  # コンストラクタ
  def __init__(self):
    self.__where = ""
    self.__sql = "SELECT COUNT(LOGINUSER) FROM memoLogin WHERE 1 = 1 "
    self.__bindVal = []
    self.__valueList = ""
    self.__collumList = ""
    
  # ログイン情報取得クエリ
  def loginSelect(self):
    for col in self.__collumList:
      # passwordを複合化して比較
      if col.upper() == 'LOGINPASSWORD':
        collum = "pgp_sym_decrypt(" + col.upper() + ", 'Yosshy3499')"
      else:
        collum = col.upper()
      self.__bindVal += [self.__valueList[col.upper()][1]]
      self.__where += " and " + collum + " = %s"
    
    self.__sql = self.__sql + self.__where + " ;"
    
  @property
  def valueList(self):
    return self.__valueList

  @valueList.setter
  def valueList(self,valueList):
    self.__valueList = valueList
    
  @property
  def sql(self):
    return self.__sql

  @sql.setter
  def sql(self,sql):
    self.__sql = sql
    
  @property
  def bindVal(self):
    return self.__bindVal

  @bindVal.setter
  def bindVal(self,bindVal):
    self.__bindVal = bindVal
    
  @property
  def collumList(self):
    return self.__collumList

  @collumList.setter
  def collumList(self,collumList):
    self.__collumList = collumList