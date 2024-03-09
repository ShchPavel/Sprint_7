import allure

from project_requests.get_orders import get_orders


class TestGetOrders:
    @allure.title('Проверка что запрос на получение заказов возвращает в теле список заказов')
    def test_get_orders_return_id_list_success(self):
        order_list = []

        response = get_orders()
        for collection in response.json()['orders']:
            order_list.append(collection['id'])
        assert len(order_list) > 0
