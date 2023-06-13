from django.db import models
from django.urls import reverse
# Create your models here.
class blog(models.Model):             #It's called models.Model and not models.model (case sensitive)
    name=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    img= models.ImageField(upload_to='picture',null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    desc= models.TextField()
    autor= models.CharField(max_length=100)
    date= models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.name)

class comment(models.Model):
    comments = models.CharField(max_length=100)




    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogs')


