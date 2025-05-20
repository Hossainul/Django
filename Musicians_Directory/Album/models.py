from django.db import models
from Musicians.models import musician

# Create your models here.


class RatingChoices(models.TextChoices):
    ONE = '1', '★☆☆☆☆'
    TWO = '2', '★★☆☆☆'
    THREE = '3', '★★★☆☆'
    FOUR = '4', '★★★★☆'
    FIVE = '5', '★★★★★'

class addAlbum(models.Model):
    album_name = models.CharField(max_length=50)
    realse_date = models.DateTimeField()
    ratings = models.CharField(max_length=1, choices = RatingChoices, default = "5")
    album_author = models.ForeignKey(musician, on_delete=models.CASCADE, default=None)
 

    def __str__(self):
        return self.album_name


