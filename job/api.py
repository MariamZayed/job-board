from .models import job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

@api_view()
def jobListAPI(request):
    job_list = job.objects.all()
    data = JobSerializer(job_list, many=True).data # many=True to return all jobs #JobSerializer is done to transform them to json
    return Response({"data:":data})

@api_view(['GET']) #عشان انا مش رايح اعدل ولا امسح ولا اضيف
def jobDetail(request, job_id):
    job_detail = job.objects.get(id=job_id)
    data = JobSerializer(job_detail).data
    return Response({"data:":data})


# Generic view #https://www.django-rest-framework.org/api-guide/generic-views/#examples
class JobListAPI(generics.ListAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer