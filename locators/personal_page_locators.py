from selenium.webdriver.common.by import By

from locators.login_page_locators import LoginPageLocators


class PersonalPageLocators(LoginPageLocators):
    """Локаторы личного кабинета пользователя в Stellar Burgers."""

    BTN_LOGOUT = (By.XPATH,
                  './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    """Кнопка 'Выход' для выхода из аккаунта."""

    BTN_ORDER_HISTORY = (By.XPATH, './/a[@href="/account/order-history"]')
    """Кнопка перехода в раздел 'История заказов'."""

    CODE_INPUT = (By.NAME, "code")
    """Поле ввода кода из письма для восстановления пароля."""

    BTN_RECOVER = (By.XPATH, './/button[text()="Восстановить"]')
    """Кнопка 'Восстановить' на форме запроса сброса пароля."""