from selenium.webdriver.common.by import By

from locators.burger_constructor_page_locators import MainPageLocators


class OrderFeedPageLocators(MainPageLocators):
    """Локаторы элементов раздела 'Лента заказов' на странице Stellar Burgers."""

    ALL_TIME_ORDERS_COUNT = (By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p')
    """Счётчик выполненных заказов за всё время."""

    TODAY_ORDERS_COUNT = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p')
    """Счётчик выполненных заказов за сегодня."""

    FIRST_ORDER_IN_LIST = (By.XPATH, './/a[@class="OrderHistory_link__1iNby"]')
    """Первый заказ в списке заказов (карточка)."""

    FIRST_ORDER_NAME_IN_LIST = (By.XPATH, './/h2[@class="text text_type_main-medium mb-2"]')
    """Название первого заказа в списке заказов."""

    FIRST_ORDER_ID_IN_LIST = (By.XPATH, './/p[@class="text text_type_digits-default"]')
    """Номер первого заказа в списке заказов."""

    FIRST_ORDER_NAME_IN_DETAILS = (By.XPATH,
                                   './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]/h2')
    """Название заказа в модальном окне деталей заказа."""

    FIRST_ORDER_IN_WORKING_LIST = (By.XPATH, './/li[@class="text text_type_digits-default mb-2"]')
    """Первый заказ в списке заказов со статусом "В работе"."""