from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['teacher', 'question', 'response']
        widgets = {
            'response': forms.RadioSelect(choices=Response.SCALE_CHOICES),
        }
