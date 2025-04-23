"""
Форма обратной связи для веб-приложения Flask.

Содержит два поля:
- contact — для ввода контактной информации (email, телефон, Telegram)
- message — для текста сообщения

Включает валидацию полей с помощью стандартных и пользовательских валидаторов.
Форма используется на главной странице сайта.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

from .validators import validate_contact


class ContactForm(FlaskForm):
    """Форма обратной связи с валидацией контактных данных.

    Attributes:
        contact: Поле для ввода email, телефона или Telegram
        message: Поле для ввода текста сообщения
    """

    contact = StringField(
        label='Ваш контакт',    # Создания тега <label>Ваш контакт</label>
        validators=[
            DataRequired(message="Поле обязательно для заполнения"),
            Length(min=5, max=100, message="Длина должна быть 5-100 символов"),
            validate_contact    # Вызов кастомной функции для проверки поля
        ],
        render_kw={
            'placeholder': 'email, телефон (+7...) или Telegram (@username)',
            'class': 'form-input'
        }
    )

    message = TextAreaField(
        label='Сообщение',  # Создания тега <label>Сообщение</label>
        validators=[
            DataRequired(message="Поле обязательно для заполнения"),
            Length(min=10, max=1000, message="Сообщение должно быть 10-1000 символов")
        ],
        render_kw={
            'rows': 5,
            'class': 'form-textarea',
            'placeholder': 'Ваше сообщение...'
        }
    )
