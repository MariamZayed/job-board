from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):# ModelForm  means that I have form model
    class Meta:
        model = Apply
        fields = ['name', 'email', 'cv', 'cover_letter', 'website']# remove job field and commit it in view