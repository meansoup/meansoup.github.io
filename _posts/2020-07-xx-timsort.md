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

1. 작은 수의 sort에 서도 quick이나 merge sort보다 빠른 속도를 보입니다..
2. 큰 수에 있어서도 빠른 속도를 보입니다.
3. real data에서 강합니다.
   - 테스트를 하는 데이터(실험실에서나 보이는)들에서는 whole random data 이기 때문에 기존의 sorting들과 유사한 속도.
   - real data들은 부분 sorting 되어 있거나 연속적인 값인 경우가 많아 더 효율적.
4. worst case에서도 기존의 merge sort처럼 O(nlogn)을 유지합니다.
   - quick sort와 대비하여 사용되는 이유가 되기도 함.

## 주요 개념
Tim sort의 기본은 merge sort 입니다.
여러가지 기술들로 여러 부분의 단점들을 개선해낸 sorting 알고리즘입니다.


### binary insersion sort
insertion sort의 O(n^2)를 `C1 * n^2 + a1` 라고 표현한다면 merge sort의 O(nlogn)을 `C2 * nlogn + a2`라고 표현할 수 있는데, 작은 n에서는 C1과 C2의 크기가 성능에 큰 영향을 미치며 insertion sort가 더 효율적임.
따라서 성능 개선을 목적으로 tim sort는 작은 단위에서 insertion sort를 사용.
효율을 위해 binary search로 넣을 위치를 찾음.

### run
run은 각각이 insertion sort로 sorted 된 기본 단위입니다.
Tim sort는 run이라는 덩어리를 만들어놓고 run들을 merge하는 방식으로 진행됩니다.
`minRun`을 통해 run의 최소 크기를 정함.
- ary의 크기를 `N`이라하면 `minRun = min(N, MIN_MERGE)`
- `MIN_MERGE`의 경우  2^5 ~ 2^6 의 값을 사용.
  - 이는 통계적으로 insertion sort가 더 빠른 크기.
  - 전체 크기에서 mergesort가 가장 효율적일 수 있는 `minRunLength`를 계산하여 사용.
  - merge sort는 2의 제곱수일 때 가장 효율이 좋음.

### merge stack
각각의 run은 stack에 쌓이고 Tim sort의 merge는 stack에서 run들을 가져와 병합하는 방식으로 이루어집니다.
기존의 merge sort에서 중요한 부분들이 run을 도입하여 Tim sort에서 추가적으로 고려해야 되는 부분들이 있습니다.
Tim sort에서 이 부분에서 중요하게 고려한 부분은 다음과 같습니다.

1. stack의 갯수를 조절합니다.
  - merge sort는 stack을 사용하지 않음.
  - run을 무자비하게 쌓으면 stack의 메모리 문제.
2. 길이가 유사한 크기의 run 끼리 병합합니다.
  - merge sort에서는 유사/동일한 크기의 덩어리를 병합하는 것이 기본.
3. 인접한 run을 병합합니다.
  - merge sort에서는 인접한 덩어리를 병합하는 것이 기본.
  - 안정성과 효율적인 처리를 위해.
  
