from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):#UserCreationForm not modle.ModelForm becuase we need encription for password, modle.ModelForm for normal forms
    class Meta:
        model= User
        fields = ['username', 'password1', 'password2', 'email'] #اما اجي اعمل سين اب هعمل بالبيانات ديه بس, ولما يتسجل يبقى يروح على البروبافيل بتاعه يزود بيانات براحته الي هما تحت

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phone_number','image']