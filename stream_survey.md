# 幾款主流的 streamming framework (2022, Aug)


1. Storm
   1. 低延遲、難以高吞吐、不保證 exacylt-once
2. Spark Streamming
   1. micro batch for streamming - 實現 exacylt-once
   2. 無法完全即時(能夠到達秒級)
3. Flink
   1. 低延遲、高吞吐、exactly-once, 有狀態計算, 基於事件

# Apache Flink

* Java, Scala, distributed streamming
* 支援 amazon kinesis, kafka, hdfs, cassandra, elasticsearch 資料儲存系統


Pros : 只要維護一套
Cons : 中間結果不落地、丟失很麻煩、難以檢查結果(難以開發)

[Flink Official documentation](https://flink.apache.org/)

# ref

[Flink 框架在大数据架构中的应用介绍](https://zhuanlan.zhihu.com/p/114176781)

[Flink不止于计算，存算一体才是未来](https://zhuanlan.zhihu.com/p/485734742)