# Steps

1. 開一台虛擬機(e.g. gce)
2. 權限管理 
   - super users / developers
   - ssh
1. 共用 binary
   - conda, httpie, ag, ...
2. 工作環境
   - jupyterhub
   - spark / pyspark
   - flink / pyflink

# JupyterHub

[Install JupyterHub and JupyterLab from the ground up¶ Official](https://jupyterhub.readthedocs.io/en/1.2.1/installation-guide-hard.html)

## 3.1.0

using conda to handle jupyterhub, npm, nodejs and proxy

https://jupyterhub.readthedocs.io/en/3.1.0/quickstart.html

* using `conda`

### Trouble shooting

- cannot login with user name and password

```
c.LocalAuthenticator.create_system_users = True
# solved login only once
# https://stackoverflow.com/questions/73192732/cannot-log-in-with-user-to-jupyterhub-pam-authentication-failed
c.PAMAuthenticator.open_sessions = False


## Allow named single-user servers per user
#  Default: False
# c.JupyterHub.allow_named_servers = False
```

- can bew login with multiple users --> use sudo or [less privileges](https://github.com/jupyterhub/jupyterhub/wiki/Using-sudo-to-run-JupyterHub-without-root-privileges)
  - why not root? - isn't safe 
  - `sudo access restricted to launching and monitoring single-user servers.`
  - install systemwise python by [this](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/) to make sure shawdo user can spawn notebook
    - `add to 2 lines /etc/sudoers`
    - `sudo groupadd jupyterhub` (開 group), `sudo usermod -a -G jupyterhub joetsai` (加到 group), `groups` 檢查 user groups,`groups rhea` 檢查 `rhea` 所在的 group ,  需要重新登入 - [ref](https://www.techrepublic.com/article/how-to-create-users-and-groups-in-linux-from-the-command-line/)
    - `sudo -u rhea python3 -c "import pamela, getpass; print(pamela.authenticate('$USER', getpass.getpass()))"`
    - a lot of error - still a mystery....

## jupyter extension

1. https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html
   1. `conda install -c conda-forge jupyter_contrib_nbextensions`
   2. `conda install -c conda-forge jupyter_nbextensions_configurator`

cmd : `jupyter contrib nbextension install --user`
* 都裝在 user 下 `e.g. /home/username/.jupyter/jupyter_nbconvert_config.json`

cmd : `jupyter nbextensions_configurator enable --user`
* 開啟 UI

## Legacy

0. [check root access](https://superuser.com/questions/553932/how-to-check-if-i-have-sudo-access)
1. we don't have permission in /opt/, we use ~/jupyterhub
   1. `.venv/bin/pip install -U pip` - to prevent missing rust dependency
   2. `.venv/bin/pup install wheel jupyterhub jupyterlab ipywidgets`
   3. `sudo apt install nodejs npm`
      1.`which nodejs`, `which npm` (nodejs 以及他的管理工具)
