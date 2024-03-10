import requests
from data import Urls
import allure


class DeleteOrder:
    @staticmethod
    @allure.step('Удаляем курьера, используя его id')
    def delete_specific_courier(courier_id):
        response = requests.delete(Urls.delete_courier_url + str(courier_id))
        return response
