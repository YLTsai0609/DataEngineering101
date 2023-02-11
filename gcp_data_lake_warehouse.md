## GCP Introduction

<img src='./assets/gcpair_13.png'></img>

<img src='./assets/gcpair_14.png'></img>

<img src='./assets/gcpair_15.png'></img>

app engine可以做到 auto-scaling

通常整理好準備分析的資料會放到bigquery

pubsub則是溝通工具，可以放到data lake

### gcs

上傳檔案不用錢，下載才要錢，可視為無限大的檔案空間

但實質上是key-value pair，所以其實你要rename folder，會比較麻煩

### network

google自己建置海底電纜，google有自家的網路，所以google自己的服務之間溝通速度會快很多

On-Premise - 地端機器

## Realtime BI Dashboard

有分成 batch 跟 streamming

<img src='./assets/gcpair_1.png'></img>

其實上圖中最棘手的是左邊

多樣性(資料格式的不同，怎麼做整理和統一)，並且是大家比較不會注意到的

三張圖會對應到google的三個服務

## Pub/Sub(Reliable Realtime messaging)

event-based : message queue，有事件就上傳

<img src='./assets/gcpair_2.png'></img>

<img src='./assets/gcpair_3.png'></img>

1. 該服務會保證對方一定收的到(像是手機訊息進火車山洞)，對方還是收的到
2. Server服務 - 不用自己寫
3. 後面可以接收集資料的地方(資料湖)
4. message queue(可作為broker)，發送者不需要知道訂閱者
5. 對應open source工具 - Kafka, RabbitMQ(Sacaling服務時會用到)

<img src='./assets/gcpair_4.png'></img>

## Cloud dataflow

### Pipeline

<img src='./assets/gcpair_5.png'></img>

Apache Beam - 可以同時support batch/streamming

<img src='./assets/gcpair_6.png'></img>

有各種template，只需實作商業邏輯即可

<img src='./assets/gcpair_7.png'></img>

<img src='./assets/gcpair_8.png'></img>

Apache Beam 只是一張設計圖，可以經由Spark，或是google dataflow的運算引擎來運算

<img src='./assets/gcpair_9.png'></img>

以上是具體程式碼

同時支援batch / streamming?

<img src='./assets/gcpair_10.png'></img>

1. 換Input / output
2. streamming要有一個window，來做groupby，其他幾乎一樣

<img src='./assets/gcpair_11.png'></img>

Auto Scaling!
Monitorable!

### Runner

Dataflow - spark on gcp
<img src='./assets/gcpair_12.png'></img>

## Visulization

Data Studio

# Data Warehouse

All Modules

1. Engineering a Data Warehouse Solution - Data Lakes and Storages
2. BigQuery as a Data Warehouse - BugQuery Basics
3. BigQuery Performance - ETL tools
4. Streamming Pipelines - Operation Management
5. BigQuery Analytics and Visulizations - Summary and Event Wrap Up

Topics   

1. Data Engineering
2. Data Lake
3. Data Warehouse
4. Data Ingress
5. Analytics and Visulization

<img src='./assets/gcpair_17.png'></img>

BigQuery 算是承先啟後，在GCP上的資料管理扮演相當多角色

## Data Engineering

<img src='./assets/gcpair_18.png'></img>

1. Raw Materials - 把不同種類的原始資料(木材，鋼筋水泥)聚集再一起，才有辦法蓋房子

<img src='./assets/gcpair_19.png'></img>

2. ETL - 整理，整理成能用的樣子

<img src='./assets/gcpair_20.png'></img>

3. 開始蓋房子(訓練模型、提取insight)

<img src='./assets/gcpair_21.png'></img>

4. 自動化，可在不同的業務場景重現出來 - 就像工地會有工頭

1 - 4 : MLOps

<img src='./assets/gcpair_23.png'></img>

Data source - 原始資料來源

Data Lake - 原始資料聚集處(最好是NoSQL) - 啥都可以丟

Data Pipeline - 對Data Lake裡面的各種資料做加工，轉換

Data Warehouse / Data Mart - 可以被分析或是訓練的資料

<img src='./assets/gcpair_24.png'></img>

### Data Lake

<img src='./assets/gcpair_25.png'></img>

unstructure data - gcs
semi, scrutcture data - bigquery(身兼data lake, data warehouse)

<img src='./assets/gcpair_26.png'></img>

gcs, bigquery - 可作為data lake使用

1. 幾乎啥都可以存
2. 都可以scaling
3. 寫入快，寫入之後可以馬上被查詢到
4. 好的權限管控
5. 容易連接資源

<img src='./assets/gcpair_27.png'></img>

### Data Warehouse

<img src='./assets/gcpair_28.png'></img>

<img src='./assets/gcpair_31.png'></img>

### Data Ingress(ETL work)

<img src='./assets/gcpair_29.png'></img>

<img src='./assets/gcpair_30.png'></img>

## Wrong view of ML

<img src='./assets/gcpair_32.png'></img>

一般人理解都是由左往右的思考，但其實真正在解商業問題時，需要由右往左思考，再來考量是否需要ML

# GCS and CloudSQL

<img src='./assets/gcpair_33.png'></img>

### CloudSQL

<img src='./assets/gcpair_34.png'></img>

Transacrtional workload - ACID保證

存的時候讀取不會出問題

Cloud Spanner - 資料庫跨全球

### GCS

<img src='./assets/gcpair_35.png'></img>

1. 自動備份(檔案不會遺失或是毀損)
2. 容易上傳下載

物件會被分級，依照存取頻率，arxiv等級就會很便宜，要常常取得就會稍微貴一點

3. 檔案分級不影響存取速度，區域才會影響存取速度

<img src='./assets/gcpair_36.png'></img>

<img src='./assets/gcpair_37.png'></img>

模擬FileSystem，但是其實背後是Key-Value的NoSQL

<img src='./assets/gcpair_38.png'></img>

Retension Policy - 多久之後把檔案刪掉 - 用於Hot-data

Versioning - 如果有檔案被覆蓋，想要rollback，gcs做得到

<img src='./assets/gcpair_39.png'></img>

權限管理 - Reader, Writer, Owner, ACL(per user)

也會自動作加密

<img src='./assets/gcpair_40.png'></img>

區域方面可以選 

Region/Dual-region/Multi-region

存取等級

Standard
Nearline
Coldline
Archive

# Reference

[data warehouse vs data mart](https://kknews.cc/zh-tw/code/oeoylvp.html)

[pyspark parquet to googlebigquery](pixlake/pixlake/etl/foodapp/reporting/multi_dimensional/export_bigquery.py)