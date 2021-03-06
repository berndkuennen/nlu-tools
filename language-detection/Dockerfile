
##
## Dockerfile to build a small web service with polyglot
## to detect the language of some text
##

## -- build & run --
## $ docker build   -t detect:0.1
## $ docker run --name detect --rm -d -p 5000:5000 detect:0.1
## then point your browser to http://localhost:5000/
## (if running on your local computer)

#-- get os and update
FROM ubuntu:18.04 as base
RUN apt-get update      \
 && apt-get upgrade -y  \
 && apt-get install -y  software-properties-common  curl

#-- install python, then clean up
FROM base as python3
RUN apt-get install python3 python3-pip -y && \
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

#-- create wsgi web server 
FROM python3 as wsgi
RUN  python3 -m pip install uwsgi flask
RUN  groupadd wsgi \
 &&  useradd -g wsgi -s /bin/sh wsgi

#-- first install libicu (uses https sources) and git client, plus numpy
FROM wsgi
RUN  apt-get -y install apt-transport-https     \
 &&  apt-get update                             \
 &&  apt-get -y install libicu-dev git          \
 &&  python3 -m pip  install numpy

# polyglot can't be installed via pip in 16.7.4
# see: https://github.com/aboSamoor/polyglot/issues/100
RUN  python3 -m pip  install  -U git+https://github.com/aboSamoor/polyglot.git@master

WORKDIR   /flask
COPY *.py /flask/

#-- start web service on port 5000
EXPOSE 5000
CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --uid wsgi -w wsgi:app

