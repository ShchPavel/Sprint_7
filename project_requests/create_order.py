import copy
import json
import allure
import requests
from data import Urls, OrderBody


class CreateOrder:
    @staticmethod
    @allure.step('Создаем новый заказ')
    def create_order_with_specific_color(color_list=None):
        payload = copy.deepcopy(OrderBody.order_body_without_color)
        if color_list is not None:
            payload['color'] = color_list
        response = requests.post(Urls.CREATE_ORDER_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json; charset=utf-8'})
        return response

