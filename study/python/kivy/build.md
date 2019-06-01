---
layout: normal
title: Kivy android build
---

## android build

[android build](https://kivy.org/doc/stable/guide/packaging-android.html)는 ubuntu에서만 가능함.  
[Buildozer](https://github.com/kivy/buildozer)를 통해 전체 build process를 간편하게 실행할 수 있음. 현재 kivy에서 추천하고 있는 방법.  

build 과정
1. sudo pip install buildozer
2. buildozer init
3. edit buildozer.spec
4. buildozer android debug deploy run


### issue

* installing/updating sdk platform tools if necessary:  
    `buildozer.spec`에서 log_level=2 로 하면 해결 됨

* Aidl not found, please install it[:](https://github.com/kivy/buildozer/issues/824)  
    license 관련 문제가 나올 때, `y` 를 입력

#### Command failed:
command failed에 대해서는 빨간색 command failed위의 마지막 로그들을 보면 됨.

* ValueError: storage dir path cannot contain spaces ...  
    폴더에 빈칸이 있으면 안 됨.

* [ErrorReturnCode_127](https://github.com/kivy/buildozer/issues/829)  
    `sudo apt-get install automake`  
    `sudo apt-get install autoconf`   
    `sudo apt-get install libltdl-dev`  

* [ErrorRetrunCode_1](https://github.com/kivy/buildozer/issues/678#issuecomment-431596608)  
    `buildozer android update`

* BUILD FAILURE: NO main.py(o) found in your app directory ...  
    main.py가 있어야 함.

* Execution failed for task ':compileDebugJavaWithJavac'  
  * [`buildozer android clean`](https://groups.google.com/forum/#!topic/kivy-users/cJBzDagRJjw) - 해결 안됨.  

  * [pip install python-for-android](https://python-for-android.readthedocs.io/en/latest/quickstart/)  
    python-for-android sdk, ndk가 설치되지 않아서 그런 것으로 보임.  
    위 명령어를 통해 설치하고, sdk는 `command line tools`를 받아서 명령어로 설치. ndk는 받기.  

    sdkmanager 명령어가 `repositories.cfg`관련 fail이 난다면 [`touch ~/.android/repositories.cfg`](https://askubuntu.com/questions/885658/android-sdk-repositories-cfg-could-not-be-loaded)로 생성

    buildozer에서 명확한 문제가 나오지 않을때, 위 사이트에서 p4a 명령어를 사용하여 빌드 시, 보다 구체적인 에러 문구를 확인할 수 있음.  