
##
## Dockerfile to build a small web service with polyglot
## to detect the language of some text
##

## -- build & run --
## $ docker build -f Dockerfile  -t language-detector:poc .
## $ docker run --rm --detach -p 5000:5000 language-detector:poc
## then point your browser to http://localhost:5000/
## (if running on your local computer)

#-- get os and update, install python, then clean up
FROM ubuntu:latest as python3
RUN  apt-get update			\
 &&  apt-get upgrade -y			\  
 &&  apt-get -y install python3-pip	\
 &&  apt-get clean

#-- create wsgi web server 
FROM python3 as wsgi
RUN  python3 -m pip install uwsgi flask  \
 &&  groupadd wsgi                       \
 &&  useradd -g wsgi -s /bin/sh wsgi

#-- first install icu and git client, plus some python tools
FROM wsgi
RUN  apt-get -y install python3-icu git         \
 &&  pip install -U numpy setuptools

# polyglot can't be installed via pip in 16.7.4
# see: https://github.com/aboSamoor/polyglot/issues/100
RUN  python3 -m pip  install  -U git+https://github.com/aboSamoor/polyglot.git@master

WORKDIR   /flask
COPY *.py /flask/

#-- start web service on port 5000
EXPOSE 5000
CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --uid wsgi -w wsgi:app

