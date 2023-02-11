# Ref

[[Data] Data Pipeline 101（五） — 冪等性](https://medium.com/bryanyang0528/data-data-pipeline-101-%E4%BA%94-%E5%86%AA%E7%AD%89%E6%80%A7-e6ec61fd7b)

[Wiki](https://zh.wikipedia.org/wiki/%E5%86%AA%E7%AD%89)

* and some private metirial

# Idempotency

Key : 反覆執行同樣的 ETL 排程，會得到一樣的結果

e.g. 有一隻 ETL 每天早上 8:00 會計算前一天的營業額
    * runtime : 4/1 執行
    * inflow : 3/31 的資料
4/2 時重新執行 4/1 的排程，也能得到一模一樣的結果，我們希望這支程式是可信賴的(reliable)

通常一般程式指蘊含業務邏輯，但是 ETL 除了業務邏輯之外，還包含了資料，所以要達到 idempotency 有兩個前提

1. ETL 可以重複執行
2. ETL 所需要的資料必須被保留

## ETL 可以重複執行

1. 是否能重跑任一時間點的資料
   -  今天 4/5 我能不能夠讓程式去執行 4/1, 3/31, 甚至 半年的 ETL 排程，並且得到一樣的結果 - 寫 SQL 時把時間單位當成變數
2. 是否考量冷啟動
   - 目標表 / 中介表的 Create Table 有沒有被包含在 ETL 中，還是需要先在其他地方建立表個才能執行，當目標表格被刪除時(或是尚未被建立) ETL 能不能照常執行?
3. 避免塞入重複資料 
   - 程式要能夠重複執行還能得到相同結果的話，表示目標表得不能單純的使用 append 的方式來新增資料
   - 如果是摘要行表格，就要使用 update 的方式來確保 key 不會重複，如果目標表格不支援 update，就直接以 drop partition 的方式來避免塞入重複資料(例如 date partition) 

## ETL 程式所需要的資料

除了業務邏輯之外，還需要一模一樣的資料才行，然而為了避免過多原始資料造成儲存空間費用的增加或浪費，通常會設定資料的 Life Cycle

1. 剛進來的原始資料都放在熱區給 ETL 使用
2. 會透過一個或幾個 ETL 整理出時間顆粒度較粗、維度非常多的表
3. 其他 ETL 再根據上面的大表產生特殊用途的小表
4. 原始資料可以過了特定時間(例如半年/一年/三年)，進入 col zone