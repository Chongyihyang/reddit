from django import forms
from .models import *

class Post_create(forms.ModelForm):
    title = forms.CharField()
    description = forms.TextInput()
    image=forms.ImageField(required=False)
    video=forms.FileField(required=False)

    class Meta:
        model = Post
        fields = ['title','description','image','video']

        