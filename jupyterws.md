# JupyterHub WorkStation

<img src='./assets/hub_arct.png'></img> 

[Implementation by docker/gcloud](https://github.com/YLTsai0609/jupyter_workstation)


# Comparsion

## [VertexAI - WorkBench](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/introduction)

pros : 
* easier to getting start (pre installed package)
* integrated with GCP service(scheduling, feature store , ...)

cons : 
* 3rd jupyterlab extension is not supported (nbextension, templates)
* not ssh accessable for the respceted VM


## jupyterhub (install from scrach) + GCE

pros : 

* customized
  * nb-extension supported.
  * ssh accesaable
  * not user mapping issue between host and container

cons : 
* dirty work
* resource management is not the best option compare with each instance.

## jupyterhub (Docker) + GCE

pros : 

* customized
  * nb-extension supported.

cons : 
* more knowledge about docker
* user mapping issue between host and container







