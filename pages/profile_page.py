import allure

from locators.personal_page_locators import PersonalPageLocators
from pages.burger_constructor_page import MainPage


class PersonalPage(MainPage):
    """
    Page Object страницы личного кабинета пользователя.
    Содержит действия по переходу к истории заказов и выходу из аккаунта.
    """

    @allure.step('Нажать на кнопку "История заказов"')
    def click_on_order_history_button(self):
        """
        Кликает по кнопке "История заказов" в личном кабинете.
        """
        self.page_loading_wait()
        self.click_on_element(PersonalPageLocators.BTN_ORDER_HISTORY)

    @allure.step('Нажать на кнопку "Выход" и дождаться загрузки страницы')
    def click_on_logout_button(self):
        """
        Кликает по кнопке "Выход" и дожидается перехода на страницу логина.
        """
        self.page_loading_wait()
        self.click_on_element(PersonalPageLocators.BTN_LOGOUT)
        self.wait_for_element(PersonalPageLocators.TEXT_LOGIN)