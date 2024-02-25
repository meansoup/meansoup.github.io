---
layout: post
title: "too many open file 이슈 확인하고 해결하기"
sidebar_label: "too many open file"
parent: linux
grand_parent: 개발도구
permalink: /docs/dev-tools/linux/too_many_open_file
sitemap:
  lastmod: 2024-02-25
---

## too many open files in system

 ```
 open config.property: too many open files in system
 ```

**too many open files in system**는 linux에서 열린 파일 수가 너무 많아서 더 이상 파일을 열 수 없다는 오류 메시지이다.  
linux에서는 동시에 열 수 있는 파일 수가 제한되어 있고, 이 제한을 초과하여 파일을 열려고 할 때 오류가 발생한다.

오류가 발생하는 이유는 설정된 자원보다 더 많은 요청을 하기 때문이다.  
프로세스가 동시에 많은 파일을 열 때 발생할 수 있는데, 주로 이런 경우는 **file open 후 close 하지 않는 코드 상의 버그일 가능성이 높다**.  
버그인지 아닌지 확인하기 위해 linux의 property를 먼저 확인한다.


## file open limit 확인하기

file open limit을 확인할 때 **user의 resource limit을 체크하는 ulimit**을 사용한다.  
ulimit에는 두 가지 limit이 있다.

1. hard limit: -H 옵션으로 접근하며, super user만 수정할 수 있는 limit
2. soft limit: -S 옵션으로 접근하며, 사용자가 hard limit 내에서 변경할 수 있는 limit

process는 당연히 둘 중 더 작은 limit인 soft limit으로 resource가 제한된다.

 ```bash
 ulimit -n # 혹은 ulimit -Sn
 ```

다음은 hard limit을 확인한다.

 ```bash
 ulimit -Hn
 ```

필요하다면 hard limit 보다 작은 값으로 soft limit을 변경한다.

 ```bash
 ulimit -n 99999
 ```

hard limit 보다 큰 값으로 soft limit을 변경하려고 하면 에러가 발생한다.


## file open 확인하기

limit을 확인했다면, 어떤 process가 file open을 많이하는지 확인할 필요가 있다.  
limit이 작고 실제 file open을 많이 하는 케이스도 있겠지만 대부분은 close가 제대로 되지 않으면서 발생하는 케이스가 많다.
어떤 process가 어떤 file을 open 하는지를 보면 이런 이슈를 분리할 수 있다.  
정상적인 케이스라면 limit을 늘리면 될 것이고, 그렇지 않다면 버그를 수정하면 된다.

### 1. file nr

 ```bash
 cat /proc/sys/fs/file-nr
 ```

file-nr은 3개의 숫자를 갖는다. 순서대로 그 의미는
1. 할당된 file handles 수
2. 할당 되었지만 사용되지 않은 file handles 수
3. 최대 file handles 수


 ```bash
 cat /proc/sys/fs/file-nr && date
 ```

위 명령어를 주기적으로 호출해보면서 file-nr에서 보이는 file 할당 수가 시간이 지날수록 계속 증가한다면 file close가 잘 안되고 있는 것이라고 추정할 수 있다.  
date와 함께 남기면 시간 별로 file-nr을 추적하기 용이하다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
참고사항
{: .label .label-green}  

file-nr의 마지막 값인 최대 file hadles 수는 **cat /proc/sys/fs/file-max**와도 같은 값이다.  
이 값과 **ulimit -Hn**는 다르다.  
**file-max는 linux 시스템에서 열 수 있는 File descriptor의 최대 수에 대한 설정 값**으로 시스템 전체와 모든 프로세스에 적용된다.  
반면 **ulimit은 사용자나 프로세스 수준의 File descsriptor 제한**을 설정한다.
</div>


### 2. lsof

lsof는 **list open files 명령어**로 open file을 확인할 수 있다.  
여기서 pid를 통해 특정 process의 open file을 체크할 수 있다.

 ```bash
 lsof -p 1234567 # 1234567은 pid로, ps -ef를 통해 이슈가 발생한 pid를 찾아야한다.
 lsof -p 1234567|wc -l && date
 ```

lsof를 통해 어떤 process가 open file 이슈를 만드는지 그리고 어떤 파일에 대한 open이 계속 남아있고, 증가하는지를 확인할 수 있다.  
위와 동일하게 date를 통해 기록을 남기며 특정 process가 이슈를 만드는지 체크할 수 있다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  

```bash
lsof -p 1234567
```

 ```
 COMMAND    PID USER   FD      TYPE             DEVICE SIZE/OFF     NODE NAME    
 app-test- 1234567 user  181r      REG      259,1          2    4392717 /app/test/config.property
 app-test- 1234567 user  182r      REG      259,1          2    4392717 /app/test/config.property
 app-test- 1234567 user  183r      REG      259,1          2    4392717 /app/test/config.property
 app-test- 1234567 user  184r      REG      259,1          2    4392717 /app/test/config.property
 app-test- 1234567 user  185r      REG      259,1          2    4392717 /app/test/config.property
 app-test- 1234567 user  186r      REG      259,1          2    4392717 /app/test/config.property
 app-test- 1234567 user  187r      REG      259,1          2    4392717 /app/test/config.property
 ```

이번에 내가 겪은 이슈의 `lsof` 결과이다. 동일한 파일인 **config.property**에 대해 open이 반복되고 있었고, close 없이 계속해서 open file 수가 증가했다.  
**FD**는 File Descriptor의 약자로 181r의 r은 read file이라는 표현이다.  

지금 상황은 config.property를 주기적으로 open하고 close 하지 않는 것으로 분석할 수 있다.
</div>


## 이슈 처리

이런경우 대부분의 이슈는 반복문 안에서 open file에 대한 close가 의도한대로 동작하지 않아서 발생한다.    
이슈 수정 후에 다시 수행하면서 위와 동일한 로직으로 open file이 증가하지 않는 것을 확인할 수 있다.

이번엔 golang에서 만든 코드가 for loop안에 defer close를 잘못 사용하여 발생한 이슈로 close를 적절하게 변경하여 해결했다.

## reference

- https://docs.kernel.org/admin-guide/sysctl/fs.html#file-max-file-nr
- https://www.baeldung.com/linux/error-too-many-open-files
- https://www.baeldung.com/linux/soft-limit-hard-limit
