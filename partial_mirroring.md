# Ref

https://medium.com/bryanyang0528/data-pipeline-design-patterns-2-partial-mirroing-5d2da927c42e

# 適用情境

SELECT AND FILTER(部分鏡像)

原始資料表的部分欄位 / 部分紀錄 同步到其他地應用取用


SELECT - 場景，遇到敏感資料，紙漿不敏感的資料同步出來，敏感資料就不處理

FILTER - 事件類型只想要分析特性事件類型

1. 因為只讀取部分資料，所以只需計算欄位數 x 資料筆數
2. 如果原始資料的數量還是很多(row-based 資料庫)，by row 的計算量還是比較大，為了避免原始資料酷的負擔，更新頻次也不應該太即時

# 技術規格討論

1. 原始Table的比數和欄位數量
2. 原始Table的每日資料變化量
3. 每日適合同步的時間(通常是半夜，或是來源資料庫負擔較輕的時候)
4. 確認選取欄位名稱
5. 確認選取紀錄邏輯
6. 確認來源資料庫和目標資料庫使用者的技術
7. 確認雙邊Schema，根據技術不同，能支援的Data Type 也不同



# 處理流程

Data pipeline 流程大致如下

1. 刪除 Mirror table(需要使用 if exist 避免冷啟動時失敗)
2. 建立 Ｍirror Table Schema
3. 讀取 Source Table 寫入 Mirror Table(如果原始資料 > 10k筆，可以採 mini-batch)
4. 比對 Source Table 和 Mirror Table 資料筆數
