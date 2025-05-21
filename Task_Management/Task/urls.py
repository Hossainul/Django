from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name = "add_task"),
    path('Edit/<int:id>',views.Edit, name = "edit_task"),
    path('Delete/<int:id>', views.delete, name = "delete_task")
]
