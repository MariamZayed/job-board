from django.urls import path,include
from .  import views
app_name= 'job' #name of the application

urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('add-job',views.add_job, name='add_job'), #put string url before parameter routes
    path('<str:slug>',views.job_detail, name='job_detail'),
]
