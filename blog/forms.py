'''
Created on 28/04/2016

@author: seacosta
'''
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)