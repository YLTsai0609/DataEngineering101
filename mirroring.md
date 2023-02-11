# Ref

https://medium.com/bryanyang0528/data-pipeline-design-patterns-1-mirroring-df62a8875665

# 適用場景

將原始資料表一模一樣的複製到其他地方供其他應用取用

e.g. 後端有一個存放使用者個人資料的 Table，分析上極具價值，通常不會讓分析端直接打後端的Table，而是同步一份出來，放到Data Warehouse / Data lake

1. 全表寫入，所以不適合太大的表
2. 全表寫入，更新頻次不會太即時，適用不需要即時同步的資料


# 技術規格討論

1. Table 數量
2. Table 數量的變化(用以預測全表同步可以用多久)
3. 每天適合同步的時間
4. 確認來源資料庫和目標資料庫使用者的技術
5. 確認雙邊資料的Schema，根據技術不同，能夠支援的Data Type 也會不一樣

# 處理流程

Data pipeline 流程大致如下

1. 刪除 Mirror table(需要使用 if exist 避免冷啟動時失敗)
2. 建立 Ｍirror Table Schema
3. 讀取 Source Table 寫入 Mirror Table(如果原始資料 > 10k筆，可以採 mini-batch)
4. 比對 Source Table 和 Mirror Table 資料筆數