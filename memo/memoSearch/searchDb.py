# 件数クエリ
def searchSelectCountSql(request='',pageNum=0,partVal='',nameVal=''):    
  # 条件設定
  where = " WHERE 1 = 1 "
  if partVal != "":
    where += " AND PART = '" + str(partVal) + "' "
    
  sql = "SELECT COUNT(*) AS FULLCT FROM memo " + where + ";"

  return sql

# クエリ
def searchSelectSql(request='',pageNum=0,partVal='',nameVal=''):
  # ページャ設定
  if int(pageNum) == 1:
    pos = str(int(pageNum)-1)
  else:
    pos = str((int(pageNum)-1) * 3)
   
  # 条件設定
  where = " WHERE 1 = 1 "
  if partVal != "":
    where += " AND PART = '" + str(partVal) + "' "

  return "SELECT ID,PART,NAME,GENDER,CONTENTS,BIKO,REGIST_DATE FROM memo " + where + " offset " + pos + " limit 3 ;"