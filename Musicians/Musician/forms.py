from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile,addALBUM
from django.core.validators import ValidationError


class registerUser(UserCreationForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id' : 'required'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id' : 'required'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs = {'id' : 'required'})
    )

    is_musician = forms.BooleanField(required=True, label="Are you a musician?")

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'is_musician']
    


## change password using old one
class passwordChange(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        new_password1 = self.cleaned_data["new_password1"]

        if old_password == new_password1:
            raise ValidationError("This password is too similar to previous one.")
        return new_password1

# change password without old one

class passwordChangeWithout(SetPasswordForm):
    class Meta:
        model = User
        fields = '__all__'



# # for edit profile 

# class ProfileForm(forms.ModelForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = Profile
#         fields = ['image', 'bio', 'website']
#         widgets = {
#             'bio': forms.Textarea(attrs={'rows': 3}),
#         }

#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)

#         if user:
#             self.fields['first_name'].initial = user.first_name
#             self.fields['last_name'].initial = user.last_name
#             self.fields['email'].initial = user.email

#     def save(self, commit=True):
#         profile = super().save(commit=False)
#         user = profile.user
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()
#             profile.save()
#         return profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
        
    #     if self.user:
    #         self.fields['first_name'].initial = self.user.first_name
    #         self.fields['last_name'].initial = self.user.last_name
    #         self.fields['email'].initial = self.user.email

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.exclude(pk=self.user.pk).filter(email=email).exists():
    #         raise ValidationError("This email is already in use.")
    #     return email

    # def save(self, commit=True):
    #     profile = super().save(commit=False)
    #     self.user.first_name = self.cleaned_data['first_name']
    #     self.user.last_name = self.cleaned_data['last_name']
    #     self.user.email = self.cleaned_data['email']
    #     if commit:
    #         self.user.save()
    #         profile.save()
    #     return profile
    


# add album forms
class addAlbumForm(forms.ModelForm):
    class Meta:
        model = addALBUM
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'Release_date' : forms.DateTimeInput(attrs = {'type' : 'datetime-local'}),
        }