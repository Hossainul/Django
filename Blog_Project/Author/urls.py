from django.urls import path,include
from Author.views import addAuthor

urlpatterns = [
    path('add_author/', addAuthor, name = "add_author"),
]
