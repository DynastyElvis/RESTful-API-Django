from django import path
from . import views

Urlpatterns = [
    path('',views.getData)
]