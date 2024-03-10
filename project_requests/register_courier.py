import requests
from helpers import DataGenerator
from data import Urls
import allure


class RegisterCourier:
    @staticmethod
    @allure.step('Регистрируем юзера с рандомнымми логином, паролем, именем')
    def register_new_random_courier_and_return_response():

        login = DataGenerator.generate_random_string()
        password = DataGenerator.generate_random_string()
        first_name = DataGenerator.generate_random_string()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Urls.REGISTER_COURIER_URL, data=payload)

        return response

    @staticmethod
    @allure.step('Регистрируем юзера с определенными логином, паролем, именем')
    def register_new_specific_courier_and_return_response(login=None, password=None, first_name=None):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Urls.REGISTER_COURIER_URL, data=payload)

        return response
