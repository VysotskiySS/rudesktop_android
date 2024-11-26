import os
import pytest
import uiautomator2 as u2
import allure
from config import *
from pages.base_page import BasePage
from pages.main_page import MainPage

def pytest_addoption(parser):
    parser.addoption('--device', action='store', default=device_id, help='emulator id')

@pytest.fixture
def connect_to_device(request):
    return u2.connect(request.config.getoption('--device'))

@allure.title("Запустить приложение")
def open_app(d):
    d.implicitly_wait(10)
    d.app_clear(package)
    d.app_start(package, stop=True)

@allure.step("Закрытие приложения")
def teardown(d):
    BasePage(d).get_screen()
    d.app_stop(package)
    d.app_clear(package)

@pytest.fixture()
def setup(request):
    dev_id = request.config.getoption('--device')
    os.environ["device_id"] = dev_id
    d = u2.connect(dev_id)
    open_app(d)
    yield
    teardown(d)
