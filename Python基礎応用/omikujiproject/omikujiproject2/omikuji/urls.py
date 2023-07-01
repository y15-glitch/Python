from django.urls import path

from . import views

urlpatterns = [
    path('kuji/', views.index),
]
