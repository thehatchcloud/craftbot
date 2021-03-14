# craftbot
A Minecraft control bot for Discord, written in Python

## Development Setup

The following tools are needed:

1. Docker
2. Python
3. Code editor (I'm using Visual Studio Code)

### Load a development server in Docker

Get the development server up and running:

```bash

docker run -it -p 25565:25565 ubuntu:bionic

```

Upon login update the server, and install necessary tools:

```bash

> apt-get update && apt-get upgrade
> apt-get install wget screen rsync zip jq cron openjdk-8-jdk-headless

```

Install the Minecraft Server Manager tool (you'll need to follow the manual steps because the automated scripts are all written using sudo and the docker container is logged in as root):

```bash

wget https://git.io/6eiCSg -O /etc/msm.conf
mkdir -p /opt/msm
useradd minecraft --home /opt/msm
chown -R minecraft:minecraft /opt/msm
chmod -R 775 /opt/msm
mkdir /dev/shm/msm
chown -R minecraft:minecraft /dev/shm/msm
chmod -R 775 /dev/shm/msm
wget https://git.io/J1GAxA -O /etc/init.d/msm
chmod 755 /etc/init.d/msm
ln -s /etc/init.d/msm /usr/local/bin/msm
msm update
wget https://git.io/pczolg -O /etc/cron.d/msm
service cron reload
msm jargroup create minecraft minecraft

```

