FROM python:3.9

ADD requeriments.txt /code/
ADD datasets/ /code/

WORKDIR /code

RUN python -m pip install --upgrade pip

RUN pip install -r requeriments.txt
