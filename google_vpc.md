# Google VPC

1. Virtual Private Cloud - 雲端內部溝通IP網段
2. 可使用 Compute Enginer 提供網路連接，也包含 GKE cluster, App engine, ...
3. 內部 HTTP(S) load balancer

# 建置 VPC

1. `建立虛擬私人雲端網路`，可自訂網段
2. 選擇防火牆歸則
3. `gcloud compute addresses list`

# Peering

1. 同專案不同VPC
2. 不同專案

兩邊需同時建立該服務(Peering) 才可進行網路通訊

# Ref

[GCP的雲端世界系列 第 6 篇 VPC (一)](https://ithelp.ithome.com.tw/articles/10262895)

[GCP的雲端世界系列 第 7 篇 VPC (二)](https://ithelp.ithome.com.tw/articles/10262899)

[網路對等連線](https://ithelp.ithome.com.tw/articles/10265026)