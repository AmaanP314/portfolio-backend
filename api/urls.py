from django.urls import path
from .views import send_email, health_check

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
    path('health-check/', health_check, name='health_check'),
]

