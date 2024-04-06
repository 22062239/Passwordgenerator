from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('result.html', views.generate_password, name='generate_password'),
]