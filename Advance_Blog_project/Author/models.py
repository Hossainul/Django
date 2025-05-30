from django.db import models
from django import forms
from Category.models import add_category

# Create your models here.

class addPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.CharField()
    category = models.ManyToManyField(add_category)
