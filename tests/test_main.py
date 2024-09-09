# file: test_main.py
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
    def test_first(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.set_id('382760227')
        page.click_connect()

        time.sleep(2)
        page.allow_access()


        page.get_screen()

