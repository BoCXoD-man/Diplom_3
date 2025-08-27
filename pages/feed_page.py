import allure

from locators.feed_page_locators import OrderFeedPageLocators
from pages.burger_constructor_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(MainPage):
    """
    Page Object страницы Ленты заказов.
    Содержит действия со списком заказов и статистикой.
    """

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        """
        Кликает по кнопке "Конструктор" в хедере страницы Ленты заказов.
        """
        self.page_loading_wait()
        self.click_on_element(OrderFeedPageLocators.BTN_CONSTRUCTOR)

    @allure.step('Нажать на первый заказ из списка')
    def click_on_first_order_in_list(self):
        """
        Кликает по первому заказу из основного списка заказов.
        """
        self.page_loading_wait()
        self.click_on_element(OrderFeedPageLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Получить номер первого заказа в списке')
    def get_id_of_first_order_in_list(self):
        """
        Возвращает номер (ID) первого заказа в списке.
        Return:
            str: номер заказа.
        """
        return self.get_text_on_element(OrderFeedPageLocators.FIRST_ORDER_ID_IN_LIST)

    @allure.step('Получить имя заказа из модального окна деталей')
    def get_name_of_first_order_from_details_popup(self):
        """
        Возвращает имя заказа, отображаемого в модалке деталей.
        Return:
            str: имя заказа.
        """
        return self.get_text_on_element(OrderFeedPageLocators.FIRST_ORDER_NAME_IN_DETAILS)

    @allure.step('Получить имя первого заказа в списке')
    def get_name_of_first_order_in_list(self):
        """
        Возвращает имя первого заказа в списке.
        Return:
            str: имя заказа.
        """
        return self.get_text_on_element(OrderFeedPageLocators.FIRST_ORDER_NAME_IN_LIST)

    @allure.step('Получить общее количество выполненных заказов')
    def get_number_of_all_orders_counter(self):
        """
        Получает число из счётчика "Выполнено за всё время".
        Return:
            str: число заказов.
        """
        return self.get_text_on_element(OrderFeedPageLocators.ALL_TIME_ORDERS_COUNT)

    @allure.step('Получить номер первого заказа в списке "В работе"')
    def get_number_of_last_order_in_working_list(self):
        """
        Возвращает номер заказа из секции "В работе".
        Return:
            str: номер заказа.
        """
        return self.get_text_on_element(OrderFeedPageLocators.FIRST_ORDER_IN_WORKING_LIST)

    @allure.step('Получить количество заказов за сегодня')
    def get_number_of_today_orders_counter(self):
        """
        Получает число из счётчика "Выполнено за сегодня".
        Return:
            str: число заказов.
        """
        return self.get_text_on_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT)

    @allure.step('Ожидать увеличения счётчика всех заказов')
    def wait_for_all_orders_counter_to_increase(self, previous_value: int, timeout: int = 30):
        """
        Ждёт, пока счётчик "Выполнено за всё время" увеличится относительно переданного значения.
        Args:
            previous_value (int): предыдущее значение счётчика.
            timeout (int): таймаут ожидания в секундах.
        """
        def counter_has_increased(driver):
            try:
                current = int(self.get_number_of_all_orders_counter())
                return current > previous_value
            except Exception:
                return False

        WebDriverWait(self.driver, timeout).until(counter_has_increased)
