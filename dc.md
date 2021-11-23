# Ref

[那些大數據書不會教的資料工程](https://medium.com/@fchern/%E9%82%A3%E4%BA%9B%E5%A4%A7%E6%95%B8%E6%93%9A%E6%9B%B8%E4%B8%8D%E6%9C%83%E6%95%99%E7%9A%84%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B-19f848829062)

The data cleaning for traffic analysis : 把網路爬蟲流量、惡意使用者流量標記出來，Dashboard就可以過去掉這些流量

# 都不做的時候

會從 Dashboard 看到，之後便覺得哪裡怪怪的，再回頭修正

# 如何清理

## 根據使用者的使用頻率

1. groupby by `cookie`, `ip`, `user_agent` 能用也得不多，因為 http 是 stateless
2. 一段時間內的活動次數過多(每小時超過N，每天超過Z)
3. 逛網頁的特性(有廣告必點？有點連必點？)
4. 你的日誌系統log的顆粒度要足夠細，細到你可以"看"到一小時之內的所有資料
5. 要countDistinct，有時候做不到exact， hyperloglog, count min sketch 都可以用，可以參考 Mining of the Massive Dataset 來看

## 一些聽說的方法

1. 蜜罐 (honey pot) - 在網站上埋人眼看不到的連結，`display:none`，如果會點進這種連結的就是機器人
2. 執行js並回報 - 不能執行 js 的使用者多半也問題 - 可以跳出身份驗證

以上兩種多半會交由前端實作