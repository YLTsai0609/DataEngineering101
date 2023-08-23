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

# Hive-Partitioning

* if your data is stored by hive-partitioning .e.g `gs://basename/date=20230706`
* by default, you sync `gs://basename/date=20230706/*.parquet`, the date column will be disappear.
* or we could open the hive partition detection so that bq remember to add on the partition field
* [reference](https://cloud.google.com/bigquery/docs/hive-partitioned-loads-gcs)


# Physical bytes and Logical bytes

* cost saving - logical is cheaper than pysical (2x)
* logical table size which is **uncompressed bytes** (aka logical bytes). 
* pysical bytes (compressed, store on disk) - If you switch to physical billing model, then you will be charged for actual bytes stored in the disk which can be much smaller than the uncompressed bytes.


# How to check the query plan(to check the broadcast hash join is used)

https://www.rathishkumar.in/2023/03/joins-in-bigquery-broadcast-hash-nested-repeated-best-practices.html


# Data definition language statement (DDL)

* to create and modify bigquery resource / create / alter / delete for tables / table clones / table snapshot / views / user-defined functions / and row-level access policies

* CREATE TABLE / CREATE TABLE AS (sql) / CREATE VIEW / DROP TABLE / DROP VIEW
  * could use CREATE OR REPLACE TABLE PARTITION BY ...

[for more detail - Data definition language (DDL) statements in GoogleSQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#console)