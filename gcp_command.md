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
`gcloud beta compute ssh --zone "asia-east1" "research-hulk" --project "pixnet-gt"`|ssh into compute machine|google will create your account

備註 : 無Domain Name時，使用外部ip連線
e.g. ssh user_name@machine_name

https://console.cloud.google.com/compute/instancesDetail/zones/asia-east1-b/instances/joe-lab?authuser=3&hl=zh-TW&project=pixnet-gt&rif_reserved


`gcloud compute`, `gcloud alpha compute`, `gcloud beta compute`

