from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserChangeForm
from django import forms


class passwordChange(PasswordChangeForm):
    class Meta :
        model = User
        fields = "__all__"

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.instance.first_name

    
class editProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ["image","details","phone","address","car_brand_name","car_license"]


    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        instance = kwargs.get('instance')

        if instance and not instance.is_seller:
            self.fields['car_brand_name'].widget = forms.HiddenInput()
            self.fields['car_license'].widget = forms.HiddenInput()



class buycarForm(forms.Form):
    quantity = forms.IntegerField(min_value = 1, label = "quantity")