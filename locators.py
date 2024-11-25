# file: locators.py
from config import *
import uiautomator2 as u2

# d = u2.connect(device_id)


class MainLocators:
    # SYSTEM
    ALLOW_ACCESS_TO_MANAGE_ALL_FILES_SWITCH = '//android.widget.ScrollView/android.view.View[2]'
    BACK_BTN = '//androidx.compose.ui.platform.ComposeView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'
    OK_KEYBOARD = '//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_ime_action"]/android.widget.FrameLayout[1]'
    X_BTN_CLIPBOARD = '//*[@resource-id="com.android.systemui:id/dismiss_button"]'
    CLIPBOARD_PREVIEW = '//*[@resource-id="com.android.systemui:id/clipboard_preview"]'
    PERMISSION_ALLOW_BTN = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'

    CHANGE_CERT_WARNING_TITLE = '//*[@content-desc="Сертификат сервера изменился"]'
    CHANGE_CERT_TEXT = '//*[contains(@content-desc="Сертификат сервера не является доверенным. Это может быть по разным причинам, например:")]'
    ACCEPT_NEW_CERT_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.Button[2]'
    CLOSE_BTN = '//*[@content-desc="Закрыть"]'

    # POPUP
    CANCEL_BTN = '//*[@content-desc="Отменить"]'
    OK_BTN = '//*[@content-desc="ОК"]'
    TITLE_WARNING = '//*[@content-desc="Предупреждение"]'

    # NAVBAR
    CONNECTION_BTN = '//*[contains(@content-desc, "Соединение")]'
    CHAT_BTN = '//*[contains(@content-desc, "Чат")]'
    ACCESS_BTN = '//*[contains(@content-desc, "Доступ")]'
    SETTINGS_BTN = '//*[contains(@content-desc, "Настройки")]'

    # CONNECTION_TAB
    REMOTE_ID_FIELD = '//*[@text="Удаленный идентификатор"]'
    CONNECT_BTN = '//*/android.widget.Button[1]'
    LAST_SEANSES = '//*[@content-desc="Последние сеансы"]'
    FAVOTITES = '//*[@content-desc="Избранное"]'
    ADDRESS_BOOK = '//*[@content-desc="Адресная книга"]'
    MESSAGE_UPDATE_APP = '//*[@content-desc="Приложение устарело. Обновите его через Google Play или на сайте rudesktop.ru"]'
    SEARCH_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.Button[1]'
    SEARCH_FIELD = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.EditText[1]'
    CANCEL_SEARCH = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.Button[1]'
    TITLE_WRONG_PASS = '//*[@content-desc="Неверный пароль"]'
    RETRY_ENTER_PASS = '//*[@content-desc="Попробовать снова"]'

    #CONNECTION
    BUTTON_MORE_OPTIONS_CONNECTION = '//*/android.widget.ImageView/*'
    DEVICE_IN_LIST = '//*//android.view.View//android.widget.ImageView'
    FILE_TRANSFER = '//*[@content-desc="Передача файлов"]'
    WAKE_ON_LAN = '//*[@content-desc="Разбудить (Wake On Lan)"]'
    RENAME = '//*[@content-desc="Переименовать"]'
    DELETE = '//*[@content-desc="Удалить"]'
    EDIT_TAG = '//*[@content-desc="Редактировать тег"]'
    ADD_TO_FAVORITES = '//*[@content-desc="Добавить в избранное"]'
    ADD_TO_ADDRESS_BOOK = '//*[@content-desc="Добавить в Адресную книгу"]'
    ALIAS_FIELD = '//*/android.widget.EditText[1]'

    # CHAT
    TITLE = '//*[@content-desc="RuDesktop"]'
    CHAT_ICON_USER = '//android.widget.Button'
    CHAT_FIELD = '//*[@text="Написать сообщение..."]'
    CHAT_SEND_BTN = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'

    # ACCESS
    START_SERVICE_BTN = '//*[@content-desc="Запустить службу"]'
    STOP_SERVICE_BTN = '//*[@content-desc="Остановить службу"]'
    CATCH_SCREEN_SW = '//*[@content-desc="Захват экрана"]'
    CATCH_INPUT_SW = '//*[@content-desc="Захват ввода"]'
    RECIEVE_FILES_SW = '//*[@content-desc="Передача файлов"]'
    CATCH_AUDIO_SW = '//*[@content-desc="Захват аудио"]'
    LEN_TEMP_PASS = '//*[@content-desc="Длина временного пароля"]'
    USE_TEMP_PASS = '//*[@content-desc="Использовать временный пароль"]'
    USE_PASS = '//*[@content-desc="Использовать постоянный пароль"]'
    USE_ALL_PASS = '//*[@content-desc="Использовать оба пароля"]'
    COPY_ID = '//*/android.widget.Button[1]'
    RESET_PASS = '//*/android.widget.Button[2]'
    COPY_PASS = '//*/android.widget.Button[3]'
    PASS_MORE_OPTIONS = '//*/android.widget.Button[4]'
    START_NOW_BTN = '//*[@resource-id="android:id/button1"]'
    CONNECTION_ERROR = '//*[@content-desc="Ошибка подключения. Нажмите, чтобы посмотреть подробности."]'
    VIEW_AND_ACCEPT_BNT = '//*[@content-desc="Просмотреть и принять"]'
    ACCEPT_BTN = '//*[@content-desc="Принять"]'
    SET_PERMANENT_PASS_BTN = '//*[@content-desc="Установить постоянный пароль"]'
    PASSWORD_FIELD = '//*[@text="Пароль"]'
    PASSWORD_CONFIRM_FIELD = '//*[@text="Подтверждение"]'
    PASSWORD_FIELD_FILLED = '//*[@text="•••••, Пароль"]'
    PASSWORD_CONFIRM_FIELD_FILLED = '//*[@text="•••••, Подтверждение"]'
    PASSWORD_WARNING_LENGTH = '//*[@content-desc="Слишком коротко, не менее 6 символов"]'
    PASSWORD_WARNING_IDENTITY = '//*[@content-desc="Подтверждение не идентично"]'
    PASS_LEN_6 = '//*[@content-desc="6"]'
    PASS_LEN_8 = '//*[@content-desc="8"]'
    PASS_LEN_10 = '//*[@content-desc="10"]'
    TEMP_PASS = '//*/android.widget.Button[2]/..'

    # SETTINGS
    ACCOUNT_TITLE = '//*[@content-desc="Аккаунт"]'
    LOGIN = '//*[@content-desc="Аккаунт"]/android.view.View[1]'
    LOGIN_ADDRESS_BOOK = '//*[@content-desc="Войти"]'
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
    RESET_SETTINGS_EN = '//*[@content-desc="Reset settings"]'
    DEFAULT_LANGUAGE = '//*[@content-desc="Default"]'
    RUSSIAN_LANGUAGE = '//*[@content-desc="Русский"]'
    ENGLISH_LANGUAGE = '//*[@content-desc="English"]'
    KAZAK_LANGUAGE = '//*[@content-desc="Қазақ"]'
    DAYTIME_THEME = '//*[@content-desc="Дневная"]'
    NIGHT_THEME = '//*[@content-desc="Ночная"]'
    SYSTEM_THEME = '//*[@content-desc="Системная"]'
    TITLE_RESET_SETTINGS = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'
    RESET_SETTINGS_CONFIRM = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.Button[2]'
    RESET_SETTINGS_CLOSE = '//*[@content-desc="Закрыть"]'
    RESET_SETTINGS_CLOSE_EN = '//*[@content-desc="Close"]'
    DOMAIN_AUTH_METHOD_RB = '//*[@content-desc="@win2012.local"]'

    # CHAT
    CHAT_HIDE = '//*[@content-desc="Чат"]/android.widget.Button[1]'
    CHAT_X = '//*[@content-desc="Чат"]/android.widget.Button[2]'
    CHAR_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]'

    UPDATE = '//*[@content-desc="Обновить"]'

    SERVER_TO_CONNECT_FIELD = '//*[contains(@text, "Сервер для подключения")] OR //*[@text="1.rz.rudesktop.ru:443"]'
    LOGIN_FIELD = '//*[@text="Логин"]'
    SEE_OR_HIDE_PASS_BTN = '//*/android.widget.Button[1]'
    SAVE_PASS_SW = '//*[@content-desc="Запомнить пароль"]'
    WARNING_INVALID_EMAIL_OR_PASS = '//*[@content-desc="Неверный E-Mail или пароль"]'
    WARNING_NOT_FOUND_USER_AD = '//*[@content-desc="Не удалось найти пользователя в службе каталогов"]'
    ADD_ID = '//*[@content-desc="Добавить ID"]'
    ADD_TAG = '//*[@content-desc="Добавить тег"]'
    CANCEL_SELECT_TAG = '//*[@content-desc="Отменить выбор всех тегов"]'
    CLEAR_FIELD_RENAME_TAG = '//*/android.widget.EditText[1]'

    CONNECT_BNT_MORE_OPTION = '//*[@content-desc="Подключиться"]'

# CONNECTION_SCREEN
class CSLocators:
    BUTTON_X = '//*/android.widget.Button[1]'
    BUTTON_DISPLAY = '//*/android.widget.Button[2]'
    BUTTON_KEYBOARD = '//*/android.widget.Button[3]'
    BUTTON_MOUSE = '//*/android.widget.Button[4]'
    BUTTON_CHAT = '//*/android.widget.Button[5]'

    BUTTON_MORE_OPTION = '//*/android.widget.Button[6]'
    BUTTON_HIDE_PANEL = '//*/android.widget.Button[7]'
    BUTTON_SHOW_PANEL = '//android.widget.Button'
    ALL_SCREEN = '//android.widget.FrameLayout[1]'

    # MORE OPTIONS
    UPDATE = '//*[@content-desc="Обновить"]'
    PASSWORD_OS= '//*[@content-desc="Пароль операционной системы"]'
    PASTE = '//*[@content-desc="Вставить"]'
    ORIGINAL_SCALE = '//*[@content-desc="Оригинальный масштаб"]'
    INSERT_CTRL_ALT_DEL = '//*[@content-desc="Вставить Ctrl + Alt + Del"]'
    BLOCK_SESSION = '//*[@content-desc="Заблокировать сессию"]'
    REBOOT_REMOTE_DEVICE = '//*[@content-desc="Перезапустить удаленное устройство"]'
    START_RECORD_SESSION = '//*[@content-desc="Начать запись сессии"]'

    # MOUSE OR SENSOR
    MOUSE_MODE_BTN = '//*[@content-desc="Режим мыши"]'
    SENSOR_MODE_BTN = '//*[@content-desc="Сенсорный режим"]'

    # CHAT
    TITLE_CHAT_WINDOW = '//*[@content-desc="Чат"]'
    CHAT_FIELD = '//*[@text="Написать сообщение..."]'
    CHAT_HIDE_BTN = '//*[@content-desc="Чат"]/android.widget.Button[1]'
    CHAT_CLOSE_BTN = '//*[@content-desc="Чат"]/android.widget.Button[2]'
    CHAT_SHOW_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'

    # DISPLAY
    ORIGINAL_SCALE_DISPLAY = '//*[@content-desc="Оригинал масштаба"]'
    ADAPTIVE_SCALE_DISPLAY = '//*[@content-desc="Масштаб адаптивный"]'
    GOOD_IMAGE_QUALITY = '//*[@content-desc="Хорошее качество изображения"]'
    BALANCED_QUALITY = '//*[@content-desc="Сбалансированное качество"]'
    FAST_REACTION_TIME = '//*[@content-desc="Быстрое время реакции"]'
    SHOW_REMOTE_CURSOR = '//*[@content-desc="Показать удаленный курсор"]'
    SHOW_QUALITY = '//*[@content-desc="Показать качество"]'
    DISABLE_SOUND = '//*[@content-desc="Отключить звук"]'
    DISABLE_CLIPBOARD = '//*[@content-desc="Отключить буфер обмена"]'
    LOCK_SCREEN_AFTER_END_SESSION = '//*[@content-desc="Блокировка экрана после завершения сеанса"]'









