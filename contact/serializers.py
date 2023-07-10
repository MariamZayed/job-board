from rest_framework import serializers 
from .models import Contact

# Serializers define the API representation.
class ContactSerializer(serializers.ModelSerializer): #https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
    class Meta:
        model = Contact
        fields = ['email','subject','message']