import allure
import pyperclip
from rich.style import Style

from locators import *
from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, d):
        super().__init__(d)
        self.d = d

    @allure.step("Разрешить доступ")
    def allow_access(self):
        self.wait_a_second(3)
        if self.get_elements_amount(MainLocators.ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH) > 0:
            self.click(MainLocators.ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH, 'свитч Разрешить доступ на управление всеми файлами')
            self.click(MainLocators.BACK_BTN, 'кнопка [назад]')

    def accept_new_cert(self):
        if self.get_elements_amount(MainLocators.TITLE_CHANGE_CERT_SERVER) >0:
            self.click(MainLocators.ACCEPT_NEW_CERT_BTN)
            self.wait_a_second(10)

    def allow_permission(self):
        self.click(MainLocators.PERMISSION_ALLOW_BTN, 'While using the app')

    @allure.step("Закрыть окно предупреждения")
    def check_warning(self):
        assert self.get_elements_amount(MainLocators.TITLE_WARNING) == 1
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    @allure.step("Установить ID")
    def set_id(self, id_string):
        self.click(MainLocators.REMOTE_ID_FIELD)
        for i in range(len(id_string)):
        #     self.wait_a_second()
            self.d.send_keys(id_string[i])

    def click_connect(self):
        self.wait_a_second(3)
        self.click(MainLocators.CONNECT_BTN, 'кнопка [Подключиться] в поле Удаленный идентификатор')

    def connect_from_id(self, auth='yes', save='no'):
        self.click_connection_nav_bar()
        self.clear_last_seanses()
        self.set_id(valid_remote_device_id)
        self.click_connect()
        if auth == 'yes':
            self.enter_passwd()
            if save == 'yes':
                self.click_save_pass()
            self.click(MainLocators.OK_BTN)
        self.check_connection_screen()

    def check_id_last_seanses(self):
        self.wait_a_second(2)
        id_device_last = self.get_id_or_alias_device()
        id_device_last = id_device_last.replace(' ', '')
        assert id_device_last == valid_remote_device_id, f'Ожидался id {valid_remote_device_id}, но получен {id_device_last}'

    def connect_from_invalid_id(self):
        self.click_connection_nav_bar()
        self.set_id(invalid_remote_device_id)
        self.click_connect()
        self.wait_element('//*[@content-desc="Ошибка подключения"]')
        self.wait_element('//*[@text="ID не существует"]')
        self.click_ok()
        self.wait_element(MainLocators.CONNECTION_BTN)

    def connect_from_history(self):
        self.click(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION)
        self.click(MainLocators.CONNECT_BNT_MORE_OPTION)

    def reconnect(self):
        self.click_connection_nav_bar()
        self.click_connect()
        self.enter_passwd()
        self.click_ok()
        self.check_connection_screen()

    def click_connection_nav_bar(self):
        self.click(MainLocators.CONNECTION_BTN, 'кнопка [Соединение] в нав.баре')

    def click_chat_nav_bar(self):
        self.click(MainLocators.CHAT_BTN, 'кнопка [Чат] в нав.баре')

    def click_access_nav_bar(self):
        self.click(MainLocators.ACCESS_BTN, 'кнопка [Доступ] в нав.баре')

    def click_settings_nav_bar(self):
        self.click(MainLocators.SETTINGS_BTN, 'кнопка [Настройки] в нав.баре')

    @allure.step("Запустить службу")
    def start_service(self):
        self.allow_access()
        self.click_access_nav_bar()
        self.click(MainLocators.START_SERVICE_BTN, 'кнопка [Запустить службу]')
        self.check_warning()
        if self.get_elements_amount(MainLocators.VIEW_AND_ACCEPT_BNT) > 0:
            self.click(MainLocators.VIEW_AND_ACCEPT_BNT, 'кнопка [Просмотреть и принять]')
            self.click(MainLocators.ACCEPT_BTN, 'кнопка [Принять]')
            self.click(MainLocators.OK_BTN, 'кнопка [ОК]')
        self.click(MainLocators.START_NOW_BTN, 'кнопка [Start now]')

    @allure.step("Остановить службу")
    def stop_service(self):
        self.click(MainLocators.STOP_SERVICE_BTN, 'кнопка [Остановить службу]')
        self.click(MainLocators.CANCEL_BTN, 'кнопка Отменить')
        self.wait_element(MainLocators.STOP_SERVICE_BTN)
        self.click(MainLocators.STOP_SERVICE_BTN, 'кнопка [Остановить службу]')
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    def click_ok(self):
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    def change_server(self, server_to_connect):
        self.click(MainLocators.SERVER_TO_CONNECT, 'кнопка [Сервер для подключения]')
        self.click('//*/android.widget.EditText')
        self.d.clear_text()
        self.d.send_keys(server_to_connect)
        self.click_ok()

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
        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка [Ночная тема] на экране Настройки')
        self.click(MainLocators.NIGHT_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (27, 27, 27), f'Цвет иконки {color} а должен быть (27, 27, 27)'
        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка [Ночная тема] на экране Настройки')
        self.click(MainLocators.SYSTEM_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (240, 240, 240), f'Цвет иконки {color} а должен быть (240, 240, 240)'
        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка [Ночная тема] на экране Настройки')
        self.click(MainLocators.NIGHT_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (27, 27, 27), f'Цвет иконки {color} а должен быть (27, 27, 27)'
        self.click(MainLocators.NIGHT_THEME_SETTINGS, 'кнопка [Ночная тема] на экране Настройки')
        self.click(MainLocators.DAYTIME_THEME)
        color = self.get_color('//*[@content-desc="Ночная тема"]')
        assert color == (240, 240, 240), f'Цвет иконки {color} а должен быть (240, 240, 240)'

    def change_settings(self):
        self.click(MainLocators.LANGUAGE, 'кнопка [Язык интерфейса]')
        self.click(MainLocators.ENGLISH_LANGUAGE, 'радиобаттон English')

    @allure.step("Запустить приложение")
    def start_app(self):
        self.wait_a_second(3)
        self.d.app_start(package)
        self.wait_a_second()

    @allure.step("Сбросить настройки")
    def reset_settings(self):
        self.change_settings()
        self.swipe_to_element(MainLocators.RESET_SETTINGS_EN)
        self.click(MainLocators.RESET_SETTINGS_EN, 'кнопка [Сбросить настройки]')
        self.click(MainLocators.RESET_SETTINGS_CLOSE_EN, 'кнопка [Закрыть]')
        self.click(MainLocators.RESET_SETTINGS_EN, 'кнопка [Сбросить настройки]')
        self.wait_a_second()
        self.click(MainLocators.RESET_SETTINGS_CONFIRM, 'кнопка [Сбросить настройки]')
        self.start_app()
        self.ok_warning_server_to_connect()
        self.click_settings_nav_bar()
        self.wait_element(MainLocators.LANGUAGE)

    @allure.step("Установить постоянный пароль")
    def set_permanent_pass(self, passwd):
        self.click(MainLocators.PASS_MORE_OPTIONS, 'кнопка [...] в блоке Ваше устройство')
        self.click(MainLocators.SET_PERMANENT_PASS_BTN, 'кнопка [Установить постоянный пароль]')
        self.set_text(MainLocators.PASSWORD_FIELD, passwd)
        self.set_text(MainLocators.PASSWORD_CONFIRM_FIELD, passwd)
        self.wait_a_second()
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    def click_more_option(self):
        self.click(MainLocators.PASS_MORE_OPTIONS, 'кнопка [...] в блоке Ваше устройство')

    @allure.step("Установить постоянный пароль")
    def check_set_permanent_pass(self):
        self.click_more_option()
        self.click(MainLocators.SET_PERMANENT_PASS_BTN, 'кнопка [Установить постоянный пароль]')
        self.set_text(MainLocators.PASSWORD_FIELD, '12345', 'поле Пароль')
        self.wait_a_second()
        self.wait_element(MainLocators.PASSWORD_WARNING_LENGTH, 'сообщение о минимальной длине')
        self.wait_element(MainLocators.PASSWORD_WARNING_IDENTITY, 'сообщение о идентичности полей')
        self.set_text(MainLocators.PASSWORD_FIELD_FILLED, '6', 'поле Пароль')
        self.wait_a_second()
        self.wait_hidden_element(MainLocators.PASSWORD_WARNING_LENGTH, 'сообщение о минимальной длине')
        self.set_text(MainLocators.PASSWORD_CONFIRM_FIELD, '12345', 'поле Подтверждение')
        self.wait_element(MainLocators.PASSWORD_WARNING_IDENTITY, 'сообщение о идентичности полей')
        self.set_text(MainLocators.PASSWORD_CONFIRM_FIELD_FILLED, '6', 'поле Подтверждение')
        self.wait_a_second()
        self.wait_hidden_element(MainLocators.PASSWORD_WARNING_LENGTH, 'сообщение о минимальной длине')
        self.wait_hidden_element(MainLocators.PASSWORD_WARNING_IDENTITY, 'сообщение о идентичности полей')
        self.wait_a_second()
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    @allure.step("Изменить длину пароля")
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

    @allure.step("Обновить временный пароль")
    def update_temp_pass(self):
        old_temp_pass = self.get_temp_pass()
        self.click(MainLocators.RESET_PASS, 'кнопка [Обновить временный пароль]')
        self.wait_a_second()
        new_temp_pass = self.get_temp_pass()
        assert old_temp_pass != new_temp_pass, f'Пароль устройства не изменился. Пароль до обновления {old_temp_pass}, после обновления {new_temp_pass}'

    @allure.step("Копировать временный пароль")
    def copy_temp_pass(self):
        self.click(MainLocators.COPY_PASS, 'кнопка [Копировать временный пароль]')

    @allure.step("Копировать ID")
    def copy_id(self):
        self.click(MainLocators.COPY_ID, 'кнопка [Копировать ID]')

    @allure.step("Отправить в чат")
    def click_chat_send_btn(self):
        # self.wait_a_second()
        # self.click(MainLocators.CHAT_SEND_BTN, 'кнопка [Отправить]')
        # self.wait_a_second()
        x,y = self.get_element('//*/android.view.View[3]').center()
        self.coordinate_click(x,y)

    @allure.step("Закрыть превью буфера обмена")
    def click_x_on_clipboard_preview(self):
        if self.get_elements_amount(MainLocators.X_BTN_CLIPBOARD) > 0:
            self.click(MainLocators.X_BTN_CLIPBOARD, 'кнопка [Х] на clipboard preview')

    def check_copy_id(self):
        # self.update_temp_pass()
        self.copy_temp_pass()
        text_to_paste = pyperclip.paste()
        self.click_x_on_clipboard_preview()
        self.click_chat_nav_bar()
        self.set_text(MainLocators.CHAT_FIELD, text_to_paste)
        self.wait_a_second(3)
        self.click_chat_send_btn()

    def check_copy_pass(self):
        self.click_access_nav_bar()
        self.copy_id()
        text_to_paste = pyperclip.paste()
        self.click_x_on_clipboard_preview()
        self.click_chat_nav_bar()
        self.set_text(MainLocators.CHAT_FIELD, text_to_paste)
        self.wait_a_second(3)
        self.click_chat_send_btn()

    @allure.step("Нажать - О программе")
    def click_about_app(self):
        self.swipe_to_element(MainLocators.VERSION)
        self.click(MainLocators.VERSION, '[О программе]')
        self.press_back()
        self.wait_element(MainLocators.VERSION, '[О программе]')

    @allure.step("Авторизоваться")
    def login(self, login=f'{valid_login}', password=f'{valid_password}', method='local'):
        self.click_settings_nav_bar()
        self.click(MainLocators.LOGIN, 'кнопка [Войти]')
        if method == 'domain':
            self.click('//*[@content-desc="@win2012.local"]')
        self.set_text(MainLocators.LOGIN_FIELD, login)
        self.set_text(MainLocators.PASSWORD_FIELD, password)
        self.click(MainLocators.OK_BTN)
        self.wait_a_second()
        self.wait_hidden_element(MainLocators.WARNING_INVALID_EMAIL_OR_PASS)
        self.wait_hidden_element('//*[@content-desc="Локальный"]')
        if method == 'local':
            self.wait_element(f'//*[@content-desc="Выйти ({login})"]')
        else:
            self.wait_element(f'//*[@content-desc="Выйти ({login}@win2012.local)"]')

    def logout(self, login=valid_login, method='local'):
        self.click(MainLocators.LOGIN, 'кнопка [Выйти]')
        if method == 'local':
            self.wait_hidden_element(f'//*[@content-desc="Выйти ({login})"]')
        else:
            self.wait_hidden_element(f'//*[@content-desc="Выйти ({login}@win2012.local)"]')

    @allure.step("Авторизоваться с невалидными данными")
    def login_invalid(self, login=f'{invalid_login}', password=f'{invalid_password}', method='local'):
        self.click(MainLocators.LOGIN, 'кнопка [Войти]')
        if method == 'domain':
            self.click(MainLocators.DOMAIN_AUTH_METHOD_RB)
        self.set_text(MainLocators.LOGIN_FIELD, login)
        self.set_text(MainLocators.PASSWORD_FIELD, password)
        self.click(MainLocators.OK_BTN)
        if method == 'domain':
            self.wait_element(MainLocators.WARNING_NOT_FOUND_USER_AD)
        else:
            self.wait_element(MainLocators.WARNING_INVALID_EMAIL_OR_PASS)
        self.click_cancel()
        self.wait_element(MainLocators.LOGIN)

    @allure.step("Авторизоваться через адресную книгу")
    def login_address_book(self, login=f'{valid_login}', password=f'{valid_password}'):
        self.open_address_book()
        self.click(MainLocators.LOGIN_ADDRESS_BOOK, 'кнопка [Войти]')
        self.set_text(MainLocators.LOGIN_FIELD, login)
        self.set_text(MainLocators.PASSWORD_FIELD, password)
        self.click(MainLocators.OK_BTN)
        self.wait_hidden_element(MainLocators.WARNING_INVALID_EMAIL_OR_PASS)
        self.wait_hidden_element(MainLocators.LOGIN_ADDRESS_BOOK)
        self.wait_element('//*[@content-desc="Теги"]')

    @allure.step("Открыть адресную книгу")
    def open_address_book(self):
        self.click_connection_nav_bar()
        self.click(MainLocators.ADDRESS_BOOK, 'вкладка [Адресная книга]')

    @allure.step("Авторизоваться")
    def check_login_cloud(self, login=f'{valid_login}', password=f'{valid_password}'):
        self.click_settings_nav_bar()
        self.click(MainLocators.LOGIN, 'кнопка [Войти]')
        self.set_text(MainLocators.LOGIN_FIELD, login)
        self.set_text(MainLocators.PASSWORD_FIELD, password)
        self.click(MainLocators.SEE_OR_HIDE_PASS_BTN, 'кнопка [Показать/скрыть пароль]')
        self.click(MainLocators.SAVE_PASS_SW, 'свитч Сохранить пароль')

    @allure.step("Отменить изменение сервера после сброса кэша при запуске приложения")
    def cancel_warning_server_to_connect(self):
        self.wait_a_second(3)
        if self.get_elements_amount('//*[@content-desc="Сервер для подключения"]') > 0:
            self.click(MainLocators.CANCEL_BTN)

    @allure.step("Подтвердить изменение сервера после сброса кэша при запуске приложения")
    def ok_warning_server_to_connect(self):
        self.wait_a_second(3)
        if self.get_elements_amount('//*[@content-desc="Сервер для подключения"]') > 0:
            self.click(MainLocators.OK_BTN)
        self.start_app()

    def click_more_option_connect(self):
        self.click(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION, 'кнопка [...] в строке подключения')

    @allure.step("Нажать кнопку [...] в блоке Теги")
    def click_more_option_address_book(self):
        self.coordinate_click(980, 583) # не смог подобрать локатор, пока клик по координатам, ЗАМЕНИТЬ!!!

    @allure.step("Добавить устройство в адресную книгу по ID")
    def add_device_to_address_book_from_id(self):
        self.click_connection_nav_bar()
        self.click(MainLocators.ADDRESS_BOOK)
        if self.get_elements_amount('//*[@content-desc="Пусто"]') > 0:
            self.click_more_option_address_book()
            self.click(MainLocators.ADD_ID)
            self.set_text('//*/android.widget.EditText', valid_remote_device_id)
            self.click_ok()

    @allure.step("Добавить теги")
    def add_tag(self):
        self.click_more_option_address_book()
        self.click(MainLocators.ADD_TAG, 'Добавить тег')
        self.set_text('//*[contains(@text, "Раздельно запятой")]', 'teg1, teg2; teg3')
        self.click_ok()
        self.update_tag()

    @allure.step("Переименовать тег")
    def rename_tag(self):
        teg1 = '//*[@content-desc="teg1"]'
        self.wait_a_second()
        self.long_click(teg1)
        self.click(MainLocators.RENAME, 'Переименовать')
        self.d(text="teg1").clear_text()
        self.set_text(MainLocators.CLEAR_FIELD_RENAME_TAG, 'renamed_teg_1')
        self.click_ok()
        self.update_tag()

    def update_tag(self):
        self.click_more_option_address_book()
        self.click(MainLocators.UPDATE)

    @allure.step("Удалить тег")
    def delete_tag(self):
        renamed_teg_1 = '//*[@content-desc="renamed_teg_1"]'
        self.wait_a_second(2)
        self.long_click(renamed_teg_1)
        self.click(MainLocators.DELETE, 'Удалить')

    @allure.step("Редактировать тег устройства")
    def edit_device_tag(self):
        self.click('//*[@content-desc="teg2"]')
        self.wait_element('//*[@content-desc="Пусто"]')
        self.click('//*[@content-desc="teg2"]')
        self.click_more_option_connect()
        self.click(MainLocators.EDIT_TAG, 'кнопка [Редактировать тег]')
        self.click('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]')
        self.click_ok()
        self.click('//*[@content-desc="teg3"]')
        self.wait_element('//*[@content-desc="Пусто"]')
        self.click('//*[@content-desc="teg2"]')
        self.wait_hidden_element('//*[@content-desc="Пусто"]')

    @allure.step("Отменить выбор всех тегов")
    def cancel_select_all_tags(self):
        self.click('//*[@content-desc="teg2"]')
        self.wait_element('//*[@content-desc="Пусто"]')
        self.click_more_option_address_book()
        self.click(MainLocators.CANCEL_SELECT_TAG)
        self.update_tag()
        self.wait_hidden_element('//*[@content-desc="Пусто"]')

    @allure.step("Удалить все теги")
    def delete_all_tags(self):
        count = self.get_elements_amount('//*[@content-desc="Теги"]/android.view.View[1]/*')
        for i in range(count):
            self.long_click('//*[@content-desc="Теги"]/android.view.View[1]/*')
            self.click(MainLocators.DELETE)

    @allure.step("Нажать показать/скрыть пароль")
    def click_show_hide_pass(self):
        self.click('//*/android.widget.Button[1]')

    @allure.step("Нажать сохранить пароль")
    def click_save_pass(self):
        self.click('//*[@content-desc="Запомнить пароль"]')

    @allure.step("Ввести пароль")
    def enter_passwd(self, passwd=valid_password):
        self.set_text('//*[contains(@text, "Пароль")]', passwd)

    @allure.step("Проверка что выполнено удаленное подключение")
    def check_connection_screen(self):
        self.wait_element('//android.widget.FrameLayout[1]')
        self.wait_hidden_element('//*[@content-desc="Неверный пароль"]')
        self.click_x_on_clipboard_preview()

    @allure.step("Завершить подключение")
    def close_connection(self):
        self.close_popup()
        self.wait_a_second()
        self.wait_element('//*/android.widget.Button[1]')
        self.click('//*/android.widget.Button[1]', 'кнопка [Х] на панели окна подключения')
        self.wait_element(MainLocators.OK_BTN)
        self.click_ok()

    @allure.step("Активировать опцию - запускать после включения")
    def start_service_after_start(self):
        self.swipe_to_element(MainLocators.START_AFTER_SWITCHING_ON)
        self.click(MainLocators.START_AFTER_SWITCHING_ON, 'свитч Запускать после включения')
        if self.get_elements_amount('//*[@resource-id="android:id/button1"]') > 0:
            self.click('//*[@resource-id="android:id/button1"]')
            self.swipe_to_element('//*[@text="RuDesktop"]/..')
            self.click('//*[@text="RuDesktop"]/..')
            self.click('//android.widget.ScrollView/android.view.View[2]')
            self.press_back()
            self.press_back()
        self.d.app_stop(package)
        self.start_app()
        self.click_access_nav_bar()
        self.wait_hidden_element('//*[contains(@content-desc, "Служба не запущена")]')

    @allure.step("Добавить устройство в Адресную книгу")
    def add_to_address_book(self):
        self.click(MainLocators.LAST_SEANSES, 'вкладка [Последние сеансы]')
        id_last_seanses = self.get_description(MainLocators.DEVICE_IN_LIST)
        id_last_seanses = self.get_text_before_newline(id_last_seanses)
        self.click_more_option_connect()
        self.click(MainLocators.ADD_TO_ADDRESS_BOOK, 'кнопка [Добавить в адресную книгу]')
        self.click(MainLocators.ADDRESS_BOOK, 'вкладка [Адресная книга]')
        id_address_book = self.get_description(MainLocators.DEVICE_IN_LIST)
        id_address_book = self.get_text_before_newline(id_address_book)
        assert id_address_book == id_last_seanses, f'ID устройства из адресной книги {id_address_book} не совпадает с ID устройства в последних сеансах {id_last_seanses}'

    def check_clear_all_device_lists(self):
        self.click(MainLocators.LAST_SEANSES)
        assert self.get_elements_amount(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION) > 0, 'Нет устройств в списке'
        self.clear_last_seanses()

        self.click(MainLocators.FAVOTITES)
        assert self.get_elements_amount(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION) > 0, 'Нет устройств в списке'
        self.clear_favorites()

        self.click(MainLocators.ADDRESS_BOOK)
        assert self.get_elements_amount(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION) > 0, 'Нет устройств в списке'
        self.clear_address_book()

    def clear_all_device_lists(self):
        self.clear_last_seanses()
        self.clear_favorites()
        self.clear_address_book()

    @allure.step("Очистить адресную книгу")
    def clear_address_book(self):
        self.click_connection_nav_bar()
        self.click(MainLocators.ADDRESS_BOOK, 'вкладка Адресная книга')
        self.del_all_devices_from_list()
        self.wait_element('//*[@content-desc="Пусто"]')

    @allure.step("Удалить все устройства из списка")
    def del_all_devices_from_list(self, count_save_in_list=0):
        i = self.get_elements_amount(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION)
        while i > count_save_in_list:
            self.click_more_option_connect()
            self.click(MainLocators.DELETE, 'кнопка [Удалить]')
            i -= 1

    @allure.step("Очистить избранное")
    def clear_favorites(self):
        self.click_connection_nav_bar()
        self.click(MainLocators.FAVOTITES, 'вкладка Избранное')
        self.wait_a_second(2)
        self.del_all_devices_from_list()
        self.wait_element('//*[@content-desc="Пусто"]')

    @allure.step("Добавить устройство в Избранное")
    def add_to_favorites(self):
        self.click(MainLocators.LAST_SEANSES, 'вкладка [Последние сеансы]')
        id_last_seanses = self.get_description(MainLocators.DEVICE_IN_LIST)
        self.click_more_option_connect()
        self.click(MainLocators.ADD_TO_FAVORITES, 'кнопка [Добавить в Избранное]')
        self.click(MainLocators.FAVOTITES, 'вкладка [Избранное]')
        id_favorites = self.get_description(MainLocators.DEVICE_IN_LIST)
        assert id_favorites == id_last_seanses, f'ID устройства из адресной книги {id_favorites} не совпадает с ID устройства в последних сеансах {id_last_seanses}'

    @allure.step("Переименовать устройство")
    def set_alias(self, alias):
        self.click_connection_nav_bar()
        self.click_more_option_connect()
        self.click(MainLocators.RENAME, 'кнопка [Переименовать]')
        self.set_text(MainLocators.ALIAS_FIELD, alias)

    def click_cancel(self):
        self.click(MainLocators.CANCEL_BTN, 'кнопка [Отменить]')

    @allure.step("Переименовать устройство и проверить отображение имени")
    def check_set_alias(self, alias='Test-Device_123'):
        self.set_alias(alias)
        self.click_cancel()
        name = self.get_description(MainLocators.DEVICE_IN_LIST)
        name = name.replace(" ", "")
        assert valid_remote_device_id in name, f'Ожидалось {valid_remote_device_id}, но в строке {name} не найдено'
        self.set_alias(alias)
        self.click_ok()
        name = self.get_description(MainLocators.DEVICE_IN_LIST)
        assert alias in name, f'Ожидалось {alias}, но в строке {name} не найдено'

    @allure.step("Очистить список последних сеансов")
    def clear_last_seanses(self):
        self.click_connection_nav_bar()
        self.click(MainLocators.LAST_SEANSES, 'вкладка Последние сеансы')
        self.wait_a_second(2)
        self.del_all_devices_from_list()

    @allure.step("Считываем временный пароль")
    def get_temp_pass(self):
        string = self.get_description(MainLocators.TEMP_PASS)
        string = string.split('\n')
        temp_pass = string[4]
        return temp_pass

    @allure.step("Считываем идентификатор устройства")
    def get_id(self):
        string = self.get_description(MainLocators.TEMP_PASS)
        string = string.split('\n')
        id = string[2]
        return id

    @allure.step("Считываем идентификатор устройства")
    def get_id_or_alias_device(self):
        string = self.get_description(MainLocators.DEVICE_IN_LIST)
        string = string.split('\n')
        id = string[0]
        return id

    @allure.step("Проверка иконки подключения Прямое/Мост")
    def check_icon_connection_color(self, r, g, b):
        # Делаем скрин, определяем цвет пикселя в иконке по координатам и сравниваем с тем что на входе
        self.click(CSLocators.BUTTON_DISPLAY, 'кнопка [Дисплей]')
        x, y = self.get_element(CSLocators.ALL_SCREEN).center()
        y = 520
        self.get_screen()
        color = self.get_color_pixel(x,y)
        assert color == (r, g, b), f'Ожидалось {r, g, b}, а получено {color}'
        self.click(CSLocators.BUTTON_DISPLAY, 'кнопка [Дисплей]')
        self.close_connection()

    @allure.step("Активировать опцию [Всегда подключаться через мост]")
    def activate_connect_always_from_bridge(self):
        self.click_settings_nav_bar()
        self.click(MainLocators.CONNECTING_VIA_A_BRIDGE_SW)

    def click_search_btn(self):
        self.click(MainLocators.SEARCH_BTN, 'кнопка [Поиск]')

    def click_x_btn_in_search_field(self):
        self.click(MainLocators.CANCEL_SEARCH, 'кнопка [x] в поле [Поиск]')

    @allure.step("Выполнить поиск по ID")
    def search_by_id(self):
        self.click_connection_nav_bar()
        self.click_search_btn()
        # self.wait_a_second()
        # self.click('//*[@text="Поиск"]')
        self.wait_a_second(2)
        self.d.send_keys(invalid_remote_device_id)
        self.wait_a_second(2)
        self.wait_hidden_element(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION)
        self.click_x_btn_in_search_field()
        self.click_search_btn()
        self.d.send_keys(valid_remote_device_id)
        self.wait_a_second()
        self.wait_element(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION)
        self.click_x_btn_in_search_field()

    @allure.step("Выполнить поиск по псевдониму устройства")
    def search_by_alias(self, alias='alias'):
        self.set_alias(alias)
        self.click_ok()
        self.click_search_btn()
        self.d.send_keys('invalid_alias')
        self.wait_a_second()
        self.wait_hidden_element(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION)
        self.click_x_btn_in_search_field()
        self.click_search_btn()
        self.d.send_keys(alias)
        self.wait_a_second()
        self.wait_element(MainLocators.BUTTON_MORE_OPTIONS_CONNECTION)
        self.click_x_btn_in_search_field()

    @allure.step("Удалить псевдоним устройства")
    def delete_alias(self):
        self.click_more_option_connect()
        self.click(MainLocators.RENAME, 'пункт меню [Переименовать]')
        self.d.clear_text(MainLocators.ALIAS_FIELD)
        self.click_ok()

    @allure.step("Перезапустить удаленное устройство")
    def reboot_remote_device(self):
        self.click(CSLocators.BUTTON_MORE_OPTION, 'кнопка [...] на панели в окне подключения')
        self.click(CSLocators.REBOOT_REMOTE_DEVICE, 'пункт меню [Перезапустить удаленное устройство]')
        self.wait_element('//*[@content-desc="Перезапустить удаленное устройство"]')
        self.click_ok()
        self.wait_element('//*[@text="Ожидание перезагрузки удалённого устройства..."]')
        self.wait_a_second(60)

        # # Поменяем ожидание на цикл с проверкой
        # max_time = 100  # Максимальное время ожидания
        # check_interval = 10  # Интервал проверки

        # start_time = time.time()
        # while time.time() - start_time < max_time:
        #     waiting_reboot_gone = self.is_element_hidden('//*[@text="Ожидание перезагрузки удалённого устройства..."]')
        #     connection_error_gone = self.is_element_hidden('//*[@content-desc="Ошибка подключения"]')
        #     unstable_connection_gone = self.is_element_hidden(
        #         '//*[@text="Обнаружено нестабильное соединение, попытка повторного подключения..."]')
        #
        #     # Проверка, все ли три условия выполнены
        #     if waiting_reboot_gone and connection_error_gone and unstable_connection_gone:
        #         break
        #     print("Ожидание, пока все условия будут выполнены...")
        #     time.sleep(check_interval)

        self.wait_hidden_element('//*[@text="Ожидание перезагрузки удалённого устройства..."]')
        self.wait_hidden_element('//*[@content-desc="Ошибка подключения"]')
        self.wait_hidden_element('//*[@text="Обнаружено нестабильное соединение, попытка повторного подключения..."]')

    def check_alias_last(self, alias):
        self.click_settings_nav_bar()
        self.set_alias(alias)
        self.click_ok()
        device_alias = self.get_id_or_alias_device()
        assert alias == device_alias, f'Ожидался псевдоним устройства {alias}, но найден псевдоним {device_alias}'

    def check_alias_favorites(self, alias):
        self.add_to_favorites()
        device_alias = self.get_id_or_alias_device()
        assert alias == device_alias

    def check_alias_address_book(self, alias):
        self.add_to_address_book()
        device_alias = self.get_id_or_alias_device()
        assert alias == device_alias

    def check_msg_in_chat_main_window(self):
        string = self.get_description('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View')
        string = string.split('\n')
        msg = string[1]
        text = 'Съешь ещё этих мягких французских булок, да выпей чаю'
        assert msg == text, f'Ожидался текст {text}, но получен {msg}'

    @allure.step("Повторно ввести пароль")
    def wrong_pass_retry(self):
        if self.get_elements_amount(MainLocators.TITLE_WRONG_PASS) > 0:
            self.click(MainLocators.RETRY_ENTER_PASS)
            self.enter_passwd()
            self.click_ok()

    def check_version(self, version):
        self.swipe_to_element(MainLocators.VERSION)
        current_version = self.get_version()
        assert version == current_version, f'Текущая версия {current_version} не совпала с ожидаемой версией {version}'

    def get_version(self):
        string = self.get_description(MainLocators.VERSION)
        string = string.split('\n')
        version = string[0]
        version = version.split(': ')[1]
        return version
