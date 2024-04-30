---
layout: post
title: intellij 대소문자 변경 단축키
sidebar_label: intellij 대소문자 변경 단축키
parent: Intellij
grand_parent: 개발도구
lang: ko
permalink: /docs/dev-tools/intellij/upper-case
sitemap:
  lastmod: 2022-06-30
---

uppercase to lowercase.  

대문자를 소문자로, 소문자를 대문자로 바꾸는 intellij 단축키가 있다.  
이게 별 것 아닌 것 같지만 세로 편집과 함께하면 효율성이 극대화 된다.

ubuntu에서 옵션을 찾아서 수행하다가 안됐던 것을 해결해서 정리해본다.


### 내가 대소문자 단축키를 사용하는 방법

나는 평소에도 세로 편집을 굉장히 자주 사용한다.  
getter & setter의 변경, entity와 dto 간의 mapping과 factory 생성 등에서 세로 편집은 굉장한 효율을 낸다.  
여기에 대소문자 변경까지 단축키로 더해지면 굉장하다.

![usage](/images/post/dev-tools/intellij/toggle-case/usage.gif)


### toggle case shortcut

intellij에서는 대소문자 변경을 toggle case라고 이름 지었다.  

**ctrl + shift + U** 를 통해서 대문자를 소문자로, 소문자를 대문자로 바꿀 수 있다.


### ubuntu 이슈

windows나 mac에서는 사용할 수 있는데,  
ubuntu에서는 계속 shortcut이 동작하지 않았다.  

이번에 확인했는데, ubuntu에서는 이미 **ctrl + shift + U**를 emoji 단축키로 사용하고 있다.  
이건 거의 사용하지 않는 키니까 변경하거나 삭제하면 된다.


### ubuntu 이슈 해결

1. 커맨드에 `ibus-setup` 입력
2. `Emoji tab`으로 이동
3. `ctrl + shift + U`가 세팅되어 있는 unicode code point를 선택
4. 삭제 혹은 이동 

나 같은 경우는 해당 코드를 삭제했다.


### reference

https://youtrack.jetbrains.codm/issue/IDEA-112533