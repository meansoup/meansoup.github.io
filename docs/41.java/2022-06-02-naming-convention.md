---
layout: post
title: "Google, MS, Oracle의 Java naming convention & 약어 convention"
sidebar_label: "Java naming convention"
parent: Java
lang: ko
permalink: /docs/java/naming-conventions
sitemap:
  lastmod: 2024-05-18
---

네이밍 규칙은 당연히 class, variable, method를 떠나서 명확하고 단순해야 한다.  
팀 내에 네이밍에 대한 룰이 정해져있지 않다면 네이밍에 대한 논란이 생기기 쉽고, 팀원마다 생각이 달라 합의를 보기 어려운 경우가 있다.

최근 우리팀에서는 약어 규칙을 어떻게 할 것인가에 대한 논란이 있었다.  
각자 다른 생각을 정리하기 위해 여러 기업들의 naming convention을 같이 정리해보았다.  

결국 우리 팀은 정리된 약어 규칙을 기반으로 네이밍 룰을 정의했다.


### Package

- package에는 소문자와 숫자만 사용한다. *(Oracle / Google)*   
  ✔️ com.example.deepspace  
  ⚠️ com.example.deepSpace  
  ⚠️ com.example.deep_space  

### Class

- class name은 명사거나 명사구여야 한다. *(W3 / Oracle / Google)*  
  ✔️ SpaceShip  
  ⚠️ launchSpaceship  
- class name의 첫 글자는 대문자여야 한다. UpperCamelCase *(W3 / Oracle / Google)*  
  ✔️ SpaceShip  
  ⚠️ spaceship  
  ⚠️ spaceShip  


### variable

- variable은 <u>lowerCamelCase</u>[^1]이어야 한다.  *(W3 / Google / Oracle)*  
  ✔️ speed  
  ⚠️ Speed  
  ⚠️ SPEED  
- variable는 명사거나 명사구여야 한다. *(W3 / Google)*  
  ✔️ fuelLevel  
  ⚠️ calculateFuel  
- 임시 변수를 제외하고는 한 문자 변수는 안된다. *(Oracle)*  
  ✔️ point  
  ⚠️ p

### Method

- method는 동사거나 동사구여야 한다. *(Oracle / Google)*  
  ✔️ calculateDistance  
  ⚠️ distance  
- method은 <u>lowerCamelCase</u>[^1]이어야 한다. *(Oracle / Google)*  
  ✔️ calculateDistance  
  ⚠️ CalculateDistance  
  ⚠️ calculate_distance  

### Constant

- **_** 로 구분된 단어로 모두 대문자여야 한다. *(Oracle / Google)*  
  ✔️ MAX_SPEED  
  ⚠️ MaxSpeed  
  ⚠️ max_speed  

### Test

- test class는 Test라는 postfix로 끝난다 *(Google)*  
  ✔️ CalculatorTest  
  ⚠️ TestCalculator

### 공통 규칙

- 내부에서 여러 단어가 사용될 때 각 단어의 첫 글자는 대문자여야 한다. *(Oracle / Google)*  
  ✔️ DeepSpaceMissionControlCenter  
  ⚠️ deepspacemissioncontrolcenter  
  ⚠️ deep_space_mission_control_center

- 의미없는 prefix, postfix를 사용하지 않는다. *(Google)*  
  ✔️ name    
  ⚠️ name_  
  ⚠️ mName  

### 약어 규칙

- 약어가 full name보다 대중적이고 더 잘 이해되는 단어가 아닌 이상 전체 단어를 사용해야 한다. *(W3 / MS)*  
- 약어를 사용할 때도 동일하게 <u>CamelCase</u>[^2]를 적용해야한다. *(MS)*
  - 예를 들면 **UUIDIP**라는 변수를 생성할 때, **uuidIp**가 맞고, 이는 **Id** 처럼 하나의 약어만 사용할 때도 마찬가지다.
  - 약어도 camelCase를 적용하는 이유는 대표적으로
    1. **가독성**이 훨씬 좋다.
    2. 약어를 혼동하지 않을 수 있다. (AB, CDE, ABC, DE 와 같은 약어가 있을 때, ABCDE는 어떤 약어인지 알 수 없다)  

  ✔️ JSON  
  ⚠️ ID -> ️✔️ Id    
  ⚠️ Win -> ️✔️ Window    
  ⚠️ UUIDIPJSON -> ️✔️ UuidIpJson  
  ⚠️ ABCDE -> ️✔️ AbcDe  
  ⚠️ ABCDE -> ️✔️ AbCde  


### Reference

- https://www.w3.org/2005/rules/wg/wiki/Arch/Naming_Conventions
- https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html
- https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-1.1/141e06ef(v=vs.71)?redirectedfrom=MSDN
- https://google.github.io/styleguide/javaguide.html#s5-naming

---

[^1]: CamelCase와 달리 lowerCamelCase는 첫 문자는 소문자로 시작한다. 그 이후의 단어의 첫 문자는 대문자가 된다.
[^2]: CamelCase는 낙타의 등 모양을 본따서 지어진 이름으로 여러 단어가 합쳐진 경우 각 단어의 첫 글자를 대문자로 표기하는 기법이다.  
