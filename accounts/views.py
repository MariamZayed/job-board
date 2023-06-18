from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate,login
from . models import Profile
from .forms import UserForm, ProfileForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='home') # Redirect to home page if user is authenticated
from django.http import HttpResponse

def hello_world(request):
    print("Hello World")
    print("Hello World")
    print("Hello World")
    message = 'Hello World'
    return HttpResponse(message)

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)# request.POST means take data which came from POST form 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            home_url = reverse('home:home')
            return redirect(home_url) 
    else:
        form = SignupForm() 
        home_url = reverse('home:home')
        return redirect(home_url) 
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save(commit=False)
            profile_form.user= request.user
            profile_form.save()
            return redirect(reverse('accounts:profile'))
    else:
        user_form = UserForm(instance=request.user) #instance is used to show data in form
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})


class CustomLoginView(LoginView):

    @staticmethod
    def redirect_authenticated_user(request):
        if request.user.is_authenticated:
            return redirect('home:home')  # Redirect to the home page or any other desired page
        else:
            return super().dispatch(request, *args, **kwargs)

# @login_required(login_url='home:home')
# def login(request): #this is a custom method to login
#     return redirect('home:home')