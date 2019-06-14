---
layout: normal
title: 궁금증
---

### python 조건과 sqlite의 조건 속도 차이

DB 사용 중 문득 든 생각. 당연하겠지만.. sql 문으로 처리하는게 빠를까?  
개역한글 성경 db 테스트.  
테스트 구문: **여호와**, **하나님**  
결과: 총 31105절 중, **1147**건 검색.  

* sql - 0.023075 s
```python
def search_by_sql():
    start = time.time()
    query = "select * from bibleKorHRV \
             where content like '%여호와%' and content like '%하나님%'"
    cur.execute(query)
    res = cur.fetchall()
    print("time: " + str(time.time() - start))
```

* py - 0.069226 s
```python
def search_by_py():
    start = time.time()
    query = "select * from bibleKorHRV"
    cur.execute(query)
    res = cur.fetchall()
    for verse in res:
        if "하나님" in verse[3] and "여호와" in verse[3]:
            pass
    print("time: " + str(time.time() - start))
```