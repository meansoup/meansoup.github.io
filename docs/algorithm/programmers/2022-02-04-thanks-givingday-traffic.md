---
layout: post
title: 추석 트래픽
tag:
  - programmers
parent: programmers
grand_parent: algorithm
permalink: /docs/algorithm/programmers/thanks-givingday-traffic
---

## 문제
programmers의 2022 KAKAO BLIND RECRUITMENT 문제
- [https://programmers.co.kr/learn/courses/30/lessons/17676](https://programmers.co.kr/learn/courses/30/lessons/17676)

## 접근 방식

이번 문제는 내가 제일 잘 풀지 않았을까?  
문제를 보고 처음 접근한 방식은 이거다.  

모든 요청의 시작점과 끝점에서만 traffic count가 변한다는 것.  
그러니까 모든 시점에서 최대 traffic을 보는 것이 아니라, 시작점과 끝점들에서만 traffic을 확인하면 된다.

![접근 방식](/images/post/algorithm/programmers/thanks_givingday_traffic.JPG)

그림을 보면, 모두 표현하진 못했지만 나는 결국 파란 선에서만 max 값을 체크하겠다는 것이다.

접근 방식을 정리해보면,
1. 시작 점과 끝 점에서만 traffic을 확인한다.
2. traffic은 특정 시점이 아니라 1초 간의 traffic을 카운트 한다.

## 코드

이번 문제는 설명 없이 코드 이해가 쉽지 않을 수도 있다.  

1. 우선 주어진 time을 millisec으로 변환한다.
2. elapsed time도 역시나 millisec으로 변환한다.
3. elapsed time은 999ms를 추가했다.
  - 1000ms는 문제가 1초 간의 traffic을 카운트 하기 때문에 추가했다. 위 그림을 보면 특정 시각의 traffic을 count할 수 있는데, **elapsed를 1초로 늘여서 그래프를 그리면 어디서 잡든 1초 간의 traffic을 체크할 수 있다**. 이 부분은 좀 이해가 안될 수 있으니 깊게 생각해보면 좋을 것 같다.
  - 1ms를 뺐는데, 예제에서 보이듯 elapsed가 2초면 0.001 초부터 2.000 초까지 계산하기 때문에
4. 시작 시각과 끝 시각을 넣고 정렬한다.
5. 정렬된 시각에서 시작하고 끝나지 않은 시점의 max traffic을 계산한다.

```py
from datetime import datetime

def solution(lines):
    
    times = []
    for line in lines:
        ymd_hms, t = line.rsplit(' ', 1)
        millis = datetime.strptime(ymd_hms, "%Y-%m-%d %H:%M:%S.%f").timestamp() * 1000
        elapsed = float(t[:-1]) * 1000 + 999

        times.append((millis - elapsed, 's'))
        times.append((millis, 'e'))

    times.sort()

    max_cnt, cnt = 0, 0
    for _, v in times:
        if v == 's':
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt -= 1

    return max_cnt


if __name__ == "__main__":
    lines = [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]
    print(solution(lines))

    lines =  [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]
    print(solution(lines))
```