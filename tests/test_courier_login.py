from project_requests.courier_login import login_known_courier_and_return_response
from helpers import DataGenerator
import allure

class TestCourierLogin:
    @allure.title('Проверка успешного логина с корректными логином и паролем')
    def test_loggining_using_correct_login_and_password_courier_successful(self, create_temp_courier):
        login, password = create_temp_courier
        login_response = login_known_courier_and_return_response(login, password)
        assert login_response.status_code == 200 and 'id' in login_response.text

    @allure.title('Проверка неуспешного логина с использованием только пароля')
    def test_loggining_only_password_fail(self, create_temp_courier):
        login, password = create_temp_courier
        login_response = login_known_courier_and_return_response(password=password)
        assert login_response.status_code == 400 and login_response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка неуспешного логина с использованием только логина')
    def test_loggining_only_login_fail(self, create_temp_courier):
        login, password = create_temp_courier
        login_response = login_known_courier_and_return_response(login=login)
        assert login_response.status_code == 504

    @allure.title('Проверка неуспешного логина с некорректным паролем')
    def test_loggining_incorrect_password_fail(self, create_temp_courier):
        login, password = create_temp_courier
        login_response = login_known_courier_and_return_response(login=login, password=DataGenerator.generate_random_string())
        assert login_response.status_code == 404 and login_response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка неуспешного логина с некорректным логином')
    def test_loggining_incorrect_login_fail(self, create_temp_courier):
        login, password = create_temp_courier
        login_response = login_known_courier_and_return_response(login=DataGenerator.generate_random_string(), password=password)
        assert login_response.status_code == 404 and login_response.json()['message'] == 'Учетная запись не найдена'



