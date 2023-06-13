from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)        
    subject = models.CharField(max_length=254)   
    message = models.CharField(max_length=1000)   

    def __str__(self):
        return self.email