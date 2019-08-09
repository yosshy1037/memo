from django.http.response import HttpResponse
from django.shortcuts import render

def db_test_select(request):
  import sqlite3
  import pdb

  # データベースファイルのパス
  dbpath = 'sample_db.sqlite'

  # データベース接続とカーソル生成
  connection = sqlite3.connect(dbpath)

  #pdb.set_trace()
  # 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
  # connection.isolation_level = None

  cursor = connection.cursor()

  # エラー処理（例外処理）
  try:
    tableList = []
    createList = []
    collum = []
    collumList = []
    
    ## テーブル名取得
    result = cursor.execute('select name from sqlite_master where type="table"')
 
    # 全件取得は cursor.fetchall()
    # res = cursor.fetchall()
    # print(res)
    
    # ループして取得
    for row in result:
       tableList.append(row[0])
    
    ## create文取得
    result = cursor.execute('select sql from sqlite_master')
    # ループして取得
    for row in result:
       createList.append(row[0])
    
    ## テーブル定義取得
    result = cursor.execute('PRAGMA table_info("' + tableList[0] + '")')
    # ループして取得
    for row in result:
       collum.append(row[0])
       collum.append(row[1])
       collum.append(row[2])
       collum.append(row[3])
       collum.append(row[4])
       collum.append(row[5])
       collumList.append(collum)
       collum = []
       
  except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
   
  
  # 接続を閉じる
  connection.close()
  
  # 引数渡す
  d = {
       'table_list': tableList,
       'create_list': createList,
       'collum_list': collumList
  }
  
  #画面描画
  return render(request, 'db.html', d)