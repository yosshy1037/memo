from django.http.response import HttpResponse
from django.shortcuts import render

def db_test(request):
  import psycopg2

  conn = psycopg2.connect("dbname=memo user=admin password=kanai")

  cur = conn.cursor()
  cur.execute("DROP TABLE memoContents;")
  conn.commit()
  cur.close()

  cur = conn.cursor()
  cur.execute("CREATE TABLE memoContents (id serial PRIMARY KEY, num integer, data varchar);")
  cur.execute("INSERT INTO memoContents (num, data) VALUES (%s, %s)",(100, "abc'def"))
  cur.execute("SELECT id,num,data FROM memoContents;")
  a = cur.fetchone()
  conn.commit()
  cur.close()
  conn.close()
  
  d = {
        'test': a,
  }
  
  return render(request, 'dbIns.html', d)