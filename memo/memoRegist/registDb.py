# 件数クエリ
def registInsert(request='',valueList=''):    
  sql = "INSERT INTO memo ("
  value = ""
  
  # ループして取得
  ct = 0
  for colName in valueList:
    if ct == 0:
      sql += colName
      if valueList[colName][0] == "str" :
        value += "'" + str(valueList[colName][1]) + "'"
      elif valueList[colName][0] == "int" :
        value += str(valueList[colName][1])
      elif valueList[colName][0] == "date" :
        value += "'" + str(valueList[colName][1]) + "'"
    else:
      sql += "," + colName
      if valueList[colName][0] == "str" :
        value += ",'" + str(valueList[colName][1]) + "'"
      elif valueList[colName][0] == "int" :
        value += "," + str(valueList[colName][1])
      elif valueList[colName][0] == "date" :
        value += ",'" + str(valueList[colName][1]) + "'"
    ct += 1
  
  sql += ") VALUES (" + value + ");"
  return sql