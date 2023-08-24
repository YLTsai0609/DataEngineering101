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

## Creating GCE

1. create from GCP public images - https://cloud.google.com/compute/docs/instances/create-start-instance#publicimage
    * e.g. ubuntu, deep-learning, the list : `gcloud compute images list`
    ```bash
    gcloud compute instances create VM_NAME \
    [--image=IMAGE | --image-family=IMAGE_FAMILY] \
    --image-project=IMAGE_PROJECT
    --machine-type=MACHINE_TYPE
    ```

2. create with container
    * first, upload container to gcr
    ```bash
    gcloud compute instances create-with-container nginx-vm \
    --container-image=gcr.io/cloud-marketplace/google/nginx1:1.12
    ```

* with custom image
* with additional non-boot-disk
* with subnet

## GCE ssh trouble shooting

GCE 可能會有防火牆設定，導致 ssh 無法進入

具體來說會看到的 error : 

```
ssh: connect to host 222.111.111.111 port 22: Operation timed out
ERROR: (gcloud.compute.ssh) [/usr/bin/ssh] exited with return code [255]. See https://cloud.google.com/compute/docs/troubleshooting#ssherrors for troubleshooting hints.
```

(網頁版 ssh 連線) - 可以用 GUI 診斷，可進一步確認是防火牆問題

<img src='./assets/gcpc_1.png'></img>

也可以透過 command line 來診斷 e.g. `gcloud compute ssh INSTANCE_NAME --troubleshoot`

## GCE Firewall

* GCP 防火牆的概念 - 你不說可以，就是全部都不可以

* 因此，create firewall rules 時
  * 會要求輸入 --source-ranges : 被允許的機器ip
  * 也會要求輸入 -- allow tcp:XX : 被允許的 port




1. `gcloud compute firewall-rules list` - 列出所有防火牆規則
2. ``gcloud compute --project "project-id" firewall-rules create FIREWALL_INSTANCE --source-ranges "111.222.333.444/24" --allow tcp:22`` - 建立防火牆規則
    -- source-ranges 如果寫 0:0:0:0/0 表示都可以連

3. ``gcloud compute --project "project-id" ssh INSTANCE_NAME --zone "asia-east1-a" --command 'echo "Hello World"'` - 透過 gcloud ssh 連線進機器，然後 hello world`

[ref - gcloud compute firewall-rules create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)

[ref - roubleshooting SSH errors](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors#ssh_troubleshooting_tool)

[How to open a specific port such as 9090 in Google Compute Engine](https://stackoverflow.com/questions/21065922/how-to-open-a-specific-port-such-as-9090-in-google-compute-engine)

## GCE 靜態IP

1. [設定靜態IP - 手動設定](https://ikala.cloud/gce-static-ip-address/)
   * 也可以直接設定 DNS
2. [靜態IP收費 - 0.02USD / hour](https://ephrain.net/gcp-google-cloud-platform-%E4%B8%8A%E7%9A%84%E9%9D%9C%E6%85%8B-ip-%E8%A2%AB%E6%94%B6%E8%B2%BB%E5%95%A6%EF%BC%81/)
