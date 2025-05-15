from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home, name ="home"),
    path("about/",views.about, name = "about"),
    path("form/", views.form, name = "form"),
    path("djnago_form/",views.django_form, name = "django_form"),
    path("student_form/",views.student_form, name ="student_form"),
]
