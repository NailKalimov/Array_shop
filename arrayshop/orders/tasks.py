from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order number {order_id}'
    message = f'Dear {order.first_name}\n\n'\
                f'You have succefuly placed in order!\n'\
                f'Your order ID is {order_id}.'
    mail_sent = send_mail(subject,
                          message,
                          from_email='admin@array.com',
                          recipient_list=[order.email])
    return mail_sent