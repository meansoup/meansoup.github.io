---
layout: post
title: "[jekyll] Dependency Error, Jekyll::Errors::MissingDependencyException"
parent: error & bug
permalink: /docs/error-bug/kotlin/jekyll-cannot-load-such-file
sitemap:
   lastmod: 2022-01-31
---

Dependency 추가 후 jekyll local build 중 에러가 발생했다.  

## 빌드 에러 메세지

```
Dependency Error: Yikes! It looks like you don't have jekyll-sitemap or one of its dependencies installed. In order to use Jekyll as currently configured, you'll need to install this gem. If you've run Jekyll with `bundle exec`, ensure that you have included the jekyll-sitemap gem in your Gemfile as well. The full error message from Ruby is: 'cannot load such file -- jekyll-sitemap' If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/!
                    ------------------------------------------------
      Jekyll 4.2.1   Please append `--trace` to the `serve` command
                     for any additional information or backtrace.
                    ------------------------------------------------
Traceback (most recent call last):
        21: from C:/Ruby27-x64/bin/jekyll:23:in `<main>'
        20: from C:/Ruby27-x64/bin/jekyll:23:in `load'
        19: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/exe/jekyll:15:in `<top (required)>'
        18: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary.rb:21:in `program'
        17: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/program.rb:44:in `go'
        16: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `execute'
        15: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `each'
        14: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `block in execute'
        13: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/commands/serve.rb:86:in `block (2 levels) in init_with_program'
        12: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/command.rb:91:in `process_with_graceful_fail'
        11: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/command.rb:91:in `each'
        10: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/command.rb:91:in `block in process_with_graceful_fail'
         9: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/commands/build.rb:30:in `process'
         8: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/commands/build.rb:30:in `new'
         7: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/site.rb:36:in `initialize'
         6: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/site.rb:131:in `setup'
         5: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/plugin_manager.rb:22:in `conscientious_require'
         4: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/plugin_manager.rb:30:in `require_gems'
         3: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:57:in `require_with_graceful_fail'
         2: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:57:in `each'
         1: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:60:in `block in require_with_graceful_fail'
C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:60:in `require': cannot load such file -- jekyll-sitemap (LoadError)
        21: from C:/Ruby27-x64/bin/jekyll:23:in `<main>'
        20: from C:/Ruby27-x64/bin/jekyll:23:in `load'
        19: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/exe/jekyll:15:in `<top (required)>'
        18: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary.rb:21:in `program'
        17: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/program.rb:44:in `go'
        16: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `execute'
        15: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `each'
        14: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/mercenary-0.4.0/lib/mercenary/command.rb:221:in `block in execute'
        13: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/commands/serve.rb:86:in `block (2 levels) in init_with_program'
        12: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/command.rb:91:in `process_with_graceful_fail'
        11: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/command.rb:91:in `each'
        10: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/command.rb:91:in `block in process_with_graceful_fail'
         9: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/commands/build.rb:30:in `process'
         8: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/commands/build.rb:30:in `new'
         7: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/site.rb:36:in `initialize'
         6: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/site.rb:131:in `setup'
         5: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/plugin_manager.rb:22:in `conscientious_require'
         4: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/plugin_manager.rb:30:in `require_gems'
         3: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:57:in `require_with_graceful_fail'
         2: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:57:in `each'
         1: from C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:58:in `block in require_with_graceful_fail'
C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/jekyll-4.2.1/lib/jekyll/external.rb:73:in `rescue in block in require_with_graceful_fail': jekyll-sitemap (Jekyll::Errors::MissingDependencyException)
```

## 원인

해결이 좀 어처구니가 없다.

sitemap dependency는 이미 추가해놓았었는데 새로운 dependency 추가 후 local build로 테스트하려다가 실패했다.
sitemap은 이미 gh-pages에서 정상동작 하고 있었고..

원인을 보자면,
1. sitemap은 gemfile에 add 되어있지 않았는데 gh-pages에서 동작함. (gh-pages에서 기본적으로 가지고 있나보다)
2. 새로운 dependency를 **gemfile**과 **_config.yml**에 추가 후 빌드.
3. sitemap이 gemfile에 없어서 애러 발생.

## 해결

1. GemFile에 아래 코드 추가
   ```
    gem 'jekyll-sitemap'
   ```
2. bundle update
3. jekyll serve
4. 문제 해결
