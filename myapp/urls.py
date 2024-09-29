from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('pace/2022', views.pace2022, name='pace2022'),
    path('pace/2023', views.pace2023, name='pace2023'),
    path('pace/2024', views.pace2024, name='pace2024'),
]
