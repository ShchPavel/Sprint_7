import allure
from project_requests.get_orders import GetOrder


class TestGetOrders:
    @allure.title('Проверка что запрос на получение заказов возвращает в теле список заказов')
    def test_get_orders_return_id_list_success(self):
        order_list = []

        response = GetOrder.get_orders_without_parameters()
        for collection in response.json()['orders']:
            order_list.append(collection['id'])
        assert len(order_list) > 0
