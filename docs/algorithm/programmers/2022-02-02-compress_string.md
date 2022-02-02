---
layout: post
title: 문자열 압축
tag:
  - programmers
parent: programmers
grand_parent: algorithm
permalink: /docs/algorithm/programmers/compress_string
nav_order: 5
---

## 문제
[https://programmers.co.kr/learn/courses/30/lessons/60057](https://programmers.co.kr/learn/courses/30/lessons/60057)

## 접근 방식
이번 문제는 푸는데 시간이 정말 오래걸렸는데 원인은 **문제를 제대로 읽지 않았기 때문**이다.  

**문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.** 라는 설명이 있었는데도 나는 이런 요구사항을 명확하게 보지 않고 문제를 생각했다.
- `abcabcdecdecde` 같은 문제를 어떻게 풀어야 할까 고민을 한참 했다.
- 문제를 다시 보고 요구사항을 확인해보니 간단한 문제.


1. 제일 앞부터 정해진 길이만큼이기 때문에 size를 늘려가며 확인할 수 있을 것이다.
2. 사이즈 크기와 관계 없이 더 짧은 경우가 있을 수 있다.

## 코드
```py
def solution(s):
    shortest = len(s)
    for i in range(1, len(s)//2 + 1):

        cur = s[:i]
        cnt = 1
        removed_size = 0

        for j in range(i, len(s), i):
            if cur == s[j:j + i]:
                cnt += 1
            else:
                if cnt != 1:
                    removed_size += i * cnt - len(str(cnt)) - i
                
                cur = s[j:j + i]
                cnt = 1

        if cnt != 1:
            removed_size += i * cnt - len(str(cnt)) - i
        
        shortest = min(shortest, len(s) - removed_size)

    return shortest

if __name__ == "__main__":
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
```