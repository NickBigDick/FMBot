import requests
import json

webhook_url = 'https://3fdf-141-101-202-151.eu.ngrok.io'
webhook_url = 'http://127.0.0.1:5000/user/anal'

data = {'name': 'Коля',
        'result': 'Здесь будет информация из FM, которую мы обработаем и отправим пользователю'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
