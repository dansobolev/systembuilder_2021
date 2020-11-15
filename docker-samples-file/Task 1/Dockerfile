FROM ubuntu:latest

MAINTAINER Daniil daniil.sob56@gmail.com

# downloading Git
RUN apt update
RUN apt install -y git

# downloading Python
RUN apt-get update \
  && apt-get install -y python3-pip python3-venv \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


RUN git clone https://github.com/dansobolev/systembuilder_2021 
RUN python3 -m venv myvenv 
RUN /bin/bash -c "source myvenv/bin/activate"
    
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["pip3", "list"]
