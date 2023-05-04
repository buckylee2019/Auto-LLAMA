FROM python:3.10-slim

RUN apt-get update \
&& apt-get install -y build-essential curl wget g++ git make snap python3-venv    
RUN  curl -fsSL https://deb.nodesource.com/setup_18.x | bash - 
RUN  apt-get update     && apt-get install -y nodejs
RUN git clone https://github.com/keldenl/gpt-llama.cpp.git
RUN git clone https://github.com/ggerganov/llama.cpp \
    && cd llama.cpp\
    && make     \
    && python3 -m pip install -r requirements.txt

WORKDIR /gpt-llama.cpp

EXPOSE 8000
RUN npm install 

CMD ["sh", "-c", "PORT=8000 npm start"]