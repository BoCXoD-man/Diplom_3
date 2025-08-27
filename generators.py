import random
from faker import Faker

fake = Faker()


def generate_user_data():
    """
    Генерирует валидные данные для нового пользователя: email, пароль и имя.
    Return:
        tuple: email (str), password (str), name (str)
    """
    email_prefix = f'testuser{random.randint(1000, 9999)}'
    email = f'{email_prefix}@{fake.free_email_domain()}'
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    name = fake.first_name()

    return email, password, name