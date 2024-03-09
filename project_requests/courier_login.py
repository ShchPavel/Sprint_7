import json
import allure

import requests
from data import Urls


@allure.step('Выполняем логин от имени курьера')
def login_known_courier_and_return_response(login=None, password=None):
    payload = {}

    # Добавляем login в payload только если он был предоставлен
    if login is not None:
        payload["login"] = login

    # Добавляем password в payload только если он был предоставлен
    if password is not None:
        payload["password"] = password

    response = requests.post(Urls.base_url + '/api/v1/courier/login', data=json.dumps(payload), headers={'Content-Type': 'application/json; charset=utf-8'})
    return response
