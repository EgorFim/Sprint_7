import allure
import requests
from data import BASE_URL

class TestCreateCourier:
    @allure.title('Проверка соответствия статус-кода при создании курьера')
    @allure.description('Создаем курьера и проверяем статус-код из ответа')
    def test_create_courier_status_code(self,courier):
        courier.register_new_courier_and_return_all_information()
        assert courier.register_new_courier_and_return_all_information()[1] == 201

    @allure.title('Тест на ошибку при создании курьера с существующим логином')
    @allure.description('Создаем одного курьера и пытаемся создать второго курьера с логином первого')
    def test_create_another_courier_with_same_login(self,courier):
        courier.register_new_courier_and_return_all_information()
        login_pass = courier.register_new_courier_and_return_all_information()[0]
        payload = {
    "login": login_pass[0],
    "password": login_pass[1],
    "firstName": login_pass[2]
}
        response = requests.post(f'{BASE_URL}courier',data=payload)
        r = response.json()
        assert response.status_code == 409 and r['message'] == "Этот логин уже используется. Попробуйте другой."


    @allure.title('Тест на ошибку при создании курьера без указания логина')
    @allure.description('Создаем курьера без данных в поле логин и ждем ошибки')
    def test_create_courier_without_all_information(self,courier):
        payload ={
            "login": "",
            "password": "1234",
            "firstName": "saske"
        }
        response = requests.post(f'{BASE_URL}courier', data=payload)
        r = response.json()
        assert r['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Тест на наличии данных в теле ответа при создании курьера')
    @allure.description('Создаем курьера и проверяем данные в теле ответа')
    def test_create_courier_response_body(self,courier):
      assert courier.register_new_courier_and_return_all_information()[2] == {"ok":True}

    @allure.title('Тест на наличии ошибки при создании курьера если нет одного из полей')
    @allure.description('Отправляем запрос на создание курьера без поля login')
    def test_create_courier_without_one_of_field(self,courier):
        payload ={
            "password": "1234",
            "firstName": "saske"
        }
        response = requests.post(f'{BASE_URL}courier', data=payload)
        r = response.json()
        assert r['message'] == 'Недостаточно данных для создания учетной записи'





