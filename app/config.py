"""
Конфигурационные классы Flask-приложения для разных сред (разработка и продакшн).

Содержит:
- Config: Базовые настройки (почта, секретный ключ и пр.).
- DevConfig: Конфигурация для режима разработки (DEBUG=True, IS_PRODUCTION=False).
- ProdConfig: Конфигурация для продакшн-среды (DEBUG=False, IS_PRODUCTION=True).
- check_env_vars(): Проверка наличия всех необходимых переменных окружения.

Использует:
- python-dotenv для загрузки переменных из .env
- Переменные окружения для конфиденциальных данных

Необходимые переменные окружения (.env):
    SECRET_KEY: Секретный ключ для подписи сессий
    MAIL_SERVER: SMTP-сервер
    MAIL_PORT: Порт SMTP
    MAIL_USE_SSL: Использовать SSL
    MAIL_USERNAME: Логин почты
    MAIL_PASSWORD: Пароль почты
    MAIL_DEFAULT_SENDER: Email отправителя
    MAIL_RECIPIENT: Email получателя

Пример использования:
    app.config.from_object('app.config.DevConfig')
"""
import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """
    Базовый класс конфигурации Flask-приложения. Содержит общие настройки для всех сред (dev/prod).

    Атрибуты:
        SECRET_KEY (str): Секретный ключ для подписи сессий и токенов.

        MAIL_SERVER (str): SMTP-сервер для отправки почты (Yandex).
        MAIL_PORT (int): Порт SMTP-сервера (для SSL).
        MAIL_USE_SSL (bool): Использовать SSL-шифрование.
        MAIL_USERNAME (str): Логин почтового аккаунта.
        MAIL_PASSWORD (str): Пароль приложения -  Яндекс Почты.
        MAIL_DEFAULT_SENDER (str): Email отправителя по умолчанию.
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')


class DevConfig(Config):
    """
        Конфигурация для среды разработки. Наследует все параметры класса Config.

        Атрибуты:
            DEBUG (bool): Режим отладки (включен).
            IS_PRODUCTION (bool): Флаг продакшн-среды (выключен).
    """
    DEBUG = True
    IS_PRODUCTION = False


class ProdConfig(Config):
    """
        Конфигурация для продакшн-среды. Наследует все параметры класса Config.

        Атрибуты:
            DEBUG (bool): Режим отладки (выключен).
            IS_PRODUCTION (bool): Флаг продакшн-среды (включен).
    """
    DEBUG = False
    IS_PRODUCTION = True
