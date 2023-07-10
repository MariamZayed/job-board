from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings


class AddContactAPI(generics.CreateAPIView):# generic view for creating objects.
    serializer_class = ContactSerializer

    def perform_create(self, serializer):# In your code, your AddContactAPI class inherits from generics.CreateAPIView, which provides the base implementation for creating objects. By overriding perform_create in your AddContactAPI class, you can extend the behavior of creating a contact object and add your custom logic specific to that action.
        subject = self.request.data.get('subject')
        message = self.request.data.get('message')
        email = self.request.data.get('email')
        
        instance = serializer.save() #it performs the process of saving the validated data and creating a new object in the database. #If the data is valid, serializer.save() creates a new object instance using the validated data. It maps the validated data to the corresponding fields of the model specified in the serializer's Meta class.
                                    #The new object is then saved to the database using the appropriate model's save() method. This creates a new record in the database with the data provided.
                                    #Finally, the serializer.save() method returns the newly created object instance.
                                    # You can use this instance variable for further operations or to access any attributes or methods of the created object. For example, you use instance.email, instance.subject, and instance.message
        # Send email notification
        email_subject = 'New Contact Message'
        email_message = f"A new contact message has been received.\n\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        
        send_mail(email_subject, email_message, email, [settings.EMAIL_HOST_USER])

        return instance