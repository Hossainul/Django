from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.signUp.as_view(), name = "register"),
    path("login/", views.loginUser.as_view(), name = "login")
]
