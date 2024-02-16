---
layout: post
title: Curl to Code (Python/Java ..)
sidebar_label: Curl to Code (Python/Java ..)
parent: 사이트
permalink: /docs/dev-tools/site/curl-to-code
grand_parent: 개발도구
sitemap:
  lastmod: 2022-02-06
---

api 테스트나 여러 서버의 작업을 위해 request를 curl로 짜는 일이 많다.  
이렇게 작성한 curl로 python 코드를 짜려고 할 때 번거롭거나 귀찮은 경우가 많다.  

나 같은 경우는 간단한 스크립트를 작성하려고 curl을 짜다가,  
생각보다 귀찮아지면 python으로 옮기는 경우가 있는데 이럴 때 참고하는 편이다.

opensource 프로젝트인 **curlconverter**를 소개한다.  
curl을 입력하면 code를 작성해주는 프로젝트.  
내가 주로 쓰는 python, java, go를 모두 지원한다.  

## 사용법

[curlconverter.com](https://curlconverter.com/#python) 에 접속해서 사용한다.  

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

![curlconverter](/images/post/tips/curl-converter.JPG)
</div>

# reference

[https://stackoverflow.com/questions/42604586/converting-a-curl-to-python-requests](https://stackoverflow.com/questions/42604586/converting-a-curl-to-python-requests)  
[https://curlconverter.com/](https://curlconverter.com/)  