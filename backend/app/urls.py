from django.urls import path
from .views import send_message  # Ensure this matches the function name in views.py

urlpatterns = [
    path('send_message/', send_message, name='send_message'),
]