---
layout: post
title: http 1.0 semantics
parent: http
nav_order: 2
grand_parent: internet
permalink: /docs/internet/http/http1.0/semantics
sitemap:
   lastmod: 2023-06-18
---

## multipart form data

http의 단순 전송은 크게 신경쓸게 없다.

보통 http 응답은 한 번에 한 파일씩 반환하므로 경계를 신경쓸 필요가 없다.
그런데 multipart를 이용하는 경우 한 번의 요청에 여러 파일을 전송할 수 있으므로 받는 쪽에서 파일을 나눠야 한다.

```
Content-Type: multipart/form-data; boundary=boundary-example

--boundary-example
Content-Disposition: form-data; name="text"

Sample text part.
--boundary-example
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

This is the content of the file.

--boundary-example--
```

Content-Type은 multipart/form-data,  
boundary에는 랜덤하게 생성된 경계 문자열이 들어가고,  
body는 이 경계 문자열로 블록이 나뉜다.
- 경계 문자열에 --이 prefix로 붙는다

각각의 블록 내부도 http와 같이 **header** 후에 **빈 줄** 그리고 **body**로 이루어진다.  
그리고 파일의 마지막도 경계 문자열로 끝난다.  
- 마지막 경계 문자열은 prefix와 postfix 모두 --를 붙여 끝낸다.

## content negotiation

통신 방법을 최적화하고자 하나의 요청 안에 서버와 클라이언트가 서로 최고의 설정을 공유하는 시스템을 말한다.  
이를 위해 header를 이용한다.

| request header      | response header      | negotiation target      |
|  ---  |  ---  |  ---  |
|  Accept     | Content-Type      |  mime type     |
|  Accept-Language     | Content-Language      | 표시 언어      |
|  Accept-Charset        | Content-Type      | 문자의 문자셋      |
|  Accept-Encoding      | Content-Encoding      |  body 압축     |

### 파일 종류 결정

```
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
```

서버는 요청에서 요구한 형식 중에서 파일을 반환한다.  
우선 순위를 해서개 위에서부터 차례로 지원하는 포맷을 찾고 일치하면 그 포맷을 반환한다.  
서로 일치하는 요청이 없다면 서버가 406 Not Acceptable 오류를 반환한다.  

### 표시 언어

```
Accept-Language: en-US,en;q=0.8,ko;q=0.6
```

동일하게 적혀있는 우선순위로 요청을 보낸다. en-Us, en, ko 순

### 문자셋

```
Accept-Charset: windows-949,utf-8;q=0.7,*;q=0.3
```

현대의 어떤 브라우저도 Accept-Charset을 송신하지 않는다.  
브라우저가 문자셋 인코더를 내장하고 있어 미리 negotiation 할 필요가 없어졌기 때문으로 여겨진다.  
문자셋은 mime type과 함께 Content-Type header에 실려 응답된다.  

```
Content-Type: text/html; charset=UTF-8
```

### 압축

압축은 전송속도 향상을 위한 것이다.  
통신에 걸리는 시간보다 압축과 해제가 짧은 시간에 이루어짐으로 압축을 함으로써 웹페이지를 표시할 때 걸리는 전체적인 처리 시간을 줄일 수 있다.  

통신량이 줄어들기 때문에 시간 뿐만 아니라 통신 비용(사용자 데이터, 서버 데이터, 전력 소비 등)도 줄어든다.  

```
Accept-Encoding: deflate, gzip
```

이렇게 header를 보내면 전송받은 목록 중 지원하는 방식이 있으면 응답할 때 그 방식으로 압축된 콘텐츠를 반환한다.  
서버가 gzip을 지원한다면 헤더는 이렇다.

```
Content-Encoding: gzip
```

이제는 서버에서 받아올 때 뿐 아니라 서버로 올릴 때도 압축을 사용한다.  
목적은 압축을 통해 얻는 이득을 업로드에도 누리기 위해서.  
이런 경우엔 동일하게 Content-Encoding을 클라이언트가 header에 싣어서 보낸다.  

### 쿠키

쿠키랑 웹사이트의 정보를 브라우저 쪽에 저장하는 작은 파일이다.  
쿠키도 http header를 기반으로 구현되었다.  

예를 들면 서버에서 access 시간을 저장하기 위해 이렇게 header를 보낼 수 있다.  

```
Set-Cookie: LAST_ACCESS_DATE=Jun/18/2023
Set-Cookie: LAST_ACCESS_TIME=12:04
```

이러면 클라이언트가 이 값을 저장하고 다음에 방문할 때 서버에 이런 형식으로 보낸다.

```
Cookie: LAST_ACCESS_DATE=Jun/18/2023
Cookie: LAST_ACCESS_TIME=12:04
```

이렇게 서버가 상태를 유지하는 stateful처럼 보이게 서비스를 제공할 수 있다.  

쿠키를 사용할 때 주의할점
- 영속성 문제가 있다. 데이터는 사라진다.
- 따라서 db 대신 쓸 수 없다.
- 용량 문제도 있다. 최대 4KB로 더 보낼 수 없다.
- 쿠키는 header로 항상 통신되는데 쿠키가 많아지면 통신량이 늘고 성능이 떨어진다.
- 사용자가 자유롭게 접근할 수 있고 수정도할 수 있어 민감정보는 넣으면 안된다.
- http의 경우 평문으로 전송되서 유의할 필요가 있다.


쿠키는 몇 가지 속성(Expires, Max-Age, Domain, Path, Secure, ...)으로 제어하고 제한할 수 있다.  
쿠키의 이런 기능 추가 역사는 웹 보안의 역사와도 이어진다고.


### 캐시

콘텐츠가 변경되지 않았을 때 로컬에 저장된 파일을 재사용함으로써 다운로드 횟수를 줄이고 성능을 높이는 매커니즘.  
GET / HEAD method 이외는 기본적으로 캐시되지 않는다.

캐시의 방식
1. 갱신 일자에 따른 캐시
    - 서버가 데이터 수정 시간을 헤더로 주고, 클라이언트가 다음 요청에 이를 헤더에 넣는다.
    - 수정이 생겼으면 200에 새로운 데이터를
    - 수정이 생기지 않았으면 304 Not Modified를 반환
2. expries
    - 갱신 일자에 따른 캐시는 서버에 콜을 한번 더 넣어야 한다.
    - expires에 날짜와 시간을 넣어서 지정한 기간 내에선 캐시를 강제로 사용한다.
3. ETag
    - 날짜와 시간을 이용한 캐시 비교만으로 해결할 수 없을 때
    - 동적으로 바뀌는 요소가 많아져서 캐시 유효성 판단이 어려워질 때
    - ETag(Entity Tag)는 순차적 갱신 일시가 아니라 파일의 해시 값으로 비교한다.
    - 갱신 일자에 따른 캐시처럼 ETag를 받고 다음 요청에 받은 ETag를 넣어 보낸다.
    - 서버에서 비교해서 같다면 304 Not Modified를 반환
    - ETag는 http 1.1의 기능이다.

캐시는 Cache-Control header로 유연하게 캐시 제어를 지시할 수 있다.
- 서버에서 내리는 값들도 있고, 클라이언트에서 요청할 때 사용할 수 있는 값들도 있다.
- Cache-Control도 http 1.1의 기능이다.

## reference

- Real World Http chapter 2