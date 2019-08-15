from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_name/", views.get_name, name="get_name"),
    path("get_animal/", views.get_animal, name="get_animal"),
    path("view_org/", views.view_org, name="view_org"),
]
