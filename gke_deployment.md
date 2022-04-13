# Deployment

* deployment 中可以設定 pods 的數量，有助於
  * 藍綠部署(1 - 1) / 金絲雀部署(小量部署) / 漸進式部署
  * 可以做到無停機的系統升級(Zero Downtime Rollout)
* 用於水平擴展

# Service 

網路的抽象化 - 可用於流量分配

command : `gcloud compute instance list` - 如果建立 cluster，想要查看 VM 的狀況


Ref : [Kubernetes 基礎教學（二）實作範例：Pod、Service、Deployment、Ingress](https://cwhu.medium.com/kubernetes-implement-ingress-deployment-tutorial-7431c5f96c3e)