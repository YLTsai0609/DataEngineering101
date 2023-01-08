# Installation

https://cloud.google.com/storage/docs/gsutil_install


# Words

| command  | what is it                 | note             |
|----------|----------------------------|------------------|
| `gsutil` | `google storage utils` | 用於管理gcs資源，例如建立bucket，列出bucket等    |
| `gcould` | `google could shell tools` | 用於操作gcp專案資源 |

[Google Cloud Shell 入門：gcloud & gsutil](https://titangene.github.io/article/getting-started-with-cloud-shell-gcloud-and-gsutil.html)

# gcould

## login
可以透過gcloud auth login 進行帳號登入，接著就可以設定project

## set project

```
(base) joetsai@thor:~$ gcloud config set project pixnet-gt
Updated property [core/project].
```

## Manage your project

```
(base) joetsai@thor:~/work/research-appengine/recommender/food$ gcloud config configurations list
NAME     IS_ACTIVE  ACCOUNT            PROJECT              COMPUTE_DEFAULT_ZONE  COMPUTE_DEFAULT_REGION
default  False      joetsai@pixnet.tw  pixnet-gt
lab      True       joetsai@pixnet.tw  pixnet-research-lab
```
## auth

`gcloud auth list`

```
ACTIVE  ACCOUNT
        279150585509-compute@developer.gserviceaccount.com
*       joetsai@pixnet.tw

To set the active account, run:
    $ gcloud config set account `ACCOUNT`
```
# handy commands

## gcs

`which gsutil`

`gsutil --help`

https://cloud.google.com/storage/docs/quickstart-gsutil#whats-next


| command example | usage  | note |
|----------------|---------|------|
| gsutil ls -l   | list resource/files on google storage |     gcs     |
| gsutil cp local_file gs://yurenke-test/abc.json| upload resource to google cloud storage| gcs |
| gsutil mv gs://yurenke-test/abc.json gs://bcd/aaa.json |move bucket from a to b|gcs
| gsutil rm/rb gs://yurenke-test/abc.json  |remove thr bucket|gcs
| gsutil version  |show the version info about gsutil|gcs


## bq

`which bq`

`bq --help`

https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet#bq_1

https://cloud.google.com/bigquery/docs/managing-partitioned-table-data#append-overwrite

| command example | usage  | note |
|----------------|---------|------|
|`bq head --max_rows 5 'pixnet-gt:project_poi.poi_20210803'`| query 5 rows in `dataset_id.table_id`
|
|` bq load --source_format=PARQUET --time_partitioning_type=DAY pixnet-gt:project_food_app.poi_article_naive_pair gs://pixlake/spark/_warehouse/recommender/poi/poi_article_naive_pair/v1/date=20210802/*.parquet`|upload parquet data (day_partitioned) into bigquery dataset.table with gcs bucket|dataset id should be already exist.
|`bq mk bq_load_codelab`|make a dataset in your project|
|`bq show bq_load_codelab`| viewing the dataset's properties|
|`bq load --source_format=CSV ...`|upload csv data to bigquery|

# GCE

command example|usage|note
-----|-----|-----
`gcloud beta compute ssh --zone "asia-east1" INSTANCE_NAME --project "project_name"`|ssh into compute machine|google will create your account
`gcloud compute ssh INSTANCE_NAME --troubleshoot`|trouble shooting for your computing engine|
`gcloud compute --project "project-id" firewall-rules create INSTANCE_NAME --source-ranges "111.222.333.444/24" --allow tcp:22`|add firwall config on your instance|
`gcloud compute  firewall-rules list \| ag INSTANCE_NAME` | check whatever the firewall rules applied on your VM|
`gcloud compute --project "project-id" ssh INSTANCE_NAME --zone "asia-east1-a" --command 'echo "Hello World"'`| hello world using gcloud ssh| the auth will expired

備註 : 無Domain Name時，使用外部ip連線
e.g. ssh user_name@machine_name

https://console.cloud.google.com/compute/instancesDetail/zones/asia-east1-b/instances/joe-lab?authuser=3&hl=zh-TW&project=pixnet-gt&rif_reserved


`gcloud compute`, `gcloud alpha compute`, `gcloud beta compute`

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

`gcloud compute --project "project-id" firewall-rules create INSTANCE_NAME --source-ranges "111.222.333.444/24" --allow tcp:22`

-- source-ranges 如果寫 0:0:0:0/0 表示都可以連

`gcloud compute --project "project-id" ssh INSTANCE_NAME --zone "asia-east1-a" --command 'echo "Hello World"'` - 透過 gcloud ssh 連線進機器，然後 hello world

[ref - roubleshooting SSH errors](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors#ssh_troubleshooting_tool)

[GCP上建置 firewall 防火牆](https://ikala.cloud/gcp-firewall-waf/)

[How to open a specific port such as 9090 in Google Compute Engine](https://stackoverflow.com/questions/21065922/how-to-open-a-specific-port-such-as-9090-in-google-compute-engine)