# forms.py
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm,UserChangeForm
from django import forms
from django.core.exceptions import ValidationError

class registerForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password : ",
        widget=forms.PasswordInput(attrs={'type': 'password'}),
        help_text="",
    )
    password2 = forms.CharField(
        label="Confirmed Password :",
        widget=forms.PasswordInput(attrs={'type': 'password'}),
        help_text="",
    )
    first_name = forms.CharField(
        label="First Name :",
        widget=forms.TextInput(attrs={'id': 'required'}),
    )
    last_name = forms.CharField(
        label="Last Name :",
        widget=forms.TextInput(attrs={'id': 'required'}),
    )
    email = forms.EmailField(
        label="Email :",
        widget=forms.EmailInput(attrs={'id': 'required'}),
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class customUpdateform(PasswordChangeForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password'}),
        help_text=" "
    )

    def clean_new_password1(self):
        old_password = self.cleaned_data.get("old_password")
        new_password1 = self.cleaned_data.get("new_password1")
        if old_password == new_password1:
            raise ValidationError("The new password must be different from the old password.")
        return new_password1

class customSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password'}),
        help_text=" "
    )

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if self.user.check_password(new_password1):
            raise ValidationError("The new password must be different from the old password.")
        return new_password1


class userChangeData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]