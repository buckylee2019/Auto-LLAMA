# Auto-local-GPT: An Autonomous LLM Experiment

 

This project uses [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) to experiment the posibility of using local LLM. 
Reference [gpt-llmam.cpp](https://github.com/keldenl/gpt-llama.cpp) to build custom API. 

## Run
To run the auto-local-gpt:

1. Put the models you'd like to try to certain directory. 
```
For example:  
wget https://huggingface.co/eachadea/ggml-vicuna-13b-1.1/resolve/main/ggml-vicuna-13b-1.1-q4_1.bin
```

2. Set the environment variables to .env

```
EMBED_DIM=5120
OPENAI_API_BASE_URL=localhost:8000/v1
OPENAI_API_KEY=<if use custom url replace it with model path>
```

3. Run the docker command, which will automatically start the API endpoint at port 8000

```bash
docker run -it -d -v <your models directory>:/llama.cpp/models -p 8000:8000 buckylee/auto-local-gpt:latest
```

4. Run Auto-gpt
For Linux:

```bash
./run.sh
```