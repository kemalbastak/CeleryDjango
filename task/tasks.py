from .models import Tasks
from django.core.mail import send_mail
from celery import shared_task
from core import settings
import time
from datetime import datetime, timedelta


def get_due_date(day: int):
    """
    day: adds days to today
    returns: [today+day, today+day]
    ex: The day of today is 2021-11-12
    create_date_range(3) returns 2021-11-15
    """
    return [(datetime.today()+timedelta(day)).strftime('%Y-%m-%d'), (datetime.today()+timedelta(day)).strftime('%Y-%m-%d')]

@shared_task
def send_mail_func(day):
    users = Tasks.objects.filter(due_date__range=get_due_date(day))
    print("send mail func")
    for user in users[0:5]:
        mail_subject = f"Merhabalar taskınızın tamamlanmasına {day} kalmıştır."
        message = f"Taskınızı kontrol ediniz. {user.user}. Tamamlanma günü {user.due_date}"
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

