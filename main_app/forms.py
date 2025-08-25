from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):

    # its jsut boilerplate
   class Meta:
        model = Feeding
        fields = ['date', 'meal']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

   