---
layout: post
title: A website that arbitrarily receives Requests for verification
sidebar_label: webhook site
parent: website
lang: en
permalink: /docs/tools/website/webhook-site
grand_parent: Tools
sitemap:
  lastmod: 2024-09-01
---

There is a website that issues a server URL that arbitrarily receives the requested requests.  
When you send a request to this URL, it analyzes whether the request was received correctly and how it was received.

When starting development without proper infrastructure, identifying issues becomes much more challenging.

- Is there a problem on the client side?
- Is there an issue on the server side?
- Is the server running properly?
- Is there a problem with gateway registration?
- Are there any infra-related permission issues?

When you have to start by checking if **the server is not working**, there are too many things to verify at the beginning.

For a server developere, there are cases where test clients written for acceptance or scenario tests do not properly reach the server (either local or dev).

This time, I wanted to verify if the multi-part request call I made was correct, and while searching for a way to confirm this, I discovered this website.

## How to Use

- Visit [https://webhook.site/](https://webhook.site/).
- On the site, you will be provided with a randomly generated webhook URL.
  - For example: `https://webhook.site/554e2d76-a7ee-46c3-8f9f-ce6819fbcedf`
- Send your test request to this host.
- Review the analyzed call on the webpage.
