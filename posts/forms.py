from django import forms
from .models import BlogPost,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
