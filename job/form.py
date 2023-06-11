from django import forms
from .models import Apply,job

class ApplyForm(forms.ModelForm):# ModelForm  means that I have form based on a model
    class Meta:
        model = Apply
        fields = ['name', 'email', 'cv', 'cover_letter', 'website']# remove job field and commit it in view

class JobForm(forms.ModelForm):# ModelForm means that I have form based on a model
    class Meta:
        model = job 
        fields = '__all__'
        exclude = ('slug','owner', )