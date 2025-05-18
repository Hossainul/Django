from django import forms
from Author.models import Author
from django.core import validators

class Add_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        labels = {
           'name' : 'Full Name',
        }
        
        help_texts = {
            'name' : 'please enter your name'
        }