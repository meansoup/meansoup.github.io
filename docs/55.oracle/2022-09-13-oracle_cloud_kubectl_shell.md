---
layout: post
title: OCI cloud shell에서 kubectl 설정하기
parent: oci
permalink: /docs/oci/kubectl_shell
sitemap:
  lastmod: 2022-09-13
---

## 설정하기

**oci ce cluster create-kubeconfig**을 통해 cloud shell이 kubectl을 통해 접근할 수 있는 config를 setup한다.  
oci는 낯선데 당연히 aws cli 같은 역할을 하겠지.

`oci ce cluster create-kubeconfig --cluster-id {clusterId} --file $HOME/.kube/config --region ap-seoul-1 --token-version 2.0.0`
- 이 명령어를 cloud shell에 치면 된다.
- clusterId는 oracle console에서 확인
- region은 cluster가 있는 region


## 수행

```sh
userId@cloudshell:~ (ap-seoul-1)$ oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.oc1.ap-seoul-1..... --file $HOME/.kube/config --region ap-seoul-1 --token-version 2.0.0
New config written to the Kubeconfig file /home/userId/.kube/config
```

이후에 kubectl이 잘 동작한다.

### reference

- https://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-cloudshell/index.html