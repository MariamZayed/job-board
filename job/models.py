from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField( blank=True, null=True) # we made it that way as when we hit the save button in admin dashboard it would create slug automatically

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)# remove spaces
        super(job, self).save(*args, **kwargs) # save old instance with new instance(slug which already motified x)


    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey(job, related_name='apply_job', on_delete=models.CASCADE)

    def __str__(self):
        return self.name