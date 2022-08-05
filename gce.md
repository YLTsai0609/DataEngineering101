# 直接進入機器


```
gcloud compute ssh --zone "asia-east1-a" "foodapp-coco-pixmarketing-api-5g2t"  --project "pixnet-soyummy"
```
# 規格評估

1. 規格評估 前 -  後 (ex: n1-standard-1 - e2-medium)
   
    解釋: 費用 n1-standard-1 > e2-medium, 但規格差不多

    以下為要注意的

    n1-standard-1 - e2-medium

    g1-small - e2-small

    n1-highmem-2 - n2d-custom-2-13 (這個的意思:  2vCPU , 12GRAM)

    n1-standard-2 - e2-standard-2 (確認可以換)

    n2 系列, 應該都可以換 n2d, 但一樣請精算一下成本

    其他的規格, 請 評估效能 後, 再用 https://cloud.google.com/products/calculator 算一下成本, 以低的為主
    

# 鉛直擴展

e.g. 加大記憶體

[GCM教學：如何變更VM執行個體的CPU數量、記憶體大小或硬碟大小？](https://mrtang.tw/blog/post/how-to-change-a-machine-type-on-google-compute-engine)

1. 需要停機
   1. 要注意網路設定是不是跑掉(domain name, ssl, ...) - 需調整成靜態 IP
   2. 可能需要重新掛載 SSD


NOTE: [GCP教學：將臨時外部IP位址改為靜態IP位址](https://mrtang.tw/blog/post/reserving-a-static-external-ip-address-google-cloud-platform)