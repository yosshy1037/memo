## 登録者検索クエリ
class registConnectSql():
  
  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__sql = ""
    self.__collum = ""
    self.__where = " WHERE 1 = 1 "
    self.__bindVal = []
    self.__valueList = {}
    self.__detailNum = 0
    
  # 検索クエリ
  def registSearchSql(self):
    self.__sql = "SELECT ID,LOGINUSERID,REGISTID,DELETE_FLG FROM memoRegistUser"
    self.__where = " WHERE 1 = 1 "
    self.__order = " ORDER BY ID ASC"
    
    # カラム+値でループ
    for col in self.__valueList:
      if col == "ID":
        if int(self.__valueList[col][1]) != 0:
          self.__bindVal += [int(self.__valueList[col][1])]
          self.__where += " AND " + str(col) + " = %s"
      elif col == "LOGINUSERID":
        if str(self.__valueList[col][1]) != "":
          self.__bindVal += [str(self.__valueList[col][1])]
          self.__where += " AND " + str(col) + " = %s"
      elif col == "REGISTID":
        if str(self.__valueList[col][1]) != "":
          self.__bindVal += [str(self.__valueList[col][1])]
          self.__where += " AND " + str(col) + " = %s"
    
    self.__sql += self.__where + self.__order + ";"
  
  # 更新クエリ
  def registUpdateSql(self):
    self.__where = " WHERE 1 = 1 "
    self.__bindVal = []
    self.__bindWhereVal = []
    self.__sql =  "UPDATE memoRegistUser SET "
    
    # ループして取得
    ct = 0
    for colName in self.__valueList:
      if colName == 'ID':
        # 条件生成
        self.__bindWhereVal += [int(self.__valueList[colName][1])]
        self.__where += " AND " + str(colName) + " = %s"
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
    self.__bindVal += self.__bindWhereVal
    
    self.__sql +=  self.__collum + self.__where + ";"

  # 登録クエリ
  def registInsertSql(self):
    self.__sql =  "INSERT INTO memoRegistUser ("
    value = ""
    
    # ループして取得
    ct = 0
    for colName in self.__valueList:
      if colName == "LOGINUSERID" or colName == "REGISTID":
        continue
      elif colName == "RESULTLOGINUSERID":
        if ct == 0:
          self.__sql += "LOGINUSERID"
          value += "%s"
        else:
          self.__sql +=  ",LOGINUSERID"
          value += ",%s"
        self.__bindVal += [str(self.__valueList[colName][1])]
      elif colName == "RESULTREGISTID":
        if ct == 0:
          self.__sql += "REGISTID"
          value += "%s"
        else:
          self.__sql +=  ",REGISTID"
          value += ",%s"
        self.__bindVal += [str(self.__valueList[colName][1])]
      else:
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
    self.__valueList = {}
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
    self.__bindVal = []
    self.__bindVal = bindVal