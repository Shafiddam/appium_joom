import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        # deviceName='emulator-5554',
        deviceName='1325437499100958',
        # appPackage='com.android.settings',
        # appActivity='.Settings',
        language='ru',
        locale='RU'
    )
    # Добавим вывод для отладки (чтобы видеть, куда подключаемся)
    print(f"\nПодключаюсь к Appium по адресу: {appium_server_url}")
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()


appium_server_url = os.getenv('APPIUM_URL','http://localhost:4723')


class TestAppium:
    """
    # Локаторы для Joom в эмуляторе:
    JOOM_ICON = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Joom"]')  # эмулятор
    SETTINGS_ICON = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Настройки"]')  # эмулятор
    PROFILE_ICON = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.joom:id/main_bottom_bar"]/android.view.ViewGroup[5]')  # эмулятор
    CURRENCY_MENU = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.joom:id/recycler"]/android.widget.Button[3]')
    USD_RADIO = (AppiumBy.XPATH, '//android.widget.RadioButton[@text="Доллар США"]')
    BUTTON_FIND = (AppiumBy.ID, 'com.joom:id/start_button')
    SEARCH_FIELD = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.joom:id/search"]')
    SEARCH_FIELD_2 = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.joom:id/search_field"]')
    SEARCH_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.joom:id/input"]')
    SEARCH_TITLE_DRESS = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.joom:id/row_layout_title" and @text="Категория: Платья"]')
    BUTTON_SORT = (AppiumBy.XPATH,'//android.widget.LinearLayout[@content-desc="Сортировка, Не выбрано"]/android.widget.ImageView')
    BUTTON_ASK = (AppiumBy.XPATH, '//android.widget.RadioButton[@text="По возрастающей цене"]')
    """

    # Локаторы для Joom в телефоне:
    DESC_JOOM_ICON = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Джум"]')
    BOTTOM_BAR_HOME = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="tech.jm:id/bottom_bar_home"]')
    BOTTOM_BAR_SEARCH = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="tech.jm:id/bottom_bar_search"]')
    BOTTOM_BAR_FAVORITES = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="tech.jm:id/bottom_bar_favorites"]')
    BOTTOM_BAR_CART = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="tech.jm:id/bottom_bar_cart"]')
    BOTTOM_BAR_PROFILE = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="tech.jm:id/bottom_bar_profile"]')

    SETTINGS_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Настройки"]/android.widget.ImageView')
    CURRENCY_MENU = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="tech.jm:id/recycler"]/android.widget.Button[5]')
    BYN_RADIO = (AppiumBy.XPATH, '//android.widget.RadioButton[.//*[contains(@text, "Белорусский рубль")]]')
    BUTTON_FIND = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Поиск"]')
    SEARCH_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск в Джум"]')
    SEARCH_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="tech.jm:id/search_field_input"]')
    SEARCH_TITLE_DRESS = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="tech.jm:id/row_layout_title" and @text="Платья"]')
    BUTTON_SORT = (AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Сортировка, Не выбрано"]')
    BUTTON_SORT_ASK = (AppiumBy.XPATH, '//android.widget.RadioButton[@resource-id="tech.jm:id/row_layout_title" and @text="По возрастающей цене"]')

    TAB_STOCKS = (AppiumBy.XPATH, '//android.widget.TextView[@text="Акции"]')
    TAB_BEST = (AppiumBy.XPATH, '//android.widget.TextView[@text="Лучшее"]')

    ITEM_1 = (AppiumBy.XPATH, '//android.widget.GridView[@resource-id="tech.jm:id/feed_recycler"]/androidx.compose.ui.platform.ComposeView[2]/android.view.View/android.view.View')
    ICON_HEART = (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Избранное"]')
    MENU_FAVORITE = (AppiumBy.XPATH, '//android.widget.GridView[@resource-id="tech.jm:id/recycler"]/androidx.compose.ui.platform.ComposeView[5]/android.view.View/android.view.View')
    ITEM_IN_FAVORITE = (AppiumBy.XPATH, '//android.widget.GridView[@resource-id="tech.jm:id/feed_recycler"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View')

    # Вспомогательные методы
    @staticmethod
    def element_is_clickable(driver, locator):
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def is_clickable(driver, locator):
        """ Проверяет кликабельность по атрибуту и возвращает True, иначе False """
        element = driver.find_element(*locator)
        print (element.get_attribute("clickable"))
        return element.get_attribute("clickable") == "true"

    @staticmethod
    def wait_for_element_presence(driver, locator, timeout=20):
        """ Ждёт появления элемента и возвращает его. """
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден по локатору: {locator}")

    @staticmethod
    def return_parent_element(driver, locator):
        element = driver.find_element(*locator)
        return element.find_element(AppiumBy.XPATH, "..")

    @staticmethod
    def swipe_up(driver, duration=1000):
        """Свайп вверх по центру экрана (прокрутка списка вверх)."""
        window_size = driver.get_window_size()
        width = window_size['width']
        height = window_size['height']
        start_y = int(height * 0.8)  # Стартовая точка — ближе к низу экрана (например, 80% высоты)
        end_y = int(height * 0.2)  # Конечная точка — выше (например, 20% высоты)
        x = int(width / 2)  # по центру по горизонтали
        driver.swipe(x, start_y, x, end_y, duration)

    @staticmethod
    def swipe_down(driver, duration=2000):
        """Свайп вниз """
        size = driver.get_window_size()
        width, height = size['width'], size['height']
        x = int(width * 0.5)
        start_y = int(height * 0.3)
        end_y = int(height * 0.8)
        print(f"\nwidth = {width}, height = {size['height']} \nstart_y = {start_y}, end_y = {end_y}")
        driver.swipe(x, start_y, x, end_y, duration)

    @staticmethod
    def swipe_left(driver, percent=0.4, duration=1000):
        size = driver.get_window_size()
        x, y = int(size['width'] * 0.5), int(size['height'] * 0.8)
        width = int(size['width'])
        start_x = x + int(width * percent)
        end_x = x - int(width * percent)
        print(f"\nwidth = {width}, height = {size['height']} \ny = {y}, start_x = {start_x}, end_x = {end_x}")
        driver.swipe(start_x, y, end_x, y, duration)

    def start_joom(self, driver):
        # driver.terminate_app("com.joom") # случай когда запускаем в эмуляторе
        driver.terminate_app("tech.jm")
        driver.press_keycode(3)  # HOME (код 3)
        self.element_is_clickable(driver, self.DESC_JOOM_ICON).click()

    def test_joom_select_currency(self, driver):
        """ Выбор валюты.
        Шаги:
            Перейти в профиль
            Выбрать настройки
            Выбрать “Валюта”
            Выбрать “Доллар США” (его нет, заменил на "белорусский рубль")
            Перейти на Главную страницу
        Ожидаемый результат: цены в долларах
        """
        self.start_joom(driver)
        self.element_is_clickable(driver, self.BOTTOM_BAR_PROFILE).click()
        self.element_is_clickable(driver, self.SETTINGS_ICON).click()
        self.element_is_clickable(driver, self.CURRENCY_MENU).click()
        self.element_is_clickable(driver, self.BYN_RADIO).click()
        driver.back()
        self.element_is_clickable(driver, self.BOTTOM_BAR_HOME).click()

    def test_joom_sort(self, driver):
        """ Сортировка.
        Шаги:
            Нажать “Поиск в Joom”
            Ввести “Платья”
            Выбрать из предложенных вариантов “платья”
            Выбрать “Сортировать”
            Выбрать “По возрастающей цене”
        Ожидаемый результат: цена товаров стала отсортирована по возрастанию.
        """
        self.start_joom(driver)
        self.element_is_clickable(driver, self.BUTTON_FIND).click()
        self.element_is_clickable(driver, self.SEARCH_FIELD).click()
        self.element_is_clickable(driver, self.SEARCH_INPUT).click()
        self.element_is_clickable(driver, self.SEARCH_INPUT).send_keys("Платья")
        self.element_is_clickable(driver, self.SEARCH_TITLE_DRESS).click()
        self.element_is_clickable(driver, self.BUTTON_SORT).click()
        self.element_is_clickable(driver, self.BUTTON_SORT_ASK).click()
        # Ожидаемый результат: цена товаров стала отсортирована по возрастанию:
        # взять два первых отсортированных значения из БД и сравнить их с выводом на UI

    def test_joom_swipe_left(self, driver):
        """ Вкладки.
        Шаги:
            Открыть главный экран.
            Сделать свайп влево.
        Ожидаемый результат: вкладка 'Акции' открыта (активна), вкладка 'Лучшее' не активна.
        """
        self.start_joom(driver)
        self.wait_for_element_presence(driver, self.TAB_STOCKS)
        self.swipe_left(driver)
        element = self.wait_for_element_presence(driver, self.TAB_STOCKS)
        assert element.get_attribute("selected") == "true", "Ошибка: вкладка 'Акции' не открыта (не активна)"
        element = self.wait_for_element_presence(driver, self.TAB_BEST)
        assert element.get_attribute("selected") == "false", "Ошибка: вкладка 'Лучшее' открыта (активна)"

    def test_add_to_favorite(self, driver):
        """ Добавление в избранное.
        Шаги:
            Открыть товар.
            Добавить товар в избранное.
            Перейти на вкладку профиля.
            Открыть список с избранными товарами.
            Обновить экран (потянуть вниз).
        Ожидаемый результат: в списке избранного есть один товар.
        """
        self.start_joom(driver)
        self.element_is_clickable(driver, self.ITEM_1).click()
        self.element_is_clickable(driver, self.ICON_HEART).click()
        driver.back()
        self.element_is_clickable(driver, self.BOTTOM_BAR_PROFILE).click()
        self.element_is_clickable(driver, self.MENU_FAVORITE).click()
        self.swipe_down(driver)
        element = self.wait_for_element_presence(driver, self.ITEM_IN_FAVORITE)
        assert element.is_displayed(), "Элемент в избранном не отображается"

