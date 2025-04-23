"""
Пользовательские валидаторы для форм Flask-WTF.

Содержит:
- `validate_contact` — проверяет, что контактные данные соответствуют одному из допустимых форматов:
    - email (user@example.com)
    - телефон (+71234567890)
    - Telegram (@username)

Этот валидатор подключается к формам через параметр `validators` и используется для дополнительной проверки
поля контакта.
"""
import re

from flask_wtf import FlaskForm
from wtforms.validators import ValidationError
from wtforms.fields.simple import StringField


def validate_contact(_: FlaskForm, field: StringField) -> None:
    """Проверяет, что контактные данные соответствуют email, телефону или Telegram.

    Args:
        _: Форма Flask-WTF, к которой принадлежит поле
        field: Поле формы для валидации

    Raises:
        ValidationError: Если значение не соответствует ни одному из форматов
    """
    value = field.data

    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    phone_regex = re.compile(r'^\+?[1-9]\d{7,14}$')
    telegram_regex = re.compile(r'^@[a-zA-Z0-9_]{5,32}$')

    is_email = email_regex.match(value)
    is_phone = phone_regex.match(value)
    is_telegram = telegram_regex.match(value)

    if not (is_email or is_phone or is_telegram):
        raise ValidationError(
            'Введите email (user@example.com), телефон (+71234567890) или Telegram (@username)'
        )
