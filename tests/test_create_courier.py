from helpers import DataGenerator
from project_requests.register_courier import register_new_random_courier_and_return_response, register_new_specific_courier_and_return_response
import allure

class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    def test_random_courier_creating_successful(self):
        test_response = register_new_random_courier_and_return_response()
        assert test_response.status_code == 201 and test_response.text == '{"ok":true}'

    @allure.title('Проверка ошибки при создании курьера, если такой курьер уже был зарегистрирован ранее')
    def test_creating_same_courier_fail(self):
        login = DataGenerator.generate_random_string()
        password_1 = DataGenerator.generate_random_string()
        first_register_random_courier_response = register_new_specific_courier_and_return_response(login, password_1)
        password_2 = DataGenerator.generate_random_string()
        second_register_same_courier_response = register_new_specific_courier_and_return_response(login, password_2)
        assert ((first_register_random_courier_response.status_code == 201
                 and first_register_random_courier_response.text == '{"ok":true}') and
                (second_register_same_courier_response.status_code == 409 and
                 second_register_same_courier_response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'))

    @allure.title('Проверка неуспешного создания курьера c использованием только логина')
    def test_creating_courier_only_login_fail(self):
        login = DataGenerator.generate_random_string()
        response = register_new_specific_courier_and_return_response(login=login)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка неуспешного создания курьера c использованием только пароля')
    def test_creating_courier_only_password_fail(self):
        password = DataGenerator.generate_random_string()
        response = register_new_specific_courier_and_return_response(password=password)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверка неуспешного создания курьера без использования и логина и пароля')
    def test_creating_courier_without_login_and_password_fail(self):
        response = register_new_specific_courier_and_return_response()
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи'
