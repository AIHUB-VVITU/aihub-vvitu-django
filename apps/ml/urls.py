from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<str:id>/', views.play_ml, name="ml"),
]