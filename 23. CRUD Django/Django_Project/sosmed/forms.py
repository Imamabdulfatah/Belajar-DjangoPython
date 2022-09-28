from django import forms
from django.forms import fields
from django.forms.models import model_to_dict

from .models import Instagram

class InstagramForm(forms.ModelForm):
    class Meta:
        model   = Instagram
        fields  =[
            'nama_depan',
            'nama_belakang',
            'username',            
        ]