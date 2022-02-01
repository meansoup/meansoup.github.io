---
layout: post
title: 신고 결과 받기
tag:
  - programmers
parent: programmers
grand_parent: algorithm
permalink: /docs/algorithm/programmers/get_report_list
nav_order: 5
---

## 문제
[https://programmers.co.kr/learn/courses/30/lessons/92334](https://programmers.co.kr/learn/courses/30/lessons/92334)

## 접근 방식
loop를 최대한 줄일 수 있는 방향으로 생각해보기.  

1. 우선 id의 index로 answer를 반환해야하니, index를 찾기 위한 dict를 만들기
2. reportee에 대한 reporters를 체크할 수 있게 dict 만들기

## 코드
```py
def add_to_dict(dic, key, val):
    if key not in dic:
        dic[key] = set()

    dic[key].add(val)


def solution(id_list, report, k):
    id_idx_map = {id_list[i]: i for i in range(0, len(id_list))}
    report_by_user = dict()

    for r in report:
        reporter, reportee = r.split()
        add_to_dict(report_by_user, reportee, reporter)

    answer = [0] * len(id_list)
    for _, reporters in report_by_user.items():
        if len(reporters) >= k:
            for reporter in reporters:
                idx = id_idx_map[reporter]
                answer[idx] += 1

    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    ans = solution(id_list, report, k)
    print(ans)
```