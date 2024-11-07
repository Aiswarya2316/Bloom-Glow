from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message', 'rating']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
