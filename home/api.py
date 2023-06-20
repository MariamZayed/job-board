from job.models import job 
from job.serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

class GetHomeAPI(generics.ListAPIView):
    queryset = job.objects.order_by('published_at')[:6]
    serializer_class = JobSerializer
