---
layout: post
title: OKE docker registry github action 적용하기
parent: oci
permalink: /docs/oci/docker-login
---

## docker login github action

우선 docker에서 제공하는 github action이 있다.  
**docker/login-action**을 사용하면 굉장히 쉽게 container registry에 접근할 수 있다.  

그런데 나는 oracle에서 이게 잘 안됐고, 다음엔 안까먹기 위해 정리해본다.  
여기서 의미하는 여러 value들에 대한 정의가 나한테는 명확하지 않았고 리소스도 많지 않았다.

```yml
    - name: Login to Oracle Container Registry
    uses: docker/login-action@v2
    with:
        registry: icn.ocir.io
        username: ${{ secrets.OCI_DOCKER_NAME }}
        password: ${{ secrets.OCI_AUTH_TOKEN }}
```

### icn.ocir.io:  

**icn**의 자리는 region name이다.  
region name은 reference에 명시한 url에서 확인할 수 있다.  
한국은 icn.

### OCI_DOCKER_NAME:  

여기서 OCI_DOCKER_NAME은 `<tenancy-namespace>/<username>`

tenancy-namespace는 oracle에서 관리하는 tenancy의 id를 가리킨다.  
**Profile > Tenancy > Object storage namespace** 에서 확인 가능.  
- 나는 cn********ev (12자리)

username은 email 형식의 계정이다.
- 나는 ~@gmail.com

그래서 DOCER_NAME은
- 나는 cn********ev/~@gmail.com
- 혹은 cn********ev/oracleidentitycloudservice/~@gmail.com 이기도 하다는데 난 잘 안됐다.

### OCI_AUTH_TOKEN:  

OCI_AUTH_TOKEN은 oracle cloud에서 발급한 토큰을 말한다.  
**Profile > My profile > Auth tokens** 에서 발급 가능.  
- 당연히 발급받은 토큰은 발급 시점에만 key를 확인할 수 있다.
- 발급 시에 복사해두고, 그렇지 못했다면 재발급.

### 확인 추천

1. 우선 아래 reference 처럼 docker login을 cmd에서 해본다.  
2. git action에서 key를 yml에 명시해서 해본다.
3. key를 secrets로 넣어서 해본다.

git action에서 그냥 하려다가 몇 번 실패하면 스트레스가 이만 저만이 아니다.

### reference

- https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionslogintoocir.htm
- https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability