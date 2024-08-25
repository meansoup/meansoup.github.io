---
layout: post
title: What is HATEOAS? Why and when using HATEOAS, and issues when not in use
sidebar_label: HATEOAS
parent: APIs
lang: en
nav_order: 1
permalink: /docs/apis/rest/hateoas
sitemap:
  lastmod: 2024-08-25
---

HATEOAS is one of the design principles of RESTful web services, which makes RESTful APIs self-descriptive, simplifying and enhancing the scalability of interactions between clients and servers.

HATEOAS stands for '**H**ypermedia **a**s **t**he **E**ngine **o**f **A**pplication **S**tate,' which is the principle of using hypermedia to dynamically interact between the server and the client.  
HATEOAS provides hypermedia links related to the resource in the API response, allowing the next actions to be determined dynamically based on the provided hypermedia.

To understand why HATEOAS is used, let's look at the issues that arise when HATEOAS is not used.  
For comparison, we'll use the example of implementing GitHub's repository retrieval API.

The key is **how the data is delivered when other data** is needed in one api.

* [non-HATEOAS](#non-hateoas)
  1. [When the server fills in and returns the data](#1-when-the-server-fills-in-and-returns-the-data)
  2. [When using APIs with predetermined data for the client](#2-when-using-apis-with-predetermined-data-for-the-client)
* [HATEOAS](#hateoas)

## non-HATEOAS

### 1. When the server fills in and returns the data

When retrieving a repository and additional information about a user is needed, the user's detailed information is added to the repository retrieval API.  
The client starts by receiving small user information related to the repository. 
However, over time, the requirements change and data that is not related to the repository query is returned.

As these requirements accumulate, the repository retrieval API might evolve into an API that returns multiple pieces of information beyond just repository retrieval.

#### Issues

- The API performs more than its intended function.
- The API becomes harder to understand.
- The server has to consider various exceptions for multiple domain concepts to support the API.
- The server cannot determine which values in the API are being used by the client.
- When supporting multiple clients, there may be several APIs that provide similar functions.

### 2. When using APIs with predetermined data for the client

To retrieve a repository and then additional information about a user, the client calls the predetermined API. It might be called as **get user api**.  
The process involves calling the predetermined user information retrieval API using the user ID obtained from the repository.

The client must hardcode the API endpoint.  
The client becomes the subject of managing endpoints and relies on endpoints.

#### Issues

- A strong coupling between the client and server emerges due to the endpoint.
- The coupling resulting from the client's endpoint makes server API changes more difficult.
- If the server updates the API version, client modifications are required.
- There is a need to share and explain the API with the client.
- When supporting multiple clients, there is an overhead in explaining the API to each client.

## HATEOAS

[GitHub's Get Repository Example](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository)

```json
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  }
}
```

Referring to GitHub's API, when retrieving a repository, the response includes hypermedia URLs that allow access to the other resource.  
Even without checking the GitHub API specification, the concise response makes it clear what is included.  
If each of the owner's resources is needed, further retrieval can be made via the hypermedia URLs provided in the response.

Each **API's provided resources and roles become clearer**, and in this way, **HATEOAS can serve as self-descriptive API documentation**.

Between the client and the server, there is only a minimal agreement on which field's link the client must check to determine the desired state.  
The client interacts by following the links provided by the server to retrieve the necessary resources.  
As a result, **the coupling between the client and server is minimized**, and **the server can change the API independently of the client**.

The downside is that network overhead may occur as the client follows links to check the state.

