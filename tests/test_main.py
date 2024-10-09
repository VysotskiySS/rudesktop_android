# file: test_main.py
from faker import Faker
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Основной экран")
class TestMain:

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Запустить службу')
    @allure.testcase("")
    def test_start_service(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.view_and_accept()
        page.click_access_nav_bar()
        page.click_start_service()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Подключиться по ID')
    @allure.testcase("")
    def test_input_id(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.set_id('487765343')
        page.click_connect()
        page.allow_access()
        page.get_screen()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Отправка сообщения в чат')
    @allure.testcase("")
    def test_chat(self, connect_to_device):
        page = MainPage(connect_to_device)
        base = BasePage(connect_to_device)
        new_message = base.faker.text()
        page.send_message_to_chat(new_message)

    # @pytest.mark.main
    # @pytest.mark.smoke
    # @allure.title('Изменить Сервер для подключения')
    # @allure.testcase("")
    # def test_change_server_to_connect(self, connect_to_device):
    #     page = MainPage(connect_to_device)
    #     page.click_settings_nav_bar()
    #     page.change_server()
    #     print('EBANY FLUTTER')

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Смена языка интерфейса')
    @allure.testcase("")
    def test_change_language(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.click_settings_nav_bar()
        page.check_change_language()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Смена темы')
    @allure.testcase("")
    def test_change_theme(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.click_settings_nav_bar()
        page.check_change_theme()
