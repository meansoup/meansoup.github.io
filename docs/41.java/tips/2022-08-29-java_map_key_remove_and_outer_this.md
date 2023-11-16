---
layout: post
title: map key로 쉽게 remove 하는 trick과 outer.this 하기
parent: Java Tips
grand_parent: Java
permalink: /docs/java/tip/java_map_key_remove_and_outer_this
sitemap:
  lastmod: 2022-08-29
---

오늘 일하는데 hashmap에서 key들을 받아서 map의 entry를 지우는 코드가 굉장히 지저분했다.  
iterator로 entry를 받아서 조건에 맞는다면 remove.  
그런데 이런 remove가 지저분하게 여러개.

이 코드를 고치기 위해 방법을 찾다가 재밌는 코드를 발견했다.  

## remove multiple keys from map efficiently

효율적으로 그리고 깔끔하게 key들로 map을 지워내기.

```java
map.keySet().remove(key);
map.keySet().removeIf(key -> key.startsWith(prefix));
```

keySet은 map과 연결되어 keySet에서만 지워도 map이 지워진다는 것이다.
흥미롭다. 어떻게 이게 가능할까.


## HashMap과 HashMap.keySet 코드 분석

```java

public class HashMap<K,V> extends AbstractMap<K,V> implements Map<K,V>, Cloneable, Serializable {

    public Set<K> keySet() {
        Set<K> ks = keySet;
        if (ks == null) {
            ks = new KeySet();
            keySet = ks;
        }
        return ks;
    }

    final class KeySet extends AbstractSet<K> {
        public final int size()                 { return size; }
        public final void clear()               { HashMap.this.clear(); }
        public final Iterator<K> iterator()     { return new KeyIterator(); }
        public final boolean contains(Object o) { return containsKey(o); }
        public final boolean remove(Object key) {
            return removeNode(hash(key), key, null, false, true) != null;
        }
        public final Spliterator<K> spliterator() {
            return new KeySpliterator<>(HashMap.this, 0, -1, 0, 0);
        }
        public final void forEach(Consumer<? super K> action) {
            Node<K,V>[] tab;
            if (action == null)
                throw new NullPointerException();
            if (size > 0 && (tab = table) != null) {
                int mc = modCount;
                for (Node<K,V> e : tab) {
                    for (; e != null; e = e.next)
                        action.accept(e.key);
                }
                if (modCount != mc)
                    throw new ConcurrentModificationException();
            }
        }
    }
}
```

HashMap 코드 내부에 위치한 keySet 코드이다.  
흥미로운건 size, iterator, contains 등 모든 반환 값은 HashMap의 함수나 값을 쓰고 있다는 것.  
그리고 HashMap.this.clear() 와 같은 코드.  

**확인할 포인트:**  
- 우선 keySet은 HashMap과 별개라고 생각했는데 keySet이 생성된 이후에도 HashMap을 자유롭게 접근할 수 있다는 점에서 놀랐다. 이게 static도 아닌데 접근이 되서 놀랐는데 덕분에 java에 대한 이해도가 늘었다.
- HashMap.this 코드가 이해가 안됐다. static도 아니고 이렇게 쓴다니. 이거에 대해선 아래에 다룬다.
- inner class를 가장 효율적으로 짜는 아주 좋은 예시 코드인 것 같다. 가끔 개발에 쓸 수 있을 것 같다.

 
## java parent.this 하기

HashMap.this에 대해 이해가 되지 않아서 찾아봤다.  
keySet이 HashMap의 값을 사용할 수 있는 것을 아우르는 중요한 개념이 있다.  

non static inner class는 outer class에 대한 참조를 갖는다.  
그리고 outer class name과 this를 함께 사용하면 이 참조를 얻을 수 있다.  

요긴하게 쓰일 수 있는 개념이자 팁.  
좀 더 이해하기 쉬운 예시를 첨부한다. 

```java
public class Outer {
     class Inner {
         public Inner inner() {
             return this;
         }
 
         public Outer outer() {
             return Outer.this;
         }
     }
 }
```

## 결론

그래서 keySet을 사용해서 하는 모든 remove 연산은 실제 hashMap에 영향을 미친다.  
이게 미치는 과정이 흥미롭고 배울점이 많다.


### reference

multiple keys로 map remove 하기
- https://stackoverflow.com/questions/17675804/remove-multiple-keys-from-map-in-efficient-way

hashmap.this에 대한 설명
- https://stackoverflow.com/questions/16999611/hashmap-this-clear-what-does-this-mean-how-does-this-work