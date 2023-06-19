from django.urls import path,include
from .  import views
from . import api
app_name= 'job' #name of the application

urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('add-job',views.add_job, name='add_job'), #put string url before parameter routes
    path('<str:slug>',views.job_detail, name='job_detail'),
    path('jobs/category/<str:category_name>/', views.filtered_job_list, name='filtered_job_list'),


    ##api
    path('api/jobs',api.jobListAPI, name='jobListAPI'),
    path('api/jobs/<int:job_id>',api.jobDetail, name='jobDetail'),

    # Generic views 
    path('api/v2/jobs',api.JobListAPI.as_view(), name='JobListAPI'),# we put as_view to represent it as function cause without it it's a class 
    path('api/v2/add-job',api.AddJobAPI.as_view(), name='AddJobAPI'),
    path('api/v2/<str:slug>',api.JobDetailAPI.as_view(), name='AddJobAPI'),
    path('api/v2/category/<str:category_name>',api.FilteredJobListAPI.as_view(), name='FilteredJobListAPI'),
]
