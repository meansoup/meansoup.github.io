---
layout: post
title: "DynamoDB Secondary Index: Considerations and Cost Issues"
sidebar_label: "Secondary Index"
parent: DynamoDB
grand_parent: aws
nav_order: 1
lang: en
permalink: /docs/aws/dynamo/si
sitemap:
  lastmod: 2024-05-22
---

To optimize queries in DynamoDB, it is necessary to utilize Secondary Indexes.

In DynamoDB, you can use Secondary Indexes to query data in the table using alternative keys besides the primary key. Secondary Indexes include the following:
- Attributes for the alternative key, primary key attributes, and optionally a subset of other attributes from the base table (projected attributes).

DynamoDB automatically creates indexes based on the table's primary key and updates all indexes automatically whenever the table is modified.

DynamoDB supports two types of Secondary Indexes: GSI (Global Secondary Index) and LSI (Local Secondary Index).  
AWS currently advises against using LSI, so this document will focus on the concepts and precautions of using GSI, as well as the reasons for avoiding LSI.

## GSI (Global Secondary Index)

**GSI** is called 'Global' because queries on this index can span all partitions and are not limited to a specific partition.

- It can have a partition key and, optionally a sort key, which are different from the table's original partition key and sort key.
- Key values do not need to be unique.
- It can be created when the table is created or added to an existing table.
- It can be deleted after table creation.
- It supports eventual consistency only.
- It has separate provisioned throughput settings for read and write operations (RCU, WCU).
- Queries return only the projected attributes in the index.
- Up to 20 GSIs can be created per table.

### Partitions in GSI

In GSI, **key values do not need to be unique.** This allows multiple data items to be stored under the same key, which is not possible in the main table.

For example, consider a main table with attributes **name, age, country, passportNo**.  
To ensure uniqueness, you might set the primary key to passportNo.  

However, if you need to query by country, you can set country as the primary key of a GSI.  
This allows you to store and retrieve multiple non-unique data items under the same country key.

Is this structure safe?  
GSI internally shards and partitions based on the key, ensuring safety.  
Theoretically, you can store unlimited data under the same key.  
The main table also shard primary key, but the main table cannot have multiple data for the same primary key.


### GSI CU (Capacity Unit) in GSI

GSI has separate Capacity Units (CUs) from the main table.  
When reading or writing to GSI, it consumes separate CUs, but this is related to main table operations.

For GSI's RCU, throttling does not affect the main table.  
However, for GSI's WCU, if throttling occurs, writes to the main table will also fail.  
DynamoDB internally <u>writes to both the main table and all related GSIs when data changes</u>[^1], so a write failure in GSI leads to a failure in the main table.

In summary, writes to DynamoDB are tied to writes in GSI.  
Updates in DynamoDB can result in delete and write operations in GSI.

Revisiting the previous example, if the country changes from KR to US, the projected data for the KR key in GSI is deleted, and the data is written to the US key.  
This results in the consumption of 2 CUs for one write operation in DynamoDB.

Since a significant portion of DynamoDB costs comes from CUs, a data structure that uses 3 CUs per write (1 for the main table and 2 for GSI) is not cost-effective.  
Multiple GSIs can be applied to a DynamoDB table, so cost considerations should be factored into GSI design.

## LSI (Local Secondary Index)

**LSI** is called 'Local' because the index is located within the same table partition as the item with the specified partition key.  
This means queries are restricted to data with the specified partition key value.

- The partition key of an LSI is the same as the table's partition key.
- It can only be created when the table is created.
- It cannot be deleted after table creation.
- It supports both eventual and strong consistency.
- It uses the table's read and write capacity without separate provisioning.
- Queries can return attributes not projected into the index.
- All items with the same partition key and their corresponding LSI items are stored within the same partition. The total size of this collection cannot exceed 10GB.
- Up to 5 LSIs can be created per table.

LSI has clear disadvantages and lacks distinct advantages over GSI, so it is not currently recommended.
1. LSIs cannot be added or deleted after table creation.
2. They share resources with the main table.
3. There is a 10GB size limit per partition key.

Using GSI is generally a better option.

---

[^1]: Refer to the [relationship between main table and GSI table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.ThroughputConsiderations) and the [impact of GSI CU shortages on the main table](https://repost.aws/knowledge-center/dynamodb-gsi-throttling-table).
 