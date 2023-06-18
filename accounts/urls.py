from django.urls import path,include
from .  import views
app_name= 'accounts' #name of the application

urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('',views.CustomLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('profile',views.profile, name='profile'),
    path('profile/edit',views.profile_edit, name='profile_edit'),
]
