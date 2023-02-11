# Small Tables

* Daily update / by your refresh freq - build `yyyymmdd` or `yyyymmdd-timekey` partitioned files

# Large Chunk

1. .sql file
2. ?

## what is .sql file?

[Ref : Is .sql file different for MySQL and SQL? stackoverflow](https://stackoverflow.com/questions/2234798/is-sql-file-different-for-mysql-and-sql)

* file extension `sql` is essentially meaningless.
* It just there so that you know what the file is.
* It will just be aplain text file containing SQL.
* which you can open in Notepad / VSCode.

* So that the sql file you read, you must laod into the database.
* It's usually for backupDB

# Embulk


[embulk](https://www.embulk.org/)

[embulk - github](https://github.com/embulk/embulk)

* from different source A to target B 
* parallel execution
* data validation
* error recovery
* deterministic behavior
* Idempotent retrying
* From 
  * csv file
  * s3
  * hdfs
  * mysql
  * salesforce
  * ...
* To
  * Hive
  * ElasticSearch
  * Cassandra
  * Redis
* written in Java

## Hints

* connect to the Proxy Server， then we can perform seprated write/read