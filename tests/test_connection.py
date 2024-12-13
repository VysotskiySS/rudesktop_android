# file: test_connection.py
from faker import Faker
import pytest
from pages.main_page import MainPage
from pages.cs_page import CSPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Экран подключения")
class TestConnection:

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Всегда подключаться через мост')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=139")
    def test_always_connect_from_bridge(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.allow_access()
        page.ok_warning_server_to_connect()
        page.connect_from_id()
        page.check_icon_connection_color(250, 248, 251)
        page.activate_connect_always_from_bridge()
        page.reconnect()
        page.check_icon_connection_color(62, 125, 70)

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
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=149")
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=150")
    def test_password_os(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        main = CSPage(connect_to_device)
        main.set_password_os()
        main.check_password_os()
        main.get_screen()
        # Нужно добавить проверку на то что действительно прошла авторизация, пока кроме сравнения скрина или цвета точки ничего не придумал

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Скрыть / показать панель на экране подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=148")
    def test_panel_cs(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs =  CSPage(connect_to_device)
        cs.hide_show_panel_cs()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Режим мыши и сенсорный режим')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=199")
    def test_mouse_and_sensor_mode(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.mouse_or_sensor_mode()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Чат')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=127")
    def test_chat(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.check_send_msg_to_chat()
        cs.hide_chat()
        cs.show_chat()
        cs.close_chat()
        main.close_connection()
        main.click_chat_nav_bar()
        main.check_msg_in_chat_main_window()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Скрыть / Показать панель управления окна подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=148")
    def test_hide_panel(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.hide_panel()
        cs.show_panel()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Показывать качество / Изменить качество')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=141")
    def test_quality(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.check_quality()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Вставить Ctrl + Alt + Del')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=156")
    def test_ctrl_alt_del(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.send_ctrl_alt_del()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Изменение масштаба')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=143")
    def test_change_scale(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.login()
        main.connect_from_id(auth='no')
        cs = CSPage(connect_to_device)
        cs.check_change_scale_mode()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Меню [...] на панели в окне подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=203")
    def test_more_options(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.check_more_options()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Меню [Дисплей] на панели в окне подключения')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=203")
    def test_display_options(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.check_display_options()

    @pytest.mark.connection
    @pytest.mark.smoke
    @allure.title('Начать / Остановить запись сессии')
    @allure.testcase("https://dev.corp.rudesktop.ru/-/testy/projects/2/suites/8?test_case=206")
    def test_record_session(self, connect_to_device):
        main = MainPage(connect_to_device)
        main.allow_access()
        main.ok_warning_server_to_connect()
        main.connect_from_id()
        cs = CSPage(connect_to_device)
        cs.check_record_session()

