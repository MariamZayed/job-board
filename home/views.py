from django.shortcuts import render
from job.models import job

# Create your views here.
def index(request):
    recent_jobs = job.objects.order_by('published_at')[:6]  # Retrieve the 5 most recent jobs

    return render(request, 'home/home.html', {'recent_jobs': recent_jobs})