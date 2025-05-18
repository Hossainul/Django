from django.urls import path,include
from Categories.views import add_categori

urlpatterns = [
    path('add_categories/',add_categori, name = "add_categories")
]
