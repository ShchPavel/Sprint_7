import requests
from data import Urls
import allure


@allure.step('Получаем список заказов')
def get_orders():
    response = requests.get(Urls.base_url + '/api/v1/orders')
    return response

