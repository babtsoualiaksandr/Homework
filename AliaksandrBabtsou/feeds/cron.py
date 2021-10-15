import requests


def cron_run():
    req = requests.get('http://localhost:8080/items/')
