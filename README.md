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

