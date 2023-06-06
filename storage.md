# Parquet

https://parquet.apache.org/

third-party : https://zhuanlan.zhihu.com/p/141908285

* Compressed
* Supposed nested type - e.g. Array(Struct(key, value))
* Easily integrated with BigQuery, Spark, Flink, Hadoop, …
  * Unified data storage format for big data ecosystem

# Parquet & GCS supported

## Java (Spark) & (Pyspark)

Spark - there is a package for that - spark.hadoop.fs.gs.impl com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem

## Python

[pyarrow](https://github.com/apache/arrow/tree/master/python)

* pandas use pyarrow as backend e.g. [pd.read_parquet](https://github.com/pandas-dev/pandas/blob/v1.5.3/pandas/io/parquet.py#L447-L509)
* Ray using pyarrow as backend e.g. [ray.Dataset.read_parquet](https://docs.ray.io/en/latest/_modules/ray/data/read_api.html#read_parquet)

pyarrow - 7.0 ~ 10.0 only support python 3.7+
