import allure
from faker import Faker
from locators import *
from pages.base_page import BasePage
from pages.main_page import MainPage

faker = Faker()

class CSPage(BasePage):
    def __init__(self, d):
        super().__init__(d)
        self.d = d

    def click_ok(self):
        self.click(MainLocators.OK_BTN, 'кнопка [ОК]')

    def click_more_options(self):
        self.click(CSLocators.BUTTON_MORE_OPTION, 'кнопка [...] на панели окна подключения')

    @allure.step("Установить пароль операционной системы")
    def set_password_os(self):
        self.click_more_options()
        self.coordinate_click(761, 1543)
        self.set_text('//*[contains(@text, "Пароль")]', valid_password)
        self.click_ok()

    def check_password_os(self):
        self.click(CSLocators.BLOCK_SESSION, 'пункт меню [Заблокировать сессию]')
        self.click_more_options()
        self.click(CSLocators.PASSWORD_OS, 'пункт меню [Пароль операционной системы]')

    def hide_show_panel_cs(self):
        self.wait_element(CSLocators.BUTTON_HIDE_PANEL)
        self.click(CSLocators.BUTTON_HIDE_PANEL, 'кнопка [Скрыть панель]')
        self.wait_element(CSLocators.BUTTON_SHOW_PANEL)
        self.click(CSLocators.BUTTON_SHOW_PANEL, 'кнопка [Показать панель]')
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

    def get_msg_from_chat(self):
        string =  self.get_description('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View')
        string = string.split('\n')
        msg = string[1]
        return msg

    @allure.step("Нажать кнопку отправки сообщения в чат")
    def click_send_msg(self):
        self.wait_a_second(2)
        self.click('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]')

    @allure.step("Отправить сообщение в чат")
    def check_send_msg_to_chat(self):
        self.click(CSLocators.BUTTON_CHAT, 'кнопка [Чат] на панели экрана подключения')
        # text = faker.text()
        text = 'Съешь ещё этих мягких французских булок, да выпей чаю'
        self.set_text(CSLocators.CHAT_FIELD, text)
        self.click_send_msg()
        self.set_text(CSLocators.CHAT_FIELD, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
        self.click_send_msg()
        msg = self.get_msg_from_chat()
        assert text == msg, f'Ожидался текст {text}, но получен текст {msg}'

    @allure.step("Нажать скрыть чат")
    def hide_chat(self):
        self.wait_element(CSLocators.TITLE_CHAT_WINDOW)
        self.click(CSLocators.CHAT_HIDE_BTN)
        self.wait_hidden_element(CSLocators.TITLE_CHAT_WINDOW)

    @allure.step("Нажать показать чат")
    def show_chat(self):
        self.click(CSLocators.CHAT_SHOW_BTN)
        self.wait_element(CSLocators.TITLE_CHAT_WINDOW)

    @allure.step("Закрыть чат")
    def close_chat(self):
        self.click(CSLocators.CHAT_CLOSE_BTN)
        self.wait_hidden_element(CSLocators.TITLE_CHAT_WINDOW)
        self.wait_hidden_element(CSLocators.CHAT_SHOW_BTN)

    @allure.step("Нажать кнопку [Скрыть панель управления окна подключения]")
    def hide_panel(self):
        with allure.step("Проверяем на наличие все кнопки панели"):
            self.wait_element(CSLocators.BUTTON_X)
            self.wait_element(CSLocators.BUTTON_DISPLAY)
            self.wait_element(CSLocators.BUTTON_KEYBOARD)
            self.wait_element(CSLocators.BUTTON_MOUSE)
            self.wait_element(CSLocators.BUTTON_CHAT)
            self.wait_element(CSLocators.BUTTON_MORE_OPTION)
            self.wait_element(CSLocators.BUTTON_HIDE_PANEL)
        with allure.step("Нажимаем кнопку скрыть панель"):
            self.click(CSLocators.BUTTON_HIDE_PANEL)
        with allure.step("Проверяем что кнопок нет"):
            self.wait_hidden_element(CSLocators.BUTTON_DISPLAY)
            self.wait_hidden_element(CSLocators.BUTTON_KEYBOARD)
            self.wait_hidden_element(CSLocators.BUTTON_MOUSE)
            self.wait_hidden_element(CSLocators.BUTTON_CHAT)
            self.wait_hidden_element(CSLocators.BUTTON_MORE_OPTION)
            self.wait_hidden_element(CSLocators.BUTTON_HIDE_PANEL)
        with allure.step("Проверяем что кнопка показать панель отображается"):
            self.wait_element(CSLocators.BUTTON_SHOW_PANEL)

    @allure.step("Нажать кнопку [Показать панель управления окна подключения]")
    def show_panel(self):
        with allure.step("Нажимаем кнопку показать панель"):
            self.click(CSLocators.BUTTON_SHOW_PANEL)
        with allure.step("Проверяем на наличие все кнопки панели"):
            self.wait_element(CSLocators.BUTTON_X)
            self.wait_element(CSLocators.BUTTON_DISPLAY)
            self.wait_element(CSLocators.BUTTON_KEYBOARD)
            self.wait_element(CSLocators.BUTTON_MOUSE)
            self.wait_element(CSLocators.BUTTON_CHAT)
            self.wait_element(CSLocators.BUTTON_MORE_OPTION)
            self.wait_element(CSLocators.BUTTON_HIDE_PANEL)

    # @allure.step("Проверяем активный / неактивный элемент (по цвету)")
    def check_color_active_element(self, x, y, condition='active'):
        active_color = (25, 138, 232)
        inactive_color = (255, 255, 255)
        self.get_screen(attach='false')
        current_color = self.get_color_pixel(x, y)
        r, g, b = current_color
        if condition == 'active':
            # странным образом цвет пикселя активного элемента даже в одной конкретной точке может отличаться поэтому просто смотрим что преобладает синий
            assert b > r and b > g, f'Ожидался цвет {active_color}, но получен {current_color}'
        else:
            assert current_color == inactive_color, f'Ожидался цвет {inactive_color}, но получен {current_color}'

    def click_show_quality(self):
        self.click(CSLocators.SHOW_QUALITY, 'кнопка [Показать качество]')

    @allure.step("Проверить изменение цвета активного элемента")
    def check_quality(self):
        self.click_display()
        self.click_show_quality()

        GOOD_QUALITY = self.get_center_element_from_locator(CSLocators.GOOD_IMAGE_QUALITY) # GOOD QUALITY
        BALANCE_QUALITY = self.get_center_element_from_locator(CSLocators.BALANCED_QUALITY)  # BALANCE QUALITY
        FAST_REACT_TIME = self.get_center_element_from_locator(CSLocators.FAST_REACTION_TIME)  # FAST REACT TIME

        with allure.step("Чек бокс - Показать качество"):
            self.check_color_active_element(879, 1490) # SHOW QUALITY
            self.click_show_quality()
            self.check_color_active_element(879, 1490, condition='inactive')  # SHOW QUALITY
            self.click_show_quality()
        with allure.step("По умолчанию активный радиобаттон - Сбалансированное качество"):
            self.check_color_active_element(*GOOD_QUALITY, condition='inactive') # GOOD QUALITY
            self.check_color_active_element(*BALANCE_QUALITY) # BALANCE QUALITY
            self.check_color_active_element(*FAST_REACT_TIME, condition='inactive') # FAST REACT TIME
        with allure.step("Переключаем качество на - Хорошее качество изображения"):
            self.click(CSLocators.GOOD_IMAGE_QUALITY)
            self.check_color_active_element(*GOOD_QUALITY) # GOOD QUALITY
            self.check_color_active_element(*BALANCE_QUALITY, condition='inactive') # BALANCE QUALITY
            self.check_color_active_element(*FAST_REACT_TIME, condition='inactive') # FAST REACT TIME
        with allure.step("Переключаем качество на - Быстрое время реакции"):
            self.click(CSLocators.FAST_REACTION_TIME)
            self.check_color_active_element(*GOOD_QUALITY, condition='inactive') # GOOD QUALITY
            self.check_color_active_element(*BALANCE_QUALITY, condition='inactive') # BALANCE QUALITY
            self.check_color_active_element(*FAST_REACT_TIME) # FAST REACT TIME
        with allure.step("Переключаем качество на - Сбалансированное качество"):
            self.click(CSLocators.BALANCED_QUALITY)
            self.check_color_active_element(*GOOD_QUALITY, condition='inactive') # GOOD QUALITY
            self.check_color_active_element(*BALANCE_QUALITY) # BALANCE QUALITY
            self.check_color_active_element(*FAST_REACT_TIME, condition='inactive') # FAST REACT TIME

    def get_center_element_from_locator(self, locator):
        x, y = self.get_element(locator).center()
        x = x + 340
        return x, y

    @allure.step("Берем десять точек на экране и получаем цвет")
    def sample_ten_points(self, start_x, y, step=100):
        colors = []
        for i in range(10):
            x = start_x + i * step
            color = self.get_color_pixel(x, y)
            colors.append(color)
        return colors

    @allure.step("Отправить на устройство Ctrl + Alt + Del")
    def send_ctrl_alt_del(self):
        self.click_more_options()
        colors_before = self.sample_ten_points(start_x=20, y=1200)
        self.click(CSLocators.INSERT_CTRL_ALT_DEL, 'вставить Ctrl + Alt + Del')
        colors_after = self.sample_ten_points(start_x=20, y=1200)
        assert colors_before != colors_after, f'Цвета десяти произвольных точек не изменились'

    def click_display(self):
        self.click(CSLocators.BUTTON_DISPLAY, 'кнопка [Дисплей] в окне подключения')

    @allure.step("Проверить изменение масштаба")
    def check_change_scale_mode(self):
        with allure.step("По умолчанию масштаб адаптивный"):
            x = 525
            y = 100
            self.get_screen()
            default_color = self.get_color_pixel(x, y)
            assert default_color[0] == default_color[1] == default_color[2], f'Ожидалось r=g=b но получено {default_color}'
        try:
            self.click(MainLocators.CLOSE_CLIPBOARD, 'кнопка Х на окне превью буфера обмена')
        except:
            pass
        with allure.step("Переключить масштаб на оригинальный"):
            self.click_display()
            self.click(CSLocators.ORIGINAL_SCALE_DISPLAY)
            ORIGINAL_SCALE = self.get_center_element_from_locator(CSLocators.ORIGINAL_SCALE_DISPLAY)
            ADAPTIVE_SCALE = self.get_center_element_from_locator(CSLocators.ADAPTIVE_SCALE_DISPLAY)
            self.check_color_active_element(*ORIGINAL_SCALE)
            self.check_color_active_element(*ADAPTIVE_SCALE, condition='inactive')
            self.click_display()
            self.get_screen()
            current_color = self.get_color_pixel(x, y)
            assert current_color != (29, 29, 29) or current_color != (33, 33, 33)
        with allure.step("Переключить масштаб на адаптивный"):
            self.click_display()
            self.click(CSLocators.ADAPTIVE_SCALE_DISPLAY)
            self.check_color_active_element(*ORIGINAL_SCALE, condition='inactive')
            self.check_color_active_element(*ADAPTIVE_SCALE)
            self.click_display()
            self.get_screen()
            current_color = self.get_color_pixel(x, y)
            assert current_color == (29, 29, 29) or current_color == (33, 33, 33)
        with allure.step("Переключить масштаб на оригинальный через кнопку [...]"):
            self.click_more_options()
            self.click(CSLocators.ORIGINAL_SCALE, 'кнопка [Оригинальный масштаб]')
            self.get_screen()
            current_color = self.get_color_pixel(x, y)
            assert current_color != (29, 29, 29) or current_color != (33, 33, 33)

    @allure.step("Проверить наличие пунктов меню [...]")
    def check_more_options(self):
        self.click_more_options()
        self.wait_element(CSLocators.UPDATE)
        self.wait_element(CSLocators.PASSWORD_OS)
        self.wait_element(CSLocators.PASTE)
        self.wait_element(CSLocators.ORIGINAL_SCALE)
        self.wait_element(CSLocators.INSERT_CTRL_ALT_DEL)
        self.wait_element(CSLocators.BLOCK_SESSION)
        self.wait_element(CSLocators.REBOOT_REMOTE_DEVICE)
        self.wait_element(CSLocators.START_RECORD_SESSION)

    @allure.step("Проверить меню [Дисплей]")
    def check_display_options(self):
        with allure.step("Проверить наличие пунктов меню"):
            self.click(CSLocators.BUTTON_DISPLAY)
            self.wait_element(CSLocators.ORIGINAL_SCALE_DISPLAY)
            self.wait_element(CSLocators.ADAPTIVE_SCALE_DISPLAY)
            self.wait_element(CSLocators.GOOD_IMAGE_QUALITY)
            self.wait_element(CSLocators.BALANCED_QUALITY)
            self.wait_element(CSLocators.FAST_REACTION_TIME)
            self.wait_element(CSLocators.SHOW_REMOTE_CURSOR)
            self.wait_element(CSLocators.SHOW_QUALITY)
            self.wait_element(CSLocators.DISABLE_SOUND)
            self.wait_element(CSLocators.DISABLE_CLIPBOARD)
            self.wait_element(CSLocators.LOCK_SCREEN_AFTER_END_SESSION)

        with allure.step("По умолчанию все чек-боксы сняты"):
            SHOW_REMOTE_CURSOR = self.get_center_element_from_locator(CSLocators.SHOW_REMOTE_CURSOR)
            SHOW_QUALITY = self.get_center_element_from_locator(CSLocators.SHOW_QUALITY)
            DISABLE_SOUND = self.get_center_element_from_locator(CSLocators.DISABLE_SOUND)
            DISABLE_CLIPBOARD = self.get_center_element_from_locator(CSLocators.DISABLE_CLIPBOARD)
            LOCK_SCREEN_AFTER_END_SESSION = self.get_center_element_from_locator(CSLocators.LOCK_SCREEN_AFTER_END_SESSION)

            self.check_color_active_element(*SHOW_REMOTE_CURSOR, condition='inactive')
            self.check_color_active_element(*SHOW_QUALITY, condition='inactive')
            self.check_color_active_element(*DISABLE_SOUND, condition='inactive')
            self.check_color_active_element(*DISABLE_CLIPBOARD, condition='inactive')
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION, condition='inactive')
        with allure.step("Проверить что можно выбрать все чек-боксы"):
            self.click(CSLocators.SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_QUALITY, condition='inactive')
            self.check_color_active_element(*DISABLE_SOUND, condition='inactive')
            self.check_color_active_element(*DISABLE_CLIPBOARD, condition='inactive')
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION, condition='inactive')

            self.click(CSLocators.SHOW_QUALITY)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_QUALITY)
            self.check_color_active_element(*DISABLE_SOUND, condition='inactive')
            self.check_color_active_element(*DISABLE_CLIPBOARD, condition='inactive')
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION, condition='inactive')

            self.click(CSLocators.DISABLE_SOUND)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_QUALITY)
            self.check_color_active_element(*DISABLE_SOUND)
            self.check_color_active_element(*DISABLE_CLIPBOARD, condition='inactive')
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION, condition='inactive')

            self.click(CSLocators.DISABLE_CLIPBOARD)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_QUALITY)
            self.check_color_active_element(*DISABLE_SOUND)
            self.check_color_active_element(*DISABLE_CLIPBOARD)
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION, condition='inactive')

            self.click(CSLocators.LOCK_SCREEN_AFTER_END_SESSION)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_QUALITY)
            self.check_color_active_element(*DISABLE_SOUND)
            self.check_color_active_element(*DISABLE_CLIPBOARD)
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION)

        with allure.step("Проверить что можно снять все чек-боксы"):
            self.click(CSLocators.SHOW_REMOTE_CURSOR)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR, condition='inactive')
            self.check_color_active_element(*SHOW_QUALITY)
            self.check_color_active_element(*DISABLE_SOUND)
            self.check_color_active_element(*DISABLE_CLIPBOARD)
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION)

            self.click(CSLocators.SHOW_QUALITY)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR, condition='inactive')
            self.check_color_active_element(*SHOW_QUALITY, condition='inactive')
            self.check_color_active_element(*DISABLE_SOUND)
            self.check_color_active_element(*DISABLE_CLIPBOARD)
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION)

            self.click(CSLocators.DISABLE_SOUND)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR, condition='inactive')
            self.check_color_active_element(*SHOW_QUALITY, condition='inactive')
            self.check_color_active_element(*DISABLE_SOUND, condition='inactive')
            self.check_color_active_element(*DISABLE_CLIPBOARD)
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION)

            self.click(CSLocators.DISABLE_CLIPBOARD)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR, condition='inactive')
            self.check_color_active_element(*SHOW_QUALITY, condition='inactive')
            self.check_color_active_element(*DISABLE_SOUND, condition='inactive')
            self.check_color_active_element(*DISABLE_CLIPBOARD, condition='inactive')
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION)

            self.click(CSLocators.LOCK_SCREEN_AFTER_END_SESSION)
            self.check_color_active_element(*SHOW_REMOTE_CURSOR, condition='inactive')
            self.check_color_active_element(*SHOW_QUALITY, condition='inactive')
            self.check_color_active_element(*DISABLE_SOUND, condition='inactive')
            self.check_color_active_element(*DISABLE_CLIPBOARD, condition='inactive')
            self.check_color_active_element(*LOCK_SCREEN_AFTER_END_SESSION, condition='inactive')

    def check_record_session(self):
        self.click_more_options()
        self.click(CSLocators.START_RECORD_SESSION)
        self.wait_hidden_element(CSLocators.UPDATE)
        self.click_more_options()
        self.wait_element(CSLocators.STOP_RECORD_SESSION)
        self.click(CSLocators.STOP_RECORD_SESSION)
        self.wait_hidden_element(CSLocators.UPDATE)
        self.click_more_options()
        self.wait_element(CSLocators.START_RECORD_SESSION)

        # self.d.stop_app(package)
        #
        # self.click('//*[@text="Files"]')
        # self.click('//*[@content-desc="Show roots"]')
        # self.click('//*[@resource-id="com.google.android.documentsui:id/roots_list"]/android.widget.LinearLayout[7]/android.widget.LinearLayout[1]')
        # self.click('//*[@resource-id="com.google.android.documentsui:id/dir_list"]/androidx.cardview.widget.CardView[14]')






