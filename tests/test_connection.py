# file: test_connection.py
from faker import Faker
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Экран подключения")
class TestConnection:

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Перезапустить удаленное устройство')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=158")
    def test_reboot_remote_device(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.reboot_remote_device()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Пароль операционной системы')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=150")
    def test_password_os(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.set_password_os()
        page.check_password_os()
        # Нужно добавить проверку на то что действительно прошла авторизация, пока кроме скрина или цвета точки ничего не придумал