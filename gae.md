# Google App Engine

[Third Party Introduction](https://medium.com/@dada8397/%E5%BE%9E%E9%9B%B6%E9%96%8B%E5%A7%8B%E7%9A%84gcp%E4%B9%8B%E6%97%8501-google-app-engine-2a7f375c2928)

[doc](https://cloud.google.com/appengine/docs/flexible/python/quickstart?hl=zh-tw)


1. Serveless
2. get configs in `app.yaml`
   1. handlers : a list of URL patterns and descriptions of how they should be handled

# Hello world

Check this [Third Party Introduction](https://medium.com/@dada8397/%E5%BE%9E%E9%9B%B6%E9%96%8B%E5%A7%8B%E7%9A%84gcp%E4%B9%8B%E6%97%8501-google-app-engine-2a7f375c2928)


`git clone https://github.com/dada8397/gae-demo`

the app.yaml

```
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /
  static_files: www/index.html
  upload: www/index.html

- url: /(.*)
  static_files: www/\1
  upload: www/(.*)
```

check your own gcp projects

1. list project

```
(base) joetsai@thor:~/work/yulong/gae-demo$ gcloud config list
[core]
account = joetsai@pixnet.tw
disable_usage_reporting = True
project = pixnet-gt

Your active configuration is: [default]
```

1. deploy your gae by 

```
$ gcloud config set project helloworld-277717
$ gcloud app deploy
```

or 

```
gcloud app deploy --project=helloworld-277717
```

then you will get

```
(base) joetsai@thor:~/work/yulong/gae-demo$ gcloud app deploy --project=pixnet-research-lab
Services to deploy:

descriptor:      [/home/joetsai/work/yulong/gae-demo/app.yaml]
source:          [/home/joetsai/work/yulong/gae-demo]
target project:  [pixnet-research-lab]
target service:  [default]
target version:  [20210427t231206]
target url:      [https://pixnet-research-lab.df.r.appspot.com]

```

2. Done!

```
Beginning deployment of service [default]...
╔════════════════════════════════════════════════════════════╗
╠═ Uploading 3 files to Google Cloud Storage                ═╣
╚════════════════════════════════════════════════════════════╝
File upload done.
Updating service [default]...done.
Setting traffic split for service [default]...done.
Deployed service [default] to [https://pixnet-research-lab.df.r.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse --project=pixnet-research-lab
```

3. You can check the service tab of `app engine` to monitor your services.

# Quickstart for Python in the App Engine Flexible Environment


[follow by the google app engine for python doc](https://cloud.google.com/appengine/docs/flexible/python/quickstart?hl=zh-tw)

[`app.yaml` documentation](https://cloud.google.com/appengine/docs/standard/python3/config/appref)

# Settings

## `app.yaml` config

[Configuring your App with app.yaml](https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml)


[app.yaml Configuration File](https://cloud.google.com/appengine/docs/flexible/python/reference/app-yaml)


example

```
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

runtime: python
env: flex
entrypoint: gunicorn -b :$PORT main:app

runtime_config:
  python_version: 3

# This sample incurs costs to run on the App Engine flexible environment. 
# The settings below are to reduce costs during testing and are not appropriate
# for production use. For more information, see:
# https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml
manual_scaling:
  instances: 1
resources:
  cpu: 1
  memory_gb: 0.5
  disk_size_gb: 10
```

### Auto-scaling

e.g.

```
automatic_scaling:
  min_num_instances: 1
  max_num_instances: 15
  cool_down_period_sec: 180
  cpu_utilization:
    target_utilization: 0.6
  target_concurrent_requests: 100

```

word|means|note
-----|-----|-----
min_num_instance|min instance given to your service|default = 2 to reduce latency
max_num_instance|max instance given to your service|default = 8, maximum numner is limited by your project resource quota
cool_down_peroid_sec|the number autoscaler should wait before it starts collecting information from a new instance|This value should > 60, default = 120
cpu-utilization|Use this header if you are going to specify the target CPU utilization|
target-utilization|a value to decide increase / decrease instance, CPU use in averaged across all running instance|Default is 0.5
target_concurrent_requests|(Beta, 2021 May) Target concurrent requests per instance, a value to decide increase / decrease instance|no effect if its value is not specified|
min_idle_instances|minimum number of instance for App Engine creating idle instance(0 to 1000)|This functionality sucks|
max_idle_instances|maximum number of instance for App Engine creating idle instance(0 to 1000)|This functionality sucks|

* idle adj. 空閒

Google claims : `min-idle-instance` are ready to support your application in case you receive high traffic or CPU intensive tasks.

Unlike the `min_instance`, they can process your incoming request **immediately**


## `cron.yaml`

[Scheduling Jobs with cron.yaml](https://cloud.google.com/appengine/docs/standard/python3/scheduling-jobs-with-cron-yaml)

example

```
cron:
- description: "daily summary job"
  url: /tasks/summary
  schedule: every 24 hours
- description: "monday morning mailout"
  url: /mail/weekly
  schedule: every monday 09:00
  timezone: Australia/NSW
- description: "new daily summary job"
  url: /tasks/summary
  schedule: every 24 hours
  target: beta
```


## Split traffic

[Splitting Traffic](https://cloud.google.com/appengine/docs/standard/python/splitting-traffic)

There are splitting traffic and migrate traffic.

1. They are basically for A/B Testing and new delopyment config test.
2. **Only supports different version in one serice**

