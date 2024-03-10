class Urls:
    base_url = 'https://qa-scooter.praktikum-services.ru'
    login_url = base_url + '/api/v1/courier/login'
    create_order_url = base_url + '/api/v1/orders'
    delete_courier_url = base_url + '/api/v1/courier'
    get_orders_url = base_url + '/api/v1/orders'
    register_courier_url = base_url + '/api/v1/courier'


class OrderBody:
    order_body_without_color = {
        "firstName": "1",
        "lastName": "1",
        "address": "1",
        "metroStation": 1,
        "phone": "1",
        "rentTime": 1,
        "deliveryDate": "1",
        "comment": "1"
    }


class ResponseText:
    ERROR_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    ERROR_NOT_ENOUGH_INFO_TO_LOGIN = 'Недостаточно данных для входа'
    TEXT_ACCOUNT_CREATED_SUCCESSFULLY = '{"ok":true}'
    ERROR_LOGIN_IS_ALREADY_IN_USE = 'Этот логин уже используется. Попробуйте другой.'
    ERROR_NOT_ENOUGH_INFO_TO_CREATE_ACCOUNT = 'Недостаточно данных для создания учетной записи'
