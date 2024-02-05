import requests, uuid, json

# Add your key and endpoint
# Key was deleted
endpoint = "https://api.cognitive.microsofttranslator.com/"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "japanwest"

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

path = '/translate'
constructed_url = endpoint + path
def aztranslate(text,options,key):
    if options == "jpn" or options == "jp" or options == "ja":
        params = {
            'api-version': '3.0',
            'from':'ja',
            'to': ['zh']
        }
    elif options == "en":
        params = {
            'api-version': '3.0',
            'from':'en',
            'to': ['zh']
        }

    # You can pass more than one object in body.
    body = [{
        'text': str(text)
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    # print(response)
    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    output = response[0]["translations"][0]["text"]#成功
    print(output)
    return output