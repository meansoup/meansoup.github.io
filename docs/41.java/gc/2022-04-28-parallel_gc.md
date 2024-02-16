---
layout: post
title: "Parallel GC는 무엇이고 언제 쓰기 좋은걸까?"
sidebar_label: "[GC type] 2. Parallel GC"
nav_order: 3
parent: Garbage Collection
grand_parent: Java
permalink: /docs/java/gc/parallel_gc
math: mathjax3
sitemap:
  lastmod: 2024-02-16
---

앞서 본 [Serial Garbage Collection](/docs/41.java/gc/2022-04-16-serial_gc.md)은 단점이 명확하다.  
Serial은 thraed의 낭비가 크다.  
multiple CPU 로부터 성능을 뽑아내기 위해 Parallel GC를 사용한다.

## Serial vs Parallel

serial GC STW
- ![serial](/images/post/java/gc/serial.jpg)

parallel GC STW
- ![parallel](/images/post/java/gc/parallel.jpg)

serial은 GC를 단일 thread로 하기 때문에 위와 같이 thread의 낭비가 크다.  
parallel은 thread를 효율적으로 사용하고 더 빠르게 GC를 수행할 수 있다.

## Parallel GC 란?

Parallel GC는 Serial GC와 비슷하다.  
multiple CPU를 사용해서 application throughput을 향상시킬 수 있기 때문에 **throughput collector**라고도 불린다.  

Young GC를 수행하는데 multiple thread를 사용하는게 특징이다.  
default로 N개의 CPU일 때 collection에서 N개의 GC thread를 사용한다.  

## usage

Parallel GC는 GC가 발생하면 모든 thread를 중지하고 multi-thread를 사용하여 GC 작업을 수행한다.  
따라서 GC 작업은 중단 없이 효율적으로 수행된다.  
일반적으로 application 에 사용되는 시간 대비 GC 시간을 최소화할 수 있는 방법이다.  
그러나 이후에 나오는 다른 GC들에 비해 한 번의 [STW](/docs/41.java/gc/2022-04-14-gc_basic.md#stw-stop-the-world)는 긴 편이다.

위와 같은 이유로 **개별의 STW가 길어지는 것은 수용할 수 있으나 전체적인 성능이 중요한 작업을 진행할 때 Parallel GC가 사용되기 적합**하다.  
- 대표적으로 **batch process**나 대량의 **database query**가 있다.

## command

`-XX:+UseParallelGC`으로 사용할 수 있다.  
- java -XX:+UseParallelGC -jar demo.jar

GC thread의 수를 조절하기 위해 `XX:ParallelGCThreads`를 사용할 수 있다.
- -XX:ParallelGCThreads=**N**

**Maximum garbage collection pause time**을 설정하기 위해 `-XX:MaxGCPauseMillis`을 사용할 수 있다.
- -XX:MaxGCPauseMillis=**N**
- 기본적으로는 maxGcPause time은 설정되어 있지 않다.
- 이 값이 설정되면 maxGcPause 시간을 맞추기 위해 heap size 등의 parameter가 조정된다.
- 이를 통해 GC의 **Throughput**이 줄어들 수 있다.
- 이 시간이 항상 충족되지는 않을 수 있다.

GC에 사용되는 시간의 비율을 **Throughput**이라고 한다.  
`-XX:GCTimeRatio`를 통해 ratio를 설정할 수 있다. 
- -XX:GCTimeRatio=**N**
  - $$ \frac{1}{1 + N} $$ 으로 세팅되며, default **N** = 99로, GC에서 전체 시간의 1%를 사용하는 것을 목표로 한다.
- 이는 $$ \frac{GC time}{application time} $$ 을 의미한다.  

### priorify

Parallel 에서의 우선순위는 아래와 같다.
1. Maximum garbage collection pause time
2. Throughput

**Maximum garbage collection pause time**이 충족된 이후에만 **Throughput**을 고려한다.  
마찬가지로 **Throughput**이 충족되어야 max heap size를 고려한다.
- [GC 공통 command](/docs/41.java/gc/2022-04-16-serial_gc.md#공통-command)에서 `-Xmx`를 통해 max heap size를 설정할 수 있다.


---


## Parallel Old GC 란?

Young GC와 Old GC 모두 multithread를 사용하는 GC이다.  
지금은 Parallel GC하면 Parallel Old GC를 언급하는 경우가 많다.


### command

`-XX:+UseParallelOldGC`으로 사용할 수 있다.  
- java -XX:+UseParallelOldGC -jar demo.jar

## reference

- https://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html
- https://docs.oracle.com/en/java/javase/18/gctuning/parallel-collector1.html
- https://www.informit.com/articles/article.aspx?p=2496621&seqNum=2