import allure
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
        подписи «Введите код из письма». После этого ждёт поле ввода кода.
        """
        self.click_on_element(PasswordLocators.BTN_RECOVER)

        # ждём либо URL /reset-password, либо ярлык-подсказку
        self.wait_any(
            conditions=[
                lambda d: self.wait_for_url("/reset-password", timeout=1) or True,
                lambda d: self.is_present(PasswordLocators.LABEL_CODE_HINT, timeout=1)
            ],
            timeout=10
        )

        # финально убеждаемся, что инпут кода есть в DOM
        self.wait_for_presence(PasswordLocators.CODE_INPUT, timeout=10)

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