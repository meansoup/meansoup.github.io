---
layout: post
title: "What is DynamoDB Streams and When Should You Use It?"
sidebar_label: "Streams"
parent: DynamoDB
grand_parent: aws
nav_order: 4
lang: en
permalink: /docs/aws/dynamo/streams
sitemap:
  lastmod: 2024-06-24
---

As a service reaches maturity, enterprises begin to look for ways to reduce service costs.  
Since our service has been in the maturity phase for quite some time, we face pressure to reduce costs every year.

I often wondered, "Can we use DynamoDB Streams even if it's great, given our situation?"  
Then, I found a very suitable case.

First, let's understand what DynamoDB Streams is.


## DynamoDB Streams

DynamoDB Streams is a service that captures and delivers changes in DynamoDB.

Streams has the following characteristics:
- It keeps track of changes in DynamoDB in chronological order.
- You can see what data has changed through Streams Record.
- Streams Record stores data for 24 hours.
- It can easily integrate with other AWS services.
- It is easy to enable/disable without affecting the DynamoDB table.
- You can specify the information to deliver
  - KEYS_ONLY, NEW_IMAGE, OLD_IMAGE, NEW_AND_OLD_IMAGE

Since you can receive all changes via Streams, there are various ways to utilize Streams.  
**It can be used for data analysis, asynchronous tasks, data replication, backup, event delivery, and more.**

However, as mentioned earlier, **the problem is the cost**.  
Delivering all changes to Streams means **additional costs for all changes**.


## When Should You Use It?

If there is no cost pressure, Streams can be conveniently used for all the cases mentioned above, such as data analysis, asynchronous tasks, and data replication.  
However, considering the steeply increasing cloud costs as usage increases, it may not be appropriate to use Streams a lot simply because the current cost is low.

I found a very suitable case for Streams while designing a new system.  
We designed the user table in DynamoDB considering scalability and were considering statistics for users.  
To easily extract statistics, a database capable of various queries was necessary.

In the case of the user DB, the data cannot increase indefinitely (even if the entire world's population becomes users, it is only 7 billion).  
At the same time, the data in the user DB does not change frequently.  
Therefore, although there may be a lot of accumulated data, the Streams generated during continuous service are not many.


Let's take Instagram as an example.  
Instagram has about 1.5 billion users and generates about 100 million posts per day.

If you store post data in DynamoDB and use Streams, at least 100 million Streams Records will be generated every day, which can be a cost issue.

However, considering the 1.5 billion users, **most user data is updated during the registration scenario, and changes are infrequent thereafter**.  
If 1.5 billion Streams Records are generated over several years of Instagram service, this would be a very low cost.


## Cost Calculation

We will calculate the cost using the commonly used Streams and Lambda.  
The costs are organized based on the <u>AWS pricing document</u>[^1] as of June 24, 2024.  
The costs are the same in the USA (Oregon), and Europe (Ireland) Korea (Seoul).

### Streams

- ~~The first 2.5 million DynamoDB Streams read request units per month are free~~
- ~~Thereafter, $0.0217 per 100,000 DynamoDB Streams read request units~~
- Charges for reading data from DynamoDB Streams, but **<u>free when invoked from Lambda</u>**[^2]

Streams incurs no read request costs when used with Lambda.

### Lambda

Lambda cost calculation is a bit complex.  
There are separate charges for CPU per second, per request, and memory usage.

CPU (x86) charges
- First 6 billion GB-seconds per month: $0.0000166667 per GB-second
- Next 9 billion GB-seconds per month:  $0.000015 per GB-second
- Next 15 billion GB-seconds per month: $0.0000133334 per GB-second

Per request charge
- $0.20 per 1 million requests

Memory (MB) per millisecond charges
- 128 MB    $0.0000000021
- 512 MB    $0.0000000083
- 1,024 MB  $0.0000000167
- 1,536 MB  $0.0000000250
- 2,048 MB  $0.0000000333


### Cost Example and Calculation

Let's calculate the cost of linking Instagram's user DB to a statistics DB using DynamoDB Streams and Lambda.
- AWS RDS would be needed, but this cost is not included here.

- Scenario: **1.5 billion user data requests are made to Lambda through DynamoDB Streams.**
- Assumptions:
  - Using the cheapest 128 MB memory, assume Lambda runs for 1 second.

- Total cost: $28,450
  - Streams: $0
  - CPU per second cost: $25,000 (0.0000166667 * 1,500,000,000)
  - Per request cost: $300 (0.20 * 1,500)
  - Memory cost: $3,150 (0.0000000021 * 1,500,000,000 * 1,000)

In a real service, more Streams Records may be generated due to user changes.  
However, paying a total of $28,000 for Streams over several years of service is expected to be a very small cost compared to the service scale.


### Cost Optimization

In Streams, you can save on Lambda costs by receiving records in batches.  
You can modify the following properties to receive records in batches:

**<u>Batch size</u>**[^3]:  
- The number of records sent to Lambda in each batch.
- The maximum is 10,000 records, and multiple records are delivered in a single invocation.
- It must not exceed the payload limit of 6MB.

**<u>Batch window</u>**[^3]:  
- The time to collect records before invoking Lambda. (unit: seconds)

Let's assume the batch size is set to 1000 and the batch window is set to 10.  
If more than 1000 records are collected, Lambda is invoked. If fewer than 1000 records are collected, Lambda is invoked after 10 seconds.

It is important to note that **<u>batch size and window operate on a per-shard basis within Streams</u>**[^4].  
If there are 10 shards, the batch window and size apply to each shard individually, so during a 10-second batch window,  a total of 10 Lambdas could be invoked  becaouse each of the 10 shards collects records.

Therefore, sending data in batch sizes does not mean that a Lambda invocation will occur for each batch size of records.


---

[^1]: Refer to the [Streams pricing document](https://aws.amazon.com/dynamodb/pricing/provisioned/) and the [Lambda pricing document](https://aws.amazon.com/lambda/pricing/).
[^2]: You can check the cost when using Streams with Lambda in the [Streams usage](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_StreamsUsage.html) document.
[^3]: Check property at [spec for batch window & size](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping).
[^4]: Refer to the stackoverflow about [Streams shard & Stremas Batch](https://stackoverflow.com/questions/75448464/dynamodb-streams-small-number-of-items-per-batch).  