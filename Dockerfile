FROM python:3.6

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY ./manage.py /app
COPY . /app