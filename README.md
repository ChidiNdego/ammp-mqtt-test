# AMMP MQTT Task: Data Acquisition From MQTT Broker

## Task 1: Conceptual Part

### Question 1

#### What pros and cons do you see with respect to obtaining readings from an MQTT broker, vs getting them via a REST API?

MQTT is a lightweight publish/subscribe architecture that is designed for resource-constrained devices and low-bandwidth setups. It is used a lot for Internet of Things devices, or other machine-to-machine communication.

Pros:
* Designed for resource-constrained devices
* Best for low-bandwidth setups
* 

Cons:
* Useful for sending only small portions of data to servers
* 

### Question 2

#### How would you run an acquisition function that subscribes to an MQTT broker? For example would you trigger it periodically via a scheduler, or would you have it running as some sort of continuous "listener" function?

### Question 3

#### What underlying AWS service would you run it on? E.g. EC2 vs ECS vs Lambda, etc.


## Task 2: Conceptual Part

| Details            |              |
|-----------------------|---------------|
| Programming Language: |  Python 3  |

### What it Does

The `app.py` application aims to connect to AMMP's MQTT staging server, subscribes to a topic, receives a message dumped to JSON and eventually outputs the necessary information about some remote IoT device.

### Setup

* Clone this repository
* Navigate to repository path
* Open a terminal to install the necessary dependencies

```
pip3 install -r requirements.txt
```

* Run app with the following command-line argument

```
app.py -n <hostname> -p <port> -t <topic> -u <username> -P <password> --cafile <certification_file>
```

With the right credentials, you should have an output similar to this below:

![Sample Payload Output](./images/sample_output.png)