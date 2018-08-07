## Purpose
This repository serves as a simple example of Kafka using pykafka. Follow the
instructions below to get the sample kafka instance, producer and consumer up and
running.

## Requirements
In order to use this repo, you'll need to have python 3.6+ installed locally. In
addition to python, you'll need [Docker](https://www.docker.com/) setup and running
on your machine.

## Starting Kafka
First things first, you'll need to pull the Docker image for kafka and zookeeper.
The latest version of kafka as of the writing of this document is 1.1.1. To pull
an image with this version, run the following in your terminal:

```
docker pull brandoshmando/kafka
```

From there, you need to get the docker virtual machine up and running with there
following:

```
docker-machine start
```

Once the vm has started, you can map your current terminal env to the vm and
start the kafka instance with the following:

```
eval $(docker-machine env)
docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=`docker-machine ip \`docker-machine active\`` --env ADVERTISED_PORT=9092 brandoshmando/kafka
```

## Producer / Consumer Setup
Before starting the producer / consumer, make sure you have this repo cloned locally
and a virtual environment created / activated with the requirements installed.

Open two terminal windows, side by side, and navigate to the root of this project.
Run the following in both windows to map your env to the running docker vm:

```
eval $(docker-machine env)
```

We need to add two env variables for the producer / consumer instances to reference:

`ZOOKEEPER` - This refers to the host where your zookeeper instance can contacted
`KAFKA` - This refers to the hosts where your kafka instance can contacted


Run the following in both terminal windows:

```
export KAFKA=`docker-machine ip \`docker-machine active\``:9092
export ZOOKEEPER=`docker-machine ip \`docker-machine active\``:2181
```

To start the consumer, run the following one of the terminal windows:

```
python consumer.py
```

To start the producer, run the following in the other terminal window:

```
python producer.py
```

The producer will prompt you for input. Type whatever message you would like,
and hit enter. You should see the message printed out in the consumer's terminal.

Easy peazy!
