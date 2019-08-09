from django.http.response import HttpResponse
from django.shortcuts import render

def db_test(request):
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
  # CREATE
      cursor.execute("DROP TABLE IF EXISTS sample2")
      cursor.execute("CREATE TABLE IF NOT EXISTS sample2 (id INTEGER PRIMARY KEY, name TEXT)")

      # INSERT
      cursor.execute("INSERT INTO sample2 VALUES (1, '佐藤')")
      
      # プレースホルダの使用例
      # プレースホルダには疑問符(qmark スタイル)と名前(named スタイル)の2つの方法がある
      cursor.execute("INSERT INTO sample2 VALUES (2, ?)", ('鈴木',))
      cursor.execute("INSERT INTO sample2 VALUES (?, ?)", (3, '高橋'))
      cursor.execute("INSERT INTO sample2 VALUES (:id, :name)",{'id': 4, 'name': '田中'})
      
      # 複数レコードを一度に挿入 executemany メソッドを使用
      persons = [
          (5, '伊藤'),
          (6, '渡辺'),
      ]
      
      #cursor.executemany("INSERT INTO sample2 VALUES (?, ?)", persons)
      # わざと主キー重複エラーを起こして例外を発生させてみる
      #cursor.execute("INSERT INTO sample2 VALUES (1, '中村')")
  except sqlite3.Error as e:
      print('sqlite3.Error occurred:', e.args[0])
   
  # 保存を実行（忘れると保存されないので注意）
  connection.commit()
   
  # 接続を閉じる
  connection.close()
  
  return render(request, 'db.html')