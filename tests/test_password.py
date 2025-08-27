import allure

from pages.login_page import LoginPage
from pages.password_pages import PasswordPage
from data import ExpectedText, Url


class TestPasswordPage:
    """
    Набор UI-тестов для страниц восстановления и ввода пароля.
    Охватывает переходы, ввод e-mail и изменения состояния поля пароля.
    """

    @allure.title('Проверка успешного ввода почты для восстановления пароля')
    def test_send_email_for_recover_password(self, new_user, to_forgot_password_page):
        """
        Проверяет, что при вводе корректной почты на странице восстановления
        отображается ожидаемый placeholder у поля ввода кода.
        Args:
            new_user (dict): фикстура с данными нового пользователя.
            to_forgot_password_page (WebDriver): драйвер, уже открытый на странице восстановления пароля.
        """
        page = PasswordPage(to_forgot_password_page)
        page.fill_email_input(new_user['user_body']['email'])
        page.click_on_recover_button()
        actual_text = page.get_text_of_code_input()
        assert actual_text == ExpectedText.MAIL_CODE_PLACEHOLDER_TEXT

    @allure.title('Проверка открытия страницы восстановления пароля по кнопке "Восстановить пароль"')
    def test_open_recover_password_page_from_recover_button(self, to_login_page):
        """
        Проверяет переход со страницы логина на страницу восстановления пароля
        по клику на кнопку «Восстановить пароль».
        Args:
            to_login_page (WebDriver): драйвер, уже открытый на странице логина.
        """
        page = LoginPage(to_login_page)
        page.click_on_forgot_password_button()
        assert page.get_current_page_url() == Url.PASSWORD_URL

    @allure.title('Проверка активности поля пароля по клику на кнопку скрытия пароля')
    def test_click_hide_password_icon_makes_active_password_field(self, to_login_page):
        """
        Проверяет, что при клике на иконку скрытия/показа пароля
        поле пароля становится активным (фокус устанавливается).
        Args:
            to_login_page (WebDriver): драйвер, уже открытый на странице логина.
        """
        page = LoginPage(to_login_page)
        page.click_on_hide_password_icon()
        assert page.check_active_password_field()