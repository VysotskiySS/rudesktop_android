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

    @allure.step("Разрешить доступ")
    def allow_access(self):
        self.wait_a_second()
        if self.get_elements_amount(MainLocators.ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH) > 0:
            self.click(MainLocators.ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH, 'свитч Разрешить доступ на управление всеми файлами')
            self.click(MainLocators.BACK_BTN, 'кнопка назад')

    @allure.step("Закрыть окно предупреждения")
    def check_warning(self):
        assert self.get_elements_amount(MainLocators.TITLE_WARNING) == 1
        self.click(MainLocators.OK_BTN, 'кнопка ОК')

    @allure.step("Установить ID")
    def set_id(self, id_string):
        self.set_text(MainLocators.REMOTE_ID_FIELD, id_string)
        # self.click(MainLocators.OK_KEYBOARD, 'кнопка ОК на экранной клавиатуре')

    def click_connect(self):
        self.wait_a_second()
        self.click(MainLocators.CONNECTION_BTN, 'кнопка Подключиться в поле Удаленный идентификатор')

    def click_connection_nav_bar(self):
        self.click(MainLocators.CONNECTION_BTN, 'кнопка Соединение в нав.баре')

    def click_chat_nav_bar(self):
        self.click(MainLocators.CHAT_BTN, 'кнопка Чат в нав.баре')

    def click_access_nav_bar(self):
        self.click(MainLocators.ACCESS_BTN, 'кнопка Доступ в нав.баре')

    def click_settings_nav_bar(self):
        self.click(MainLocators.SETTINGS_BTN, 'кнопка Настройки в нав.баре')

    @allure.step("Запустить службу")
    def start_service(self):
        self.allow_access()
        self.click_access_nav_bar()
        self.click(MainLocators.START_SERVICE_BTN, 'кнопка Запустить службу')
        self.check_warning()
        if self.get_elements_amount(MainLocators.VIEW_AND_ACCEPT_BNT) > 0:
            self.click(MainLocators.VIEW_AND_ACCEPT_BNT, 'кнопка Просмотреть и принять')
            self.click(MainLocators.ACCEPT_BTN, 'кнопка Принять')
            self.click(MainLocators.OK_BTN, 'кнопка ОК')
        self.click(MainLocators.START_NOW_BTN, 'кнопка Start now')

    @allure.step("Остановить службу")
    def stop_service(self):
        self.click(MainLocators.STOP_SERVICE_BTN, 'кнопка Остановить службу')
        self.click(MainLocators.CANCEL_BTN, 'кнопка Отменить')
        self.wait_element(MainLocators.STOP_SERVICE_BTN)
        self.click(MainLocators.STOP_SERVICE_BTN, 'кнопка Остановить службу')
        self.click(MainLocators.OK_BTN, 'кнопка ОК')

    def click_ok(self):
        self.click(MainLocators.OK_BTN, 'кнопка ОК')

    def change_server(self):
        self.click(MainLocators.SERVER_TO_CONNECT, 'кнопка Сервер для подключения')

    def check_change_language(self):
        self.click(MainLocators.LANGUAGE, 'пункт меню Язык интерфейса')
        self.click(MainLocators.ENGLISH_LANGUAGE, 'радиобаттон English')
        self.wait_element('//*[@content-desc="Language"]')
        self.click('//*[@content-desc="Language"]', 'пункт меню Language (Язык интерфейса)')
        self.click(MainLocators.RUSSIAN_LANGUAGE, 'радиобаттон Русский')
        self.wait_element('//*[@content-desc="Язык интерфейса"]')
        self.click('//*[@content-desc="Язык интерфейса"]', 'пункт меню Язык интерфейса')
        self.click(MainLocators.KAZAK_LANGUAGE)
        self.wait_element('//*[@content-desc="Тіл"]')
        self.click('//*[@content-desc="Тіл"]', 'пункт меню Тіл (Язык интерфейса)')
        self.click(MainLocators.DEFAULT_LANGUAGE, 'пункт меню Язык интерфейса')
        self.wait_element('//*[@content-desc="Язык интерфейса"]')

    def check_change_theme(self):
        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка Ночная тема на экране Настройки')
        self.click(MainLocators.NIGHT_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (27, 27, 27), f'Цвет иконки {color} а должен быть (27, 27, 27)'

        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка Ночная тема на экране Настройки')
        self.click(MainLocators.SYSTEM_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (240, 240, 240), f'Цвет иконки {color} а должен быть (240, 240, 240)'

        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка Ночная тема на экране Настройки')
        self.click(MainLocators.NIGHT_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (27, 27, 27), f'Цвет иконки {color} а должен быть (27, 27, 27)'

        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка Ночная тема на экране Настройки')
        self.click(MainLocators.DAYTIME_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (240, 240, 240), f'Цвет иконки {color} а должен быть (240, 240, 240)'

    def change_settings(self):
        self.click(MainLocators.LANGUAGE, 'кнопка Язык интерфейса')
        self.click(MainLocators.ENGLISH_LANGUAGE, 'радиобаттон English')

    @allure.step("Запустить приложение")
    def start_app(self):
        self.wait_a_second(3)
        self.d.app_start(package)
        self.wait_a_second()

    def reset_settings(self):
        self.change_settings()
        self.swipe_to_element(MainLocators.RESET_SETTINGS_EN)
        self.click(MainLocators.RESET_SETTINGS_EN, 'кнопка Сбросить настройки')
        self.click(MainLocators.RESET_SETTINGS_CLOSE_EN, 'кнопка Закрыть')
        self.click(MainLocators.RESET_SETTINGS_EN, 'кнопка Сбросить настройки')
        self.wait_a_second()
        self.click(MainLocators.RESET_SETTINGS_CONFIRM, 'кнопка Сбросить настройки')
        self.start_app()
        self.click_settings_nav_bar()
        self.wait_element(MainLocators.LANGUAGE)


