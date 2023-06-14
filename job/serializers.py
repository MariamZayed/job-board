from rest_framework import serializers 
from .models import job

# Serializers define the API representation.
class JobSerializer(serializers.ModelSerializer): #https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
    class Meta:
        model = job
        fields = '__all__'