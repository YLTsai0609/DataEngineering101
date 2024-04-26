# Fee
* [ref](https://www.elastic.co/guide/en/cloud/current/ec-billing-dimensions.html#ec_how_can_i_control_the_storage_cost)
* Data Transfer (Data-out and Data inter-node)
    * Free - 100GB/Month
* Storage
    * Binding on GCS cost

* 機器 VM, 硬碟, 記憶體是透過 ElasticSearch 代管，並不會出現在我們自己的 project


# Introduction

[親愛的，我把ElasticSearch上雲了](https://ithelp.ithome.com.tw/articles/10238560)

Elastic Cloud是一個由Elasticsearch公司提供的SaaS平台，主打就是非常簡單的就能夠部屬一個屬於你的ELK系統。而所謂簡單就能部屬，我們就要先知道原先要如何架構一個ELK服務。

Elastic Cloud優點
花費最小力氣建構ELK應用
在原先ELK易於擴增的特性上，更能夠展現這個特點(雲端調整主機速度快速)
ELK效能監控及校調方便
持續更新ELK
資料儲存、保留以及安全性能夠有效確保

相對的，以上的優點，其實筆者認為在本地端，若你是一個有經驗的使用者，你也許能夠更加有系統性的去建構這些部分；因此若你今天是一個常常變動、另外不希望花費太多時間找人在管理這個服務，Elastic Cloud也許是個好選擇

# Deployment

整個 ELK 為主

方案

1. I/O Optimized
2. Memory Optimized
3. Compute Optimized
4. Hot-Warm

不同得 Node 介紹 

Master-eligible node：master節點可以想像成是主枝幹，主要是為了控制cluster的角色，具有投票權的主要節點角色
Data node：簡單來說就是控管Data的任務，包含增刪查改、搜尋以及分群的計算數值(aggregation)
Ingest node：主要是為了負責前處理pipline的節點，可以想像成用來弭補logstash前處理的不足
Machine learning node：負責處理機器學習計算的，若你預計要在Elasticsearch服務中使用機器學習，必須至少指定一個instance這個角色
Transform node：transform node就是用來進行transform任務的節點，transform意指將目前的一個indice，轉換成summary過的(例如aggreation或其他的)indice
Coordinating node：負責處理轉發的節點，意思是當今天有一個任務是需要傳遞給data node，可以透過coordinating node先接收，再轉查給data node，算是一定程度的load balance

1. 不需要的功能(ML, Transform, Logistic)



