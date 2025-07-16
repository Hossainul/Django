# from django.db import models
# from multiselectfield import MultiSelectField
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Create your models here.

# INSTRUMENT_CHOICES = [
#     ('GUITAR', 'Guitar'),
#     ('PIANO', 'Piano'),
#     ('DRUMS', 'Drums'),
#     ('VIOLIN', 'Violin'),
#     ('FLUTE', 'Flute'),
# ]


# class addMusicians(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField(unique=True)
#     phone_number = models.IntegerField()
#     instrument_type = MultiSelectField(choices=INSTRUMENT_CHOICES, max_choices=5, max_length=100)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_musician = models.BooleanField(default=False)
#     image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
#     bio = models.TextField(blank=True)
#     website = models.URLField(blank=True)



from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_musician = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
INSTRUMENT_TYPE = [
    ('Guiter' , 'guiter'),
    ('Drum' , 'drum'),
    ('Mixer' , 'mixer'),
    ('DJ' , 'dj'),
    ('Electice Guiter' , 'eletic guiter'),
    
]



class addALBUM(models.Model):
    title = models.CharField(max_length=100)
    Release_date = models.DateTimeField()
    number_of_songs = models.IntegerField()
    details = models.TextField(null = True)
    image = models.ImageField(upload_to='album/image', null = True, blank = True)
    instrument_type = MultiSelectField(choices = INSTRUMENT_TYPE, max_choices = 5, max_length = 100)
    user = models.ForeignKey(User, on_delete= models.CASCADE, null= True)

    def __str__(self):
        return self.title