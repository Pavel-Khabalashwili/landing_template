"""
Валидатор для конфигурации приложения.
"""
import os


def check_env_file():
    """Проверяет наличие .env файла."""
    if not os.path.exists('.env'):
        raise FileNotFoundError("Пожалуйста создайте .env файл из .env.example")

def check_env_vars():
    """
    Проверяет наличие всех необходимых переменных окружения.

    Raises:
        ValueError: Если какая-то переменная отсутствует
    """
    required_vars = [
        'SECRET_KEY',
        'MAIL_SERVER',
        'MAIL_PORT',
        'MAIL_USERNAME',
        'MAIL_PASSWORD',
        'MAIL_DEFAULT_SENDER',
        'MAIL_RECIPIENT'
    ]

    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f"Отсутствуют необходимые переменные среды: {', '.join(missing_vars)}")
