from django.urls import path
from genshin_wish import views

urlpatterns = [
    path("", views.home, name="home"),
    path("main/", views.main, name="main"),
]