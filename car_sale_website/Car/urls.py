from django.urls import path
from . import views

urlpatterns = [
   path('add/', views.carAdd.as_view(), name = "car_add"),
   path('car/information/edit/<int:pk>/', views.carEdit.as_view(), name = "car_edit"),
   path('car/delete/<int:pk>/', views.carDelete.as_view(), name = "car_delete"),
]
