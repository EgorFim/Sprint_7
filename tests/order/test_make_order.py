import allure
import pytest
import requests
from data import BASE_URL,ORDER_1,ORDER_2,ORDER_3

class TestOrder:
    @allure.title('Тест создания заказа самоката разных цветов')
    @allure.description('Создаем заказы через параметризацию с разными цветами самоката')
    @pytest.mark.parametrize('order_data',[ORDER_1,ORDER_2,ORDER_3])
    def test_make_order_with_any_color_samokat(self,order,order_data):
        responce_order = order.create_order(order_data)
        assert responce_order[0] == 201 and responce_order[1]


    @allure.title('Тест на получение списка заказов в теле ответа на запрос')
    @allure.description('Запрашиваем доступные заказы окло станции метро и проверяем наличие списка в теле ответа')
    def test_receiving_orders_list(self):
        response = requests.get(f'{BASE_URL}orders?limit=10&page=0&nearestStation=["1"]')
        print(response.json()['orders'])











