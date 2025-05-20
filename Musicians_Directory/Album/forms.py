from django import forms
from Album.models import addAlbum

class addalbumForm(forms.ModelForm):
    class Meta:
        model = addAlbum
        fields = "__all__"

        widgets = {
            'ratings' : forms.RadioSelect(),
            'realse_date' : forms.DateTimeInput(attrs={'type' :'datetime-local'})
        }