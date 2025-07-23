from . import models
from django import forms

class carAddingform(forms.ModelForm):
    class Meta : 
        model = models.addCar
        exclude = ["user"]
      
        

    