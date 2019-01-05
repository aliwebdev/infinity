from django import forms
from .models import HourValue


class HourValueForm(forms.ModelForm):
    class Meta:
        model = HourValue
        fields = (
            'date',
        )
