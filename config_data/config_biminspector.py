import json
from os import path

#токен пока не нужен
token_path = path.abspath(r"C:\USERS\tevosiannkh\AppData\Local\PIK\Auth\cache.json") # noqa
with open(token_path, "r") as f:
    file = json.load(f)
    token = file["access_token"]
headers = {
    #'FmClientType': 'fm-webapp',
    'Authorization': 'Bearer ' + token
}

headers_json = {
    #'FmClientType': 'fm-webapp',
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json; charset=utf-8'
}
