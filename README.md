# openwhisk-nlc-action
An OpenWhisk docker action that uses Watson Natural Language Classifier to classify input text.

# Overview
In the next few sections, we will see how to build serverless solution to apply natural language processing to an input text using Watson Natural Language Classifier and open technologies such as IBM OpenWhisk & Docker.

# Components Involved
- [Watson Natural Language Classifier](https://www.ibm.com/watson/developercloud/nl-classifier.html)
- [OpenWhisk](https://new-console.ng.bluemix.net/openwhisk/)
- [Docker Container](https://www.docker.com/)

# Setup Watson Natural Language Classifier
Watson NLC enables developers to create natural language interface for their application. The service interprets the intent behind text and returns a corresponding classification with associated confidence levels. You can find the details of Watson NLC [here](https://www.ibm.com/watson/developercloud/nl-classifier.html).

For this demo, we will use [Watson NLC toolkit](https://www.ibm.com/watson/developercloud/doc/nl-classifier/tool_overview.shtml) to manage classifier.
