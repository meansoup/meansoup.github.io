---
#layout: post
#title: intellij toggle case shortcut (upper -> lower, lower -> upper)
#sidebar_label: intellij toggle case shortcut
#parent: intellij 설정하기
#grand_parent: 개발도구
#lang: en
#permalink: /docs/dev-tools/intellij/upper-case
#sitemap:
#  lastmod: 2022-06-30
---

There is a shortcut in IntelliJ that changes uppercase to lowercase and vice versa.  
This seems like a small thing, but it maximizes efficiency when used with vertical editing.  

I was trying to find and perform this shortcut on Ubuntu, but I couldn't solve the issue. So I will summarize what I did to solve it.

### How I use the shortcut for changing case

I usually use vertical editing very often.  
It is very efficient for changing getters & setters, mapping between Entities and DTOs, and creating factories. If you add a shortcut for changing case to uppercase and lowercase, it's great.

![usage](/images/post/dev-tools/intellij/toggle-case/usage.gif)

### Toggle case Shortcut

In IntelliJ, this shortcut is called as **toggle case**.  
You can change uppercase to lowercase and lowercase to uppercase using **ctrl + shift + U**.


### Issue in Ubuntu

This shortcut works on Windows and Mac, but not on Ubuntu.  
I recently found out that **ctrl + shift + U** is already used as an emoji shortcut in Ubuntu.  
This shortcut(emoji) is rarely used, so you can change or delete it.

### Fix issue in Ubuntu

1. Enter `ibus-setup` in the command
2. Go to the `Emoji tab`
3. Select the Unicode code point where `ctrl + shift + U` is set
4. Delete or move it

In my case, I deleted the corresponding code.


### reference

https://youtrack.jetbrains.codm/issue/IDEA-112533