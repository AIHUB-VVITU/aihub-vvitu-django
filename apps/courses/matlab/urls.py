from django.urls import path, re_path
from . import views

app_name = 'matlab'

urlpatterns = [
    re_path(r'^/?$', views.index, name="index"),
    re_path(r'^experiment_desc/?$', views.exp_detail, name="experiment_detail"),
    re_path(r'^experiment_view/?$', views.exp_view, name="experiment_viewer")
]
