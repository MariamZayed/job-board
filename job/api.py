from .models import job , Category
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

class AddJobAPI(generics.CreateAPIView):# generic view for creating objects.
    serializer_class = JobSerializer

class JobDetailAPI(generics.RetrieveAPIView):# RetrieveAPIView : which is a generic view for retrieving a single object.
    queryset = job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'slug' # indicating that the slug field should be used to retrieve the job object.

class FilteredJobListAPI(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):# method is overridden to provide the custom queryset based on the category name.
        category_name = self.kwargs['category_name'] # category_name is extracted from the URL by using kwargs 
        return job.objects.filter(category__name=category_name)#category__name is used to perform a lookup on the name field of the related Category model within the job model.