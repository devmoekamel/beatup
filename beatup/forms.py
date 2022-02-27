from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.http import request
from .models import *
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget



class registerform(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']



class postform(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model= Post
        fields =['text']
        