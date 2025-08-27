import allure

from locators.login_page_locators import LoginPageLocators
from pages.burger_constructor_page import MainPage


class LoginPage(MainPage):

    @allure.step('Авторизоваться')
    def authorize_user(self, email, password):
        """
        Авторизует пользователя с заданными email и паролем.
        Args:
            email (str): e-mail пользователя.
            password (str): пароль пользователя.
        """
        self.wait_for_element(LoginPageLocators.TEXT_LOGIN)
        self.send_keys_to_input(LoginPageLocators.INPUT_EMAIL  , email)
        self.send_keys_to_input(LoginPageLocators.INPUT_PASSWORD, password)
        self.click_on_element(LoginPageLocators.BTN_LOGIN)

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_on_forgot_password_button(self):
        """
        Кликает по кнопке "Восстановить пароль" на странице логина.
        """
        self.page_loading_wait()
        self.wait_for_element(LoginPageLocators.BTN_FORGOT_PASSWORD)
        self.scroll_to_element(LoginPageLocators.BTN_FORGOT_PASSWORD)
        self.click_on_element(LoginPageLocators.BTN_FORGOT_PASSWORD)

    @allure.step('Нажать на иконку скрытия пароля')
    def click_on_hide_password_icon(self):
        """
        Кликает по иконке скрытия пароля (делает пароль невидимым).
        """
        self.page_loading_wait()
        self.wait_for_element(LoginPageLocators.ICON_HIDE_PASSWORD)
        self.click_on_element(LoginPageLocators.ICON_HIDE_PASSWORD)

    @allure.step('Проверить активность поля ввода пароля')
    def check_active_password_field(self):
        """
        Проверяет, что поле ввода пароля активно (виден курсор).
        Return:
            bool: True, если поле активно.
        """
        return self.check_attribute_in_element_status(LoginPageLocators.INPUT_PASSWORD,
                                               'type',
                                               'text')