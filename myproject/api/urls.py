# from django import path
from . import views
from django.urls import path

urlpatterns = [
    path('',views.getData)
]