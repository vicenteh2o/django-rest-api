from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_order_confirmation_email(order_id, user_email):
    subject = "Order confirmation"
    message = f"Your order with ID {order_id} has been successfully placed."
    return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
