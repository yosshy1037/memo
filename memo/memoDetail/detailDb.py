# 更新クエリ
class detailSql():
  
  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__sql = ""
    self.__collum = ""
    self.__where = " WHERE 1 = 1 "
    self.__bindVal = []
    self.__valueList = ""
    self.__detailNum = 0
  
  # 更新クエリ
  def detailUpdateSql(self):
    self.__sql = "UPDATE memo SET "
    
    # ループして取得
    ct = 0
    for colName in self.__valueList:
      if colName == "DELETE_FLG":
        self.__where += " AND " + colName + " = %s"
        self.__bindVal += [int(self.__valueList[colName][1])]
        continue
      elif colName == "DETAILQUERY":
        self.__where += " AND ID = %s"
        urlParam = str(self.__valueList[colName][1]).replace('?', '').split("&")
        id = urlParam[0].split("=")[1]
        self.__bindVal += [int(id)]
      else:
        if ct == 0:
          if self.__valueList[colName][0] == "str" or self.__valueList[colName][0] == "date":
            self.__collum = colName + " = %s"
            self.__bindVal += [str(self.__valueList[colName][1])]
          elif self.__valueList[colName][0] == "int" :
            self.__collum = colName + " = %s"
            self.__bindVal += [int(self.__valueList[colName][1])]
        else:
          if self.__valueList[colName][0] == "str" or self.__valueList[colName][0] == "date":
            self.__collum += "," + colName + " = %s"
            self.__bindVal += [str(self.__valueList[colName][1])]
          elif self.__valueList[colName][0] == "int" :
            self.__collum += "," + colName + " = %s"
            self.__bindVal += [int(self.__valueList[colName][1])]
        ct += 1
    
    self.__sql +=  self.__collum + self.__where + ";"
    
  # 削除クエリ(論理削除)
  def detailUpdDeleteSql(self):
    self.__sql = "UPDATE memo SET "
    
    # ループして取得
    ct = 0
    for colName in self.__valueList:
      if colName == "DELETE_DATE":
        self.__collum += colName + " = %s"
        self.__bindVal += [str(self.__valueList[colName][1])]
      elif colName == "DELETE_NAME":
        self.__collum += "," + colName + " = %s"
        self.__bindVal += [str(self.__valueList[colName][1])]
      elif colName == "DELETE_FLG":
        self.__collum += "," + colName + " = %s"
        self.__bindVal += [1]
        self.__where += " AND " + colName + " = %s"
        self.__bindVal += [0]
      elif colName == "DETAILQUERY":
        self.__where += " AND ID = %s"
        urlParam = str(self.__valueList[colName][1]).replace('?', '').split("&")
        id = urlParam[0].split("=")[1]
        self.__bindVal += [int(id)]
    
    self.__sql +=  self.__collum + self.__where + ";"
  
  # 取得クエリ
  def detailSelectSql(self):
    self.__sql = "SELECT ID,PART,NAME,CONTENTS,BIKO,REGIST_DATE FROM memo WHERE ID = "
    self.__sql += self.detailNum
    
  @property
  def valueList(self):
    return self.__valueList

  @valueList.setter
  def valueList(self,valueList):
    self.__valueList = valueList
    
  @property
  def detailNum(self):
    return self.__detailNum

  @detailNum.setter
  def detailNum(self,detailNum):
    self.__detailNum = detailNum
  
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