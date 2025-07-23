from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class addCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=50)
    car_quantity = models.IntegerField()
    car_details = models.TextField()
    car_price = models.BigIntegerField()
    car_image = models.ImageField(upload_to='profile')
    

    def __str__(self):
        return self.car_model
