from django.urls import path,include
from .  import views
app_name= 'contact' #name of the application

urlpatterns = [
    path('',views.contact_message, name='contact'),
]
