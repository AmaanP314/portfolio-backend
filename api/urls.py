from django.urls import path
from .views import send_email, health_check, send_email_lab

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
    path('send-email-lab/', send_email_lab, name='send_email_lab'),
    path('health-check/', health_check, name='health_check'),
]

