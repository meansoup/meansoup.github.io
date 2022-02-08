---
layout: post
title: 무지의 먹방 라이브
parent: programmers
grand_parent: algorithm
permalink: /docs/algorithm/programmers/muzi-mukbang
--- 

## 문제
programmers의 2022 KAKAO BLIND RECRUITMENT 문제
- [https://programmers.co.kr/learn/courses/30/lessons/42891](https://programmers.co.kr/learn/courses/30/lessons/42891) 

## 접근 방식 

이번 문제도 최대한 time complexity를 줄이는 방향으로 설계를 잡아봤다.  

내가 고려한 사항
1. 몇 바퀴 돌 수 있을지? 즉 다 먹어버리는 음식이 어디까지인지.
2. 그리고 다 먹고 남은 음식들 사이에서 순서를 반복 없이 빨리 찾아보자. 

내가 설계한 내용
1. 음식을 먹을 수 있는 양(`food_time`) 순으로 sorting 한다
2. 주어진 시간(`k`)를 기준으로 몇 번 먹을 수 있는 음식까지 다 먹어내는지 확인한다.
3. 남은 시간으로 몇 번째 음식을 먹는지 확인한다.


## 코드
```py
def solution(food_times, k):
    
    val_idx = [ (food_times[i], i)  for i in range(len(food_times)) ]
    sorted_val_idx = sorted(val_idx)
    
    ex_val = 0
    for i in range(len(sorted_val_idx)):
        val, _ = sorted_val_idx[i]
        added = (val - ex_val) * (len(food_times) - i) 

        if added > k:
            target_in_remains = k % (len(food_times) - i)
            remains = sorted(e[1] for e in sorted_val_idx[i:len(food_times)])        
            return remains[target_in_remains]  + 1
        
        k -= added
        ex_val = val
    
    return -1 

if __name__ == "__main__":
    print(solution([1], 1))
    print(solution([3, 1, 2], 5))
    print(solution([1, 1, 1, 1], 3))
    print(solution([1, 1, 1, 1], 4))
    print(solution([1, 2, 3, 1], 6))
    print(solution([5, 1, 3, 3, 4], 9))
```
