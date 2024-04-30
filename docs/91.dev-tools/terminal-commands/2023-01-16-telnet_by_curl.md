---
layout: post
title: telnet 없을 때 connection 확인하기
sidebar_label: telnet 없을 때 connection 확인하기
parent: linux commands
grand_parent: Tools
permalink: /docs/dev-tools/linux-commands/telnet-by-curl
nav_order: 10
sitemap:
  lastmod: 2023-01-16
---

서버에 연결이 잘 되는지를 확인할 때 telnet이나 ping을 사용하곤 한다.  
권한 문제 등으로 연결이 되지 않거나 서버가 떠있지 않은 경우를 확인할 수 있다.

문제는 alpine 이미지로 생성한 docker를 접속할 때를 대표적으로 telnet이나 ping이 없는 경우가 있다는 것.

굉장히 파워풀한 해결책을 가져왔다.

## telnet 없이 telnet 하기

```sh
curl -v telnet://127.0.0.1:22
```

이거하나면 어디든.

## reference

[https://gist.github.com/Khoulaiz/41b387883a208d6e914b](https://gist.github.com/Khoulaiz/41b387883a208d6e914b)  