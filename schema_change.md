
# Ref

[那些大數據書不會教的資料工程（二）](https://medium.com/@fchern/%E9%82%A3%E4%BA%9B%E5%A4%A7%E6%95%B8%E6%93%9A%E6%9B%B8%E4%B8%8D%E6%9C%83%E6%95%99%E7%9A%84%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B-%E4%BA%8C-15b6e9b493f3)

資料工程中，除了規劃並實作Data pipeline，通常還會涉及如何選擇資料格式以及儲存系統

這些決策在資料產生端改變不難，但如果整個 pipeline 要更新，通常都要耗費大把時間，因此應該一開始就要有長遠的規劃

網頁工程出身 - LOG, JSON, XML, CSV

資料科學出身 - LOG, JSON - 如果是 prototype，使用自己熟悉的格式做即可

然而設計資料系統時，要考慮維護性以及可擴充性

1. 優先選擇有框架定義的儲存格式(schema defition) - 例如 protobuf, thrift, avro
   *  大數據的商業語言常常強調資料多變性，但設計資料系統時你反而會希望型別檢查再輸入資料之前就做好
   *  Why important? - 假設一個已經非常複雜的 Pipeline，總共有10+個 operator，最上游的一個資料輸入開始出現null，但 data pipeline 並沒有噴出錯誤訊息，或許你要到好多天後才會發現(甚至是客戶發現這個錯誤)，那麼在中間這段累積時間的資料怎麼辦? 回補可能會非常花時間
2. 資料要可以切分版本，不同的版本可以有不同的schema
   *  為了降低錯誤的曝光度，讓 data pipeline 有能力同時支援新舊系統，並且進行大量的資料驗證，應當要可以向上相容、向下相容(可新增欄位)
   *  自己實作的話，gcs上的資料可以在要上傳時
      *  load gcs上的資料，讀取schema， as dst_schema
      *  和 src_schema 比對
      *  將此行為寫成 func - `_is_schema_consistent`