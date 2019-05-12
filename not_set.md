현상황
page layout의 child들이 height가 적절하게 나오지 않음.


[packaging android](https://kivy.org/doc/stable/guide/packaging-android.html)

https://kivy.org/doc/stable/guide/packaging-android.html

[python-for-android](https://github.com/kivy/python-for-android)를 통해 android package를 생성할 수 있음.  

Buildozer 를 사용해서 전체 과정을 자동화할 수 있음.  

## Buildozer

전체 build 과정을 자동화하는 툴.
현재는 kivy에서 이 방법을 추천하고 있음.  

## [plyer](https://github.com/kivy/plyer)

plyer에서 여러 android API를 사용할 수 있도록 함.


## kivy database

build: [link](https://groups.google.com/forum/#!topic/kivy-users/9dnRnvt9j-w)
example: [link](https://github.com/compagni/Kivy-Sqlite3-Example/blob/master/KivyDB/main.py)



## Q

[file system vs database](https://stackoverflow.com/questions/38120895/database-vs-file-system-storage)

https://social.msdn.microsoft.com/Forums/sqlserver/en-US/f157578e-ace7-4f9c-a77f-067e2040adb3/file-system-vs-database?forum=sqlgetstarted

https://raima.com/database-system-vs-file-system/

https://stackoverflow.com/questions/2356851/database-vs-flat-files

## issue

* sqlite3.OperationalError: no such table:
```
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(BASE_DIR)
```

## tag 추가

https://jamiekang.github.io/2017/04/28/add-tag-support/