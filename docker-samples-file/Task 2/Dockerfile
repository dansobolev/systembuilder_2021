FROM ubuntu:16.04

# downloading Python
RUN apt-get update \
  && apt-get install -y python3-pip python3-venv \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# downloading certain packages
RUN pip3 install -r requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

#EXPOSE 8080

CMD ["python3", "count_frontpage_numbers.py"]




