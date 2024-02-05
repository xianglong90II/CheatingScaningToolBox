import requests
import json
API_URL = "https://api-inference.huggingface.co/models/K024/mt5-zh-ja-en-trimmed"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = b''
        for chunk in response.iter_content(chunk_size=1024):
            data += chunk
        return json.loads(data.decode('utf-8'))
    # return response.json()
    # return response.text

def hf_translate(text,options):
    if options == "jpn" or options == "jp" or options == "ja":
        output = query({
            "inputs": "ja2zh: "+ str(text)
        })
        # print("inputs"+"ja2zh: "+ str(text))
    elif options == "en":
        output = query({
            "inputs": "en2zh: "+ str(text)
        })
        # print(type(output[0]))
    print(output)
    # return output[0]["translation_text"]
    return output

# print(hf_translate("good morning","en"))

