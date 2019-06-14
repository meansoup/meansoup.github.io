---
layout: normal
title: JIT(Just In Time compiler)
---

인터프리터와 컴파일러 언어의 장점을 살려 조합한 방식으로 run time에 바로바로 컴파일하는 방식.  
code를 caching하여 같은 함수가 여러 번 불릴 때 매번 native code가 생성되는 것을 방지하여 성능을 개선.  
`JVM, .NET, V8, PyPy ...`등에서 사용 됨.  

* JVM:  
  컴파일러에서 source code를 byte code로 변환하고, JIT에서 byte code를 native code로 변환.

* C?  
  C는 native language(os 종속적)로, compiler를 통해 바로 native code로 변환되어 java와 다름.  

참조:  
  https://aboullaite.me/understanding-jit-compiler-just-in-time-compiler/  
  https://namu.wiki/w/JIT