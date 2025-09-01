class Url:
    """
    Константы с URL-адресами веб-приложения и его API.
    """

    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    """Главная страница приложения."""


    PASSWORD_URL = f'{MAIN_URL}/forgot-password'
    """Страница восстановления пароля."""

    LOGIN_URL = f'{MAIN_URL}/login'
    """Страница авторизации."""

    PERSONAL_ACC_URL = f'{MAIN_URL}/account'
    """Страница личного кабинета."""

    ORDER_HISTORY_URL = f'{MAIN_URL}/account/order-history'
    """Страница истории заказов."""

    ORDER_FEED_URL = f'{MAIN_URL}/feed'
    """Публичная лента заказов."""

    API_REG_URL = '/api/auth/register'
    """Эндпоинт API для регистрации пользователя."""

    API_USER_URL = '/api/auth/user'
    """Эндпоинт API для получения, изменения и удаления пользователя."""

    API_ORDER_URL = '/api/orders'
    """Эндпоинт API для создания заказов."""