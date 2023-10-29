from django.forms import ModelForm
from .models import Laying

class LayingForm(ModelForm):
    class Meta:
        model = Laying
        fields = ['date', 'time']