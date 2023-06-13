from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)# do this as user first created doesn't have a profile

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User) # implement this fun after user model is visited 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) # create empty profile form user instance
##source page :https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name