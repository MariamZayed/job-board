from django.urls import path
from . import api
from .  import views
app_name= 'contact' #name of the application

urlpatterns = [
    path('',views.send_message, name='contact'),

    # Generic views 
    path('api/v2/add-contact',api.AddContactAPI.as_view(), name='AddContactAPI'),
]
