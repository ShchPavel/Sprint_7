import pytest

from helpers import DataGenerator
from project_requests.register_courier import register_new_specific_courier_and_return_response
from project_requests.courier_login import login_known_courier_and_return_response
from project_requests.delete_courier import delete_specific_courier


@pytest.fixture
def create_temp_courier():
    login = str(DataGenerator.generate_random_string())
    password = str(DataGenerator.generate_random_string())
    first_name = str(DataGenerator.generate_random_string())
    try:
        reg_response = register_new_specific_courier_and_return_response(login, password, first_name)
        if reg_response.status_code == 201:
            yield login, password
    except Exception as ex:
        print(ex)
    finally:
        login_response = login_known_courier_and_return_response(login, password)
        courier_id = login_response.json()['id']
        delete_specific_courier(courier_id)




