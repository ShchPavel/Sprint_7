import requests
from data import Urls
import allure

@allure.step('Удаляем курьера, используя его id')
def delete_specific_courier(courier_id):
    response = requests.delete(Urls.base_url + '/api/v1/courier/' + str(courier_id))
    return response
