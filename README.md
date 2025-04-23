# Flask Landing Template

Шаблон для быстрого создания лендингов с формой обратной связи.

## Возможности

- Форма обратной связи с валидацией
- Отправка писем через SMTP
- Готовые конфигурации для разработки и продакшн
- Защита от CSRF-атак

## Установка

1. Создать виртуальное окружение:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создать `.env` файл:
   ```
   SECRET_KEY=your_secret_key
   MAIL_SERVER=smtp.example.com
   MAIL_PORT=465
   MAIL_USE_SSL=True
   MAIL_USERNAME=your_email@example.com
   MAIL_PASSWORD=your_password
   MAIL_DEFAULT_SENDER=your_email@example.com
   MAIL_RECIPIENT=recipient@example.com
   ```

## Запуск

```bash
python run.py  # режим разработки
python run.py --prod  # режим продакшн
```

## Структура проекта

```
app/
├── forms/          # формы
├── routes/         # маршруты
├── services/       # сервисы
├── utils/          # утилиты
├── extensions.py   # расширения
├── config.py       # конфигурация
└── __init__.py    # инициализация
```

