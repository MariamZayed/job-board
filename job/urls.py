from django.urls import path,include
from .  import views
app_name= 'job' #name of the application

urlpatterns = [
    path('',views.job_list),
    path('<int:id>',views.job_detail, name='job_detail'),
]
