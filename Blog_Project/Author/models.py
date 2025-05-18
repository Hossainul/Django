from django.db import models
from django.core import validators

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    phone = models.CharField(max_length=11, validators=[validators.validate_integer])

    def __str__(self):
        return self.name
