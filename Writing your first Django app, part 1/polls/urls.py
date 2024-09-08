from django.urls import path
from .import views

# External urls create this project 
urlpatterns = [
    path('',views.index),
]
