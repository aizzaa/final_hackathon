from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model


def send_activation_code(email, activation_code):
    User = get_user_model()
    user = User.objects.get(email=email)
    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, спасибо за регистрацию на нашем сайте!',
        'email': email,
        'domain': 'http://localhost:8000',
        'activation_code': activation_code,

    }

    msg_html = render_to_string('index.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Активация аккаунта',
        message,
        'test@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False,
    )

