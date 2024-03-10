import pytest

from helpers import DataGenerator
from project_requests.register_courier import RegisterCourier
from project_requests.courier_login import CourierLogin
from project_requests.delete_courier import DeleteOrder


@pytest.fixture
def create_temp_courier():
    login = str(DataGenerator.generate_random_string())
    password = str(DataGenerator.generate_random_string())
    first_name = str(DataGenerator.generate_random_string())
    RegisterCourier.register_new_specific_courier_and_return_response(login, password, first_name)
    yield login, password
    login_response = CourierLogin.login_known_courier_and_return_response(login, password)
    courier_id = login_response.json()['id']
    DeleteOrder.delete_specific_courier(courier_id)




