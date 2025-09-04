from selenium.webdriver.common.by import By


class PasswordLocators:
    """Локаторы страниц восстановления и сброса пароля в Stellar Burgers."""

    INPUT_EMAIL = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    """Поле ввода email на странице восстановления пароля."""

    PLACEHOLDER_CODE_FROM_MAIL = (By.XPATH,
                                  './/label[@class="input__placeholder text noselect text_type_main-default"][text()="Введите код из письма"]')
    """Плейсхолдер поля ввода кода из письма (при сбросе пароля)."""

    BTN_RECOVER = (By.XPATH, "//form//button[contains(., 'Восстановить')]")
    """Кнопка отправки email на форме восстановления пароля."""

    LABEL_CODE_HINT = (By.XPATH, "//*[text()='Введите код из письма']")
    """Текстовая подсказка на странице ввода кода 'Введите код из письма'."""

    CODE_INPUT = (
        By.XPATH,
        "//input[@name='code']"
        " | //input[@placeholder='Введите код из письма']"
        " | //input[@inputmode='numeric' or @maxlength='6' or contains(@class,'input')]")
    """Поля ввода кода на странице сброса пароля."""