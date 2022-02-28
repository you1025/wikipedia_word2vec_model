FROM python:3.9-slim

RUN apt update
RUN apt -y upgrade

RUN apt install -y sudo git build-essential curl file
RUN apt install -y mecab libmecab-dev mecab-ipadic-utf8

RUN pip install --upgrade pip
RUN pip install wikiextractor gensim

COPY ./src/data/ /usr/local/src/data/
COPY ./src/make_data.sh /usr/local/src/make_data.sh

# タイムゾーンを JST に変更
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

