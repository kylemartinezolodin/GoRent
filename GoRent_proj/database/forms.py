from django import forms
from .models import *


class RentOwnerFroms(forms.ModelForm):
    class Meta:
            model = RentOwner
            field = ('email', 'contactnumber')

class ShareeFroms(forms.ModelForm):
    class Meta:
            model = Sharee
            field = ('email', 'contactnumber')