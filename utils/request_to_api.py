import requests
from config_data.config import create_headers, create_headers_json


def send_request_to_api(url, method=None, jsonn=None, params=None, data=None, files=None):
    try:
        if jsonn:
            response = requests.request("POST", url, headers=create_headers_json(), json=jsonn)
            if response.status_code == requests.codes.ok:
                return response
        if params:
            response = requests.request("GET", url, headers=create_headers(), params=params)
            if response.status_code == requests.codes.ok:
                return response
        if data:
            response = requests.request("POST", url, headers=create_headers_json(), data=data)
            if response.status_code == requests.codes.ok:
                return response
        if all([jsonn is not None, method == "PUT"]):
            response = requests.request("PUT", url, headers=create_headers(), json=jsonn)
            if response.status_code == requests.codes.ok:
                return response
        if files:
            response = requests.post(url, headers=create_headers(), files=files)
            if response.status_code == requests.codes.ok:
                return response
        if method == "DELETE":
            response = requests.delete(url, headers=create_headers())
            if response.status_code == requests.codes.ok:
                return response
        else:
            response = requests.request("GET", url, headers=create_headers())
            if response.status_code == requests.codes.ok:
                return response
    except:
        print('Ошибка в запросе')