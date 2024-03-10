class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    LOGIN_URL = BASE_URL + '/api/v1/courier/login'
    CREATE_ORDER_URL = BASE_URL + '/api/v1/orders'
    DELETE_COURIER_URL = BASE_URL + '/api/v1/courier'
    GET_ORDERS_URL = BASE_URL + '/api/v1/orders'
    REGISTER_COURIER_URL = BASE_URL + '/api/v1/courier'


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
