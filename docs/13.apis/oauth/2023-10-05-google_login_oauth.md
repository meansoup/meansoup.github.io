---
layout: post
title: 구글 아이디로 로그인 구현하기
parent: OAuth
grand_parent: APIs
nav_order: 1
permalink: /docs/apis/oauth/google-login
---

사이드 프로젝트 개발 중, 로그인 기능을 고려하게 되었다.    
처음 로그인을 생각할 땐 회원가입, 로그인, 로그아웃, 회원탈퇴을 생각하면 뭔가 골치가 아팠다.  
더불어 사용자 계정과 비밀번호를 관리하는 것까지.  

회사에선 써볼일이 없는 OAuth를 적용해보기로 했다.
개념은 정리하지 않고 간단히 하자면 **네이버 아이디로 로그인**, **구글 아이디로 로그인** 같이 다른 소셜 서비스의 아이디로 로그인할 수 있는 약속을 말한다.


## 구글 로그인 서비스 생성

아래 링크에서 구글 로그인에 사용할 서비스를 생성한다.
- [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)

테스트나 소규모 서비스에 대해선 무료에 가깝다.


## flutter client 구현

```dart
import 'package:google_sign_in/google_sign_in.dart';

Future<String> signInGoogle() async {
  final GoogleSignInAccount? googleUser = await GoogleSignIn(
      clientId: '{YOUR_CLIENT_ID}.apps.googleusercontent.com'
  ).signIn();

  if (googleUser != null) {
    print('email = ${googleUser.email}');

    var snapshot = await googleUser.authentication;
    return snapshot.idToken ?? "";
  }

  return "";
}

Future<void> signOutGoogle() async {
  await GoogleSignIn(
    clientId: '{YOUR_CLIENT_ID}.apps.googleusercontent.com'
  ).signOut();
}
```

내가 이번에 사용한 frontend는 flutter.  
flutter의 코드는 위와 같은데, idToken을 받아오는 api이다.

위 코드를 실행하면 우리가 흔히 아는 구글 로그인 팝업이 뜬다.
팝업으로 구글 로그인을 하면 email을 print하고 idToken을 반환하는 코드이다.  

여기 client에서 받은 idToken을 server에 전달해서 idToken으로 server에서 google에서 확인된 token이 맞는지를 verify 한다.


## spring server 구현

```kotlin
@Service
class GoogleSignInService {

    private lateinit var verifier: GoogleIdTokenVerifier

    @PostConstruct
    fun init() {
        val httpTransport = NetHttpTransport()
        val jacksonFactory = JacksonFactory()
        verifier = GoogleIdTokenVerifier.Builder(httpTransport, jacksonFactory).build()
    }

    fun getIdToken(idToken: String) {
        val googleIdToken = verifier.verify(idToken) ?: throw UnAuthenticatedUserException(idToken)
    }
}
```

이번에 사용한 backend는 코프링.  
kotlin/java에서는 GoogleIdTokenVerifier를 사용한다.  
client에서 받은 idToken을 여기에 넣어주기만 하면 googleIdToken을 받아온다.  
googleIdToken은 우리가 필요한 여러 데이터들을 갖고 있다.
- [응답으로 내려오는 데이터 목록](https://developers.google.com/identity/openid-connect/openid-connect#authenticatingtheuser)

여기서 내가 필요한건, email, name, picture, locale 정도.  

## reference

- https://cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-introduction?hl=ko
- https://developers.google.com/identity/openid-connect/openid-connect#authenticatingtheuser
- https://developers.google.com/identity/protocols/oauth2