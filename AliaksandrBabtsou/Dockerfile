FROM python:3.9.7
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cron

EXPOSE 8000