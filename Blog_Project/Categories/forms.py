from django import forms
from Categories.models import Categories

class add_categories(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'