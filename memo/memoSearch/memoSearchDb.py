from django.http.response import HttpResponse
from django.shortcuts import render

def memoSearchSelect(request='',pageNum=0,partVal='',nameVal=''):
  import psycopg2
  dateTmp = []
  dateList = []

  try:
    conn = psycopg2.connect("dbname=d55hlkoc8p6llk user=mpwwqumdjipwfw password=60162450ab1fb5baf5c9c260b6fbde5823f0cb24a584b89be0ce2443bf9f855f")
    
    # ページャ設定
    if int(pageNum) == 1:
      pos = str(int(pageNum)-1)
    else:
      pos = str((int(pageNum)-1) * 3)
    
    # 条件設定
    where = " WHERE 1 = 1 "
    if partVal != "":
      where += " AND PART = '" + str(partVal) + "' "
    
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) AS FULLCT FROM memo " + where + ";")
    count = cur.fetchone()
    cur.close()
    
    cur = conn.cursor()
    cur.execute("SELECT ID,PART,NAME,GENDER,CONTENTS,BIKO,REGIST_DATE FROM memo " + where + " offset " + pos + " limit 3 ;")

    # ループして取得
    for row in cur:
       dateTmp.append(row[0])
       dateTmp.append(row[1])
       dateTmp.append(row[2])
       dateTmp.append(row[3])
       dateTmp.append(row[4])
       
       contents = row[5].replace('\n','<br>')
       
       dateTmp.append(contents)
       dateTmp.append(row[6])
       dateList.append(dateTmp)
       dateTmp = []
    
    cur.close()
    conn.close()

  except psycopg2.Error as e:
    print('psycopg2.Error occurred:', e.args[0])
  
  return dateList,count;