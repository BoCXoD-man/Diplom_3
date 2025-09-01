import allure

from pages.profile_page import PersonalPage
from pages.burger_constructor_page import MainPage
from urls import Url


class TestPersonalAcc:
    """
    Набор UI-тестов для проверки функционала Личного кабинета.
    """

    @allure.title('Проверка перехода в Личный кабинет с главной страницы')
    def test_open_personal_acc_page_from_main_page(self, login):
        """
        Проверяет переход с главной страницы в Личный кабинет
        по клику на кнопку «Личный кабинет».
        Args:
            login (WebDriver): драйвер с залогиненным пользователем.
        """
        page = MainPage(login)
        page.click_on_personal_acc_button()
        assert Url.PERSONAL_ACC_URL in page.get_current_page_url()

    @allure.title('Проверка открытия истории заказов из Личного кабинета')
    def test_open_order_history_from_personal_acc_page(self, to_personal_page):
        """
        Проверяет переход в «Историю заказов» из личного кабинета.
        Args:
            to_personal_page (WebDriver): драйвер, открытый на личном кабинете.
        """
        page = PersonalPage(to_personal_page)
        page.click_on_order_history_button()
        assert page.get_current_page_url() == Url.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта со страницы Личного кабинета')
    def test_logout_from_personal_page(self, to_personal_page):
        """
        Проверяет выход из аккаунта через кнопку «Выход»
        на странице личного кабинета.
        Args:
            to_personal_page (WebDriver): драйвер, открытый на личном кабинете.
        """
        page = PersonalPage(to_personal_page)
        page.click_on_logout_button()
        assert page.get_current_page_url() == Url.LOGIN_URL