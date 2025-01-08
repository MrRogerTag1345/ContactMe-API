"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple root view
def home(request):
    return HttpResponse("Welcome to the Django API. Navigate to /app/send_message/ to send an email.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),  # Include app URLs
    path('', home),  # Add this line to handle the root URL
]
