# Pub-Sub

[ref - GCP pubsub](https://cloud.google.com/pubsub/docs/publish-receive-messages-client-library)

* reliably
* quickly
* asynchronously
* Producer --> Topic --> subscriber
* Cloud Shell / client lib / RESTAPI
* **At least once guarantee** - Pub/Sub occasionally `delivers a message more than once` to `ensure that all messages make it to a subscriber at least once.`

create topic by : `gcloud pubsub topics create my-topic`
create subscriptions and link topic by : `gcloud pubsub subscriptions create my-sub --topic my-topic`

`pubsub_py/publisher.py`, `pubsub_py/subscriber.py`

# Comparision

|Entity|BigQuery|PubSub|
|------|--------|------|
|Dataset|Dataset|N/A|
|Table|Table|Topic / Subscription|
|Schema|Table Schema|Schema|