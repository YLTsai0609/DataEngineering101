# Ref

[[Data] Data Pipeline 101（六） — 二階段轉換](https://medium.com/bryanyang0528/data-data-pipeline-101-%E4%BA%94-%E4%BA%8C%E9%9A%8E%E6%AE%B5%E8%BD%89%E6%8F%9B-10aeed72aae7)

# 目的

為了避免 bug 導致的髒資料進入正式環境DB，可以再加入一個 Guard 的 Operator

# 從測試到正式環境

ETL 的正確性涵蓋兩個部分

1. 原始資料正確
2. 商務邏輯正確

相對嚴謹的開發流程會像這樣

1. 測試資料 --> 測試資料處理程式 --> 測試 DB
2. 測試資料 --> 正式資料處理程式 --> 測試 DB (開發ETL中)
3. 正式資料 --> 正式資料處理程式 --> 測試 DB (確認ETL可以處理正式資料)
4. 正式資料 --> 正式資料處理程式 --> 正式 DB 

# 兩階段

正式資料 --> 正式資料處理程式 --> 暫存區 --> 確認資料品質 --> 正式DB

* 變形 (質量檢查，也可以直接寫在同一個 Operator 裡面)

正式資料 --> 「正式資料處理程式 --> 暫存區（in memory） --> 確認資料品質」 => 正式DB

* 變形 (資料量大，或是需要累積多一點資料一起驗證時)，還是先落地在檢查

正式資料 --> 「正式資料處理程式 --> 暫存區（in db / other persistance storage） --> 確認資料品質」 => 正式DB
