# ログイン情報存在チェック
def loginSelectSql(request='',collumList='',valueList=''):
  where = ""
  for col in collumList:
    where += " and " + col.upper() + " = '" + valueList[col.upper()][1] +"'"
    
  sql = "SELECT COUNT(LOGINUSER) FROM memoLogin WHERE 1 = 1 " + where + " ;"
  return sql