from django.urls import path,include
from .  import views, api
app_name= 'home' #name of the application

urlpatterns = [
    path('',views.index, name='home'),

    # Generic view api
    path('api/home',api.GetHomeAPI.as_view(), name='GetHomeAPI'),

]

