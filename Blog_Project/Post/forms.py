from django import forms
from Post.models import Post

class add_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        