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
    @allure.title('')
    @allure.testcase("")
    def test_start_service(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.click_access_nav_bar()
        page.click_start_service()
        page.click_ok()
        page.click_start_now()
        page.get_screen()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('')
    @allure.testcase("")
    def test_input_id(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.set_id('382760227')
        page.click_connect()
        time.sleep(2)
        page.allow_access()
        page.get_screen()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('')
    @allure.testcase("")
    def test_chat(self, connect_to_device):
        page = MainPage(connect_to_device)
        base = BasePage(connect_to_device)
        new_message = base.faker.text()
        page.send_message_to_chat(new_message)


