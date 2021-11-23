# Ref

[[Data] Data Pipeline 101（四） — 管線系統設計與開發 — 功能面](https://medium.com/bryanyang0528/data-data-pipeline-101-%E5%9B%9B-%E7%AE%A1%E7%B7%9A%E7%B3%BB%E7%B5%B1%E8%A8%AD%E8%A8%88%E8%88%87%E9%96%8B%E7%99%BC-%E5%8A%9F%E8%83%BD%E9%9D%A2-faa3582ca050)

# 資料重力 (Data Gravity)

[Data Gravity and What It Means for Enterprise Data Analytics and AI Architectures](https://www.cio.com/article/3331604/data-gravity-and-what-it-means-for-enterprise-data-analytics-and-ai-architectures.html)


1. 2010年 Dave McCrory 提出的概念
2. 主要概念 : 隨著資料系統持續的開發，越上游的資料會越來越難做 更版 / 搬移，就像是重力定律一般。

# 設計 Data pipeline 時，需要考慮的幾個面向

1. 延遲性
   * 從收到資料到處理好資料，可以容忍多久的延遲 - 影響到 pipeline 是即時處理 / 批次處理
   * 每天看的BI報表 - 每天只要更新一次，處理頻率每天一次，所以可以容忍不是即時更新
2. 精準性
   * 銀行帳款 - 不容許誤差
   * 線上即時使用者數、推文數 - 有較寬鬆的誤差空間
3. 可用性
   * 越上游的Operator越趨近於 **資料收集** 系統 - 會注重可用性，因為一但掉資料，或是壞掉，下游應用全部gg

# 設計一個 data piepline system 需要考慮的幾個面向

1. 系統能不能支援版本回滾
   * Operator 邏輯更新時，發現Bug要修改，要把資料更新時，能否快速回滾以前的資料
2. 記錄任務進行時間
   * 能否量測每次的計算時間，某一天處理時間異常增加會發 alert.
3. 防止錯誤資料進入正式環境
   *  即資料也有測試資料和正式資料
4. 資源監控
   * 能否簡單監控甚至預測所需資源
5. 易於開發、部署
   * 開發ETL job 的人和開發 Data pipeline system 的人，可能是不同的兩群人，此套系統是否能以開發者熟悉的語言來操作
6. 自動化維運
   * Data Pipeline 系統和其他任何軟體系統一樣都需要維運，越自動的維運機制以及越完整的自我修復功能，都能大大降低未來的負擔