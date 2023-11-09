---
layout: post
title: GraphQL 쿼리
parent: GraphQL
grand_parent: APIs
nav_order: 2
permalink: /docs/apis/graphql/graphql_query
---

## 작성중!



GraphQL이 발표되기 45년 전에 IBM 직원인 Edgar M. Codd가 **A Relational Model Data for Large Shared Database**라는 논문을 발표했다.  
**Structured English Query Language**라고 불리는 SEQUEL은 나중에 **SQL**이라고 불리게 된다.  

SQL은 데이터베이스에 접근하여 데이터를 관리하거나 조작하는데 사용한다.  
쿼리문 한 줄로 여러 데이터 테이블에서 데이터 추출이 가능하다.  
그렇지만 사실 SQL의 명령어는 SELECT, INSERT, UPDATE, DELETE로 한정되어 있다.  
- 사실 이거면 다 되는거 아닌가 싶기도 하지만?

이런 SQL의 CRUD 철학은 REST에 영향을 주었고,  
REST는 CRUD에 따라 GET, POST, PUT, DELETE의 http method를 사용했다.  
하지만 실제 데이터 변경에는 endpoint url을 사용해야하고 실제 query는 사용할 수 없었다.  

앞서 말했듯 GraphQL은 query 개념을 가져다가 적용한 것이다.

## data type

GraphQL은 SQL과 구문이 다르다.  
SQL의 **SELECT** 역할을 하는 것이 GraphQL의 **Query** 이고,  
SQL의 **INSERT, UPDATE, DELETE** 역할을 하는 것이 GraphQL의 **Mutation** 이다.  

### Query

query는 받고싶은 데이터를 필드에 적어서 보낸다.  
- 이 받고 싶은 필드들을 **selection set**이라고 한다.

<div class="code-example" markdown="1" style="font-size: 0.8em">
예시
{: .label .label-yellow}  


```graphql
query {
  viewer {
    id
    url
    email
  }
}
```

예를 들면 위 query는 github graph api로 호출하는 query이다.  
1장에서 말한 것처럼 내가 필요한 값들만(id, url, email) query가 가능하다.  
여기서 viewer와 viewer의 id, url, email이 selection set이다.

그렇다면 결과는
```json
{
  "data": {
    "viewer": {
      "id": "MDQ6VXNlcjI0MzY4NTUy",
      "email": "",
      "url": "https://github.com/meansoup"
    }
  }
}
```

GraphQL의 장점은 여러 데이터를 한 번에 호출할 수 있다는 것.  
예를 들면 아래와 같이 query가 가능하다는 것.  
그리고, **query arguments**로 값들을 지정해서 가져올 수 있다는 것.

```graphql
query { 
  viewer { 
    login
    id
    email
    url
  }
  repository(owner:"meansoup", name:"meansoup.github.io") {
    createdAt
    description
  }
}
```

그렇다면 결과는
```json
{
  "data": {
    "viewer": {
      "login": "meansoup",
      "id": "MDQ6VXNlcjI0MzY4NTUy",
      "email": "",
      "url": "https://github.com/meansoup"
    },
    "repository": {
      "createdAt": "2019-04-23T12:03:43Z",
      "description": null
    }
  }
}
```
</div>

### Field type

GraphQL에서 필드는 scalar type과 object type 중 하나에 속하게 된다.  

#### Scalar type

scalar type은 아래의 다섯가지 type 중 하나를 갖는다.
- Int
- Float
- String
- Boolean
- ID

Int와 Float는 json에서 숫자 타입의 데이터를 반환하고,  
String과 ID는 json에서 문자열 데이터를 반환한다.  
ID는 유일한 문자열을 반환해야한다.

위의 예시에서 id, url, email 같은 값들이 scalar type이다.  

#### Object type

object type은 type들을 그룹으로 묶어둔 것을 말한다.  
json에서 value에 key/value set이 무한히 반복될 수 있는 것처럼 object type 안에 계속 object type이 들어있을 수 있다.

위의 예시에서 viewer, repository 같은 값들이 object type이다.




ㅇㅇㅇㅇㅇ






<!-- 



query {
  viewer {
    id
    email
    following(first:2) {
      edges {
        node {
          id
          email
        }
      }
    }
    followers(first:2) {
      edges {
        node {
          id
          email
        }
      }
    }
  }
} -->



## reference

웹 앱 API 개발을 위한 GraphQL, Eve Porcello / Alex Banks  
[https://docs.github.com/en/graphql/overview/explorer](https://docs.github.com/en/graphql/overview/explorer)
[https://tech.kakao.com/2019/08/01/graphql-basic/](https://tech.kakao.com/2019/08/01/graphql-basic/)  
[https://www.apollographql.com/blog/graphql/basics/graphql-vs-rest/](https://www.apollographql.com/blog/graphql/basics/graphql-vs-rest/)  