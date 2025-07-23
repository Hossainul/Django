from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from Car.models import addCar

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=False)
    image = models.ImageField(upload_to="profile/")
    details = models.TextField(blank=True, null= True)
    phone = PhoneNumberField(region = "BD")
    address = models.CharField(max_length=200)

    # only for seller
    car_brand_name = models.CharField(max_length=50,null = True, blank = True)
    # In your Profile model (models.py)
    car_license = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.user.username


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    car = models.ForeignKey(addCar, on_delete=models.CASCADE, null = True, blank = True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits = 10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"order by {self.user.username} - {self.car.car_model} ({self.quantity})"


    

 
  