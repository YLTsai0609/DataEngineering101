# ETL vs ELT


design pattern|pros|cons
-----|-----|-----
ETL|1. 多個 ETL 對應單一 source table，導致 source db 的計算壓力，可能需要升級機器|1. warehouse 中 query 速度快 <br> 2. transform 可能隨著需求變換，analyst 通常對 etl 工具較不熟(腳本語言)
ELT|1. 統一匯集到分散式環境，降低 source db 的計算壓力 <br>|1. warehouse 中 query 速度變慢一些

目前趨勢從 ETL 走向 ELT - 主要是因為雲端工具的興起，例如 BigQuery, Redshift, Snowflake，當需求產生或是變動時，直接在DataWarehouse進行轉換，而 SQL 對於 Analyst 又更加友善

# Batch ETL vs Streaming ETL

Streaming ETL - 根據事件、mini batch 的方式來處理累積的資料

# Ref

[ETL vs ELT](https://medium.com/@ryanyang1221/etl-vs-elt-a3a68939ff07)

[數據同步工具ETL、ELT傻傻分不清楚？3分鐘看懂兩者區別 - 有圖](https://www.twblogs.net/a/5efdda6ee94612e3fcea1126)

[[Data] Data Pipeline 101（三）—ETL](https://medium.com/bryanyang0528/data-data-pipeline-101-%E4%B8%89-etl-2a010a0e9fb5)