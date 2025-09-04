import allure

from pages.base_page import BasePage
from locators.burger_constructor_page_locators import MainPageLocators
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    """
    Page Object главной страницы конструктора Stellar Burgers.
    Содержит действия с хедером, ингредиентами, модалками и оформлением заказа.
    """

    @allure.step('Проверить кликабельность ингредиента')
    def check_if_ingredient_is_clickable(self):
        """
        Проверяет, доступен ли ингредиент для клика.
        Return:
            bool: True, если элемент кликабелен.
        """
        return self.is_element_clickable(MainPageLocators.IMG_FIRST_BUN)

    @allure.step('Закрыть модальное окно деталей ингредиента')
    def click_on_close_button_details_ingredient_screen(self):
        """
        Закрывает модалку деталей ингредиента.
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.BTN_CLOSE_INGREDIENT_MODAL)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_on_create_order_button(self):
        """
        Кликает по кнопке оформления заказа.
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.BTN_CREATE_ORDER)

    @allure.step('Нажать на изображение первого ингредиента')
    def click_on_first_ingredient(self):
        """
        Кликает по изображению первого ингредиента, чтобы открыть модалку.
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.IMG_FIRST_BUN)

    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_on_login_button(self):
        """
        Кликает по кнопке "Войти в аккаунт" на главной странице.
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.BTN_LOGIN_MAIN)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_on_order_feed_button(self):
        """
        Кликает по кнопке перехода в публичную ленту заказов.
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.BTN_ORDER_FEED)

    @allure.step('Нажать на кнопку "Личный кабинет" в шапке')
    def click_on_personal_acc_button(self):
        """
        Кликает по кнопке перехода в личный кабинет.
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.BTN_PERSONAL_ACCOUNT)

    @allure.step('Нажать на кнопку секции "Соусы"')
    def click_on_sauce_section_button(self):
        """
        Кликает по вкладке секции "Соусы".
        """
        self.page_loading_wait()
        self.click_on_element(MainPageLocators.SECTION_SAUCES)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_popup_screen(self):
        """
        Нажимает на крестик модалки заказа и ждёт её исчезновения (невидимость).
        """
        # Убеждаемся, что модалка действительно открыта
        self.wait_for_presence(MainPageLocators.MODAL_ROOT, timeout=10)

        # Пытаемся кликнуть крестик; если клик перехвачен оверлеем — закроем кликнув по оверлею
        try:
            self.click_on_element(MainPageLocators.BTN_CLOSE_ORDER_MODAL, timeout=30)
        except ElementClickInterceptedException:
            self.click_on_element(MainPageLocators.MODAL_OVERLAY, timeout=30)

        # Ждём, что модалка и оверлей исчезли (инвиз)
        self.wait_for_invisibility(MainPageLocators.MODAL_ROOT, timeout=30)
        self.wait_for_invisibility(MainPageLocators.MODAL_OVERLAY, timeout=30)

    @allure.step('Оформить заказ (перетянуть + клик)')
    def create_order(self):
        """
        Выполняет оформление заказа: перетаскивание ингредиента + кнопка.
        """
        self.drop_bun_into_order_sector()
        self.click_on_create_order_button()
    

    @allure.step('Перетащить булку в конструктор бургера')
    def drop_bun_into_order_sector(self):
        """
        Перетаскивает первую булку в область конструктора.
        Ждёт, пока счётчик на её карточке станет '2' (верх+низ).
        """
        self.page_loading_wait()
        source = MainPageLocators.INGREDIENT_FIRST_BUN
        target = MainPageLocators.SECTION_CONSTRUCTOR_LIST

        # перетаскиваем через seletools (устойчиво для FF)
        self.drag_and_drop_element(source, target)

        # в FF UI может обновляться чуть дольше — ждём счётчик '2'
        try:
            self.wait_for_text_in_element(MainPageLocators.COUNTER_FIRST_INGREDIENT, '2', timeout=8)
        except TimeoutException:
            # если интерфейс ещё не успел, даём последний шанс
            self.wait_for_text_in_element(MainPageLocators.COUNTER_FIRST_INGREDIENT, '2', timeout=5)

    @allure.step('Получить значение счётчика ингредиента')
    def get_counter_number(self):
        """
        Получает текст числового счётчика у ингредиента.
        Return:
            str: значение счётчика.
        """
        return self.get_text_on_element(MainPageLocators.COUNTER_FIRST_INGREDIENT)

    @allure.step('Получить номер созданного заказа')
    def get_order_number(self):
        """
        Получает номер заказа из модального окна.
        Return:
            str: номер заказа.
        """
        self.wait_for_loading_animation_end()
        return self.get_text_on_element(MainPageLocators.MODAL_ORDER_ID)

    @allure.step('Получить текст подтверждения успешного заказа')
    def get_successful_text_popup_order_screen(self):
        """
        Получает текст об успешном создании заказа из модального окна.
        Return:
            str: подтверждающий текст.
        """
        return self.get_text_on_element(MainPageLocators.TEXT_ORDER_SUCCESS)

    @allure.step('Получить заголовок модального окна ингредиента')
    def get_title_text_detail_ingredient_screen(self):
        """
        Получает текст заголовка модалки с деталями ингредиента.
        Return:
            str: заголовок модального окна.
        """
        return self.get_text_on_element(MainPageLocators.MODAL_INGREDIENT_TITLE)

    @allure.step("Дождаться окончания загрузки (анимация)")
    def wait_for_loading_animation_end(self, appear_timeout=5, disappear_timeout=30):
        """
        Сначала ждём, что спиннер ПРИСУТСТВУЕТ (если успеет появиться),
        затем ждём его исчезновения. Это убирает гонки.
        Args:
            appear_timeout (int): таймаут ожидания появления спиннера
            disappear_timeout (int): таймаут ожидания исчезновения спиннера
        """
        try:
            self.wait_for_presence(MainPageLocators.IMG_LOADING_ANIMATION, timeout=appear_timeout)
            self.wait_for_invisibility(MainPageLocators.IMG_LOADING_ANIMATION, timeout=disappear_timeout)
        except Exception:
            # если спиннер не появился в отведённое время — продолжаем без ошибки
            pass