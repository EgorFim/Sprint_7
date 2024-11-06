import allure
import requests
from data import BASE_URL

class TestLoginCourier:

    @allure.title('Тест на правильный статус-код в ответе при залогинивании курьера')
    @allure.description('Создаем курьера, логиним его в ситему и смотрим статус-код в теле ответа')
    def test_successful_login(self,courier):
        login_data = courier.register_new_courier_and_return_all_information()[0]
        payload = {
    "login": login_data[0],
    "password": login_data[1]
}
        response = requests.post(f'{BASE_URL}courier/login',data=payload)
        assert response.status_code == 200

    @allure.title('Тест что система возвращает id курьера при успешном логине')
    @allure.description('Залогиниванием курьера и проверяем id в теле ответа')
    def test_successful_login_and_return_id(self, courier):
            login_data = courier.register_new_courier_and_return_all_information()[0]
            payload = {
                "login": login_data[0],
                "password": login_data[1]
            }
            response = requests.post(f'{BASE_URL}courier/login', data=payload)
            r = response.json()
            assert r['id']


    @allure.title('Тест на возвращении ошибки при залогинивании курьера без заполнения пароля')
    @allure.description('Логиним курьера без пароля и ждем ответа системы в соответствии с документацией')
    def test_login_without_password(self,courier):
        login_data = courier.register_new_courier_and_return_all_information()[0]
        payload = {
            "login": login_data[0],
            "password": ''
        }
        response = requests.post(f'{BASE_URL}courier/login', data=payload)
        r = response.json()
        assert response.status_code == 400 and r['message'] == "Недостаточно данных для входа"


    @allure.title('Тест на ответ системы при залогинивании с неверными данными')
    @allure.description('Залогинивание курьера с неверным паролем и ожидание ответа системы соответственно документации')
    def test_login_with_wrong_data(self,courier):
        login_data = courier.register_new_courier_and_return_all_information()[0]
        payload = {
            "login": login_data[0],
            "password": login_data[2]
        }
        response = requests.post(f'{BASE_URL}courier/login', data=payload)
        r = response.json()
        assert response.status_code == 404 and r['message'] == "Учетная запись не найдена"








