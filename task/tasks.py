from .models import Tasks
from django.core.mail import send_mail
from celery import shared_task
from core import settings
import time


def get_users_to_email(user: object):
    email_5_days = user.objects.all()
    email_2_days = user.objects.all()
    email_1_day = user.objects.all()

@shared_task(bind=True)
def send_mail_func(self):
    users = Tasks.objects.all()
    print("send mail func")
    time.sleep(10)
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.email
        print(to_email)
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return to_email, time.time()

