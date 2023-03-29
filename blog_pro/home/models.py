from django.db import models
from django.urls import reverse
# Create your models here.
class blog(models.Model):             #It's called models.Model and not models.model (case sensitive)
    name=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    img= models.ImageField(upload_to='picture')
    desc= models.TextField()
    autor= models.CharField(max_length=100)

    # def get_urls(self):
    #     return reverse('details')