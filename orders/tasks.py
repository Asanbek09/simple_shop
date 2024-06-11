from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, You have successfully placed an order. Your order Id is {order.id}'
    mail_sent = send_mail(subject, message, 'asanbek.best@mail.ru', [order.email])
    return mail_sent