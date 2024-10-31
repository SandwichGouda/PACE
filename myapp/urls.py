from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('pace/2023', views.pace2023, name='PACE2023'),
]
