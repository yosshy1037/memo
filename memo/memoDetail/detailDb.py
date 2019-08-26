# 更新クエリ
def detailUpdate(request='',valueList=''):
  sql = "UPDATE memo SET "
  collum = ""
  where = " WHERE 1 = 1 "
  
  # ループして取得
  ct = 0
  for colName in valueList:
    if colName == "DELETE_FLG":
      where += " AND " + colName + " = " + str(valueList[colName][1])
      continue
    elif colName == "DETAILQUERY":
      where += " AND ID = " + str(valueList[colName][1]).replace('?detailNum=', '')
    else:
      if ct == 0:
        if valueList[colName][0] == "str" :
          collum = colName + " = '" + str(valueList[colName][1]) + "'"
        elif valueList[colName][0] == "int" :
          collum = colName + " = " + str(valueList[colName][1])
        elif valueList[colName][0] == "date":
          collum = colName + " = '" + str(valueList[colName][1]) + "'"
      else:
        if valueList[colName][0] == "str" :
          collum += "," + colName + " = '" + str(valueList[colName][1]) + "'"
        elif valueList[colName][0] == "int" :
          collum += "," + colName + " = " + str(valueList[colName][1])
        elif valueList[colName][0] == "date":
          collum += "," + colName + " = '" + str(valueList[colName][1]) + "'"
      ct += 1
  
  sql +=  collum + where + ";"
  return sql
  
def detailSelect(detailNum):
  sql = "SELECT ID,PART,NAME,GENDER,CONTENTS,BIKO,REGIST_DATE FROM memo WHERE ID = " + detailNum
  return sql