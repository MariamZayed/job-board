from django.urls import path,include
from .  import views
app_name= 'home' #name of the application

urlpatterns = [
    path('',views.index, name='home'),
]
