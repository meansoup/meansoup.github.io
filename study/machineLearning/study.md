---
layout: normal
title: Machine Learning
---

[모두를 위한 머신러닝 강의](https://hunkim.github.io/ml/)  
  굉장히 체계적으로 정리된 동영상 강의와 자료를 사용하여 RL에 대해 공부

## Lecture 1:

### reinforcement Learning(RL):

![01](../1_01.png)
보상을 통해 공부하도록 하는 방식  

environment와 actor, observation, reward로 구성됨   

observation(state): actor의 행동에 따라 바뀌는 상태
reward: 행동이 끝나서 받을 수 있는 보상

* 알파고의 핵심 알고리즘 중 하나이기도 함

## Lecture 2:

OpenAI GYM:  
actor, env를 다 세팅해주는 것은 어려움. openAI GYM으로 해결   
주어진 환경에서 알고리즘만 짜면 됨. 어떤 환경이든 action만 주면 됨

frozen lake:  
  쉬워 보이지만 실제 agent 입장에서 environment는 보이지 않음 -> 어려움  
  env:  
    start, frozen, hole, green 등의 장소

![01](../2_01.png)


agent -- action -> env  
agent <- reward -- env

```python
env = gym.make("Taxi-v1")   # make로 환경생성. 인자는 만들 환경
observation = env.reset()   # 환경을 초기화. 초기화된 상태를 observation이 받음
env.rendor()                # 출력
observation, reward, done, info = env.setup(action)
                            # action을 실행하고 action의 결과로 observation을 받고
                            # 혹시 있다면 reward를 보상으로 받고,
                            # 게임이 끝났는지를 done, 추가적인 정보를 info로 받음
```