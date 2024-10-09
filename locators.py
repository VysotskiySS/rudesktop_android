# file: locators.py
from config import *
import uiautomator2 as u2


# d = u2.connect(device_id)


class MainLocators:
    # SYSTEM
    ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH = '//android.widget.ScrollView/android.view.View[2]'
    BACK_BTN = '//androidx.compose.ui.platform.ComposeView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'
    OK_KEYBOARD = '//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]'

    # POPUP
    CANCEL_BTN = '//*[@content-desc="Отменить"]'
    OK_BTN = '//*[@content-desc="ОК"]'
    TITLE_WARNING = '//*[@content-desc="Предупреждение"]'

    # NAVBAR
    CONNECTION_BTN = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]'
    CHAT_BTN = '//*[contains(@content-desc, "Чат")]'
    ACCESS_BTN = '//*[contains(@content-desc, "Доступ")]'
    SETTINGS_BTN = '//*[contains(@content-desc, "Настройки")]'

    # CONNECTION_TAB
    REMOTE_ID_FIELD = '//*[@text="Удаленный идентификатор"]'
    CONNECT_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]'
    LAST_SEANSES = '//*[@content-desc="Последние сеансы"]'
    FAVOTITES = '//*[@content-desc="Избранное"]'
    ADDRESS_BOOK = '//*[@content-desc="Адресная книга"]'
    MESSAGE_UPDATE_APP = '//*[@content-desc="Приложение устарело. Обновите его через Google Play или на сайте rudesktop.ru"]'

    # CHAT
    TITLE = '//*[@content-desc="RuDesktop"]'
    CHAT_ICON_USER = '//android.widget.Button'
    CHAT_FIELD = '//*[@text="Написать сообщение..."]'
    CHAT_SEND_BTN = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'

    # ACCESS
    START_SERVICE_BTN = '//*[@content-desc="Запустить службу"]'
    CATCH_SCREEN_SW = '//*[@content-desc="Захват экрана"]'
    CATCH_INPUT_SW = '//*[@content-desc="Захват ввода"]'
    RECIEVE_FILES_SW = '//*[@content-desc="Передача файлов"]'
    CATCH_AUDIO_SW = '//*[@content-desc="Захват аудио"]'
    LEN_TEMP_PASS = '//*[@content-desc="Длина временного пароля"]'
    USE_TEMP_PASS = '//*[@content-desc="Использовать временный пароль"]'
    USE_PASS = '//*[@content-desc="Использовать постоянный пароль"]'
    USE_ALL_PASS = '//*[@content-desc="Использовать оба пароля"]'
    COPY_ID = '//*[contains(@content-desc, "Ваше устройство")]/android.widget.Button[1]'
    RESET_PASS = '//*[contains(@content-desc, "Ваше устройство")]/android.widget.Button[2]'
    COPY_PASS = '//*[contains(@content-desc, "Ваше устройство")]/android.widget.Button[3]'
    PASS_MORE_OPTIONS = '//*[contains(@content-desc, "Ваше устройство")]/android.widget.Button[4]'
    START_NOW_BTN = '//*[@resource-id="android:id/button1"]'
    CONNECTION_ERROR = '//*[@content-desc="Ошибка подключения. Нажмите, чтобы посмотреть подробности."]'
    VIEW_AND_ACCEPT_BNT = '//*[@content-desc="Просмотреть и принять"]'
    ACCEPT_BTN = '//*[@content-desc="Принять"]'

    # SETTINGS
    ACCOUNT_TITLE = '//*[@content-desc="Аккаунт"]'
    LOGIN = '//*[@content-desc="Аккаунт"]/android.view.View[1]'
    SETTINGS_TITLE = '//*[@content-desc="Настройки"]'
    SERVER_TO_CONNECT = '//*[@content-desc="Сервер для подключения"]'
    LANGUAGE = '//*[@content-desc="Язык интерфейса"]'
    NIGHT_THEME_SETTINGS = '//*[@content-desc="Ночная тема"]'
    CONNECTING_VIA_A_BRIDGE_SW = '//*[@content-desc="Всегда подключаться через мост"]/android.widget.Switch[1]'
    TITLE_SCREEN_CAPTURE = '//*[@content-desc="Запись экрана"]'
    AUTO_RECORD_INCOME_CONNECTIONS = '//*[contains(@content-desc="Автоматически записывать входящие подключения"])/android.widget.Switch[1]'
    TITLE_ACCESS = '//*[@content-desc="Доступ"]'
    ADAPTIVE_FLOW_RATE = '//*[@content-desc="Адаптивная скорость потока"]/android.widget.Switch[1]'
    ENABLE_RECORD_SESSION = '//*[@content-desc="Включить запись сессии"]/android.widget.Switch[1]'
    TITLE_ADDONS = '//*[@content-desc="Дополнения"]'
    LEAVE_RUNNING_IN_THE_BACKGROUND = '//*[contains(@content-desc, "Оставить работать в фоновом режиме")]'
    START_AFTER_SWITCHING_ON = '//*[contains(@content-desc, "Запускать после включения")]'
    TITLE_ABOUT_PROGRAM = '//*[@content-desc="О программе"]'
    VERSION = '//*[contains(@content-desc, "Version:")]'
    RESET_SETTINGS = '//*[@content-desc="Сбросить настройки"]'

    DEFAULT_LANGUAGE = '//*[@content-desc="Default"]'
    RUSSIAN_LANGUAGE = '//*[@content-desc="Русский"]'
    ENGLISH_LANGUAGE = '//*[@content-desc="English"]'
    KAZAK_LANGUAGE = '//*[@content-desc="Қазақ"]'

    DAYTIME_THEME = '//*[@content-desc="Дневная"]'
    NIGHT_THEME = '//*[@content-desc="Ночная"]'
    SYSTEM_THEME = '//*[@content-desc="Системная"]'

    '//*[@content-desc="Требуется пароль"]'
    '//*[@content-desc="Запомнить пароль"]'

    # CONNECTION_SCREEN
    BUTTON_X_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[0]'
    BUTTON_DISPLAY_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]'
    BUTTON_KEYBOARD_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[2]'
    BUTTON_MOUSE_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[3]'
    BUTTON_CHAT_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[4]'
    BUTTON_MORE_OPTIONS_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[5]'
    BUTTON_HIDE_CONNECTION_SCREEN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[5]'

    # CHAT
    CHAT_HIDE = '//*[@content-desc="Чат"]/android.widget.Button[1]'
    CHAT_X = '//*[@content-desc="Чат"]/android.widget.Button[2]'
    CHAR_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]'

    # MORE OPTIONS
    UPDATE = '//*[@content-desc="Обновить"]'
    PASSWORD_OS= '//*[@content-desc="Пароль операционной системы"]'
    PASTE = '//*[@content-desc="Вставить"]'
    ORIGINAL_SCALE = '//*[@content-desc="Оригинальный масштаб"]'
    INSERT_CTRL_ALT_DEL = '//*[@content-desc="Вставить Ctrl + Alt + Del"]'
    BLOCK_SESSION = '//*[@content-desc="Заблокировать сессию"]'
    RESTART_REMOTE_DEVICE = '//*[@content-desc="Перезапустить удаленное устройство"]'
    '//*[@content-desc="Начать запись сессии"]'











