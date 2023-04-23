import requests
import json
from autogpt.config import Config



CFG = Config()

def bam_chat_message(model, messages,temperature, max_tokens):

    url = "https://bam-api.res.ibm.com/v1/generate"
    print('messages: \n')
    messages_list = [ m['content'] for m in messages]
    print( "\n".join(messages_list))
    payload = json.dumps({
    "model_id": model,
    "inputs": [ "\n".join(messages_list)],
    "parameters": {
        "decoding_method": "sample",
        "temperature": temperature,
        "top_p": 1,
        "top_k": 50,
        "random_seed": None,
        "repetition_penalty": None,
        "stop_sequences": None,
        "min_new_tokens": max_tokens-1,
        "max_new_tokens": max_tokens
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization':'Bearer '+ CFG.bam_api_key 
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    bam_response_data = response.json()

    # Process and return the response
    print(bam_response_data)
    answer = bam_response_data["results"][0]["generated_text"].strip()

    return answer