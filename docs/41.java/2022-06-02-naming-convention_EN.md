---
layout: post
title: "Java naming convention & Abbreviations rules with Google, MS, Oracle" 
sidebar_label: "Java naming convention"
parent: Java
lang: en
permalink: /docs/java/naming-conventions
sitemap:
  lastmod: 2024-05-18
---

Naming conventions should be clear and straightforward, regardless of class, variable, or method.  
If there are no rules for naming within the team, there is a high possibility of a dispute over naming, and other team members may have different opinions, making it difficult to find an agreement.

Recently, there has been a debate in our team about abbreviation conventions.  
In order to organize different thoughts, I organized naming conventions of companies such as Google, ms, oracle.  
Ultimately, our team defined naming rules based on the compiled abbreviation conventions.

### Package

- Only lowercase letters and numbers are allowed in packages. *(Oracle / Google)*   
  ✔️ com.example.deepspace  
  ⚠️ com.example.deepSpace  
  ⚠️ com.example.deep_space

### Class

- Class names should be nouns or noun phrases. *(W3 / Oracle / Google)*  
  ✔️ SpaceShip  
  ⚠️ launchSpaceship
- The first letter of the class name should be capitalized. UpperCamelCase *(W3 / Oracle / Google)*  
  ✔️ SpaceShip  
  ⚠️ spaceship  
  ⚠️ spaceShip


### Variable

- Variables should be in <u>lowerCamelCase</u>[^1]. *(W3 / Google / Oracle)*  
  ✔️ speed  
  ⚠️ Speed  
  ⚠️ SPEED
- Variables should be nouns or noun phrases. *(W3 / Google)*  
  ✔️ fuelLevel  
  ⚠️ calculateFuel
- Single-letter variables are not allowed except for temporary variables. *(Oracle)*  
  ✔️ point  
  ⚠️ p

### Method

- Methods should be verbs or verb phrases. *(Oracle / Google)*  
  ✔️ calculateDistance  
  ⚠️ distance
- Methods should be in <u>lowerCamelCase</u>[^1]. *(Oracle / Google)*  
  ✔️ calculateDistance  
  ⚠️ CalculateDistance  
  ⚠️ calculate_distance

### Constant

- Constants should be all uppercase with words separated by **_**. *(Oracle / Google)*  
  ✔️ MAX_SPEED  
  ⚠️ MaxSpeed  
  ⚠️ max_speed

### Test

- Test class names should end with the postfix "Test". *(Google)*  
  ✔️ CalculatorTest  
  ⚠️ TestCalculator

### Common Rules

- The first letter of each word should be capitalized when multiple words are used internally. *(Oracle / Google)*  
  ✔️ DeepSpaceMissionControlCenter  
  ⚠️ deepspacemissioncontrolcenter  
  ⚠️ deep_space_mission_control_center

- Meaningless prefixes and postfixes should not be used. *(Google)*  
  ✔️ name    
  ⚠️ name_  
  ⚠️ mName

### Abbreviation Conventions

- Full words should be used instead of abbreviations unless the abbreviation is more common and easily understood. *(W3 / MS)*
- Even when using abbreviations, <u>CamelCase</u>[^2] should be applied. *(MS)*
  - For example, when creating a variable named **UUIDIP**, **uuidIp** is correct, and this applies even when using a single abbreviation like **Id**.
  - The reason for applying camelCase even to abbreviations is primarily because:
    1. It greatly enhances **readability**.
    2. Abbreviations are not confused. (For example, with abbreviations such as AB, CDE, ABC, DE, when there is ABCDE, it is unclear which abbreviation it is.)

  ✔️ JSON  
  ⚠️ ID -> ️✔️ Id    
  ⚠️ Win -> ️✔️ Window    
  ⚠️ UUIDIPJSON -> ️✔️ UuidIpJson  
  ⚠️ ABCDE -> ️✔️ AbcDe  
  ⚠️ ABCDE -> ️✔️ AbCde

### Reference

- [W3 Naming Conventions](https://www.w3.org/2005/rules/wg/wiki/Arch/Naming_Conventions)
- [Oracle Naming Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html)
- [Microsoft Naming Conventions](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-1.1/141e06ef(v=vs.71)?redirectedfrom=MSDN)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html#s5-naming)

---
[^1]: Unlike CamelCase, lowerCamelCase starts with a lowercase letter. The first letter of each subsequent word is capitalized.  
[^2]: CamelCase is a naming convention that mimics the humps of a camel, capitalizing the first letter of each word in a multi-word phrase.  
