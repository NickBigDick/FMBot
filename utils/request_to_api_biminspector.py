import requests
from config_data.config_biminspector import headers, headers_json


def send_request_to_api(url, method=None, jsonn=None, params=None, data=None):
    try:
        if jsonn:
            response = requests.request("POST", url, headers=headers_json, json=jsonn)
            if response.status_code == requests.codes.ok:
                return response
        if params:
            response = requests.request("GET", url, headers=headers, params=params)
            if response.status_code == requests.codes.ok:
                return response
        if data:
            response = requests.request("POST", url, headers=headers_json, data=data)
            if response.status_code == requests.codes.ok:
                return response
        if all([jsonn is not None, method == "PUT"]):
            response = requests.request("PUT", url, headers=headers, json=jsonn)
            if response.status_code == requests.codes.ok:
                return response
        else:
            response = requests.request("GET", url, headers=headers)
            if response.status_code == requests.codes.ok:
                return response
    except:
        print('Ошибка в запросе')