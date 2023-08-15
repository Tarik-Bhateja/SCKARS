from django.contrib import admin
from django.urls import path,include
from . import views
from home.views import index

urlpatterns = [
    path('',views.dashboard),
    path('api/',index),
     path('api/control/', views.control_device, name='control-device'),
]
