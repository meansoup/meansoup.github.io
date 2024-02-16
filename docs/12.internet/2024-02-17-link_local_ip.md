---
layout: post
title: link local ip address
sidebar_label: link local ip address 개념 명확하게 이해하기
parent: internet
nav_order: 10
permalink: /docs/internet/link-local
sitemap:
  lastmod: 2024-02-17
---

ip 주소 중 특정 ip들은 특별한 목적으로 사용되도록 설계 되었다.  
link local ip address는 특별한 목적으로 설계된 ip block이다.

## link local ip address

**169.254.0.0/16**는 RFC 6890에서 **Link Local Special Purpose Address**로 정의 되었다.   
**Link Local IP Address는 직접 연결된 하위 네트워크 내에서만 유효한 address**이다.

link local ip는 DHCP 서버나 수동으로 구성된 ip address를 사용할 수 없을 경우 auto configuration을 위한 목적의 인터페이스이다.  
정상적으로 routable ip address를 얻게 된 후에는 해당 address를 사용한다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
참고사항
{: .label .label-green}  

- link local ip address는 하위 네트워크에서만 유효하므로 네트워크 인프라에서 해당 block 내의 subnet을 생성하면 안된다.
- router는 link local ip address를 대상으로 하는 패킷은 전달할 수 없다.
- DNS는 link local ip address를 저장해선 안된다.
- 169.254.0.0/24 와 169.254.255.0/24의 각각 256개의 ip는 추후 다른 목적으로 사용하기 위해 예약되었기 때문에 사용할 수 없다.
</div>


## 클라우드와 link local ip address

AWS와 같은 cloud service provider는 클라우드의 물리적인 인프라를 제어하기 때문에 모든 인스턴스에 대해 local access가 가능하도록 구성할 수 있다.

다음과 같은 이유로 link local ip address는 자동구성 서비스에 적합하다.
- link local ip address는 source와 destination 모두에서 non-forwardable ip 이다.
- 클라우드 서비스 내에서 local network으로 연결되어 바이러스로부터 안전하다.
- 사용자가 이 주소를 subnet으로 사용할 수 없다.

이런 이유로 NTP(Network Time Protocol), IMDS(Instance Metadata Service) 등 클라우드 상의 가상 컴퓨터에 필요한 서비스를 link local ip address를 통해 제공한다.

## IMDS (Instance MetaData Service)

클라우드에서 인스턴스의 메타데이터에 접근할 필요가 있는 경우가 있다.  
예를 들면 네트워크 구성, 인스턴스 타입, 가용 영역, 인스턴스 정보 등의 메타데이터가 필요할 수 있다.

대부분의 클라우드 플랫폼에서 **169.254.169.254**를 통해 IMDS에 접근할 수 있다.  
169.254.169.254는 클라우드 인스턴스 내에서 접근 가능한 특별한 ip이다.


## reference

- 169.254.0.0/16, https://www.baeldung.com/linux/cloud-ip-meaning
- link local, https://en.wikipedia.org/wiki/Link-local_address
