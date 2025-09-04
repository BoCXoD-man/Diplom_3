import allure

from pages.burger_constructor_page import MainPage
from pages.feed_page import OrderFeedPage
from data import  ExpectedText
from urls import Url
from locators.burger_constructor_page_locators import MainPageLocators


class TestMainFeatures:
    """
    Тесты основной функциональности конструктора бургера:
    переходы, модалки, счётчики, оформление заказа.
    """

    @allure.title('Проверка открытия Ленты заказов с главной страницы')
    def test_open_order_feed_page_top_button(self, driver):
        """
        Открывает страницу ленты заказов по кнопке в хедере.
        """
        page = MainPage(driver)
        page.click_on_order_feed_button()

        assert page.get_current_page_url() == Url.ORDER_FEED_URL

    @allure.title('Проверка открытия Конструктора со страницы Ленты заказов')
    def test_open_constructor_from_order_feed_page_top_button(self, to_order_feed_page):
        """
        Возвращается из ленты заказов на главную страницу конструктора.
        """
        page = OrderFeedPage(to_order_feed_page)
        page.click_on_constructor_button()

        assert page.get_current_page_url() == Url.MAIN_URL+'/'

    @allure.title('Проверка появления окна деталей при выборе ингредиента')
    def test_open_ingredient_details_popup(self, driver):
        """
        Проверяет появление модального окна с деталями ингредиента.
        """
        page = MainPage(driver)
        page.click_on_first_ingredient()
        actual_text = page.get_title_text_detail_ingredient_screen()

        assert actual_text == ExpectedText.DETAILS_INGREDIENT_TEXT

    @allure.title('Проверка закрытия окна деталей ингредиента по нажатию на крестик')
    def test_close_ingredient_details_by_close_button(self, driver):
        """
        Закрывает окно деталей и проверяет, что элемент снова доступен для клика.
        """
        page = MainPage(driver)
        page.click_on_first_ingredient()
        page.click_on_close_button_details_ingredient_screen()

        assert page.is_element_clickable(MainPageLocators.IMG_FIRST_BUN)

    @allure.title('Проверка увеличения счетчика ингредиентов при добавлении в заказ')
    def test_add_ingredient_in_order_counter_increase(self, driver):
        """
        Проверяет, что после добавления булки в заказ счётчик увеличивается.
        """
        page = MainPage(driver)
        page.page_loading_wait()
        page.drop_bun_into_order_sector()
        counter_number = page.get_counter_number()

        assert counter_number == '2'

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_authorized_user_create_order(self, login):
        """
        Авторизованный пользователь успешно оформляет заказ.
        """
        page = MainPage(login)
        page.page_loading_wait()
        page.drop_bun_into_order_sector()
        page.click_on_create_order_button()
        actual_text = page.get_successful_text_popup_order_screen()

        assert actual_text == ExpectedText.SUCCESSFUL_CREATION_ORDER_TEXT