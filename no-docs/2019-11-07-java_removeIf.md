<!-- ---
layout: post
title: ArrayList.removeIf() in Java
tag:
  - java
---

얼마전 회사에서 ArrayList를 수정할 일이 생겼다.  
복잡한 멤버변수들을 갖는 ArrayList 였는데, 그 중 일부의 값을 사용해서 ArrayList에서 값들을 지워야했다.  
iterator를 쓰자니 지저분하여 iterator를 처리하는 별도의 함수를 만들어주어야 하는 상황이었다. (애초부터 난 iterator가 싫었다.)  
한 줄로 삭제할 수 있으면 정말 좋겠다고 생각하면서 [ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)를 살펴보던 중 `removeIf()`를 발견했다.

예제를 만들어 테스트해보면 아래와 같다.

## #1 iterator
전형적으로 사용해오던 arrayList 핸들링을 위한 iterator.  
iterator는 어떻게 써도, while - hasNext - next에서 기존 코드의 논리와 바로 연결되기 어려운 것 같다. 그래서 라인 수가 많아지는걸 제외해도 괜히 더 쓰기 싫다.

## #2 removeIf
논리적으로 이전 코드들과 바로 연결되고, 깔끔하고, 아름다운 코드.

## #3 removeIf (with out lambda)
이렇게 쓸 일은 단연코 없을건데, lambda 식이 source Insight의 코드매핑이 되지 않는다는 책임님의 요구에.. lambda 식을 없애는 removeIf를 만들어 보았다.  
여기서 중요한 점은 Predicate는 `test()`라는 method를 가지고, removeIf는 그걸 실행하는 방식이라는 것?  
막상 test라는 함수 명이 논리적으로 이어지지 않아 사용하고 싶지 않았고, 결국 `#2`의 코드를 사용하였다.

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.function.Predicate;

public class test {
    public static void main(String arg[]) {
        ArrayList<Complecate> list = new ArrayList<>();
        list.add(new Complecate("kim", "koo", 1, 1));
        list.add(new Complecate("kim", "hee", 1, 2));
        list.add(new Complecate("lee", "mia", 2, 1));
        list.add(new Complecate("lee", "hee", 2, 2));
        list.add(new Complecate("bae", "min", 3, 1));

        System.out.println("before: " + list);

// #1
        // Iterator<Complecate> it = list.iterator();
        // while (it.hasNext()) {
        //     Complecate c = it.next();
        //     if ("kim".equals(c.mStr1)) {
        //         it.remove();
        //     }
        // }

// #2
        list.removeIf(c -> "kim".equals(c.mStr1));
// #3
        // list.removeIf(new Predicate<Complecate>() {
        //     @Override
        //     public boolean test(Complecate c) {
        //         return "kim".equals(c.mStr1);
        //     }
        // });

        System.out.println("after : " + list);
    }
}

class Complecate {
    public String mStr1, mStr2;
    public int mInt1, mInt2;

    public Complecate(String s1, String s2, int i1, int i2) {
        mStr1 = s1;
        mStr2 = s2;
        mInt1 = i1;
        mInt2 = i2;
    }

    public String toString() {
        return "[s1:" + mStr1 + " s2: " + mStr2 + " i1: " + mInt1 + " i2:" + mInt2 + "]";
    }
}
```

-----
## 참고
- [ArrayList.removeIf()](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html#removeIf-java.util.function.Predicate-) - removeIf는 Predicate를 인자로 받음.  
- [Predicate](https://docs.oracle.com/javase/8/docs/api/java/util/function/Predicate.html) - Predicate는 `test()`를 functional method로 하는 functional interface. -->