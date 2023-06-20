from django.urls import path,include
from .  import views, api
app_name= 'accounts' #name of the application

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('profile',views.profile, name='profile'),
    path('profile/edit',views.profile_edit, name='profile_edit'),

    # Generic views API
    path('api/signup',api.SignUpAPI.as_view(), name='SignUpAPI'),

]
