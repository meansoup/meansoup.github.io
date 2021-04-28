---
layout: post
title: "[OmitStackTraceInFastThrow] java stacktrace 안남는 문제 해결"
tag:
  - java
  - jvm
---

java에서 NullPointException(NPE) 발생 시 stackTrace가 남지 않는 문제가 발생했다.  
흥미로운건 local test에서는 stackTrace가 남고, 실제 서버에서는 남지 않는다는 점이었다.  

이는 **JVM의 최적화 옵션** 때문인데, JVM에서는 최적화와 log 관리를 위해 stack trace를 관리한다.  
exception이 발생하면 full stack trace를 출력하고 이걸 저장했다가 같은 stack trace가 여러번 반복될 때 출력하지 않도록 한다.

처음만 출력하는 것은 아니고, 충분히 반복된 이후부터 stack trace 출력을 멈춘다.  
그렇기 때문에 local에서 띄운 경우 stack이 남고, 실제 서버에서는 이미 충분히 stack trace가 찍힌 후 이후의 exception이 남지 않고 있던 것.

이런 문제를 해결하기 위해 java 실행 시 `-XX:-OmitStackTraceInFastThrow` 옵션을 넣어주면 모든 경우에 대해 최적화 없이 stackTrace를 남길 수 있도록 한다.
- 최적화를 푸는게 맞는지는 모르겠다. 잘 준비된 서비스라면 처음 stackTrace의 에러가 발생했을 때 alert를 받고 바로 수정이 될 수 있는 구조여야지.

## 테스트
테스트 코드를 보고 돌려보면 이해가 잘된다.

```java
// test.java
public class test {
    public static void main(String[] args) {
        String string = null;
        int i = 0;
        while (i <= 13000) {
            i++;
            try {
                toStr(string);
            } catch (Exception e) {
                // if (i==1 || i == 13000) 
                e.printStackTrace();
            }
        }
    }

    private static void toStr(String obj) {
        obj.split("a");
    }

}
```

### stackTrace가 안남는 것 확인하기

1. javac test.java
2. java test
3. print 결과를 보면 trace가 쭉 남다가 어느 순간부터 안남는 것 확인

### stackTrace가 남도록 option 설정

1. javac test.java
2. java -XX:-OmitStackTraceInFastThrow test
3. 위와 다르게 끝까지 stackTrace가 남는 것 확인


## 참고

- [stackoverflow](https://stackoverflow.com/questions/2411487/nullpointerexception-in-java-with-no-stacktrace)
- [oracle tech](https://www.oracle.com/java/technologies/javase/release-notes-introduction.html#hotspot)