---
layout: normal
title: Database
---

## sqlite3

* .db 파일을 가지고 있다면 .sqlite3/.db 로 [변환](https://stackoverflow.com/questions/2049109/how-do-i-import-sql-files-into-sqlite-3)시켜줘야 함
    1. `sqlite3 database.sqlite3 < db.sql` 로 가능. 시간이 굉장히 오래 걸렸음.

* 사용 예  
```
import sqlite3

conn = sqlite3.connect("sample.splite3") # or "sample.db"
cur = conn.cursor()

sql = "select * from table"
cur.execute(sql)

res = cur.fetchall()
# res = cur.fecthone()

conn.close()
```