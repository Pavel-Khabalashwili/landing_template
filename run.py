"""
Точка входа для запуска Flask-приложения.

Импортирует функцию `create_app` из пакета `app` и создаёт экземпляр приложения
с конфигурацией для разработки.

При запуске напрямую (`python run.py`) приложение стартует.
"""
from app import create_app


app = create_app(prod=False)

if __name__ == "__main__":
    app.run()
