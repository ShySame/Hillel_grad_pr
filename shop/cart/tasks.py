from celery import shared_task

from django.core.mail import send_mail

@shared_task
def email_send(email):
    send_mail('NEW ORDER!!!', 'Your new order were add to our db', 'admin@mail.com', [email])