from django import forms
from .models import categories

class formCategories(forms.ModelForm):
    class Meta:
        model = categories
        fields = '__all__'

        labels = {
            'name' : 'category select'
        }