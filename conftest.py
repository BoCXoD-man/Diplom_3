import allure
import pytest
import requests

from selenium import webdriver

from data import Url
from generators import generate_user_data

from pages.login_page import LoginPage
from pages.burger_constructor_page import MainPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    """
    Запускает браузер (Chrome или Firefox) и открывает главную страницу Stellar Burgers.
    После завершения теста закрывает браузер.
    """
    with allure.step(f'Запустить браузер, открыть страницу {Url.MAIN_URL}'):
        if request.param == 'chrome':
            driver = webdriver.Chrome()
        elif request.param == 'firefox':
            driver = webdriver.Firefox()
        driver.get(Url.MAIN_URL)

        yield driver

        driver.quit()


@pytest.fixture
def to_login_page(driver):
    """
    Переходит на страницу авторизации через главную.
    Возвращает драйвер с открытой страницей логина.
    """
    with allure.step('Перейти на страницу авторизации'):
        page = MainPage(driver)
        page.page_loading_wait()
        page.click_on_login_button()
        return driver


@pytest.fixture
def to_forgot_password_page(to_login_page):
    """
    Переходит на страницу восстановления пароля через логин.
    Возвращает драйвер с открытой страницей восстановления.
    """
    with allure.step('Перейти на страницу восстановления пароля'):
        page = LoginPage(to_login_page)
        page.page_loading_wait()
        page.click_on_forgot_password_button()
        return to_login_page


@pytest.fixture
def to_order_feed_page(driver):
    """
    Переходит на страницу Ленты заказов через хедер.
    Возвращает драйвер с открытой лентой заказов.
    """
    with allure.step('Перейти на страницу Ленты заказов'):
        page = MainPage(driver)
        page.page_loading_wait()
        page.click_on_order_feed_button()
        return driver


@pytest.fixture
def new_user():
    """
    Создаёт нового пользователя через API.
    Возвращает словарь с данными пользователя и токенами.
    После завершения теста удаляет пользователя.
    """
    with allure.step('Создать нового пользователя'):
        email, password, name = generate_user_data()
        user_body = {
            'email': email,
            'password': password,
            'name': name
        }
        response = requests.post(f'{Url.MAIN_URL}{Url.API_REG_URL}', data=user_body)
        token = response.json()['accessToken']
        refresh_token = response.json()['refreshToken']

        user_data = {
            'user_body': user_body,
            'token': token,
            'refresh_token': refresh_token
        }

        yield user_data

    with allure.step('Удалить пользователя'):
        requests.delete(f'{Url.MAIN_URL}{Url.API_USER_URL}',
                        headers={'Authorization': token})


@pytest.fixture
def login(new_user, to_login_page):
    """
    Авторизует нового пользователя через UI.
    Возвращает драйвер с залогиненным пользователем.
    """
    with allure.step('Авторизоваться новым пользователем'):
        email = new_user['user_body']['email']
        password = new_user['user_body']['password']
        page = LoginPage(to_login_page)
        page.page_loading_wait()
        page.authorize_user(email, password)
        page.page_loading_wait()
        return to_login_page


@pytest.fixture
def to_personal_page(login):
    """
    Переходит в личный кабинет авторизованного пользователя.
    Возвращает драйвер с открытым профилем.
    """
    with allure.step('Перейти в Личный кабинет'):
        page = MainPage(login)
        page.page_loading_wait()
        page.click_on_personal_acc_button()
        return login