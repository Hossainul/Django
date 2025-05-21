from django.urls import path
from .views import addCategories,Edit

urlpatterns = [
    path('add_category/',addCategories, name = "add_category"),
    path('Edit/<int:id>', Edit, name = "edit_task")
]
