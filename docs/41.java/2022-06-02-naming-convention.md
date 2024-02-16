---
layout: post
title: "Java naming convention (Google / MS / Oracle)"
sidebar_label: "Java naming convention (Google / MS / Oracle)"
parent: Java
permalink: /docs/java/naming-convention
sitemap:
  lastmod: 2022-06-02
---

naming은 당연히 class/property/method를 떠나서 명확하고 단순해야 한다.  
최근 naming으로 작은 논란? 이 있었던 적이 있었다.  
naming은 *꼭 이래야 한다.* 라는게 없기 때문에 논란이 생기면 사람마다 생각이 달라 정리하기가 어렵다.  
convention을 명확하게 하기 위해 **주요 회사들의 naming convention**을 정리해보았다.

참고로 내가 우리 팀에서 걸렸던 부분은 [약어 convention](#약어-규칙)이고,  
이걸 정리해서 우리 팀 약어는 여기 정리된 규칙에 맞게 바뀌었다.

### Package

- package에는 소문자와 숫자만 사용한다. *(Google)*
  - com.example.deepspace 가능
  - com.example.deepSpace, com.example.deep_space 불가능

### Class

- class name은 명사거나 명사구여야 한다. *(W3 / Oracle / Google)*
- class name의 첫 글자는 대문자여야 한다. UpperCamelCase *(W3 / Oracle / Google)*
- class name은 **Every member of this class is a(n) <class name>**을 만족해야 한다. *(W3)*

### property

- property의 첫 글자는 소문자여야 한다. lowerCamelCase *(W3 / Google)*
- property는 명사거나 명사구여야 한다. *(W3 / Google)*

### Method

- method는 동사거나 동사구여야 한다. *(Oracle / Google)*
- method의 첫 글자는 소문자여야 한다. lowerCamelCase *(Oracle / Google)*

### Constant

- **_** 로 구분된 단어로 모두 대문자여야 한다. *(Oracle / Google)*

### Test

- test class는 Test라는 postfix로 끝난다 *(Google)*

### 공통 규칙

- 내부에서 여러 단어가 사용될 때 각 단어의 첫 글자는 대문자여야 한다. *(Oracle / Google)*

- 의미없는 prefix, postfix를 사용하지 않는다. *(Google)*
  - name_, mName, s_name, kName

#### 약어 규칙

- 약어가 full name보다 대중적이고 더 잘 이해되는 단어가 아닌 이상 전체 단어를 사용해야 한다. *(W3 / MS)*
  - 예를 들면 **ID**, **IP**, **XML**, **JSON**는 약어를 사용한다.
  - 예를 들면 Window 대신 Win을 사용해선 안된다.
- 약어를 사용할 때도 동일하게 camelCase를 적용한다. *(MS)*
  - 예를 들면 **USUUIDIP**와 같은 naming을 해야할 때, **usUuidIp**가 맞다는 말이다.
  - 이는 **Id** 처럼 하나의 약어만 사용할 때도 마찬가지.
  - 이유는 몇 가지가 있는데 대표적으론 이렇다.
    - 1. 가독성이 훨씬 좋다.
    - 2. AB, CDE, ABC, DE 와 같은 약어가 있을 때, ABCDE는 어떤 약어인지 구분할 수 없다.


### Reference

- https://www.w3.org/2005/rules/wg/wiki/Arch/Naming_Conventions
- https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html
- https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-1.1/141e06ef(v=vs.71)?redirectedfrom=MSDN
  - 이건 Java는 아니지만 naming rule에는 참고할 만한 것.
- https://google.github.io/styleguide/javaguide.html#s5-naming