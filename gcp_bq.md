# NOTE

To record some unique part about google bigquery

# Interactive and batch query jobs

[doc](https://cloud.google.com/bigquery/docs/running-queries)
* interactive - runs on demand
  * ASAP, limited by concurrent limit (100 concurrent interactive queries by default)
* batch - waits to run until idle compute resources are available

# Partitioning

## Partitioning vs Sharding vs clustering

[partitioning vs sharding](https://cloud.google.com/bigquery/docs/partitioned-tables)

* sharding - TableName_YYYYMMDD
  * flexible schema of each table
  * query overhead - need store metadata and permission verification for each table 

* partiting - TableName$2021071205
  * performance is better than sharding
  * only 1 schema on serving
  * does not support multiple column partitioning

```bash
    bq head --max_rows=10 'my_dataset.my_tablee$20180224'
```

[clustering](https://cloud.google.com/bigquery/docs/clustered-tables)

* clustering
  * just like indexing your table
  * ordered columns help performance
  * could be used with partitioning

## Range Partitioning

[doc](https://cloud.google.com/bigquery/docs/creating-partitioned-tables#python_1)

* bigquery offer time-based partitioning grainity (YEAR, MONTH, DAY, HOUR)
* if we would like to use 5 mins or less than 1 hour, use integer-range-partition
  * maximum 4000 partitions
  * could be full replace and filter by table decorators - `table$YYYYMMDD`, `table$PartKey`

