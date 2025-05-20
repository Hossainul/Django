from django import forms
from Musicians.models import musician

class formMusicians(forms.ModelForm):
    class Meta:
        model = musician
        fields = '__all__'