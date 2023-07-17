# Computational Framework

* 痛點是什麼?


# Solution

* Ray for ML

* Modin/Pyspark

# Survey

[Billion Rows in Pandas? CuDF, Modin, Arrow, Spark - 2022, Sep](https://www.unum.cloud/blog/2022-09-20-pandas)


# Other

## pyarrow

[github](https://github.com/apache/arrow)

[Efficient ML pipelines using Parquet and PyArrow - Ingargiola, 2022 PyCon](https://www.youtube.com/watch?v=_jYX1o-hsr0)

* notes
    * parquet, hive partitioning is supported
    * automantically compaction multiple files to single file in 1 partition (best practice is 64MB per files)
    * support overwrite without side effect
    * may add columns if any column is add into partition.