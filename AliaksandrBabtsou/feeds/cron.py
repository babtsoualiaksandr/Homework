import requests


def cron_run():
    req = requests.get('http://localhost:8000/items/')
    print(req.url)
    print(req.text)
