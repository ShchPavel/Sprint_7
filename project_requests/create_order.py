import copy
import json
import allure

import requests
from data import Urls, OrderBody


@allure.step('Создаем новый заказ')
def create_order(color_list=None):
    payload = copy.deepcopy(OrderBody.order_body_without_color)
    if color_list is not None:
        payload['color'] = color_list
    response = requests.post(Urls.base_url + '/api/v1/orders', data=json.dumps(payload), headers={'Content-Type': 'application/json; charset=utf-8'})
    return response

