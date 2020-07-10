---
layout: post
title: Tim Sort
tag:
  - algorithm
---

## 왜??

why?
- 왜 Tim sort를 공부해야 하나요?
- 알고리즘 굳이..?

which?
- 어떤 sorting 알고리즘을 쓰시나요?
- merge? quick? 만들어서 쓰시나요?
- 사용하시는 라이브러리는 어떤 sort 인가요?


## 사용처

Tim sort는 아래 언어들에서 기본 sorting 알고리즘으로 사용됩니다.

- python (since v2.3)
- java (since SE 7)
- android
- V8
- Swift

## 특징

1. hybrid sorting algorithm (merge + insertion)
2. highly optimized mergesort
3. stable and faster mergesort

## 장점

1. 작은 수의 sort에 있어서 insertion sort를 수행하므로 더 빠른 속도를 보인다.
2. 큰 수에 있어서도 merge sort를 통해 빠른 속도를 보인다.
3. real data에서 강점을 보인다.
   - 실제 테스트를 하는 데이터들은 whole random data이기 때문에 기존의 sorting들과 유사한 속도이다.
   - 실제 데이터들은 부분 sorting 되어 있거나 연속적인 값인 경우가 많아 더 좋은 효율을 보인다.
4. worst case에서도 기존의 merge sort처럼 O(nlogn)을 유지
   - quick sort 대비 장점

## 주요 개념

