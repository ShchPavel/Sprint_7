import pytest
import allure
from project_requests.create_order import CreateOrder


class TestCreateOrder:
    @pytest.mark.parametrize('color_list', (
        ['BLACK', 'GREY'],
        ['BLACK'],
        ['GREY'],
        None
    ))
    @allure.title('Проверка создания заказа с передачей параметра "color" : "{color_list}"')
    def test_create_order_different_colors(self, color_list):
        create_order_response = CreateOrder.create_order_with_specific_color(color_list)
        assert create_order_response.status_code == 201 and 'track' in create_order_response.json()
