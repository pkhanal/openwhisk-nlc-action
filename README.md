# openwhisk-nlc-action
An OpenWhisk docker action that uses Watson Natural Language Classifier to classify input text.

# Overview
In the next few sections, we will see how to build serverless cognitive solution to apply natural language processing to an input text using Watson Natural Language Classifier and open technologies such as IBM OpenWhisk & Docker.

## Use case
Let's say we want to develop a natural language interface to to interact with an IoT device. To make things simple, lets assume that we are dealing with a **Fan** as an IoT device.

# Components Involved
- [Watson Natural Language Classifier](https://www.ibm.com/watson/developercloud/nl-classifier.html)
- [OpenWhisk](https://new-console.ng.bluemix.net/openwhisk/)
- [Docker Container](https://www.docker.com/)

# Setup Watson Natural Language Classifier
Watson NLC enables developers to create natural language interface for their application. The service interprets the intent behind text and returns a corresponding classification with associated confidence levels. You can find the details of Watson NLC [here](https://www.ibm.com/watson/developercloud/nl-classifier.html).

For this demo, we will use [Watson NLC toolkit](https://www.ibm.com/watson/developercloud/doc/nl-classifier/tool_overview.shtml) to manage classifier. It is simple to get started with NLC toolkit as it provides a visual interface to define classes, add training data, create classifier, test the classifier.

The natural language interface take an input text, process it through Watson NLC and enable user to interact with the device in following ways:
 - query if device is operational
 - turn on the device
 - turn off the device

You can see the sample classes and training data created using NLC toolkit in the screenshot below:

![Training](screenshots/train.png "NLC Toolkit")

Here, we have created few classes and added some training data to create a classifier. Normally, you will go through multiple iteration depending on the size of the training data to ensure that classification works as expected for new texts.

# OpenWhisk Action
(OpenWhisk)[https://developer.ibm.com/openwhisk/] provides a distributed compute service to execute application logic in response to events. It is similar to other serverless computing platforms such as [AWS Lambda](https://aws.amazon.com/lambda/), [Azure Functions](https://azure.microsoft.com/en-us/services/functions/), [Google Cloud Functions](https://cloud.google.com/functions/), [webtask](https://webtask.io/) etc..

We will create a [docker action](https://console.ng.bluemix.net/docs/openwhisk/openwhisk_actions.html#openwhisk_actions_docker) for this example. The logic is written is python ([classifier.py](docker-action/client/classifier.py)). The logic uses the Natural Language Classifeir created earlier to process the input text and outputs the response that tells whether the input text is querying the state of the IoT device or it is trying to control the IoT device.

The example response when the input text is "turn on the fan":
```
{
  "text": "turn on the fan",
  "classes": {
    "command": 0.6486486486486487,
    "off": 0,
    "query": 0,
    "on": 0.35135135135135137
  }
}
```
The response is a bit raw but it tells you that the text is a **command** and it is trying to change the state of the device to **on**.

# Conclusion
This was a quick and high level walkthrough on how we can build serverless natural language interface that can be extended to IoT solution. We also saw that with OpenWhisk we don't have to worry about provisioning and managing the server. The input text for this example can come from different sources which can trigger OpenWhisk action and the output can be used to interact with IoT device. In future articles, we will show how can we trigger OpenWhisk actions based on sms, voice or other events.
 
