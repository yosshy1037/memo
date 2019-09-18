from ..common import const,constDef

# 検索クエリ
class searchSql():

  # コンストラクタ
  def __init__(self):
  
    # プライベート変数
    self.__sql = ""
    self.__collum = ""
    self.__where = " WHERE 1 = 1 "
    self.__order = ""
    self.__offset = ""
    self.__bindVal = []
    self.__valueList = ""
    self.__detailNum = 0
    self.__request = ""

  # 件数クエリ
  def searchSelectCountSql(self):
    self.__sql = "SELECT COUNT(*) AS FULLCT FROM memo"
    # 条件設定
    self.__bindVal = []
    self.__whereCreate()
    self.__sql = self.__sql + self.__where + ";"

  # 値取得クエリ
  def searchSelectSql(self):
    self.__sql = "SELECT ID,PART,NAME,CONTENTS,BIKO,REGIST_DATE FROM memo"
    # 条件設定
    self.__bindVal = []
    self.__whereCreate()
    self.__order = " ORDER BY ID ASC"
    self.__sql = self.__sql + self.__where + self.__order + self.__offset + ";"

  # 条件生成
  def __whereCreate(self):
    # 条件設定
    self.__where = " WHERE 1 = 1 "
    for col in self.__valueList:
      if self.__valueList[col][0] == "str":
        if col == "KEYWORD":
          if str(self.__valueList[col][1]) != "":
            self.__bindVal += ['%' + str(self.__valueList[col][1]) + '%']
            self.__bindVal += ['%' + str(self.__valueList[col][1]) + '%']
            self.__bindVal += ['%' + str(self.__valueList[col][1]) + '%']
            self.__bindVal += ['%' + str(self.__valueList[col][1]) + '%']
            self.__where += " AND ( PART LIKE %s"
            self.__where += " OR NAME LIKE %s"
            self.__where += " OR CONTENTS LIKE %s"
            self.__where += " OR BIKO LIKE %s )"
        else:
          if str(self.__valueList[col][1]) != "":
            self.__bindVal += [str(self.__valueList[col][1])]
            self.__where += " AND " + str(col) + " = %s"
      elif self.__valueList[col][0] == "date":
        if col == "REGISTSTARTDATE":
          if str(self.__valueList[col][1]) != '1999-01-01 00:00:00' and str(self.__valueList[col][1]) != "":
            self.__bindVal += [str(self.__valueList[col][1])]
            self.__where += " AND REGIST_DATE >= to_date('%s 00:00:00','YYYY-MM-DD HH24:MI:SS')"
        elif col == "REGISTENDDATE":
          if str(self.__valueList[col][1]) != '1999-01-01 00:00:00' and str(self.__valueList[col][1]) != "":
            self.__bindVal += [str(self.__valueList[col][1])]
            self.__where += " AND REGIST_DATE < to_date('%s 00:00:00','YYYY-MM-DD HH24:MI:SS')"
        else:
          if str(self.__valueList[col][1]) != '1999-01-01 00:00:00' and str(self.__valueList[col][1]) != "":
            self.__bindVal += [str(self.__valueList[col][1])]
            self.__where += " AND " + str(col) + " = %s"
      elif self.__valueList[col][0] == "int":
        if col != "PAGENUM":
          self.__bindVal += [int(self.__valueList[col][1])]
          self.__where += " AND " + str(col) + " = %s"
        else:
          # ページャ設定
          if self.__valueList[col][1] == 1:
            pos = str(int(self.__valueList[col][1])-1)
          else:
            pos = str((int(self.__valueList[col][1])-1) * const.intervalPageNum)
          self.__offset = " offset " + pos + " limit " + str(const.intervalPageNum)
    
    # ログインユーザが作成したデータのみ取得
    self.__bindVal += [str(self.__request.session['LOGINUSER'])]
    self.__where += " AND REGIST_NAME = %s"
  
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
  def request(self):
    return self.__request

  @request.setter
  def request(self,request):
    self.__request = request