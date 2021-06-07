from django import forms
from .models import *


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ('name', 'phone', 'email')
