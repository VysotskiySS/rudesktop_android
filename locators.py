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


    # NAVBAR
    CONNECTION_BTN = '//*[contains(@content-desc, "Соединение")]'
    CHAT_BTN = '//*[contains(@content-desc, "Чат")]'
    ACCESS_BTN = '//*[contains(@content-desc, "Доступ")]'
    SETTINGS_BTN = '//*[contains(@content-desc, "Настройки")]'

    # CONNECTION_TAB
    REMOTE_ID_FIELD = '//*[@text="Удаленный идентификатор"]'
    CONNECT_BTN = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]'
    LAST_SEANSES = '//*[@content-desc="Последние сеансы"]'
    FAVOTITES = '//*[@content-desc="Избранное"]'
    ADDRESS_BOOK = '//*[@content-desc="Адресная книга"]'

    # ACCESS
    START_SERVICE_BTN = '//*[@content-desc="Запустить службу"]'
    CATCH_SCREEN_SW = '//*[@content-desc="Захват экрана"]'
    CATCH_INPUT_SW = '//*[@content-desc="Захват ввода"]'
    RECIEVE_FILES_SW = '//*[@content-desc="Передача файлов"]'
    CATCH_AUDIO_SW = '//*[@content-desc="Захват аудио"]'

