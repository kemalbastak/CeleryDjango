from django.shortcuts import render
from .tasks import send_mail_func
from django.http.response import HttpResponse
from .models import Tasks
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import time
# Create your views here.
def send_mail_view(request):
    send_mail_func.delay()
    print(Tasks.objects.all()[0].email)
    print("send_mail_view")
    return HttpResponse("SENT")

