import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.burger_constructor_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

from seletools.actions import drag_and_drop


class BasePage:
    """
    Базовый класс страницы. Содержит общие методы взаимодействия с элементами UI.
    """

    def __init__(self, driver):
        """
        Инициализация драйвера браузера.
        Args:
            driver (WebDriver): активный веб-драйвер.
        """
        self.driver = driver

    @allure.step("Проверить характеристику элемента")
    def check_attribute_in_element_status(self, locator, attribute, text):
        """
        Проверяет наличие текста в атрибуте элемента.
        Args:
            locator (tuple): локатор элемента.
            attribute (str): имя атрибута.
            text (str): ожидаемое содержимое.
        Return:
            bool: результат проверки.
        """
        return EC.text_to_be_present_in_element_attribute(locator, attribute, text)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=30):
        """
        Кликает по элементу, дождавшись его кликабельности.
        В случае перехвата клика (overlay) скроллит к элементу, ждёт исчезновения оверлея
        и выполняет клик через ActionChains.
        Args:
            locator (tuple): локатор элемента.
            timeout (int): время ожидания.
        """
        element = self.wait_for_clickable(locator, timeout)
        try:
            element.click()
        except ElementClickInterceptedException:
            # Если клик перехвачен оверлеем — подстрахуемся:
            try:
                # если оверлей есть — подождём, пока исчезнет (если его нет, условие и так быстро вернётся)
                self.wait_for_element_hide(MainPageLocators.OVERLAY, 5)
            except Exception:
                pass
            # прокрутим к элементу и кликнем через ActionChains
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        """
        Перетаскивает элемент с помощью seletools (устойчиво для HTML5-DnD, особенно в Firefox).
        Args:
            source (tuple|WebElement): локатор или WebElement источника.
            target (tuple|WebElement): локатор или WebElement цели.
        """
        src_el = self.wait_for_element(source) if isinstance(source, tuple) else source
        dst_el = self.wait_for_element(target) if isinstance(target, tuple) else target
        # скроллим в центр, чтобы исключить перекрытия/вне вьюпорта
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", src_el)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dst_el)
        drag_and_drop(self.driver, src_el, dst_el)

    @allure.step("Узнать URL открытой страницы")
    def get_current_page_url(self):
        """
        Возвращает текущий URL открытой страницы.
        Return:
            str: текущий URL.
        """
        return self.driver.current_url

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        """
        Получает текст элемента.
        Args:
            locator (tuple): локатор элемента.
        Return:
            str: текст из элемента.
        """
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Элемент кликабелен?")
    def is_element_clickable(self, locator, timeout=10):
        """
        Проверяет кликабельность элемента за отведённый таймаут.
        Return:
            bool: True если стал кликабельным, иначе False
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидаем исчезновения оверлея и загрузок')
    def page_loading_wait(self):
        """
        Универсальное ожидание для главной/модальных экранов: ждём исчезновения оверлея.
        В Firefox держим таймаут больше — оверлей исчезает заметно дольше.
        """
        browser = (self.driver.capabilities or {}).get('browserName', '').lower()
        timeout = 18 if browser == 'firefox' else 10
        # основной оверлей
        try:
            self.wait_for_element_hide(MainPageLocators.OVERLAY, timeout=timeout)
        except Exception:
            # если оверлея уже нет — окей, продолжаем
            pass

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        """
        Скроллит страницу до нужного элемента.
        Args:
            locator (tuple): локатор элемента.
        """
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys):
        """
        Вводит текст в указанное поле.
        Args:
            locator (tuple): локатор поля ввода.
            keys (str): текст для ввода.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Переключиться на другую вкладку")
    def switch_to_another_window(self, locator):
        """
        Переключается на новое окно браузера.
        Args:
            locator (tuple): локатор, который должен появиться на новой вкладке.
        """
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
        self.wait_for_element(locator)

    @allure.step("Подождать кликабельность элемента")
    def wait_for_clickable(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет кликабельным.
        Args:
            locator (tuple): локатор элемента.
            timeout (int): время ожидания в секундах.
        Return:
            WebElement: найденный элемент.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Подождать, пока элемент будет удалён из DOM")
    def wait_for_detached(self, element, timeout=30):
        """
        Ждёт, когда переданный элемент исчезнет из DOM.
        Args:
            element (WebElement): ранее найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(EC.staleness_of(element))

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=30):
        """
        Ожидает, пока элемент станет видимым.
        Args:
            locator (tuple): локатор элемента.
            timeout (int): время ожидания в секундах.
        Return:
            WebElement: найденный элемент.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Подождать исчезновение элемента")
    def wait_for_element_disappear(self, locator: tuple, timeout=10):
        """
        Ожидает, пока элемент станет невидимым.
        Args:
            locator (tuple): локатор элемента.
            timeout (int): время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Ждём, пока элемент станет невидимым')
    def wait_for_element_hide(self, locator, timeout: int = 10):
        """
        Явно ждёт, пока элемент исчезнет со страницы или станет невидимым.
        Args:
            locator (tuple): (By, селектор) скрываемого элемента/оверлея.
            timeout (int): таймаут ожидания в секундах.
        Return:
            bool: True, если элемент стал невидимым в течение таймаута.
        """
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return True
    
    @allure.step("Подождать исчезновение элемента (инвиз или удалён из DOM)")
    def wait_for_invisibility(self, locator, timeout=30):
        """
        Ждёт, когда элемент станет невидимым или будет удалён из DOM.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Подождать появления элемента в DOM")
    def wait_for_presence(self, locator, timeout=10):
        """
        Ждёт появления элемента в DOM (не обязательно видимого).
        Args:
            locator (tuple): локатор
            timeout (int): таймаут в секундах
        Return:
            WebElement: найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    @allure.step("Подождать появления текста в элементе")
    def wait_for_text_in_element(self, locator: tuple, text: str, timeout: int = 10) -> bool:
        """
        Ждёт, пока указанный текст появится в элементе.
        Args:
            locator (tuple): локатор элемента (By, value).
            text (str): ожидаемый текст.
            timeout (int): таймаут ожидания в секундах.
        Return:
            bool: True, если текст появился в течение таймаута.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    @allure.step("Ждём выполнение любого условия из набора")
    def wait_any(self, conditions, timeout: int = 10, poll_frequency: float = 0.2):
        """
        Ждёт выполнение ЛЮБОГО условия из набора.
        Args:
            conditions (Iterable[Callable]): функции/EC-условия вида cond(driver).
            timeout (int): таймаут ожидания в секундах.
            poll_frequency (float): период опроса (частота попыток).
        Return:
            Any: результат первого сработавшего условия (WebElement/True и т.п.).
        """
        def _any_condition(driver):
            for cond in conditions:
                try:
                    result = cond(driver)
                    if result:
                        return result
                except Exception:
                    # Если одно из условий бросило исключение — просто пробуем остальные
                    continue
            return False  # сигнализируем WebDriverWait, что пока не готово

        return WebDriverWait(self.driver, timeout, poll_frequency).until(_any_condition)

    @allure.step("Проверить наличие элемента в DOM")
    def is_present(self, locator: tuple, timeout: int = 0) -> bool:
        """
        Проверяет наличие элемента в DOM (без падения теста).
        Args:
            locator (tuple): локатор (By, value).
            timeout (int): опциональный таймаут ожидания.
        Return:
            bool: True, если элемент найден.
        """
        try:
            if timeout > 0:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            else:
                self.driver.find_element(*locator)
            return True
        except Exception:
            return False

    @allure.step('Ждём, пока URL будет содержать подстроку: "{url_substring}"')
    def wait_for_url(self, url_substring: str, timeout: int = 10) -> bool:
        """
        Ждёт, пока текущий URL будет содержать указанную подстроку.
        Args:
            url_substring (str): часть URL.
            timeout (int): таймаут ожидания.
        Return:
            bool: True, если условие выполнено.
        """
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_substring))
        return True
    
    @allure.step("Универсальное ожидание по предикату")
    def wait_until(self, predicate, timeout: int = 10, poll_frequency: float = 0.2):
        """
        Выполняет ожидание, пока переданный предикат вернёт истину.
        Предикат должен принимать драйвер и возвращать truthy-значение.
        Args:
            predicate (Callable): функция вида predicate(driver) -> Any.
            timeout (int): таймаут ожидания в секундах.
            poll_frequency (float): частота опроса предиката.
        Return:
            Any: результат предиката, когда он вернёт истину.
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(predicate)