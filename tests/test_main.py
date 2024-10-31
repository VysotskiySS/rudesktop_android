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
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=113")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=114")
    def test_start_service(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.stop_service()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Авторизоваться (войти)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?est_case=116")
    def test_login(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.ok_warning_server_to_connect()
        page.start_service()
        page.login()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Авторизоваться (войти) через кнопку в адресной книге')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?est_case=162")
    def test_login_address_book(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.ok_warning_server_to_connect()
        page.start_service()
        page.login_address_book()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Подключиться по ID')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=115")
    def test_connect_from_id(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.close_connection()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменить Сервер для подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=118")
    def test_change_server_to_connect(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.change_server()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Смена языка интерфейса')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=119")
    def test_change_language(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.check_change_language()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Смена темы')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=120")
    def test_change_theme(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.check_change_theme()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Сброс настроек')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=131")
    def test_reset_settings(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.reset_settings()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('О программе')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=140")
    def test_about_app(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.click_about_app()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Установка постоянного пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=132")
    def test_set_permanent_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_set_permanent_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменение длины временного пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=133")
    def test_set_len_temp_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_set_len_temp_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Копирование ID и пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=134")
    def test_copy_id_and_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_copy_id_and_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Проверка создания, переименования, удаления и тп тега')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=165")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=164")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=169")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=167")
    def test_tag(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.check_tag()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Запускать после включения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=194")
    def test_start_service_after_start_app(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.start_service()
        page.click_settings_nav_bar()
        page.start_service_after_start()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Добавить в адресную книгу / Удалить из адресной книги')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=124")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=125")
    def test_add_and_delete_from_address_book(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.login()
        page.clear_address_book()
        page.click_connection_nav_bar()
        page.add_to_address_book()
        page.clear_address_book()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Добавить в избранное / Удалить из избранного')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=122")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=123")
    def test_add_and_delete_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.login()
        page.clear_favorites()
        page.click_connection_nav_bar()
        page.add_to_favorites()
        page.clear_favorites()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Задать псевдоним устройству')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=128")
    def test_set_alias(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.close_connection()
        page.clear_last_seanses()
        page.check_set_alias()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Обновление временного пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=173")
    def test_update_temp_pass(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.start_service()
        page.update_temp_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Всегда подключаться через мост')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=139")
    def test_always_connect_from_bridge(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.check_icon_connection_color(251, 255, 253)
        page.activate_connect_always_from_bridge()
        page.reconnect()
        page.check_icon_connection_color(62, 125, 70)
