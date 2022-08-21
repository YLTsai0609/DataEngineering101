# Spark Streaming Introduction

## 一次性紀錄 & 陳述式 API

極簡串流 API : 只傳送事件給 Worker ，Worker 處理剩下的事 (Apache Storm) - 這種做法稱為一次性紀錄(record-at-a-time)
* 應用程式端需做事件追蹤，因為事件可能會因為網路延遲或是發送端異常導致收不到事件
* 需要深厚的知識才能開發和維護
* 不同處理邏輯的 Worker 都需要事件追蹤，顯然事件追蹤可以被抽離出來作為獨立模組

## 陳述式 API
* 事件追蹤直接包起來，你只需要撰寫資料處理邏輯，結合分散式資料集的特性，刑成可靠性 (fault tolerance)
* Dtream (Data Stream) 就是這樣的 API

## Saprk Structured Streaming (結構化串流)

* 高階的 DataFrame API - 程式碼 和 batch 一模一樣，減少重工
* 支援處理 event-time (DStream) 沒有


## 事件時間與處理時間

事件時間 - 事件真實發生時間
處理時間 - 事件抵達處理器的時間

* 通常兩者的差距是網路傳輸時間或發送端斷網等不可靠情況

## 連續性與微批次執行

連續性執行 (continuous processing)
* one record at a time
* 低延遲(例如 20ms)
* 低最大吞吐量

micro batch
* 累積小批次輸入資料變成 batch - 故稱為 micro batch
* 分散式任務平行處理
* 延遲稍高(例如500ms ~ 10 mins)
* 高吞吐量
* 動態負載平衡(增加減少任務的數量/增加worker)
* spark structured streaming 目前是 micro batch.

Trade off (?): 


期望延遲 & 營運成本

micro batch - 100ms --> 1s / 10s / 1mins / 10 mins (時間越長營運成本越低 / worker數量減少)

micro batch + memory store - 快速響應結果

# Ref

[Spark技術手冊：輕鬆寫意處理大數據 - Chp20 串流處理基礎](https://www.books.com.tw/products/0010837191)