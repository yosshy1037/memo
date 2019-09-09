# 登録クエリクラス
class insertSql():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__sql = "INSERT INTO memo ("
    self.__collum = ""
    self.__where = " WHERE 1 = 1 "
    self.__order = ""
    self.__offset = ""
    self.__bindVal = []
    self.__valueList = ""
    self.__detailNum = 0

  # 登録クエリ
  def registInsert(self):
   
    value = ""
    
    # ループして取得
    ct = 0
    for colName in self.__valueList:
      if ct == 0:
        self.__sql += colName
        if self.__valueList[colName][0] == "str" :
          self.__bindVal += [str(self.__valueList[colName][1])]
          value += "%s"
        elif self.__valueList[colName][0] == "int" :
          self.__bindVal += [int(self.__valueList[colName][1])]
          value += "%s"
        elif self.__valueList[colName][0] == "date" :
          self.__bindVal += [str(self.__valueList[colName][1])]
          value += "%s"
      else:
        self.__sql += "," + colName
        if self.__valueList[colName][0] == "str" :
          self.__bindVal += [str(self.__valueList[colName][1])]
          value += ",%s"
        elif self.__valueList[colName][0] == "int" :
          self.__bindVal += [int(self.__valueList[colName][1])]
          value += ",%s"
        elif self.__valueList[colName][0] == "date" :
          self.__bindVal += [str(self.__valueList[colName][1])]
          value += ",%s"
      ct += 1
    
    self.__sql += ") VALUES (" + value + ");"
    
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