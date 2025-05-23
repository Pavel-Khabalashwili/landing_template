"""
Инициализация пакета маршрутов приложения.

Этот модуль отвечает за:
- Импорт и экспорт Blueprint'ов из подмодулей
- Предоставление единой точки входа для всех маршрутов приложения

Структура:
    routes/
    ├── __init__.py    # текущий файл
    ├── index.py       # маршруты главной страницы
    └── [другие модули с маршрутами]

Использование:
    from app.routes import main_bp
    app.register_blueprint(main_bp)
"""
from .index import main_bp


__all__ = ['main_bp']
