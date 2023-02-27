## Getting start on google

https://cloud.google.com/kubernetes-engine/docs/deploy-app-cluster#dockerfile

https://cloudonair.withgoogle.com/events/taiwan-cloud-onboard-architecturemodernization-2021/watch?talk=d1-session2


1. install docker runtime
2. [install kubectl binary. - official](https://kubernetes.io/zh-cn/docs/tasks/tools/install-kubectl-linux/)

NOTE:

* 可以手動開也可以 command line 開
* NodePool - 不同的 VM 屬性(例如需要 GPU)

## Create the Cluster

* `gcloud container clusters create-auto hello-cluster \
    --region='us-west1'` - create hello world cluster

`NOTE`
* Cluster & node(GCE)
  * at lease 1 cluster control plane machine
  * N+ worker machines (nodes), nodes are GCE


```bash
(base) joetsai@joelab:~$ gcloud container clusters create-auto hello-cluster     --region='us-west1'
Note: The Pod address range limits the maximum size of the cluster. Please refer to https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr to learn how to optimize IP address allocation.
Creating cluster hello-cluster in us-west1... Cluster is being health-checked...done.
Created `website-endpoint`
To inspect the contents of your cluster, go to: 
CRITICAL: ACTION REQUIRED: gke-gcloud-auth-plugin, which is needed for continued use of kubectl, was not found or is not executable. Install gke-gcloud-auth-plugin for use with kubectl by following https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke
kubeconfig entry generated for hello-cluster.
NAME           LOCATION  MASTER_VERSION   MASTER_IP    MACHINE_TYPE  NODE_VERSION     NUM_NODES  STATUS
hello-cluster  us-west1  1.24.9-gke.3200  a.b.c.d.  e2-medium     1.24.9-gke.3200  3          RUNNING
```

* we just created a 3 nodes cluster with e2-medium.

## Register kubectl to access the cluster

* [`gcloud components install gke-gcloud-auth-plugin`](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke) - to install plugin makes `kubectl` can access gke (if you use mac for this)
* verify by : `gke-gcloud-auth-plugin --version `
* `gcloud container clusters get-credentials --region us-west1 hello-cluster` - make kubectl can use the cluster
* make sure the service account has gke permission (using IAM)

* GCE 上的話，要自己裝分開的 gcloud
```
(base) joetsai@joelab:~$ gcloud components install kubectl gke-gcloud-auth-plugin
ERROR: (gcloud.components.install) You cannot perform this action because this Google Cloud CLI installation is managed by an external package manager.
Please consider using a separate installation of the Google Cloud CLI created through the default mechanism described at: https://cloud.google.com/sdk/
```

## Create the Deployment

* `kubectl create deployment hello-server \
    --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0` (from google artifact registry)

* create a deployment plan named hello-server
* using image from Artifact Registry, us-docker.pkg.dev/google-samples/containers/gke/hello-app
* `:1.0` is the image version

## Expose the Deployment

* After deploying, expose it to the internet so that users can access it.
* create a service (`--type LoadBalancer`) port 80
  * worker port (target-port) `8080`

# Inspect and view the application

`kubectl get pods` - check the Pod

`kubectl get service` - check the serivce

```
NAME           TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
hello-server   LoadBalancer   a.b.c.d   e.f.g.h   80:32287/TCP   3m53s
```

check `e.f.g.h:80`

the Dockerfile we just deploy with the loadbalancer

```
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM golang:1.19.2 as builder
WORKDIR /app
RUN go mod init hello-app
COPY *.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /hello-app

FROM gcr.io/distroless/base-debian11
WORKDIR /
COPY --from=builder /hello-app /hello-app
ENV PORT 8080
USER nonroot:nonroot
CMD ["/hello-app"]

```