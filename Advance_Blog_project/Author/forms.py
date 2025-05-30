from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import addPost


class registerForm(UserCreationForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs = {'id' : 'required'}),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs = {'id' : 'required'}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs = {'id' : 'required'}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type' : 'password'}),
        help_text = " "
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type' : 'password'}),
        help_text = " "
    )
    
    class Meta:
       model = User
       fields = ['first_name', 'last_name', 'email']


# when user change his password it wouldn't be same password(check)

class changePassword(PasswordChangeForm):
    def clean(self): # method name should be clean() otherwise don't run django automatically
        cleaned_data = super().clean()
        old_pass = self.cleaned_data.get("old_password")
        new_pass = self.cleaned_data.get("new_password1")

        if old_pass == new_pass:
            raise ValidationError("This password is same as old password")
        else:
            return cleaned_data
    

class updateInfo(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class user_addPost(forms.ModelForm):

    date = forms.CharField(
        widget=forms.DateInput(attrs={'type' : 'datetime-local'})
    )
    class Meta:
        model = addPost
        fields = "__all__"