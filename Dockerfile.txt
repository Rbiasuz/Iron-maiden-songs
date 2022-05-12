FROM python:3.9

ADD requeriments.txt /code/
ADD datasets/ /code/

WORKDIR /code

RUN pip install -r requeriments.txt
