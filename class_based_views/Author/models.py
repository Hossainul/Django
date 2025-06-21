from django.db import models
from django import forms
from Category.models import add_category
from django.contrib.auth.models import User

# Create your models here.

class addPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.CharField()
    category = models.ManyToManyField(add_category)
    #image = models.ImageField(upload_to='uploads/', blank= True, null=True) # inside global folder
    image = models.ImageField(upload_to='Author/media/uploads/', blank= True, null= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null= True)

    def __str__(self):
        return self.title

class addComment(models.Model):
    post = models.ForeignKey(addPost, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    comment = models.TextField()
    on_create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"comments by {self.name}"