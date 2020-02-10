from django import forms
from .models import Profile,Image,Comments

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']
