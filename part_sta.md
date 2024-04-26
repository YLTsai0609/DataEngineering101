# Primary Key
* Primary Key - PK, UK, 資料庫中對儲存資料已唯一完整標示 - 只能有一個 PK
  * e.g. customerID, poi_id, xxx_id, 不能為 Null
  * SELECT COUNT(DISTINCT PK) = COUNT(*)
* Entity - 多個欄位組成，用於識別一張資料表的最小單元 (records), e.g. customerID, timestamp (每個customerID 在 timestamp 下的行為) - OLAP 上的麻煩事
  * SELECT COUNT(DISTINCT CONCAT(C1, C2, ...)) WHERE C1, C2, ... IS NOT NULL = COUNT(*)
* pseudokey - auto-increament key - 用於當作 PK
  * 
* 通常 PK 的選擇會以最常使用的查詢方式 (過往是 OLTP 最常用的查詢方式，例如 userID 會查詢 SELECT * WHERE userID = 'u1', 訂單明細則會用 訂單編號、項次)
  * 在 PK 上建立 INDEX 來加速查詢

# Index

* DB 中一種加速查詢的操作方式，通常背後是以樹的結構儲存，大部分以 B+ Tree 為主 - 是一種特別平衡樹高度，以便維持查詢效率的樹結構

# Partition


* Partitioning - 大表拆成小表，常見使用日期，或者易於商業邏輯判斷的維度，例如國家
  * 容易將冷熱資料分開
* 查詢規則不需要大幅變動 - WHERE PARTITION BETWEEN A AND B
* INDEX 存在的 scope 於單表中，而非分區表

# Partitioning Strategy in for data-lake

4 mode : 

1. overwrite
2. append
3. dynamic partition overwrite
4. merge

[ref - Handling Dynamic Partitioning and Merge with Spark on BigQuery](https://starlake-ai.github.io/starlake/blog/spark-big-query-partitioning/)

