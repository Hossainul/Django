from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User



class registerUser(UserCreationForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id' : 'required'})
    )

    last_name = forms.CharField(
        widget = forms.TextInput(attrs = {'id' : 'required'})
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs = {'id' : 'required'})
    )
    
    seller = forms.BooleanField(required = False, label = "Are you seller ?! ")


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','seller']