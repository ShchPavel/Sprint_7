from helpers import DataGenerator
from project_requests.register_courier import RegisterCourier
import allure
from data import ResponseText


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    def test_random_courier_creating_successful(self):
        test_response = RegisterCourier.register_new_random_courier_and_return_response()
        assert test_response.status_code == 201 and test_response.text == ResponseText.TEXT_ACCOUNT_CREATED_SUCCESSFULLY

    @allure.title('Проверка ошибки при создании курьера, если такой курьер уже был зарегистрирован ранее')
    def test_creating_same_courier_fail(self):
        login = DataGenerator.generate_random_string()
        password_1 = DataGenerator.generate_random_string()
        first_register_random_courier_response = RegisterCourier.register_new_specific_courier_and_return_response(login, password_1)
        password_2 = DataGenerator.generate_random_string()
        second_register_same_courier_response = RegisterCourier.register_new_specific_courier_and_return_response(login, password_2)
        assert ((first_register_random_courier_response.status_code == 201
                 and first_register_random_courier_response.text == '{"ok":true}') and
                (second_register_same_courier_response.status_code == 409 and
                 second_register_same_courier_response.json()['message'] == ResponseText.ERROR_LOGIN_IS_ALREADY_IN_USE))

    @allure.title('Проверка неуспешного создания курьера c использованием только логина')
    def test_creating_courier_only_login_fail(self):
        login = DataGenerator.generate_random_string()
        response = RegisterCourier.register_new_specific_courier_and_return_response(login=login)
        assert response.status_code == 400 and response.json()['message'] == ResponseText.ERROR_NOT_ENOUGH_INFO_TO_CREATE_ACCOUNT

    @allure.title('Проверка неуспешного создания курьера c использованием только пароля')
    def test_creating_courier_only_password_fail(self):
        password = DataGenerator.generate_random_string()
        response = RegisterCourier.register_new_specific_courier_and_return_response(password=password)
        assert response.status_code == 400 and response.json()['message'] == ResponseText.ERROR_NOT_ENOUGH_INFO_TO_CREATE_ACCOUNT

    @allure.title('Проверка неуспешного создания курьера без использования и логина и пароля')
    def test_creating_courier_without_login_and_password_fail(self):
        response = RegisterCourier.register_new_specific_courier_and_return_response()
        assert response.status_code == 400 and response.json()['message'] == ResponseText.ERROR_NOT_ENOUGH_INFO_TO_CREATE_ACCOUNT
