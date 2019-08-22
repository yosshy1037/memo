# 件数クエリ
def searchSelectCountSql(valueList=''):
  sql = "SELECT COUNT(*) AS FULLCT FROM memo"
  # 条件設定
  sqlParts = whereCreate(valueList)
  where = sqlParts[0]
  sql = sql + where + ";"
  return sql

# クエリ
def searchSelectSql(valueList=''):
  sql = "SELECT ID,PART,NAME,GENDER,CONTENTS,BIKO,REGIST_DATE FROM memo"
  # 条件設定
  sqlParts = whereCreate(valueList)
  where = sqlParts[0]
  offset = sqlParts[1]
  sql = sql + where + offset + ";"
  return sql

# 条件生成
def whereCreate(valueList):
  # 条件設定
  where = " WHERE 1 = 1 "
  for col in valueList:
    if valueList[col][0] == "str":
      if col == "KEYWORD":
        if str(valueList[col][1]) != "":
          where += " AND ( PART LIKE '%" + str(valueList[col][1]) + "%'"
          where += " OR NAME LIKE '%" + str(valueList[col][1]) + "%'"
          where += " OR CONTENTS LIKE '%" + str(valueList[col][1]) + "%'"
          where += " OR BIKO LIKE '%" + str(valueList[col][1]) + "%' )"
      else:
        if str(valueList[col][1]) != "":
          where += " AND " + str(col) + " = '" + str(valueList[col][1]) + "'"
    elif valueList[col][0] == "date":
      if col == "REGISTSTARTDATE":
        if str(valueList[col][1]) != '1999-01-01 00:00:00' and str(valueList[col][1]) != "":
          where += " AND REGIST_DATE >= to_date('" + str(valueList[col][1]) + " 00:00:00','YYYY-MM-DD HH24:MI:SS')"
      elif col == "REGISTENDDATE":
        if str(valueList[col][1]) != '1999-01-01 00:00:00' and str(valueList[col][1]) != "":
          where += " AND REGIST_DATE < to_date('" + str(valueList[col][1]) + " 00:00:00','YYYY-MM-DD HH24:MI:SS')"
      else:
        if str(valueList[col][1]) != '1999-01-01 00:00:00' and str(valueList[col][1]) != "":
          where += " AND " + str(col) + " = '" + str(valueList[col][1]) + "'"
    elif valueList[col][0] == "int":
      if col != "PAGENUM":
        where += " AND " + str(col) + " = " + str(valueList[col][1]) + ""
      else:
        # ページャ設定
        if valueList[col][1] == 1:
          pos = str(int(valueList[col][1])-1)
        else:
          pos = str((int(valueList[col][1])-1) * 3)
        offset = " offset " + pos + " limit 3"
  return where,offset