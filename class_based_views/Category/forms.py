from django import forms
from .models import add_category

class categoryForm(forms.ModelForm):
    class Meta:
        model = add_category
        fields = "__all__"
    
    