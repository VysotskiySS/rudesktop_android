import allure
import pyperclip
from pkginfo.sdist import SDist

from locators import *
from pages.base_page import BasePage
from pages.main_page import MainPage

class CSPage(BasePage):
    def __init__(self, d):
        super().__init__(d)
        self.d = d

    def click_ok(self):
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    @allure.step("Установить пароль операционной системы")
    def set_password_os(self):
        self.click(CSLocators.BUTTON_MORE_OPTION)
        self.coordinate_click(761, 1543)
        self.set_text('//*[contains(@text, "Пароль")]', valid_password)
        self.click_ok()

    def check_password_os(self):
        self.click(CSLocators.BLOCK_SESSION, 'пункт меню [Заблокировать сессию]')
        self.click(CSLocators.BUTTON_MORE_OPTION, 'кнопка [...] на панели окна подключения')
        self.click(CSLocators.PASSWORD_OS, 'пункт меню [Пароль операционной системы]')

    def hide_show_panel_cs(self):
        self.wait_element(CSLocators.BUTTON_HIDE_PANEL)
        self.click(CSLocators.BUTTON_HIDE_PANEL)
        self.wait_element(CSLocators.BUTTON_SHOW_PANEL)
        self.click(CSLocators.BUTTON_SHOW_PANEL)
        self.wait_element(CSLocators.BUTTON_HIDE_PANEL)

    def mouse_or_sensor_mode(self):
        self.click(CSLocators.BUTTON_MOUSE, 'кнопка [Мышь] на панели экрана подключения')
        self.wait_element(CSLocators.SENSOR_MODE_BTN)
        self.click(CSLocators.SENSOR_MODE_BTN, 'кнопка Сенсорный режим')
        self.check_sensor_mode()
        self.click(CSLocators.MOUSE_MODE_BTN, 'кнопка Режим мыши')
        self.check_mouse_mode()

    @allure.step("Проверяем на наличие текст подсказок для режима управления [Режим мыши]")
    def check_mouse_mode(self):
        self.wait_element('//*[@content-desc="Касание одним пальцем"]')
        self.wait_element('//*[@content-desc="Левая кнопка мыши"]')
        self.wait_element('//*[@content-desc="Одно долгое нажатие пальцем"]')
        self.wait_element('//*[@content-desc="Правая мышь"]')
        self.wait_element('//*[@content-desc="Двойное нажатие и перемещение"]')
        self.wait_element('//*[@content-desc="Перетаскивание мышью"]')
        self.wait_element('//*[@content-desc="Тремя пальцами по вертикали"]')
        self.wait_element('//*[@content-desc="Колесико мыши"]')
        self.wait_element('//*[@content-desc="Движение двумя пальцами"]')
        self.wait_element('//*[@content-desc="Перемещение экрана"]')
        self.wait_element('//*[@content-desc="Сожмите, чтобы увеличить"]')
        self.wait_element('//*[@content-desc="Масштаб экрана"]')

    @allure.step("Проверяем на наличие текст подсказок для режима управления [Сенсорный режим]")
    def check_sensor_mode(self):
        self.wait_element('//*[@content-desc="Касание одним пальцем"]')
        self.wait_element('//*[@content-desc="Левая кнопка мыши"]')
        self.wait_element('//*[@content-desc="Одно долгое нажатие пальцем"]')
        self.wait_element('//*[@content-desc="Правая мышь"]')
        self.wait_element('//*[@content-desc="Движение одним пальцем"]')
        self.wait_element('//*[@content-desc="Перетаскивание мышью"]')
        self.wait_element('//*[@content-desc="Тремя пальцами по вертикали"]')
        self.wait_element('//*[@content-desc="Колесико мыши"]')
        self.wait_element('//*[@content-desc="Движение двумя пальцами"]')
        self.wait_element('//*[@content-desc="Перемещение экрана"]')
        self.wait_element('//*[@content-desc="Сожмите, чтобы увеличить"]')
        self.wait_element('//*[@content-desc="Масштаб экрана"]')

    @allure.step("")
    def check_chat(self):
        self.click(CSLocators.BUTTON_CHAT, 'кнопка [Чат] на панели экрана подключения')

