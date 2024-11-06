import allure
import requests
from data import BASE_URL,ORDER_2,ORDER_3,ORDER_1


class OrderMethods:
    @allure.step('Создаем заказ')
    def create_order(self,params):
        response = requests.post(f'{BASE_URL}orders', json=params)
        r = response.json()
        return response.status_code, r['track']




