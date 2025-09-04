import allure

from pages.feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title('Открытие деталей заказа на странице Ленты заказов')
    def test_open_order_details_popup(self, to_order_feed_page):
        """
        Проверяет, что клик по заказу открывает окно с деталями,
        и заголовок в деталях совпадает с названием заказа в списке.
        """
        page = OrderFeedPage(to_order_feed_page)
        order_name_in_list = page.get_name_of_first_order_in_list()
        page.click_on_first_order_in_list()
        order_name_in_popup = page.get_name_of_first_order_from_details_popup()

        assert order_name_in_popup == order_name_in_list

    @allure.title('Увеличение счётчика "Выполнено за все время" после нового заказа')
    def test_all_time_counter_increase_after_new_order(self, login):
        """
        Проверяет, что после оформления заказа увеличивается счётчик всех заказов.
        """
        page = OrderFeedPage(login)

        page.click_on_order_feed_button()
        counter_before = int(page.get_number_of_all_orders_counter())

        page.click_on_constructor_button()
        page.create_order()

        # Дожидаемся завершения анимации загрузки и закрываем модалку
        page.wait_for_loading_animation_end()
        page.close_order_popup_screen()

        page.click_on_order_feed_button()
        page.wait_for_all_orders_counter_to_increase(counter_before)

        counter_after = int(page.get_number_of_all_orders_counter())
        assert counter_after > counter_before, (
            f"Счётчик не увеличился: было {counter_before}, стало {counter_after}"
        )

    @allure.title('Увеличение счётчика "Выполнено за сегодня" после нового заказа')
    def test_today_counter_increase_after_new_order(self, login):
        """
        Проверяет, что после оформления заказа увеличивается счётчик заказов за сегодня.
        """
        page = OrderFeedPage(login)
        page.click_on_order_feed_button()
        counter_before = int(page.get_number_of_today_orders_counter())
        page.click_on_constructor_button()
        page.create_order()
        page.page_loading_wait()
        page.close_order_popup_screen()
        page.click_on_order_feed_button()
        counter_after = int(page.get_number_of_today_orders_counter())

        assert counter_after > counter_before

    @allure.title('Появление нового заказа в списке "В работе"')
    def test_new_order_visible_in_working_list(self, login):
        """
        Проверяет, что новый заказ виден в списке заказов "В работе".
        """
        page = OrderFeedPage(login)
        page.create_order()
        page.page_loading_wait()
        order_number = page.get_order_number()
        page.close_order_popup_screen()
        page.click_on_order_feed_button()
        working_list_number = page.get_number_of_last_order_in_working_list()

        assert order_number in working_list_number

    @allure.title('Наличие пользовательского заказа в Ленте заказов')
    def test_user_orders_visible_in_order_feed(self, login):
        """
        Проверяет, что заказ пользователя отображается в Ленте заказов.
        """
        page = OrderFeedPage(login)
        page.create_order()
        page.page_loading_wait()
        order_number = page.get_order_number()
        page.close_order_popup_screen()
        page.click_on_order_feed_button()
        first_order_in_feed = page.get_id_of_first_order_in_list()

        assert order_number in first_order_in_feed
