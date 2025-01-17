---
layout: post
title: "Why unexpected DynamoSizeLimitException occur?"
sidebar_label: "DynamoSizeLimitException"
parent: DynamoDB
grand_parent: aws
lang: en
nav_order: 1000
permalink: /docs/aws/dynamo/DynamoSizeLimitException
sitemap:
  lastmod: 2021-03-08
---

I recently encountered a **DynamoSizeLimitException** error unexpectedly.  
After investigating the issue, I discovered some details that are not covered in the official AWS documentation, which I will document here.

## What is DynamoSizeLimitException

In DynamoDB, there is a size limit for items.  
When a save request is made for an item that exceeds this predefined size, DynamoDB returns a **DynamoSizeLimitException**.

Check the [AWS DynamoDB Limits](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-items), you can find the following statement:

```
The maximum item size in DynamoDB is 400 KB, which includes both attribute name binary length (UTF-8 length) and attribute value lengths (again binary length)
```

In short, a single item cannot exceed 400KB.

## DynamoSizeLimitException Occurs Under 400KB

However, a **DynamoSizeLimitException** occurred even in cases where the item size was below 400KB.  
We were already aware of DynamoDB's size limit and had implemented logic to handle cases where the size exceeds 400KB.

Even so, the **DynamoSizeLimitException** still occurred.

Upon inspecting the item, it was only about 210KB in size.  
The cause of this issue could not be found in the official documentation.

## Why Does DynamoSizeLimitException Occur?

The root cause was found in **Local Secondary Indexes (LSI)**.  
When there is an LSI in DynamoDB, the size limit calculation changes.

LSI uses the item as a replica and doubles the size.
Thus, **if there are `n` LSIs, the maximum size used can be `n + 1` times the item size**, which in turn reduces the item size limit.  
In our case, we had one LSI, and the 210KB item exceeded the 400KB limit due to the LSI, leading to the issue.

There is one more reason why LSI should not be used.
