from django.shortcuts import render
from .models import Contact 
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def send_message(request):
    contact_msg = Contact.objects.first()
    
    if request.method == 'POST':
        # Construct an email message that uses the connection
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail( #https://docs.djangoproject.com/en/4.2/topics/email/#quick-example
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER]
        )
    

    return render(request, 'contact/contact.html',{'contact_msg':contact_msg})