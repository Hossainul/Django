from django.urls import path
from . import views

urlpatterns = [
    path('add_musicians/', views.add_musician, name = "add_musician"),
    path('edit_musicians/<int:id>', views.edit_musicians, name = "edit_musicians")
]