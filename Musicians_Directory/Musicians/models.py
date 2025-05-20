from django.db import models

# Create your models here.c
class musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    instrument = models.TextField()

    def __str__(self):
        return self.first_name



