---
layout: post
title: Understanding Different Cassandra Compaction Strategies
sidebar_label: Compaction Strategy
parent: Cassandra
grand_parent: Database
lang: en
permalink: /docs/db/cassandra/strategy
sitemap:
  lastmod: 2025-02-07
---

**<u>Compaction Strategy (CS)</u>**[^1]  
A compaction strategy in Cassandra manages the garbage collection (GC) process. There are several strategies to choose from, and selecting the right one for your workload can improve both query and compaction performance.

* [Size Tiered (STCS)](#size-tiered-stcs)
* [Leveled (LCS)](#leveled-lcs)
* [Time Window (TWCS)](#time-window-twcs)
* [Unified (UCS)](#unified-ucs)


## Size Tiered (STCS)

The default compaction strategy in Cassandra, best for write-intensive workloads.

### How It Works

STCS compacts SSTables based on their size and count:

1. When a certain number (default: 4) of similar-sized SSTables exist, compaction is triggered.
2. These SSTables are merged into a single larger SSTable.
3. If needed, the new larger SSTable is merged into an even bigger SSTable.

Because of this process, SSTables of various sizes can exist at the same time.

### Features

- Good for write-heavy workloads.
- Default if no better strategy is available.
- **Merges by size, so data is not grouped, leading to reduced read performance.**
- Since compaction works based on size, deleted data might not be removed as expected.
- **Requires extra disk space because both old and new SSTables exist during compaction.**
- Lower I/O and CPU usage compared to LCS in normal operation.
- Works better than LCS on HDD storage.
- **Can cause CPU spikes during compaction due to large SSTable merges**, which led to issues at our company.

## Leveled (LCS)

Designed to improve the read performance issues of STCS.

### How It Works

LCS organizes SSTables into levels:

1. When Memtable is flushed, data is written to SSTables in Level 0 (L0).
2. During compaction, L0 SSTables are merged with L1 SSTables.
3. If necessary, compaction continues into higher levels.

Unlike L0, SSTables in L1 and higher do not overlap.
- **This means that read operations only need to check one SSTable per level.**

### Features

- Optimized for read-heavy or update/delete-heavy workloads.
- Not suitable for pure time-series data.
- Not ideal for write-heavy workloads.
- Uses about 10% less disk space than STCS.
- Requires frequent compaction to remove duplicate and unordered data, leading to higher CPU and I/O usage.
- **Not recommended for slow storage like HDDs.**

## Time Window (TWCS)

Designed for time-series data that uses TTL and remains mostly unchanged.

### How It Works

TWCS organizes SSTables by time windows:

1. Uses predefined time windows.
2. When Memtable is flushed, data is written to an SSTable.
3. Multiple SSTables are created during a time window.
4. Once the time window closes, all SSTables from that window are merged into a single large SSTable using STCS.
5. The merged SSTable keeps the maximum timestamp.

### Features

- Organizes SSTables by time, allowing for efficient data expiration and deletion.
- More efficient disk space reclamation compared to STCS and LCS.
- Only one major compaction occurs per time window, making it efficient.
- **Can suffer performance issues if too much data is written in a single time period.**

## Unified (UCS)

Recommended for most workloads, including read-heavy, write-heavy, mixed, and time-series data.
- **No need for old compaction strategies since UCS can be configured to act like any of them.**
- It was added in Cassandra 5.0

### How It Works

UCS performs compaction at the shard level:

1. Compaction if there is more than a certain number of SSTables within the shard.
2. Uses different methods depending on the level:
    - **Leveled:** Works like LCS, moving data from L0 to L1.
    - **Tiered:** Works like STCS, stacking SSTables up to a limit before merging.

### Features

- Combines the best features of all other CS types.
- **Optimized for virtually all workloads.**
- **Automatically switches between Tiered (for writes) and Leveled (for reads) depending on workload.**
- Splits SSTables into shards for **independent and parallel compaction.**
    - LCS organizes tokens by levels, while UCS uses shard for efficient parallel compaction. (it looks like grid)
- **Can dynamically switch to another compaction strategy while running.**
- Requires fine-tuning for optimal performance.

---

[^1]: See [Compaction Strategy](https://cassandra.apache.org/doc/latest/cassandra/managing/operating/compaction/index.html) for official documentation on different strategies.

