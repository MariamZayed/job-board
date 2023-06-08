from django.db import models

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance,filename):
    imagename,extension = filename.split('.')
    print(instance)
    return 'jobs/%s.%s' % (instance.id,extension)

# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=100) # this is cloumn 
    job_type = models.CharField(max_length=20,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0) 
    exprience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)#coment it first //run mkmigrations //add in db // uncomment this line //mkmigrations
    images = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name