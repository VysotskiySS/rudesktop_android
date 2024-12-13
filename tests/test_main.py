# file: test_main.py
from faker import Faker
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Основной экран")
class TestMain:

    @pytest.mark.install
    @allure.title('Установка apk с сайта Rudesktop.ru')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=202")
    def test_install_apk_site(self, connect_to_device):
        d = u2.connect('emulator-5554')
        d.app_uninstall(package)
        d.app_install(app_link)
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.check_version('2.7.732')

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
    @allure.title('Войти / Выйти под локальной учетной записью / Выход из учетной записи (выйти)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?est_case=116")
    def test_login(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.ok_warning_server_to_connect()
        page.start_service()
        page.login()
        page.logout()

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
    @allure.title('Авторизоваться (войти) - невалидные данные')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?est_case=201")
    def test_login_invalid(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.ok_warning_server_to_connect()
        page.start_service()
        page.click_settings_nav_bar()
        page.login_invalid()
        page.login_invalid(method='domain')

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Войти / Выйти под доменной учетной записью')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?est_case=200")
    def test_login_domain(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.ok_warning_server_to_connect()
        page.start_service()
        page.login(login=valid_domain_login, method='domain')
        page.logout(login=valid_domain_login, method='domain')

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
    @allure.title('Подключиться из истории / Сохранение пароля')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=129")
    def test_connect_from_history_with_saved_pass(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id(save='yes')
        page.close_connection()
        page.connect_from_history()
        page.check_connection_screen()
        page.close_connection()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Подключиться по невалидному ID')
    @allure.testcase("")
    def test_connect_from_invalid_id(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_invalid_id()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Изменить Сервер для подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=118")
    def test_change_server_to_connect(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.click_settings_nav_bar()
        page.change_server(server_to_connect)
        # page.connect_from_id()

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
    # @pytest.mark.flaky(reruns=3)
    def test_copy_id_and_password(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.cancel_warning_server_to_connect()
        page.start_service()
        page.check_copy_id()
        page.check_copy_pass()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Проверка создания, переименования, удаления, присвоения и тп тега')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=165")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=164")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=169")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=167")
    def test_tag(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.add_device_to_address_book_from_id()
        page.open_address_book()
        page.delete_all_tags()
        page.add_tag()
        page.rename_tag()
        page.delete_tag()
        page.edit_device_tag()
        page.cancel_select_all_tags()

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
    @allure.title('Поиск по ID устройства')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=126")
    def test_search_by_id(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.clear_all_device_lists()
        page.connect_from_id(auth='no')
        page.close_connection()
        page.click_settings_nav_bar()
        page.search_by_id()
        page.add_to_favorites()
        page.search_by_id()
        page.add_to_address_book()
        page.search_by_id()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Поиск по псевдониму устройства')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=198")
    def test_search_by_alias(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.clear_all_device_lists()
        page.connect_from_id(auth='no')
        page.close_connection()
        page.click_settings_nav_bar()
        page.search_by_alias()
        page.delete_alias()
        page.add_to_favorites()
        page.search_by_id()
        page.search_by_alias()
        page.delete_alias()
        page.add_to_address_book()
        page.search_by_id()
        page.search_by_alias()

    @pytest.mark.parametrize("alias", ['Alias', 'Псевдоним'])
    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Задать псевдоним устройству (Авторизованный)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=128")
    def test_set_alias(self, connect_to_device, alias):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.clear_all_device_lists()
        page.connect_from_id(auth='no')
        page.close_connection()
        page.check_alias_last(alias)
        page.check_alias_favorites(alias)
        page.check_alias_address_book(alias)

    @pytest.mark.parametrize("alias", ['Alias', 'Псевдоним'])
    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Задать псевдоним устройству (Неавторизованный)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=128")
    def test_set_alias_un(self, connect_to_device, alias):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.clear_all_device_lists()
        page.connect_from_id()
        page.close_connection()
        page.check_alias_last(alias)
        page.check_alias_favorites(alias)

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Удалить устройство со вкладки Последние сеансы')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=121")
    def test_delete_from_last_session(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.clear_all_device_lists()
        page.connect_from_id(auth='no')
        page.close_connection()
        page.check_id_last_sessions()
        page.add_to_favorites()
        page.add_to_address_book()
        page.check_clear_last_session()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Добавить в избранное / Удалить из избранного')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=122")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=123")
    def test_add_and_delete_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.clear_all_device_lists()
        page.connect_from_id(auth='no')
        page.close_connection()
        page.check_clear_favorites()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Удалить устройство со вкладки Последние сеансы (неавтор.)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=121")
    def test_delete_from_last_session_un(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.clear_all_device_lists()
        page.connect_from_id()
        page.close_connection()
        page.check_id_last_sessions()
        page.add_to_favorites()
        page.add_to_address_book()
        page.check_clear_last_session()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Добавить в избранное / Удалить из избранного (неавтор.)')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=122")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=123")
    def test_add_and_delete_from_favorites_un(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.clear_all_device_lists()
        page.connect_from_id()
        page.close_connection()
        page.check_clear_favorites()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Добавить в адресную книгу / Удалить из адресной книги')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=124")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=125")
    def test_add_and_delete_from_address_book(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.login()
        page.clear_all_device_lists()
        page.connect_from_id(auth='no')
        page.close_connection()
        page.add_to_address_book()
        page.check_clear_address_book()


