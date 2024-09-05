# file: locators.py
from config import *
import uiautomator2 as u2


# d = u2.connect(device_id)


class MainLocators:
    # BASE
    X_BUTTON = '//android.widget.ImageButton'
    NOTIFICATION_NEGATIVE = '//*[@resource-id="ru.limeshop.android.dev:id/notification_negative_button"]'
    notification_positive_button = "ru.limeshop.android.dev:id/notification_positive_button"
    TOOLBAR_TITLE = 'ru.limeshop.android.dev:id/toolbarTitle'
    lime_logo = 'ru.limeshop.android.dev:id/banner_label_image_view'
    snack_bar_message = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    SCREENGIFTCARD = "ru.limeshop.android:id/baseContainer"
    # POPUP
    POPUP_CLEAR = '//*[@resource-id="ru.limeshop.android.dev:id/positive_button_outlined"]'
    POPUP_CANCEL = '//*[@resource-id="ru.limeshop.android.dev:id/negative_button"]'
    POPUP_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    POPUP_DESCRIPTION = '//*[@resource-id="ru.limeshop.android.dev:id/message_text_view"]'
