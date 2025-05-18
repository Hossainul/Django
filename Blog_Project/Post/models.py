from django.db import models
from Categories.models import Categories
from Author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Categories)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title