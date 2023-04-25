import sys
import os
import socketio
import time as time
from autogpt.config import Config

CFG = Config()

class NoServerException(Exception):
    pass

class Dalai:

    sio = socketio.Client()

    def __init__(self):
        self.RESULTS = {}
        self.REQ_IDS = []
        self.CURRENT_ID = None
        self.MOST_RECENT_WORD = None
        self.DONE = False
        self.RESULT = None
        self.setup()

    def setup(self):
        # try to connect
        try:
            self.sio.connect('http://159.8.211.43:3000')
        except Exception as e:
            raise NoServerException("NoServerException: No server was found, please make sure you have initiated your Dalai server")

        self.call_backs()

    def call_backs(self):
            @self.sio.on('result')
            def on_request(data):
                # Get this request ID
                req_id = data.get('request',{}).get('id')
                new_word = data.get('response','')
                self.CURRENT_ID = req_id
                
                # And if it's not already in results
                if not req_id in self.RESULTS:
                    # then initially stuff it with this data
                    self.RESULTS[req_id] = data
                    # and add this request id to the last 
                    self.REQ_IDS.append(req_id)
                # If it's already in results
                else:
                    # then simply add the new response word
                    self.RESULTS[req_id]['response'] += new_word    

                self.MOST_RECENT_WORD = str(new_word).strip()
                if self.MOST_RECENT_WORD == "<end>" or self.MOST_RECENT_WORD == "\n":
                    self.DONE = True
                    if self.REQ_IDS and self.RESULTS:
                        # get latest id
                        req_id = self.REQ_IDS[-1]
                        # get result dictionary from latest id as key
                        result = self.RESULTS[req_id]
                        # return result
                        self.RESULT = result

    def generate(self, request):
        self.sio.emit('request', request)
        while not self.DONE:
            time.sleep(0.01)

        # Reset Vars
        self.RESULTS = {}
        self.REQ_IDS = []
        self.CURRENT_ID = None
        self.MOST_RECENT_WORD = None
        self.DONE = False

        return self.RESULT

    def generate_request(self, prompt, model, id='0', n_predict=1024, repeat_last_n=64, repeat_penalty=1.3, seed=-1, temp = CFG.temperature, threads=8, top_k=40, top_p=0.9):
        request = {
            'debug': False, 
            'id':id, 
            'model':model, 
            'models':[model], 
            'n_predict':n_predict, 
            'prompt':prompt, 
            'repeat_last_n':repeat_last_n, 
            'repeat_penalty':repeat_penalty, 
            'seed':seed, 
            'temp':temp, 
            'threads':threads, 
            'top_k':top_k, 
            'top_p':top_p
            }
        return request
    
    def request(self, prompt, prettify=True):
        if prettify == False:
            return self.generate(prompt)

        else:
            response = self.generate(prompt)['response']
            response = response.replace("\n", "")
            response = response.replace("\r", "")
            response = response.replace("<end>", "")
            response = response.replace(prompt['prompt'], "")
            if not response.endswith(".") :
                response += "."
            return response



model = Dalai()

def llama_reply(messages):
   
    inputs = "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request. \n\n \
        ### Instruction: \n" + "\n".join([m['content'] for m in messages]) + "### Response: \n"
    request = model.generate_request(inputs , 'alpaca.7B')
    response = model.request(request)
    
    return (response)

