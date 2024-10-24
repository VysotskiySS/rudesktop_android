import allure
import pyperclip
from locators import *
from pages.base_page import BasePage


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

    def set_permanent_pass(self, passwd):
        self.click(MainLocators.PASS_MORE_OPTIONS, 'кнопка ... в блоке Ваше устройство')
        self.click(MainLocators.SET_PERMANENT_PASS_BTN, 'кнопка Установить постоянный пароль')
        self.set_text(MainLocators.PASSWORD_FIELD, passwd)
        self.set_text(MainLocators.PASSWORD_CONFIRM_FIELD, passwd)
        self.wait_a_second()
        self.click(MainLocators.OK_BTN, 'кнопка ОК')

    def click_more_option(self):
        self.click(MainLocators.PASS_MORE_OPTIONS, 'кнопка ... в блоке Ваше устройство')

    def check_set_permanent_pass(self):
        self.click_more_option()
        self.click(MainLocators.SET_PERMANENT_PASS_BTN, 'кнопка Установить постоянный пароль')
        self.set_text(MainLocators.PASSWORD_FIELD, '12345', 'поле Пароль')

        self.wait_a_second()
        self.wait_element(MainLocators.PASSWORD_WARNING_LENGTH, 'сообщение о минимальной длине')
        self.wait_element(MainLocators.PASSWORD_WARNING_IDENTITY, 'сообщение о идентичности полей')

        # self.clear_field(MainLocators.PASSWORD_FIELD_FILLED)

        self.set_text(MainLocators.PASSWORD_FIELD_FILLED, '6', 'поле Пароль')
        self.wait_a_second()
        self.wait_hidden_element(MainLocators.PASSWORD_WARNING_LENGTH, 'сообщение о минимальной длине')
        self.set_text(MainLocators.PASSWORD_CONFIRM_FIELD, '12345', 'поле Подтверждение')
        self.wait_element(MainLocators.PASSWORD_WARNING_IDENTITY, 'сообщение о идентичности полей')

        # self.clear_field(MainLocators.PASSWORD_CONFIRM_FIELD)

        self.set_text(MainLocators.PASSWORD_CONFIRM_FIELD_FILLED, '6', 'поле Подтверждение')
        self.wait_a_second()
        self.wait_hidden_element(MainLocators.PASSWORD_WARNING_LENGTH, 'сообщение о минимальной длине')
        self.wait_hidden_element(MainLocators.PASSWORD_WARNING_IDENTITY, 'сообщение о идентичности полей')

        self.wait_a_second()
        self.click(MainLocators.OK_BTN, 'кнопка ОК')

    def check_set_len_temp_pass(self):
        self.click_more_option()
        self.click(MainLocators.LEN_TEMP_PASS)
        self.wait_element(MainLocators.LEN_TEMP_PASS)
        self.click(MainLocators.PASS_LEN_8)
        self.wait_a_second()
        self.click_more_option()
        self.click(MainLocators.LEN_TEMP_PASS)
        self.click(MainLocators.PASS_LEN_10)
        self.wait_a_second()
        self.click_more_option()
        self.click(MainLocators.LEN_TEMP_PASS)
        self.wait_element(MainLocators.LEN_TEMP_PASS)
        self.click(MainLocators.PASS_LEN_6)

    def update_temp_pass(self):
        self.click(MainLocators.RESET_PASS, 'кнопка Обновить временный пароль')

    def copy_temp_pass(self):
        self.click(MainLocators.COPY_PASS, 'кнопка Копировать временный пароль')

    def copy_id(self):
        self.click(MainLocators.COPY_ID, 'кнопка Копировать ID')

    def click_chat_send_btn(self):
        self.wait_a_second()
        self.click(MainLocators.CHAT_SEND_BTN, 'кнопка Отправить')
        self.wait_a_second()

    def click_x_on_clipboard_preview(self):
        if self.get_elements_amount(MainLocators.X_BTN_CLIPBOARD) > 0:
            self.click(MainLocators.X_BTN_CLIPBOARD, 'кнопка Х на clipboard preview')

    def check_copy_id_and_pass(self):
        self.update_temp_pass()
        self.copy_temp_pass()
        text_to_paste = pyperclip.paste()
        self.click_x_on_clipboard_preview()
        self.click_chat_nav_bar()

        self.set_text(MainLocators.CHAT_FIELD, text_to_paste)
        self.wait_a_second(3)
        self.click_chat_send_btn()

        self.click_access_nav_bar()
        self.copy_id()
        text_to_paste = pyperclip.paste()

        self.click_x_on_clipboard_preview()
        self.click_chat_nav_bar()
        self.set_text(MainLocators.CHAT_FIELD, text_to_paste)
        self.wait_a_second(3)
        self.click_chat_send_btn()

    def click_about_app(self):
        self.swipe_to_element(MainLocators.VERSION)
        self.click(MainLocators.VERSION, 'О программе')
        self.press_back()
        self.wait_element(MainLocators.VERSION, 'О программе')

    def login(self, login=f'{valid_login}', password=f'{valid_password}'):
        self.click_settings_nav_bar()
        self.click(MainLocators.LOGIN, 'кнопка Войти')
        self.set_text(MainLocators.LOGIN_FIELD, login)
        self.set_text(MainLocators.PASSWORD_FIELD, password)
        self.click(MainLocators.OK_BTN)
        self.wait_hidden_element(MainLocators.WARNING_INVALID_EMAIL_OR_PASS)

    def check_login_cloud(self, login=f'{valid_login}', password=f'{valid_password}'):
        self.click_settings_nav_bar()
        self.click(MainLocators.LOGIN, 'кнопка Войти')
        self.set_text(MainLocators.LOGIN_FIELD, login)
        self.set_text(MainLocators.PASSWORD_FIELD, password)
        self.click(MainLocators.SEE_OR_HIDE_PASS_BTN, 'кнопка Показать/скрыть пароль')
        self.click(MainLocators.SAVE_PASS_SW, 'свитч Сохранить пароль')

    def cancel_warning_server_to_connect(self):
        self.wait_a_second(3)
        if self.get_elements_amount('//*[@content-desc="Сервер для подключения"]') > 0:
            self.click(MainLocators.CANCEL_BTN)

    def ok_warning_server_to_connect(self):
        self.wait_a_second(3)
        if self.get_elements_amount('//*[@content-desc="Сервер для подключения"]') > 0:
            self.click(MainLocators.OK_BTN)
        self.start_app()

    # def create_tag(self):

    def click_more_option_connect(self):
        self.click(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION, 'кнопка ... в строке подключения')

    def check_tag(self):
        self.click_connection_nav_bar()
        self.click(MainLocators.ADDRESS_BOOK, 'Адресная книга')

        self.wait_a_second()
        self.coordinate_click(980, 583)

        self.click(MainLocators.ADD_TAG, 'Добавить тег')
        self.set_text('//*[contains(@text, "Раздельно запятой")]', 'teg1, teg2; teg3')
        self.click_ok()

        teg1 = '//*[@content-desc="teg1"]'
        self.long_click(teg1)

        self.click(MainLocators.RENAME, 'Переименовать')
        self.d(text="teg1").clear_text()

        self.set_text(MainLocators.CLEAR_FIELD_RENAME_TAG, 'renamed_teg_1')
        self.click_ok()

        renamed_teg_1 = '//*[@content-desc="renamed_teg_1"]'
        self.long_click(renamed_teg_1)
        self.click(MainLocators.DELETE, 'Удалить')

        self.click_more_option_connect()
        self.click(MainLocators.EDIT_TAG, 'кнопка Редактировать тег')
        self.click('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]')
        self.click_ok()

        print('debug')



