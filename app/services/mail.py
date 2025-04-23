"""
Утилита для отправки email-сообщений из формы обратной связи.

Функции:
- send_email(contact: str, message: str) — отправляет сообщение с контактами пользователя.
    - В режиме разработки (IS_PRODUCTION=False): сообщение выводится в консоль.
    - В боевом режиме (IS_PRODUCTION=True): письмо отправляется на указанный email.

Использует:
- Flask-Mail для отправки сообщений
- Jinja2-шаблоны mail.txt и mail.html для формирования содержимого письма
- Flask current_app для получения конфигурации
"""
import os

from flask import current_app, render_template
from flask_mail import Message
from app.extensions import mail
from app.config import Config



def send_email(contact: str, message: str) -> None:
    """
    Отправляет сообщение либо в консоль, либо на почту

    :param contact: Контактные данные пользователя (тип данных: str)
    :param message: Сообщение пользователя (тип данных: str)
    :return: None
    """

    if current_app.config['IS_PRODUCTION']:
        msg = Message(
            subject="Сообщение с сайта VUGAR AI CONSULTING",
            recipients=[Config.MAIL_RECIPIENT],
        )

        # Добавляем текстовую версию письма
        msg.body = render_template(template_name_or_list="mail/mail.txt", contact=contact, message=message)

        # Добавляем HTML-версию письма
        msg.html = render_template(template_name_or_list="mail/mail.html", contact=contact, message=message)

        mail.send(msg)
    else:
        print("=== VUGAR AI CONSULTING ===")
        print(f"Контакт: {contact}")
        print(f"Сообщение: {message}")
        print("===========================")
