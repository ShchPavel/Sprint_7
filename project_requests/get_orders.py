import requests
from data import Urls
import allure


class GetOrder:
    @staticmethod
    @allure.step('Получаем список заказов')
    def get_orders_without_parameters():
        response = requests.get(Urls.get_orders_url)
        return response

