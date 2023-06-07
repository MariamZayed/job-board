from django.db import models

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=100) # this is cloumn 
    job_type = models.CharField(max_length=20,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0) 
    exprience = models.IntegerField(default=1)

    def __str__(self):
        return self.title