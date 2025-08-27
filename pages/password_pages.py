import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.password_pages_locators import PasswordLocators


class PasswordPage(BasePage):
    """
    Страница восстановления/сброса пароля.
    Содержит действия и проверки для форм ввода e-mail и кода из письма.
    """

    @allure.step('Ввести e-mail в поле восстановления пароля')
    def fill_email_input(self, email: str):
        """
        Вводит e-mail в поле на форме «Забыли пароль?».
        Args:
            email (str): корректный адрес электронной почты пользователя.
        """
        element = self.wait_for_element(PasswordLocators.INPUT_EMAIL)
        element.clear()
        element.send_keys(email)

    @allure.step('Нажать кнопку "Восстановить" и дождаться страницы ввода кода')
    def click_on_recover_button(self):
        """
        Нажимает кнопку «Восстановить» на форме e-mail и ожидает переход
        на экран ввода кода: либо смены URL на /reset-password, либо появления
        текста «Введите код из письма». После этого пробует дождаться поля ввода кода.
        """
        self.click_on_element(PasswordLocators.BTN_RECOVER)

        # Пытаемся дождаться смены URL на /reset-password
        try:
            WebDriverWait(self.driver, 8).until(EC.url_contains("/reset-password"))
        except TimeoutException:
            # Если URL не сменился, ждём появления явного текста-подсказки
            WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located(PasswordLocators.LABEL_CODE_HINT)
            )

        try:
            self.wait_for_presence(PasswordLocators.CODE_INPUT, timeout=5)
        except Exception:
            # Если инпута нет 
            pass

    @allure.step('Получить текст подсказки/placeholder для поля кода')
    def get_text_of_code_input(self) -> str:
        """
        Возвращает текст подсказки для поля кода.
        Сначала пытается прочитать placeholder у инпута, иначе берёт текст «Введите код из письма».
        Return:
            str: текст подсказки для ввода кода.
        """
        # Сначала пробуем прочитать placeholder у инпута (если он есть)
        try:
            if self.wait_for_presence(PasswordLocators.CODE_INPUT, timeout=3):
                placeholder = self.get_attribute(PasswordLocators.CODE_INPUT, "placeholder")
                if placeholder:
                    return placeholder
        except Exception:
            # Инпута может не быть — тогда читаем текст подсказки-лейбла
            pass

        # Фолбэк: берём текст явной подсказки
        return self.get_text_on_element(PasswordLocators.LABEL_CODE_HINT)