from django import forms
from .models import CareLog

class CareLogForm(forms.ModelForm):
    class Meta:
        model = CareLog
        fields = '__all__'
