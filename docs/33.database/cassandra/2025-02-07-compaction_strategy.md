---
layout: post
title: Cassandra Compaction Strategy 종류 및 이해하기
sidebar_label: Compaction Strategy
parent: Cassandra
grand_parent: Database
lang: kr
permalink: /docs/db/cassandra/strategy
sitemap:
  lastmod: 2025-02-07
---

**<u>Compaction Strategy (CS)</u>**[^1]  
Cassandra 내부의 GC 작업을 위한 Strategy를 의미하며 Cassandra의 몇 가지 Strategy 중 선택할 수 있다.  
workload에 맞는 compaction strategy를 선택하는 것만으로도 query와 compaction 성능 모두 챙길 수 있다.

* [Size Tiered (STCS)](#size-tiered-stcs)
* [Leveled (LCS)](#leveled-lcs)
* [Time Window (TWCS)](#time-window-twcs)
* [Unified (UCS)](#unified-ucs)

## Size Tiered (STCS)

write-intensive workloads에 적절한 cassandra의 default Compaction Strategy.

### 동작 방식

STCS는 SSTable의 size와 count를 기준으로 compaction을 진행한다.

1. 유사한 size의 SSTable을 set number(default: 4)까지 갖게 되는 경우 compaction trigger 된다.
2. SSTable을 하나의 큰 SSTable로 merge 된다.
3. 필요한 경우 SSTable이 커지면서 더 큰 SSTable로 merge 된다.

위와 같은 동작 방식으로 한 순간에는 다양한 사이즈의 SSTable이 존재할 수 있다.

### 특징

- write intensive workload에 적절하다.
- 혹은 다른 적절한 CS가 없는 경우 무난한 선택지이다.
- merge-by-size 프로세스가 **data를 grouping 하지 않으므로 여러 SSTable로 특정 row가 퍼져있을 수 있어 read 성능이 떨어질 수밖에 없다**.
- size를 기준으로 compacdtion이 동작하여 data 삭제가 발생해도 실제 data compaction이 예상대로 되지 않을 수 있다.
- **compaction 과정 중 old와 new를 위한 space가 동시에 필요하며 가장 큰 SSTable의 size가 커짐에 따라 disk space가 더 많이 필요하다**.
- 평상 시의 I/O, CPU는 LCS 보다 좋다.
- 위와 같은 이유로 HDD 사용에 LCS 보다 적합하다.
- 하나의 SSTable의 크기가 커서 **compaction 순간의 I/O, CPU는 LCS 보다 더 많이 필요하다**. 우리 회사는 이 이유로 CPU spike로 인해 장애를 겪었다.


## Leveled (LCS)

Size Tiered의 읽기 성능 이슈를 보완하기 위한 Compaction Strategy.

### 동작 방식

LCS는 SSTable을 Level로 구분한다.  
각 Level은 고정된 size limit을 가지며 limit이 초과되면 compaction이 trigger 된다.

1. Memtable이 Flush 되면 L0 (first level)의 SSTable에 쓰인다.
2. compaction이 발생하면 L0의 SSTable들은 L1의 SSTable들과 merge 된다.
3. 필요한 경우 상위 level로 compaction이 전파된다.

참고할 점은 L1 이후의 level에서는 같은 level 사이의 다른  SSTables과의 non-overlapping을 보장한다. (L0에선 보장되지 않음)
- 따라서 **read operation이 발생할 때 level 당 하나의 SSTable만 보면 된다**.

### 특징

- 읽기 성능을 최적화 하기 때문에 read heavy workload 혹은 lots of updates(or delete) workload에 적절하다.
- 순수한 시계열 데이터에는 적절하지 않다.
- write 위주의 workload에 적절하지 않다.
- STCS 보다 disk를 조금 사용한다. (대략 10% 사용)
- 작은 크기의 SSTable을 많이 생성하고, 데이터의 중복 제거와 정렬을 위한 compaction이 필수적이어서 I/O와 CPU를 많이 사용한다.
- HDD 같은 성능이 떨어지는 storage에 적합하지 않다.


## Time Window (TWCS)

TTL되고 대부분 변경되지 않는 time series data를 위해 디자인된 Compaction Strategy.

### 동작 방식

TWCS는 time window로 구분된다.  
각 SSTable은 time window로 구분되어 효율적으로 compaction.

1. 일련의 period와 관련된 time window를 갖는다.
2. Memtable이 Flush 되면 SSTable에 쓰인다.
2. time window 기간 동안 flush된 SSTable 들이 생긴다.
3. active time window가 지난 경우 time window 기간 내의 SSTable을 STCS를 통해 압축해서 하나의 Large SSTable로 compaction 한다.
4. compaction된 SSTable은 maximum timestamp를 갖는다.

### 특징

- SSTable이 time window에 따라 나뉘어지며 expire 또한 시간에 따라 drop 할 수 있다.
- 시간만 보고 SSTable을 통채로 drop 하므로 STCS나 LCS보다 disk space 회수가 안정적이고 효율적이다.
- timw window period 내에 한 번의 major compaction만 발생하여 compaction이 효율적이다.
- 특정 period에 데이터가 몰릴 경우 성능 저하가 발생할 수 있다.


## Unified (UCS)

read-heavy, write-heavy, read-write, time-series 등 대부분의 workload에서 추천된다.  
- There is no need to use legacy compaction strategies, because UCS can be configured to behave like any of them.
- cassandra 5.0에서 추가 되었다.

### 동작 방식

UCS는 shard 단위로 compaction이 진행된다.

1. shard 내의 일정 개수 이상의 SSTable이 생기면 compaction
2. 각 level 별 전략에 따라 다르게 수행
   - Leveled: LCS 처럼 L0의 데이터가 L1으로 compaction
   - Tiered:  STCS 처럼 일정 개수까지 SSTable을 쌓음

### 특징

- 다른 모든 CS들의 장점을 결합하여 최적화했다.
- 따라서 다양한 워크로드(사실상 모든 워크로드)에서 효율적이다.
- workload에 따라 내부에서 write가 많아지면 Tiered, read가 많아지면 Tiered로 전환한다.
- SSTable을 shard로 나눠서 관리하여 각 shard가 독립적(병렬적)으로 compaction 가능하고 효율적으로 compaction 가능하다.
    - LCS는 level과 level별로 token이 정렬된 구조라면, UCS는 shard 별로 level이 나뉜 grid 구조에 가깝기 때문에 shard 별 compaction이 가능한 구조.
- UCS는 실행 중 다른 CS로 동적으로 전환이 가능하다.
- 다양한 전략으로 최적화를 위한 튜닝이 필요하다.


---

[^1]: [Compaction Strategy](https://cassandra.apache.org/doc/latest/cassandra/managing/operating/compaction/index.html)에서 각 Compaction Strategy에 대한 공식 문서 참고
