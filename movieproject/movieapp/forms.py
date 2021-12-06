from django import forms
from django.db import models
from . models import MOVIE

class movieform(forms.ModelForm):
    class Meta:
        model=MOVIE
        fields=['name','disc','img','year']