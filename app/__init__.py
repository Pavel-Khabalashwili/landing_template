"""
Инициализация Flask-приложения.

Этот модуль отвечает за:
- Создание и настройку Flask-приложения
- Инициализацию расширений
- Регистрацию маршрутов
- Загрузку конфигурации

Структура:
    app/
    ├── __init__.py    # текущий файл
    ├── config.py      # конфигурация
    ├── extensions.py  # расширения
    ├── routes/        # маршруты
    ├── forms/         # формы
    ├── services/      # сервисы
    └── utils/         # утилиты

Использование:
    from app import create_app
    app = create_app(prod=False)
"""
from flask import Flask

from .config import DevConfig, ProdConfig
from .extensions import csrf, mail
from .routes import main_bp
from .utils import check_env_vars, check_env_file


def create_app(prod: bool = False) -> Flask:
    """
        Фабричная функция для создания Flask-приложения.

        Args:
            prod (bool): Флаг, указывающий, использовать ли продакшн-конфигурацию.
                         Если False — используется конфигурация для разработки (DevConfig).

        Returns:
            Flask: Настроенный объект Flask-приложения.
    """
    check_env_file()  # проверка на существаование файла env
    check_env_vars()  # проверка переменных окружения перед созданием приложения

    app = Flask(__name__)
    app.config.from_object(ProdConfig if prod else DevConfig)

    csrf.init_app(app=app)
    mail.init_app(app=app)

    app.register_blueprint(main_bp)

    return app



