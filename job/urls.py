from django.urls import path,include
from .  import views
from . import api
app_name= 'job' #name of the application

urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('add-job',views.add_job, name='add_job'), #put string url before parameter routes
    path('<str:slug>',views.job_detail, name='job_detail'),

    ##api
    path('api/jobs',api.jobListAPI, name='jobListAPI'),
    path('api/jobs/<int:job_id>',api.jobDetail, name='jobDetail'),

    # Generic views 
    path('api/v2/jobs',api.JobListAPI.as_view(), name='JobListAPI'),# we put as_view to represent it as function cause without it it's a class 

]
