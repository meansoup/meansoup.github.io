---
layout: post
title: "linux 환경변수 설정하기 - /etc/profile.d"
parent: linux
grand_parent: 개발도구
permalink: /docs/dev-tools/linux/etc_profiled
---

## etc/profile.d

`/etc/profile.d` 폴더는 linux에서 user와 system 전체 환경 변수와 스크립트를 설정하기 위한 폴더이다.
로그인 시에 폴더 안의 파일들이 자동 실행되어 환경 변수 설정 등에 사용된다.

## 사용 목적

- 스크립트 파일로 환경 변수를 export 하면 시스템 전반에 설정되는 환경변수를 세팅할 수 있다.
- 스크립트를 사용해 시스템 동작을 변경하거나 환경을 설정할 수 있다.

## 주의 사항

- 일반적으로 `.sh`로 끝나는 관례를 따른다.
- 여러 스크립트가 추가될 수 있기 때문에 명확한 이름을 사용한다.
- 스크립트는 알파벳 순서에 맞춰 수행되는 것에 주의한다.
- 시스템의 모든 사용자에게 적용된다는 점을 고려한다.

## 예시

예를 들면 실제로 내가 사용하는 로그인 토큰을 담은 환경변수 스크립트를 작성해본다.
로그인 토큰 같은 경우 사용되는 보안상의 이유로 스크립트를 git에 올리지 못하기 때문에 환경변수로 세팅해놓고 스크립트에서 환경 변수를 조회하도록 하면 좋다.

**/etc/profile.d/login_token.sh**

```bash
#!/bin/bash
export LOGIN_TOKEN="Hello_TOKEN"
```

## reference

- linuxfromscratch.org/blfs/view/11.0/postlfs/profile.html
