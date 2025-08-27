from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы страницы входа (логина) в приложение Stellar Burgers."""

    BTN_FORGOT_PASSWORD = (By.XPATH, './/a[@href="/forgot-password"]')
    """Кнопка 'Забыли пароль?' — ссылка на страницу восстановления."""

    ICON_HIDE_PASSWORD = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    """Иконка скрытия/отображения пароля в поле ввода."""

    INPUT_EMAIL = (By.XPATH, './/input[@name="name"][@type="text"]')
    """Поле ввода email."""

    INPUT_PASSWORD = (By.XPATH, './/input[@name="Пароль"]')
    """Поле ввода пароля."""
    
    TEXT_LOGIN = (By.XPATH, "//h2[.='Вход']")
    """Заголовок формы входа 'Вход'."""

    BTN_LOGIN = (By.XPATH,
                 './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"][text()="Войти"]')
    """Кнопка 'Войти' на форме авторизации."""