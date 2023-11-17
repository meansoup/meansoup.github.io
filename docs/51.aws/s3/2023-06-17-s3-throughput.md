---
layout: post
title: S3 처리량 제한
parent: S3
grand_parent: aws
nav_order: 1
permalink: /docs/aws/s3/throughput
sitemap:
  lastmod: 2023-06-17
---

우리는 팀 내에서 storage로 대부분 S3를 사용하고 있다.  
S3를 굉장히 자주, 잘 씀에도 S3를 잘쓰는 방법에 대한 노하우는 많지 않다.  

aws s3 cli를 통해 활용하는 노하우 정도.    
S3에도 dynamo처럼 처리량 제한이 있는데, 이건 잘 모르고 사용하는 편이다.


## 처리량 제한

S3의 처리량 제한은 접두사 별로 존재한다.
- 초당 3500개의 PUT (PUT/COPY/POST/DELETE)
- 초당 5500개의 GET (GET/HEAD)

이 처리량은 접두사별로 존재하기 때문에, 접두사를 분리해주면 병렬화하여 처리량을 늘릴 수 있다.
- S3의 접두사는 첫 `/` 이 등장하기 전까지의 bucket prefix.
- 예전엔 접두사의 수가 6-8 자리로 해싱을 권장했으나, 내부적으로 해시를 사용하여 해결됨. (아래 레퍼런스 참조)

## S3 처리량에 대해

사실 초당 3500개의 put을 하는건 object storage에서 쉽지 않다.    
테스트로 100KB 파일 2만 개를 올리는데 걸린 시간은 16분.  
prefix만 적절하게 사용한다면 문제가 있기는 어렵다.  
그렇지만 엔터프라이즈 급에서 prefix 설계가 잘못된다면 문제가 생길 수 있다.

dynamo의 partitionKey 제한도 그렇지만, s3 key도 이미 서비스 중에 prefix를 변경하기 어려우므로  
설계 단계에서 잘 고려될 필요가 있겠다.


## reference

- 처리량 제한 문서
  - [https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/optimizing-performance.html](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/userguide/optimizing-performance.html) 

- 접두사 수 관련 문서
  - [https://aws.amazon.com/ko/about-aws/whats-new/2018/07/amazon-s3-announces-increased-request-rate-performance/](https://aws.amazon.com/ko/about-aws/whats-new/2018/07/amazon-s3-announces-increased-request-rate-performance/)