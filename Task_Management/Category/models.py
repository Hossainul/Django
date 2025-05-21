from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField("category name:", max_length=50)

    def __str__(self):
        return self.name