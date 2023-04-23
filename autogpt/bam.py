import requests
import json
from autogpt.config import Config


<<<<<<< HEAD
CFG = Config()

def bam_chat_message(model, messages, temperature, max_tokens):

    url = "https://bam-api.res.ibm.com/v1/generate"
    print(messages)
    messages_list = [ m['content'] for m in messages]
    prepend = "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n \
    ### Instruction: /n"
    postappend = " and describe the thoughts of using this commands. Note that the key in the command dict most be same as the commands list above. \n### Response:   "
    
    payload = json.dumps({
    "model_id": model,
    "inputs": [ prepend + "\n".join(messages_list) + postappend],
    "parameters": {
        "decoding_method": "sample",
        "temperature": temperature,
        "top_p": 0.38,
        "top_k": 47,
        "random_seed": None,
        "repetition_penalty": 1.11,
        "stop_sequences": None,
        "min_new_tokens": 1,
        "max_new_tokens": 1024
    }
    })
    print(prepend + "\n".join(messages_list) + postappend)
=======

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
>>>>>>> 3c9c9c9 (add IBM bam(tested) and alpaca (not test))
    headers = {
    'Content-Type': 'application/json',
    'Authorization':'Bearer '+ CFG.bam_api_key 
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    bam_response_data = response.json()
<<<<<<< HEAD
    
    # Process and return the response
    print(bam_response_data)
    answer = bam_response_data["results"][0]["generated_text"].strip()
    print(answer)
=======

    # Process and return the response
    print(bam_response_data)
    answer = bam_response_data["results"][0]["generated_text"].strip()

>>>>>>> 3c9c9c9 (add IBM bam(tested) and alpaca (not test))
    return answer