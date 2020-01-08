---
layout: post
title: Python Restful 01
tag:
  - Django REST
---

Book name: Building RESTful Python Web Services / DJango  

예제 코드: https://github.com/PacktPublishing/Building-RESTful-Python-Web-Services

# 1. 장고를 이용한 RESTful API 개발

## 장고 가상환경 세팅
1. `python -m venv %USERPROFILE%\PythonREST\Django01`  
지정된 폴더에 파이썬 실행 파일과 가상환경을 나타내는 각 파일들이 포함된 폴더 트리가 생성 됨.  
pyenv.cfg 파일로 가상 환경에 대해 옵션을 지정하는데, 이 파일이 있는 곳이 가상 환경의 root 폴더.

1. `%USERPROFILE%\PythonREST\Django01\Scripts\activate.bat`  
가상 환경 활성화.  
해당 파일을 클릭해도 됨.  
비활성화를 위해서는 동일한 위치의 **deactivate.bat**를 누르면 됨.  

2. `pip install django`  
장고 프레임워크 설치

3. `pip install djangorestframework`  
장고 rest 설치

4. `cd /d %USERPROFILE%\PythonREST\Django01`  
루트 폴더로 이동

6. `django-admin.py startproject gamesapi`  
**gamesapi**라는 새 장고 프로젝트 생성

7. `cd gamesapi`  
생성한 프로젝트로 이동

8. `python manage.py startapp games`  
**games**라는 새 장고 앱을 생성

9.  프로젝트에 앱Config와 REST프레임워크 추가.  
gamesapi/setting.py 에서 설치된 앱을 선언하는 **INSTALLED_APPS**의 값에 아래 값들을 추가.  
    - 'rest_framework'
      - restAPI를 사용하기 위해 추가해야 함.
    - 'games.apps.GamesConfig'
      - 생성한 앱의 **app-name + .apps. + class name**를 추가해야 함.
      - class name은 gamesapi/games/apps.py 에서 확인할 수 있음.