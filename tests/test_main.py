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
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=113")
    def test_start_service(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.stop_service()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Авторизоваться (войти)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=116")
    def test_login_cloud(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.login()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Подключиться по ID')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=115")
    def test_input_id(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.set_id('487765343')
        page.click_connect()
        page.allow_access()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменить Сервер для подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=118")
    def test_change_server_to_connect(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.change_server()
        print('EBANY FLUTTER')

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Смена языка интерфейса')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=119")
    def test_change_language(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.check_change_language()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Смена темы')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=120")
    def test_change_theme(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.check_change_theme()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Сброс настроек')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=131")
    def test_reset_settings(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.reset_settings()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('О программе')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=140")
    def test_about_app(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.click_about_app()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Установка постоянного пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=132")
    def test_set_permanent_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_set_permanent_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменение длины временного пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=133")
    def test_set_len_temp_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_set_len_temp_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Копирование ID и пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?ordering=id&page=1&page_size=100&test_case=134")
    def test_copy_id_and_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_copy_id_and_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Проверка создания, переименования, удаления и тп тега')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?page=1&page_size=1000&test_case=167")
    def test_tag(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.ok_warning_server_to_connect()
        page.login()
        page.check_tag()


