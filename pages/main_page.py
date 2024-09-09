import time
import allure
import random
import pytest

from pages.base_page import BasePage
from config import *
from locators import *
# from pages.cart_page import CartPage



class MainPage(BasePage):
    def __init__(self, d):
        super().__init__(d)
        self.d = d
        # self.cart = CartPage(d)

    def allow_access(self):
        self.click(MainLocators.ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH)
        self.click(MainLocators.BACK_BTN)

    def set_id(self, id_string):
        self.set_text(MainLocators.REMOTE_ID_FIELD, id_string)
        self.click(MainLocators.OK_KEYBOARD)

    def click_connect(self):
        self.click(MainLocators.CONNECTION_BTN)

    def click_access_nav_bar(self):
        self.click(MainLocators.ACCESS_BTN)

    def click_start_service(self):
        self.click(MainLocators.START_SERVICE_BTN)

