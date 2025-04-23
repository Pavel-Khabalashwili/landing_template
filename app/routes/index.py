"""
Маршруты для веб-интерфейса приложения.

Содержит обработчик главной страницы с формой обратной связи:
- Отображает HTML-шаблон с формой (GET)
- Обрабатывает отправку формы и вызывает отправку email (POST)

Используемые компоненты:
- Blueprint для организации маршрутов
- WTForms для работы с формой
- Шаблоны Jinja2 для рендеринга HTML
"""

from flask import Blueprint, Response, render_template
from typing import Union

from app.forms import ContactForm
from app.services import send_email


main_bp = Blueprint(name="main", import_name=__name__)


@main_bp.route(rule="/", methods=['GET', 'POST'])
def index() -> Union[str, Response]:
    """
        Обрабатывает главную страницу с формой обратной связи.

        Returns:
            При GET-запросе: HTML-страницу с формой
            При успешном POST-запросе: Сообщение об успешной отправке
    """
    form = ContactForm()

    # Если форма валидна
    if form.validate_on_submit():
        contact = form.contact.data
        message = form.message.data
        send_email(contact=contact, message=message)

        info = "Спасибо! Ваше сообщение отправлено."
        return info

    return render_template(template_name_or_list='index.html', form=form)
