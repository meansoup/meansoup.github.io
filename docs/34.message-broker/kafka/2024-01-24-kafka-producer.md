---
layout: post
title: kafka producer 이해하기
sidebar_label: kafka producer 이해하기
nav_order: 3
parent: kafka
grand_parent: Message Broker
permalink: /docs/message-broker/kafka/producer
sitemap:
  lastmod: 2024-01-24
---

Producer는 메시지를 카프카 topic으로 보내는 도구이다.

## producer option

| 키                 | 용도                                                        |
|-------------------|-----------------------------------------------------------|
| bootstrap.servers | 시작 시 연결할 하나 이상의 카프카 브로커                                   |
| acks              | 메시지 전달이 성공하기 위한 producer가 요구하는 복제 확인 (acknowledgement)의 수 |
| key.serializer    | 키의 직렬화에 사용되는 클래스                                          |
| value.serializer  | 값의 직렬화에 사용되는 클래스                                          |

## bootstrap servers
 
producer는 할당된 파티션의 leader replica에만 쓸 수 있는데, topic과 **bootstrap.servers** 밖에 모르기 때문에 알고있는 server에 연결한다.
producer는 **boootstrap.servers**를 시작점으로 사용해 모든 후속 쓰기에 사용하는 브로커와 파티션에 대한 메타데이터를 가져온다.

![bootstrap-server.png](/images/post/message-broker/kafka/bootstrap-server.png)

각 브로커들은 클러스터 안의 다른 브로커들도 알고 있기 때문에 producer는 하나의 브로커를 통해 leader를 찾을 수 있다.  

## acks

acks는 producer가 완료를 받기 전에 partition leader가 follower(replica)로 부터 얼마나 많은 ack를 받아야 하는지에 대한 속성이다.  
이 값은 **all**, **-1**, **1**, **0**을 가질 수 있다.  

### acks 0

![ack0.png](/images/post/message-broker/kafka/ack0.png)

**acks가 0**인 경우 0개의 replica에 ack를 받기 때문에 **가장 적은 대기 시간**을 얻을 수 있지만 **안전한 배달을 보장하진 않는다**.

### acks all

![ackall.png](/images/post/message-broker/kafka/ackall.png)

**acks가 all** 혹은 -1인 경우 leader replica가 모든 replica 들의 ack를 기다린다는 의미이다.  
따라서 **가장 느린 대기 시간**을 갖게 되지만 **안전한 배달을 보장**한다.  

### acks 1

![ack1.png](/images/post/message-broker/kafka/ack1.png)

**acks가 1**인 경우 1개의 replica에 ack를 받는다.  
즉 leader replica의 수신을 확인하기 때문에 **비교적 적당한 안정성과 대기시간**을 가질 수 있다.  

leader가 follower에게 복사본을 만드는 사이에 다운된다면 메시지를 누락할 수 있다.

## serializer

카프카의 메시지는 byte array로 저장되기 때문에 serializer가 필요하다.  
producer의 serializer와 맞는 consumer의 deserializer가 필요하다.  
`StringSerializer`, `IntegerSerializer`와 같이 기본 제공되는 serializer들이 있으며, customSerializer를 만들 수도 있다.

여기서 key가 같으면 동일한 partition으로 전송한다.
- partition 수가 늘어나면 다른 partition으로 갈 수도 있다.
- key가 null 인 경우 사용 가능한 partition 중 랜덤으로 선택한다.

## timestamp

최신 버전의 producer에서는 event에 대한 timestamp가 포함되어 있다.  
`message.timestamp.type`을 `CreateTime`으로 설정하면 사용자가 직접 작성하거나 현재 시스템 시간으로 전달할 수 있다.  
`LogAppendTime`으로 설정하면 브로커 시간이 사용된다.  

메시지 전달이 실패하여 재시도 할 수 있기 때문에, 브로커의 시간을 사용할지 producer의 시간을 사용할지 서비스 특성에 맞게 판단해야 한다.

## reference

- Kafka In Action 4장
