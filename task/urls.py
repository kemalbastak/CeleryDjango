from django.urls import path
from . import views
urlpatterns = [
    path("deneme/", views.send_mail_view, name="deneme")
]
