---
layout: post
title: kafka consumer 이해하기
sidebar_label: kafka consumer 이해하기
nav_order: 4
parent: kafka
grand_parent: Message Broker
permalink: /docs/message-broker/kafka/consumer
sitemap:
  lastmod: 2024-01-30
---

consumer는 카프카에서 데이터를 가져와 다른 시스템이나 애플리케이션에 데이터를 제공한다.  
consumer는 consumer를 추가/제거 함으로써 처리량에 영향을 주기 때문에 중요하다.

consumer가 topic에 대해 Push 받지 않고 pull 해온다는 것이 중요하다.  
topic을 구독하는 방식을 통해 consumer는 자신의 메세지 소비 비율을 통제한다.  
구독 방식을 통해 consumer를 항상 가동할 필요 없이 다운되면 다시 수행할 수 있다.  
그러나 장시간 다운되선 안된다. (메시지 유실 가능성)

consumer 클라이언트 시작 시 연결을 시도할 수 있는 브로커를 항상 알아야 한다.   
**메세지를 생성한 직렬 변환기와 일치하는 키와 값에 대한 역직렬 변환기를 사용해야 한다.**

## consumer option

| 키                     | 용도                                  |
|-----------------------|-------------------------------------|
| bootstrap.servers     | 시작할 때 연결할 하나 이상의 카프카 브로커            |
| value.deserializer    | 값 역직렬화에 필요                          |
| key.deserializer      | 키 역직력화에 필요                          |
| group.id              | consumer group에 조인하기 위해 사용되는 ID     |
| client.id             | 유저를 식별하기 위한 ID                      |
| heartbeat.interval.ms | consumer가 그룹 코디네이터에게 ping 신호를 보낼 간격 |

## offset

consumer가 브로커에게 보내는 로그의 인덱스 위치로 offset을 사용한다.  
offset을 통해 로그에서 필요한 메시지의 위치를 알 수 있다.

![kafka_offset.png](/images/post/message-broker/kafka/kafka_offset.png)

`auto.offset.reset`을 `earliest`로 설정하면 처음부터 읽기 때문에 해당 토픽에 대한 모든 메시지를 볼 수 있다.  
기본값인 `latest`로 설정하면 consumer를 시작한 후 보낸 메시지들을 읽는다.

![partition_leaders.png](/images/post/message-broker/kafka/partition_leaders.png)

topic에 작성된 메시지를 찾기 위해 우선 topic 내에서 파티션을 찾은 다음 인덱스 기반 offset을 찾는다.  
consumer는 일반적으로 leader replica에서 읽는다.  
consumer가 어떤 파티션에 연결할지, 파티션의 리더는 어디에 있는지는 각 consumer 그룹에 대해 **그룹 코디네이터** 역할을 하는 특정 브로커를 통해 알 수 있다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
참고사항
{: .label .label-green}  

offset은 항상 각 파티션에 대해 증가한다.  
파티션 내에서 각 로그 시퀀스를 갖기 때문에 다른 파티션 간에는 offset 번호가 같아도 괜찮다.    
파티션에 offset 0이 표시되면 나중에 해당 메시지가 제거되더라도 offset 번호는 다시 사용되지 않는다.
</div>


## 파티션 수와 consumer

메시지를 읽는데는 파티션의 수도 영향을 미친다.

### 파티션 수 < consumer 수

![kafka_extra_consumer.png](/images/post/message-broker/kafka/kafka_extra_consumer.png)

파티션보다 consumer가 많으면 일부 consumer는 작업을 수행하지 않는다.  
여유 consumer는 ready 상태이다.  
consumer가 예기치 않게 실패하는 경우에도 비슷한 비율의 소비가 필요한 경우가 있다면 consumer가 있을 수 있다.  
그룹 코디네이터는 그룹 시작 초기에 어떤 consumer가 어떤 파티션을 읽을지 지정하는 것 뿐만 아니라 consumer가 추가되거나 실패하여 그룹을 종료할 때도 consumer를 할당한다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
참고사항
{: .label .label-green}  

**Q: 그렇다면 항상 많은 파티션을 사용하면 되는 것 아닌가?**

많은 파티션은 공짜가 아니다. latency를 증가시킬 수 있다.  
파티션이 많다면 브로커간에 파티션이 복제될 때까지 기다려야해서 대기시간이 길어질 수 있다. consumer에게 메시지를 전달하기 전에 동기화가 완료된다.  
consumer에 대해 파티션이 1:1 매핑이 아닌 경우 더 많은 파티션이 할당됨에 따라 메모리 요구가 증가할 수 있다.
</div>

### 파티션 수 > consumer 수

![kafka_extra_partition.png](/images/post/message-broker/kafka/kafka_extra_partition.png)

**하나의 파티션을 두 개의 consumer가 읽을 수 없다.**  
consumer보다 파티션이 많은 경우 필요에 따라 하나의 consumer가 둘 이상의 파티션을 처리한다.

하나의 파티션을 하나의 consumer가 읽는건 하나의 consumer 그룹 내에서의 이야기다.  
**서로 다른 consumer 그룹에선 각 그룹의 하나의 consumer가 파티션을 읽을 수 있다.**  
즉 파티션 기준으로 여러 consumer가 있을 수 있지만, 같은 consumer 그룹에서는 하나의 consumer만 있을 수 있다.


## 그룹 코디네이터

그룹 코디네이터는 consumer와 협력해서 특정 consumer 그룹이 읽은 topic 내부의 기록을 유지한다.

![coordinates.png](/images/post/message-broker/kafka/coordinates.png)

topic에서 다음 메시지를 읽을 위치를 결정하기 위해 offset을 커밋 좌표로 사용하고 있다.

일반적으로 다른 브로커 서비스에서는 이런 케이스에서 필요한 수만큼 동일한 메시지를 갖는 여러 큐를 갖는다.  
그렇지만 kafka는 consumer 그룹마다 코디네이션을 하기 때문에 별도의 논리적인 작업이 필요하다면 새 consumer 그룹을 사용하여 해결할 수 있다.  
consumer 그룹은 서로 consumer offset에 대한 동일한 코디네이션을 공유하지 않는다.

각 consumer들은 consumer group에 속한다.  
conumser group의 consumer들은 topic 파티션의 소유권을 공유하며 각 consumer가 해당 토픽의 다른 파티션을 분담하면서 메시지를 읽을 수 있다.

![consume_separate_group.png](/images/post/message-broker/kafka/consume_separate_group.png)

위 그림은 동일한 파티션 집합이 3개의 다른 브로커에 존재하고, kinaction_teamoffka0과 kinaction_teamsetka1이라는 2개의 consumer 그룹이 파티션에서 consume하고 있는 상황이다.  
각 그룹의 consumer는 각 브로커의 파티션에서 고유한 데이터 복사본을 가져온다.  
다른 그룹이라면 같이 동작하지 않는다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
참고사항
{: .label .label-green}  

consumer가 데이터를 사용해도 토픽에서 제거하지 않는다.  
그렇기 때문에 consumer group이 다르면 메시지를 가져갈 수 있다.
</div>


## heartbeat

consumer가 그룹 코디네이터에게 ping을 하는 것을 **heartbeat**라고 한다.  
heartbeat는 consumer가 코디네이터와 통신하여 적절한 시간내에 응답하며 작업하고 있음을 알리는 신호이다.

heartbeat가 시간 내에 응답되지 않으면 그룹 코디네이터는 리밸런싱을 시작한다.  
리밸런싱이란 consumer간 파티션 소유권을 이전하는 것을 말한다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
참고사항
{: .label .label-green}  

`heartbeat.interval.ms`를 통해 consumer가 heartbeat를 보내는 간격을 설정할 수 있다.  
`heartbeat.interval.ms`는 일반적으로 `session.timeout.ms`의 1/3 이하의 값으로 설정되어야 한다.  
`session.timeout.ms`는 클라이언트가 활성화 되어있는지 만료를 체크하는 브로커의 시간이다.
</div>


## reference

- Kafka In Action 5장
- https://docs.confluent.io/platform/current/installation/configuration/consumer-configs.html