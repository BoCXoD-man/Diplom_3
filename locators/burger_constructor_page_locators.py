from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы конструктора Stellar Burgers."""

    BTN_PERSONAL_ACCOUNT = (By.XPATH, './/a[@href="/account"]')
    """Кнопка перехода в личный кабинет."""

    BTN_LOGIN_MAIN = (By.XPATH,
                      ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
                      "[text()='Войти в аккаунт']")
    """Кнопка 'Войти в аккаунт' на главной странице."""

    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    """Оверлей, перекрывающий экран во время загрузки модального окна."""


    BTN_CONSTRUCTOR = (By.XPATH,
                       './/p[@class="AppHeader_header__linkText__3q_va ml-2"][text()="Конструктор"]')
    """Кнопка перехода в раздел 'Конструктор'."""

    BTN_ORDER_FEED = (By.XPATH,
                      './/p[@class="AppHeader_header__linkText__3q_va ml-2"][text()="Лента Заказов"]')
    """Кнопка перехода в раздел 'Лента заказов'."""

    IMG_FIRST_BUN = (By.CSS_SELECTOR, '[alt="Флюоресцентная булка R2-D3"]')
    """Изображение первой булки в списке ингредиентов."""

    INGREDIENT_FIRST_BUN = (By.CSS_SELECTOR,
                            'a.BurgerIngredient_ingredient__1TVf6[href="/ingredient/61c0c5a71d1f82001bdaaa6d"][draggable="true"]')
    """Первый элемент булки, доступный для перетаскивания в конструктор."""

    INGREDIENT_FIRST_SAUCE = (By.CSS_SELECTOR,
                              '[class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][href="/ingredient/61c0c5a71d1f82001bdaaa72"][draggable="true"]')
    """Первый элемент соуса, доступный для перетаскивания в конструктор."""

    MODAL_INGREDIENT_TITLE = (By.XPATH,
                              './/h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"][text()="Детали ингредиента"]')
    """Заголовок модального окна с деталями ингредиента."""

    BTN_CLOSE_INGREDIENT_MODAL = (By.XPATH,
                                  './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]/following-sibling::button')
    """Кнопка закрытия модального окна с деталями ингредиента."""

    COUNTER_FIRST_INGREDIENT = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')
    """Счётчик количества добавленного ингредиента на карточке."""

    SECTION_CONSTRUCTOR_LIST = (By.CSS_SELECTOR, '[class*="BurgerConstructor_basket__list"]')
    """Секция конструктора бургера (список ингредиентов)."""

    SECTION_CONSTRUCTOR_FILLINGS = (By.CSS_SELECTOR, '[class="BurgerConstructor_basket__listContainer__3P_AM"]')
    """Секция конструктора бургера (наполнители между булками)."""

    MODAL_ORDER_ID = (By.XPATH,
                      './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    """Номер созданного заказа в модальном окне."""

    BTN_CREATE_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')
    """Кнопка 'Оформить заказ'."""

    TEXT_ORDER_SUCCESS = (By.XPATH, './/p[text()="Ваш заказ начали готовить"]')
    """Текст подтверждения успешного создания заказа."""

    SECTION_SAUCES = (By.XPATH, './/span[@class="text text_type_main-default"][text()="Соусы"]')
    """Секция вкладки 'Соусы' в списке ингредиентов."""

    IMG_LOADING_ANIMATION = (By.XPATH, './/img[contains(@src, "/loading") and contains(@src, ".svg")]')
    """Анимация загрузки, отображаемая при ожидании данных."""

    BTN_CLOSE_ORDER_MODAL = (By.XPATH,
                             './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]/following-sibling::button')
    """Кнопка закрытия модального окна после оформления заказа."""

    MODAL_OVERLAY = (By.XPATH, '//*[contains(@class,"Modal_modal_overlay")]')
    """Оверлей модального окна (фон-затемнение)."""

    MODAL_ROOT = (By.XPATH, '//*[contains(@class,"Modal_modal__contentBox")]')
    """Контейнер (корневой блок) модального окна."""