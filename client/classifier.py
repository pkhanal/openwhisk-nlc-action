import requests
import json

CLASSIFIER_URL = ("https://gateway.watsonplatform.net/"
                  "natural-language-classifier/api/v1/"
                  "classifiers/{}/classify")


def classify(config):
    classifier_id = config.get('classifier_id')
    username = config.get('username')
    password = config.get('password')
    input_text = config.get('text')
    classifier_url = CLASSIFIER_URL.format(classifier_id)
    response = requests.get(classifier_url, dict(text=input_text), auth=(username, password))
    response_payload = response.json()
    classes = {classifier_class.get('class_name'): classifier_class.get('confidence')
               for classifier_class in response_payload.get('classes')}
    result = {'text': input_text, 'classes': classes}
    print(json.dumps(result))